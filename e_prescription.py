import os
import streamlit as st
from PIL import Image
import requests
import re
import numpy as np
import cv2
from typing import List, Dict, Set, Optional

def preprocess_image(img_pil: Image.Image) -> np.ndarray:
    """Basic preprocessing to improve OCR on noisy scans/handwriting."""
    try:
        import pytesseract
    except ImportError:
        st.error("pytesseract not installed. Please install: pip install pytesseract")
        return None
    img = np.array(img_pil)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray, 3)
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 35, 11)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
    cleaned = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=1)
    return cleaned

def extract_text_from_image(img_pil: Image.Image, lang: str = "eng") -> str:
    """Run Tesseract OCR on the image."""
    try:
        import pytesseract
    except ImportError:
        st.error("pytesseract not installed. Please install: pip install pytesseract")
        return ""
    try:
        pre = preprocess_image(img_pil)
        if pre is None:
            return ""
        config = "--oem 3 --psm 6"
        text = pytesseract.image_to_string(pre, lang=lang, config=config)
        return "\n".join(line.strip() for line in text.splitlines() if line.strip())
    except Exception as e:
        st.error(f"OCR failed: {str(e)}")
        try:
            text = pytesseract.image_to_string(np.array(img_pil), lang=lang, config=config)
            return "\n".join(line.strip() for line in text.splitlines() if line.strip())
        except Exception:
            return ""

SPECIALTY_MAP = {
    "fever": ["General Physician", "Internal Medicine"],
    "cold": ["General Physician"],
    "cough": ["General Physician", "Pulmonologist"],
    "flu": ["General Physician"],
    "infection": ["General Physician"],
    "pain": ["General Physician"],
    "headache": ["Neurologist", "General Physician"],
    "migraine": ["Neurologist"],
    "hypertension": ["Cardiologist", "Internal Medicine"],
    "bp": ["Cardiologist", "Internal Medicine"],
    "diabetes": ["Endocrinologist", "Internal Medicine"],
    "thyroid": ["Endocrinologist"],
    "asthma": ["Pulmonologist"],
    "tb": ["Pulmonologist"],
    "pneumonia": ["Pulmonologist"],
    "chest pain": ["Cardiologist"],
    "palpitation": ["Cardiologist"],
    "angina": ["Cardiologist"],
    "shortness of breath": ["Pulmonologist", "Cardiologist"],
    "wheezing": ["Pulmonologist"],
    "rash": ["Dermatologist"],
    "acne": ["Dermatologist"],
    "psoriasis": ["Dermatologist"],
    "eczema": ["Dermatologist"],
    "fracture": ["Orthopedic Surgeon"],
    "sprain": ["Orthopedic Surgeon"],
    "joint pain": ["Orthopedic Surgeon", "Rheumatologist"],
    "arthritis": ["Rheumatologist"],
    "kidney": ["Nephrologist"],
    "stone": ["Urologist"],
    "urinary": ["Urologist"],
    "liver": ["Gastroenterologist"],
    "stomach": ["Gastroenterologist"],
    "ulcer": ["Gastroenterologist"],
    "gastritis": ["Gastroenterologist"],
    "eye": ["Ophthalmologist"],
    "vision": ["Ophthalmologist"],
    "ear": ["ENT"],
    "throat": ["ENT"],
    "tonsil": ["ENT"],
    "tooth": ["Dentist"],
    "dental": ["Dentist"],
    "pregnancy": ["Obstetrician-Gynecologist"],
    "pcos": ["Gynecologist", "Endocrinologist"],
    "period": ["Gynecologist"],
    "fertility": ["Gynecologist"],
    "piles": ["General Surgeon", "Colorectal Surgeon"],
    "fissure": ["General Surgeon", "Colorectal Surgeon"],
    "fistula": ["General Surgeon", "Colorectal Surgeon"],
    "cancer": ["Oncologist"],
    "tumor": ["Oncologist"],
    "stroke": ["Neurologist"],
    "seizure": ["Neurologist"],
    "back pain": ["Orthopedic Surgeon", "Physiotherapist"],
    "depression": ["Psychiatrist"],
    "anxiety": ["Psychiatrist"],
    "autism": ["Psychiatrist"],
    "typhoid": ["General Physician"],
}
ALL_SPECIALTIES = sorted({s for v in SPECIALTY_MAP.values() for s in v} | {
    "Pediatrician", "Diabetologist", "Hepatologist", "Hematologist"
})
SPECIALTY_HINTS_IN_TEXT = {
    r"\bcardio": "Cardiologist",
    r"\bdermatolog": "Dermatologist",
    r"\bent\b|otolaryng": "ENT",
    r"\bophthalmolog|eye\s*care": "Ophthalmologist",
    r"\bgastro": "Gastroenterologist",
    r"\bneuro": "Neurologist",
    r"\buro": "Urologist",
    r"\bnephro": "Nephrologist",
    r"\bendo": "Endocrinologist",
    r"\bpsychi": "Psychiatrist",
    r"\brheumat": "Rheumatologist",
    r"\bortho": "Orthopedic Surgeon",
    r"\bobs?g[y|i]n|gyne?colog": "Obstetrician-Gynecologist",
    r"\bonco": "Oncologist",
}

def normalize_text(text: str) -> str:
    """Normalize text for better keyword matching."""
    t = text.lower()
    t = re.sub(r"\b(tab|cap|sos|od|bd|tid|qid|hs|stat|rx)\b", " ", t)
    t = re.sub(r"[^a-z0-9\s]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def extract_conditions(text: str) -> List[str]:
    """Extract medical conditions from text."""
    nt = normalize_text(text)
    found = set()
    for kw in SPECIALTY_MAP.keys():
        if " " in kw:
            pattern = r"\b" + re.escape(kw) + r"\b"
            if re.search(pattern, nt):
                found.add(kw)
        else:
            if re.search(r"\b" + re.escape(kw) + r"\b", nt):
                found.add(kw)
    return sorted(found)

def predict_specialties(text: str, conditions: List[str]) -> List[str]:
    """Predict medical specialties based on text and extracted conditions."""
    nt = normalize_text(text)
    hints = []
    for pat, spec in SPECIALTY_HINTS_IN_TEXT.items():
        if re.search(pat, nt):
            hints.append(spec)
    from_kw: Set[str] = set()
    for kw in conditions:
        from_kw.update(SPECIALTY_MAP.get(kw, []))
    ranked = []
    for s in hints + list(from_kw):
        if s not in ranked:
            ranked.append(s)
    if not ranked:
        ranked = ["General Physician"]
    return ranked

def geocode_location(query: str) -> Optional[Dict]:
    """Geocode using Nominatim (OSM)."""
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {"q": query, "format": "json", "limit": 1}
        headers = {"User-Agent": "prescription-finder-demo"}
        r = requests.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        if data:
            return {
                "lat": float(data[0]["lat"]),
                "lon": float(data[0]["lon"]),
                "display_name": data[0]["display_name"]
            }
    except Exception as e:
        st.error(f"Geocoding failed: {str(e)}")
        return None
    return None

def make_google_maps_url(name: str, lat: float, lon: float) -> str:
    """Generate Google Maps URL."""
    q = (name or "").strip()
    if q:
        return f"https://www.google.com/maps/search/?api=1&query={q.replace(' ', '+')}@{lat},{lon}"
    return f"https://www.google.com/maps/?q={lat},{lon}"

def search_google_places(specialty: str, lat: float, lon: float, radius_m: int, api_key: str) -> List[Dict]:
    """Search using Google Places API."""
    try:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "location": f"{lat},{lon}",
            "radius": radius_m,
            "keyword": f"{specialty} doctor",
            "type": "doctor",
            "key": api_key,
        }
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        results = []
        for p in data.get("results", []):
            name = p.get("name")
            address = p.get("vicinity") or p.get("formatted_address")
            rating = p.get("rating")
            place_id = p.get("place_id")
            plat = p.get("geometry", {}).get("location", {}).get("lat")
            plon = p.get("geometry", {}).get("location", {}).get("lng")
            maps_url = f"https://www.google.com/maps/place/?q=place_id:{place_id}" if place_id else make_google_maps_url(name, plat, plon)
            results.append({
                "name": name,
                "address": address,
                "rating": rating,
                "lat": plat,
                "lon": plon,
                "maps_url": maps_url
            })
        return results
    except Exception as e:
        st.error(f"Google Places search failed: {str(e)}")
        return []

def search_overpass(specialty: str, lat: float, lon: float, radius_m: int) -> List[Dict]:
    """Search using OpenStreetMap Overpass API."""
    try:
        query = f"""
        [out:json][timeout:25];
        (
          node(around:{radius_m},{lat},{lon})["amenity"="doctors"];
          node(around:{radius_m},{lat},{lon})["amenity"="hospital"];
          way(around:{radius_m},{lat},{lon})["amenity"="doctors"];
          way(around:{radius_m},{lat},{lon})["amenity"="hospital"];
        );
        out center tags;
        """
        headers = {"User-Agent": "prescription-finder-demo"}
        r = requests.post("https://overpass-api.de/api/interpreter",
                          data=query.encode("utf-8"), headers=headers, timeout=60)
        r.raise_for_status()
        j = r.json()
        results = []
        kw = specialty.lower()
        for el in j.get("elements", []):
            tags = el.get("tags", {})
            name = tags.get("name") or tags.get("official_name") or "Unnamed"
            lat_coord = el.get("lat") or (el.get("center", {}) or {}).get("lat")
            lon_coord = el.get("lon") or (el.get("center", {}) or {}).get("lon")
            addr_parts = [tags.get(k, "") for k in
                          ["addr:housenumber", "addr:street", "addr:city", "addr:postcode"]
                          if tags.get(k)]
            addr = ", ".join(addr_parts) or tags.get("addr:full") or ""
            results.append({
                "name": name,
                "address": addr,
                "rating": None,
                "lat": lat_coord,
                "lon": lon_coord,
                "maps_url": make_google_maps_url(name, lat_coord, lon_coord) if lat_coord and lon_coord else None,
            })
        return results
    except Exception as e:
        st.error(f"OpenStreetMap search failed: {str(e)}")
        return []

def show_page():
    st.title(" Prescription → Nearby Specialist Finder")
    st.caption("Upload a prescription photo, I'll OCR the text, guess the right medical specialty, and list nearby doctors.")
    with st.expander("⚠️ Notes & disclaimers", expanded=False):
        st.markdown("""
        - **This is a demo**. OCR on handwritten prescriptions can be imperfect. Please **review results** before using.
        - **Privacy:** The image is processed locally by your app. Be sure to comply with your institution's privacy policies.
        - **Location data:** For best results, share a city/pincode or latitude/longitude.
        - **APIs:** Google Places requires an API key. OpenStreetMap Overpass is free but has rate limits.
        """)

    uploaded_file = st.file_uploader(
        "Upload a prescription photo (PNG/JPG)",
        type=["png", "jpg", "jpeg"]
    )

    col_left, col_right = st.columns([1, 1])

    ocr_text = ""
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file).convert("RGB")
            with col_left:
                st.image(image, caption="Uploaded image", use_container_width=True)
            with st.spinner("Extracting text from image..."):
                ocr_text = extract_text_from_image(image)
            with col_right:
                st.subheader("Extracted text (OCR)")
                st.text_area("Text", value=ocr_text, height=250, key="ocr_result")
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

    suggested_specialties = []
    conditions = []
    if ocr_text.strip():
        with st.spinner("Analyzing text..."):
            conditions = extract_conditions(ocr_text)
            suggested_specialties = predict_specialties(ocr_text, conditions)

    st.divider()
    st.subheader("Step 2: Choose specialty and search area")

    default_spec = suggested_specialties[0] if suggested_specialties else ""
    specialty = st.selectbox(
        "Suggested specialty (you can change it)",
        options=[""] + ALL_SPECIALTIES,
        index=([""] + ALL_SPECIALTIES).index(default_spec) if default_spec in ALL_SPECIALTIES else 0
    )
    if not specialty:
        st.caption("Tip: a specialty will appear here after OCR, or pick one manually.")

    loc_col1, loc_col2 = st.columns([1, 1])
    with loc_col1:
        place_text = st.text_input("City / Area / Pincode (e.g., 'Chennai 600113')", value="")
    with loc_col2:
        latlon = st.text_input("Or latitude,longitude (e.g., 13.0827,80.2707)", value="")

    source = st.radio(
        "Data source",
        ["Google Places (requires API key)", "OpenStreetMap (free, rate-limited)"],
        index=0,
        horizontal=True
    )

    radius_m = st.slider("Search radius (meters)", 1000, 20000, 5000, step=500)

    if st.button("🔎 Find nearby specialists", type="primary"):
        if not specialty:
            st.error("Please choose a specialty first.")
        else:
            lat, lon = None, None
            if latlon.strip():
                try:
                    parts = [float(p.strip()) for p in latlon.split(",")]
                    if len(parts) == 2:
                        lat, lon = parts[0], parts[1]
                except Exception:
                    st.error("Invalid latitude,longitude format.")
            if lat is None and place_text.strip():
                with st.spinner("Getting location coordinates..."):
                    geocoded = geocode_location(place_text.strip())
                    if geocoded:
                        lat, lon = geocoded["lat"], geocoded["lon"]
                        st.success(f"Found location: {geocoded['display_name']}")
                    else:
                        st.error("Could not geocode the place text. Try latitude,longitude.")

            if lat is None or lon is None:
                st.warning("Provide a location to search (city/pincode or lat,lon).")
            else:
                with st.spinner("Searching nearby providers..."):
                    results = []
                    if source.startswith("Google"):
                        api_key = os.getenv("GOOGLE_MAPS_API_KEY", "")
                        if not api_key:
                            st.error("GOOGLE_MAPS_API_KEY not set in environment variables.")
                        else:
                            results = search_google_places(specialty, lat, lon, radius_m, api_key)
                    else:
                        results = search_overpass(specialty, lat, lon, radius_m)

                if results:
                    st.success(f"Found {len(results)} result(s) for {specialty}")
                    display_results = []
                    for r in results:
                        display_results.append({
                            "Name": r.get("name", "Unknown"),
                            "Address": r.get("address", "No address"),
                            "Rating": r.get("rating", "N/A"),
                        })
                    st.dataframe(display_results, use_container_width=True)
                    st.subheader("Quick Links")
                    for i, r in enumerate(results[:10]):
                        if r.get("maps_url"):
                            st.markdown(f"**{i+1}.** [{r.get('name', '(no name)')}]({r['maps_url']}) — {r.get('address', '')}")
                        elif r.get('lat') and r.get('lon'):
                            maps_url = make_google_maps_url(r.get('name', ''), r.get('lat'), r.get('lon'))
                            st.markdown(f"**{i+1}.** [{r.get('name', '(no name)')}]({maps_url}) — {r.get('address', '')}")
                        else:
                            st.markdown(f"**{i+1}.** {r.get('name', '(no name)')} — {r.get('address', '')}")
                else:
                    st.info("No results found in this radius. Try a larger radius or a broader specialty.")

    if st.checkbox("Show debug information"):
        st.divider()
        st.subheader("Debug info")
        st.json({
            "conditions_found": conditions,
            "suggested_specialties": suggested_specialties,
            "ocr_text_length": len(ocr_text) if ocr_text else 0
        })

# This is the crucial part that was missing from your code.
# It tells Python to run the show_page() function when the script is executed.
if __name__ == "__main__":
    show_page()
