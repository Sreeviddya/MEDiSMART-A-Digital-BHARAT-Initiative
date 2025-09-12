import streamlit as st
import datetime
import pandas as pd
import random

# --- Simulated Data ---
# This data is not real and is for demonstration purposes only.
urgent_blood_requirements = [
    {"blood_type": "O+ Positive", "location": "Chennai, Tamil Nadu", "urgency": "High", "hospital": "Apollo Hospitals, Greams Road, Chennai", "contact": "98765-43210"},
    {"blood_type": "A- Negative", "location": "Delhi", "urgency": "Urgent", "hospital": "AIIMS, Ansari Nagar, New Delhi", "contact": "99887-76655"},
    {"blood_type": "B+ Positive", "location": "Mumbai, Maharashtra", "urgency": "Medium", "hospital": "Fortis Hospital, Mulund, Mumbai", "contact": "90000-11111"},
    {"blood_type": "AB- Negative", "location": "Bangalore, Karnataka", "urgency": "High", "hospital": "Manipal Hospitals, Old Airport Road, Bangalore", "contact": "88888-22222"},
    {"blood_type": "O- Negative", "location": "Hyderabad, Telangana", "urgency": "Urgent", "hospital": "Yashoda Hospitals, Secunderabad", "contact": "77777-33333"},
    {"blood_type": "A+ Positive", "location": "Kolkata, West Bengal", "urgency": "Medium", "hospital": "Medica Superspecialty Hospital, Mukundapur", "contact": "66666-44444"},
    {"blood_type": "B- Negative", "location": "Ahmedabad, Gujarat", "urgency": "High", "hospital": "Care Institute of Medical Sciences, Sola", "contact": "55555-55555"},
    {"blood_type": "AB+ Positive", "location": "Jaipur, Rajasthan", "urgency": "Urgent", "hospital": "Eternal Hospital, Jagatpura, Jaipur", "contact": "44444-66666"},
    {"blood_type": "O+ Positive", "location": "Lucknow, Uttar Pradesh", "urgency": "Medium", "hospital": "Indira Gandhi Hospital, Gomti Nagar", "contact": "33333-77777"},
    {"blood_type": "A- Negative", "location": "Pune, Maharashtra", "urgency": "High", "hospital": "Ruby Hall Clinic, Bund Garden Road", "contact": "22222-88888"},
    {"blood_type": "B+ Positive", "location": "Nagpur, Maharashtra", "urgency": "Urgent", "hospital": "Wockhardt Hospital, Shankar Nagar", "contact": "11111-99999"},
    {"blood_type": "O- Negative", "location": "Indore, Madhya Pradesh", "urgency": "Medium", "hospital": "Bombay Hospital, Ring Road", "contact": "98765-12345"},
]

free_camps = [
    {"type": "General Health Checkup", "location": "A. K. Nagar Community Hall, Chennai", "date": "15th October 2025", "timings": "9:00 AM - 4:00 PM"},
    {"type": "Eye & Dental Camp", "location": "Vivekananda Park, Kolkata", "date": "22nd October 2025", "timings": "10:00 AM - 5:00 PM"},
    {"type": "Diabetes & BP Screening", "location": "Shivaji Nagar Public Ground, Pune", "date": "29th October 2025", "timings": "8:30 AM - 3:30 PM"},
    {"type": "Women's Health Camp", "location": "Begumpet Community Center, Hyderabad", "date": "5th November 2025", "timings": "9:00 AM - 4:00 PM"},
    {"type": "Cardiac Screening", "location": "Jalianwala Bagh Park, Amritsar", "date": "12th November 2025", "timings": "10:00 AM - 5:00 PM"},
    {"type": "Pediatric Health Camp", "location": "BHEL Community Hall, Bhopal", "date": "19th November 2025", "timings": "9:00 AM - 3:00 PM"},
    {"type": "Bone Density & Arthritis", "location": "Sector-15 Park, Gurgaon", "date": "26th November 2025", "timings": "9:30 AM - 4:00 PM"},
    {"type": "Mental Health Awareness", "location": "New Delhi Central Library", "date": "3rd December 2025", "timings": "11:00 AM - 2:00 PM"},
]

scanning_discounts = [
    {"center": "SRL Diagnostics", "address": "12, MG Road, Chennai", "discount": "Up to 30% off on all scans", "valid_until": "31-Dec-2025"},
    {"center": "Dr. Lal PathLabs", "address": "5, Defence Colony, New Delhi", "discount": "20% off on MRI and CT scans", "valid_until": "15-Jan-2026"},
    {"center": "Thyrocare", "address": "45, Linking Road, Mumbai", "discount": "Flat 25% off on full body checkups", "valid_until": "28-Feb-2026"},
    {"center": "Metropolis Healthcare", "address": "88, Indira Nagar, Bangalore", "discount": "15% off on X-Rays and Ultrasounds", "valid_until": "30-Apr-2026"},
]

pharmacy_discounts = [
    {"store": "Apollo Pharmacy", "address": "10, Anna Salai, Chennai", "offer": "10% off on all prescription medicines"},
    {"store": "MedPlus Pharmacy", "address": "25, Karol Bagh, New Delhi", "offer": "Buy one get one free on select health supplements"},
    {"store": "Wellness Forever", "address": "4, Colaba, Mumbai", "offer": "Up to 50% off on wellness products"},
    {"store": "Netmeds Store", "address": "Online", "offer": "Flat 20% off on first order through E-Hospital portal"},
]

general_tips = [
    " Stay hydrated by drinking at least 8 glasses of water a day, more in hot weather.",
    " Eat a balanced diet with plenty of fruits and vegetables to boost your immunity.",
    " Regular exercise for at least 30 minutes a day can significantly improve your mental and physical health.",
    " Aim for 7-8 hours of quality sleep each night for a refreshed mind and body.",
    " Spend at least 15 minutes in the sun each day to get your daily dose of Vitamin D.",
    " Practice mindfulness or meditation for 10 minutes daily to reduce stress and anxiety.",
    " Get your annual health checkup done to monitor your well-being and catch issues early.",
    " Include leafy greens like spinach and kale in your diet for essential vitamins.",
    " Read food labels carefully to monitor your sugar, salt, and fat intake.",
]

health_news = [
    {
        "title": "Government launches new health insurance scheme for rural families",
        "summary": "A new health insurance program, 'Gramin Suraksha Yojna,' aims to provide affordable healthcare access to millions of families in rural areas. The scheme offers comprehensive coverage for major surgeries and treatments, with a focus on remote and underserved populations.",
        "source": "Ministry of Health & Family Welfare"
    },
    {
        "title": "Study reveals benefits of plant-based diet on heart health",
        "summary": "A recent study published in the Indian Journal of Medicine shows a strong correlation between a plant-based diet and reduced risk of cardiovascular diseases. The study tracked thousands of participants over a decade, and experts recommend a gradual transition to such diets for better long-term health outcomes.",
        "source": "Indian Medical Association"
    },
    {
        "title": "AI-powered diagnostics tool receives approval for public use",
        "summary": "The new AI-based diagnostic tool, designed to detect early signs of retinal diseases, has been approved for use in public hospitals. The technology uses machine learning to analyze eye scans, promising to improve diagnostic accuracy and speed, especially in remote clinics with limited access to specialists.",
        "source": "National Health Authority"
    },
    {
        "title": "Awareness campaign launched to combat antibiotic resistance",
        "summary": "A nationwide campaign titled 'Antibiotic Savdhani' has been launched to educate the public on the dangers of self-medication and improper use of antibiotics. The initiative aims to reduce the growing threat of antimicrobial resistance in India.",
        "source": "Indian Council of Medical Research"
    },
]

# --- Mock AI Data Sets (10 per category) ---
mock_health_assistant_responses = [
    "Staying hydrated is key to good health. It helps with nutrient transport, body temperature regulation, and joint lubrication.",
    "For a strong immune system, focus on a diet rich in Vitamin C, Zinc, and antioxidants, found in citrus fruits, nuts, and leafy greens.",
    "Stress management is crucial. Simple techniques like deep breathing, meditation, or a short walk can significantly reduce anxiety.",
    "A good night's sleep is as important as diet and exercise. Aim for 7-9 hours to allow your body to repair and regenerate.",
    "Regular physical activity, even a brisk walk, can improve cardiovascular health, strengthen muscles, and boost your mood.",
    "Proper hand hygiene is the first line of defense against many common infections. Wash your hands with soap and water frequently.",
    "Eating a variety of whole foods, including fruits, vegetables, lean proteins, and whole grains, provides the necessary nutrients for overall well-being.",
    "Listen to your body. If you feel tired or unwell, give yourself time to rest and recover. Pushing through can sometimes make things worse.",
    "Vitamin D, often called the 'sunshine vitamin,' is essential for bone health. Spend a few minutes outdoors each day or consider a supplement after consulting a doctor.",
    "Regular health check-ups can help catch potential issues early, making them easier to manage and treat."
]

mock_symptom_data = {
    "fever, cough, body aches": {
        "conditions": ["Common Cold", "Influenza (Flu)", "COVID-19"],
        "advice": "Rest, stay hydrated, and take over-the-counter medication to manage fever and aches. If symptoms worsen or you have difficulty breathing, consult a doctor."
    },
    "headache, nausea, sensitivity to light": {
        "conditions": ["Migraine", "Sinusitis", "Dehydration"],
        "advice": "Find a dark, quiet room to rest. Drink water and avoid screens. If the headache is severe or persistent, seek medical attention."
    },
    "sore throat, runny nose, sneezing": {
        "conditions": ["Allergies", "Common Cold", "Minor viral infection"],
        "advice": "Use saline nasal sprays or gargle with warm salt water. Stay home to avoid spreading germs, and consider allergy medication if it is a recurring issue."
    },
    "chest pain, shortness of breath, dizziness": {
        "conditions": ["Anxiety attack", "Heartburn", "Potential cardiac issue"],
        "advice": "**This is an emergency. Immediately seek professional medical help.** Do not wait."
    },
    "skin rash, itching, redness": {
        "conditions": ["Allergic reaction", "Eczema", "Hives"],
        "advice": "Wash the area with cool water and avoid scratching. An over-the-counter antihistamine may help. If swelling or difficulty breathing occurs, get immediate help."
    },
    "stomach pain, diarrhea, vomiting": {
        "conditions": ["Food poisoning", "Stomach flu (gastroenteritis)", "Irritable Bowel Syndrome (IBS)"],
        "advice": "Drink small sips of water to stay hydrated and avoid solid foods for a few hours. If symptoms persist for more than a day, see a doctor."
    },
    "joint pain, stiffness, swelling": {
        "conditions": ["Arthritis", "Gout", "Injury"],
        "advice": "Apply a cold compress and rest the affected joint. Consult a doctor for a proper diagnosis and treatment plan, especially if pain is severe or chronic."
    },
    "fatigue, weight loss, increased thirst": {
        "conditions": ["Diabetes", "Thyroid disorder", "Chronic fatigue syndrome"],
        "advice": "These symptoms require a medical evaluation. Schedule an appointment with a doctor for blood tests to determine the cause."
    },
    "muscle weakness, numbness, tingling": {
        "conditions": ["Nerve compression", "Vitamin deficiency", "Multiple Sclerosis"],
        "advice": "This can indicate a serious neurological issue. See a doctor promptly for a proper diagnosis and to rule out serious conditions."
    },
    "blurred vision, frequent urination, dry mouth": {
        "conditions": ["Diabetes", "Dehydration", "Cataracts"],
        "advice": "Consult a doctor for a check-up, especially for blood sugar levels. Staying hydrated can help with some symptoms, but a diagnosis is necessary."
    }
}

mock_diet_plans = {
    "Weight Loss": [
        "**Breakfast:** Oatmeal with berries and a handful of almonds.\n**Lunch:** Large salad with grilled chicken breast and a light vinaigrette.\n**Dinner:** Baked salmon with steamed broccoli and quinoa.",
        "**Breakfast:** Scrambled eggs with spinach and whole-wheat toast.\n**Lunch:** Lentil soup with a side of mixed greens.\n**Dinner:** Turkey stir-fry with a variety of vegetables and brown rice.",
        "**Breakfast:** Greek yogurt with chia seeds and half a sliced apple.\n**Lunch:** Tuna salad sandwich on whole-grain bread with lettuce and tomato.\n**Dinner:** Chicken and vegetable skewers with a light yogurt dip.",
        "**Breakfast:** Protein smoothie with spinach, banana, and almond milk.\n**Lunch:** Black bean and corn salad with chopped bell peppers.\n**Dinner:** Grilled cod with roasted asparagus and sweet potato.",
        "**Breakfast:** A slice of avocado toast on rye bread.\n**Lunch:** A bowl of minestrone soup and a side of hummus with carrot sticks.\n**Dinner:** Lean beef patty on a lettuce bun with sliced tomatoes and onions.",
        "**Breakfast:** Cottage cheese with a sprinkle of walnuts and peaches.\n**Lunch:** Leftover dinner, a healthy and easy choice.\n**Dinner:** Vegetarian chili loaded with beans and vegetables.",
        "**Breakfast:** Whole-grain cereal with low-fat milk and a small banana.\n**Lunch:** A large, fresh garden salad with chickpeas and a light dressing.\n**Dinner:** Baked tofu with a side of stir-fried vegetables.",
        "**Breakfast:** Boiled egg with a side of fresh fruit.\n**Lunch:** Chicken tortilla soup with a small dollop of Greek yogurt.\n**Dinner:** Lentil and vegetable curry with a small portion of basmati rice.",
        "**Breakfast:** Smoothie with protein powder, kale, and mixed berries.\n**Lunch:** A sandwich on whole-wheat bread with lean ham and a slice of Swiss cheese.\n**Dinner:** Turkey meatballs with zucchini noodles and tomato sauce.",
        "**Breakfast:** Plain Greek yogurt with cinnamon and a tablespoon of honey.\n**Lunch:** Large portion of roasted vegetables (carrots, bell peppers, onions) with a small piece of cheese.\n**Dinner:** Lean steak with a side of sauteed mushrooms and green beans."
    ],
    "Muscle Gain": [
        "**Breakfast:** Scrambled eggs with cheese and spinach. A side of two pieces of bacon.\n**Lunch:** Large chicken salad with mixed greens, nuts, and high-protein dressing.\n**Dinner:** Beef steak with a side of quinoa and roasted vegetables.",
        "**Breakfast:** Protein shake with oats, banana, and peanut butter.\n**Lunch:** Tuna and pasta salad with a creamy sauce.\n**Dinner:** Grilled salmon with sweet potatoes and broccoli.",
        "**Breakfast:** Whole-wheat pancakes topped with Greek yogurt and berries.\n**Lunch:** Turkey and cheese sandwich on whole-grain bread with a side of cottage cheese.\n**Dinner:** Lean beef burgers with cheese and a side of green salad and roasted potatoes.",
        "**Breakfast:** Three-egg omelet with mushrooms and bell peppers.\n**Lunch:** Chicken breast with a side of rice and black beans.\n**Dinner:** Shrimp stir-fry with a variety of vegetables and a side of jasmine rice.",
        "**Breakfast:** A large bowl of oatmeal with protein powder, nuts, and seeds.\n**Lunch:** A large bowl of chili with beef and kidney beans.\n**Dinner:** Pork chops with a side of mashed potatoes and steamed carrots.",
        "**Breakfast:** Cottage cheese with fresh fruit and a handful of almonds.\n**Lunch:** Chicken wraps with whole-wheat tortillas, hummus, and a variety of vegetables.\n**Dinner:** A large bowl of beef stew with lots of potatoes and vegetables.",
        "**Breakfast:** Greek yogurt with granola and a handful of berries.\n**Lunch:** Grilled chicken salad with a side of corn on the cob.\n**Dinner:** Lamb chops with a side of roasted cauliflower and sweet potato.",
        "**Breakfast:** Smoothie with protein powder, banana, spinach, and almond milk.\n**Lunch:** A large bowl of lentil soup with a side of whole-wheat bread.\n**Dinner:** Fish fillet with a side of brown rice and steamed asparagus.",
        "**Breakfast:** Four-egg omelet with a side of fresh fruit.\n**Lunch:** Leftover dinner from the previous night, a healthy and easy choice.\n**Dinner:** Lean ground turkey with a side of rice and beans.",
        "**Breakfast:** Three hard-boiled eggs with a side of whole-wheat toast.\n**Lunch:** Tuna melt on whole-wheat bread with a side of salad.\n**Dinner:** Grilled steak with a side of roasted potatoes and carrots."
    ],
    "General Wellness": [
        "**Breakfast:** Oatmeal with fruit and nuts.\n**Lunch:** Salad with grilled chicken, mixed greens, and vegetables.\n**Dinner:** Salmon with roasted sweet potatoes and asparagus.",
        "**Breakfast:** Greek yogurt with a variety of berries and seeds.\n**Lunch:** Whole-grain wrap with hummus and fresh veggies.\n**Dinner:** Stir-fried tofu with brown rice and a mix of colorful vegetables.",
        "**Breakfast:** Scrambled eggs with spinach and a slice of whole-wheat toast.\n**Lunch:** A hearty lentil soup with a side salad.\n**Dinner:** Chicken breast with a side of quinoa and steamed broccoli.",
        "**Breakfast:** A fruit smoothie with a scoop of protein powder.\n**Lunch:** A large salad with grilled shrimp, chickpeas, and a light dressing.\n**Dinner:** Baked cod with roasted root vegetables.",
        "**Breakfast:** Whole-wheat toast with avocado and a sprinkle of chili flakes.\n**Lunch:** Leftover dinner from the previous night.\n**Dinner:** Vegetable and lentil curry with a small portion of basmati rice.",
        "**Breakfast:** Cottage cheese with fresh berries and a handful of almonds.\n**Lunch:** Tuna sandwich on whole-grain bread with lettuce and tomato.\n**Dinner:** Lean beef stir-fry with vegetables and a small portion of noodles.",
        "**Breakfast:** Whole-grain cereal with milk and a small banana.\n**Lunch:** A warm bowl of minestrone soup with a side of toasted bread.\n**Dinner:** Turkey meatballs with tomato sauce and zucchini noodles.",
        "**Breakfast:** Two hard-boiled eggs with a side of fresh fruit.\n**Lunch:** A large, fresh garden salad with a variety of vegetables and a light vinaigrette.\n**Dinner:** Grilled fish fillet with a side of steamed vegetables.",
        "**Breakfast:** A slice of whole-wheat toast with a little peanut butter and a banana.\n**Lunch:** A large bowl of vegetarian chili.\n**Dinner:** Chicken and vegetable skewers with a light yogurt dip.",
        "**Breakfast:** Plain Greek yogurt with a little honey and cinnamon.\n**Lunch:** Leftover salad with a variety of vegetables and a side of grilled chicken.\n**Dinner:** Lean pork chops with a side of roasted potatoes and steamed green beans."
    ]
}

mock_drug_info = {
    "Paracetamol": {
        "Uses": "Used to relieve mild to moderate pain, such as headaches, menstrual periods, and toothaches. It is also used to reduce fever.",
        "Side Effects": "Common side effects include nausea, stomach pain, and loss of appetite. Less common but serious effects can be liver damage if taken in high doses.",
        "Precautions": "Do not take more than the recommended dose. Avoid alcohol consumption while on this medication. Inform your doctor if you have a history of liver or kidney disease."
    },
    "Ibuprofen": {
        "Uses": "A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, reduce fever, and treat inflammation. Commonly used for headaches, arthritis, and menstrual pain.",
        "Side Effects": "Common side effects include stomach upset, nausea, heartburn, and dizziness. Long-term use can increase the risk of stomach bleeding.",
        "Precautions": "Take with food or milk to reduce stomach irritation. Inform your doctor if you have a history of heart disease, stomach ulcers, or high blood pressure."
    },
    "Amoxicillin": {
        "Uses": "A penicillin antibiotic used to treat bacterial infections, such as pneumonia, bronchitis, ear infections, and urinary tract infections. It is not effective against viral infections.",
        "Side Effects": "Common side effects include diarrhea, nausea, and rash. A more serious but rare side effect is a severe allergic reaction.",
        "Precautions": "Complete the full course of treatment, even if you feel better. Do not use if you have a known allergy to penicillin. Consult your doctor if you experience a severe rash."
    },
    "Loratadine": {
        "Uses": "An antihistamine used to relieve allergy symptoms such as sneezing, runny nose, itchy eyes, and hives. It is a non-drowsy medication.",
        "Side Effects": "Common side effects are dry mouth, headache, and fatigue. These are usually mild and go away as your body adjusts.",
        "Precautions": "Inform your doctor about any other medications you are taking. Use caution if you have a history of liver or kidney problems."
    },
    "Metformin": {
        "Uses": "A medication used to treat Type 2 diabetes. It works by controlling blood sugar levels and improving the body's response to insulin.",
        "Side Effects": "Common side effects include nausea, diarrhea, stomach upset, and a metallic taste in the mouth. These often improve over time.",
        "Precautions": "Do not consume large amounts of alcohol while on this medication. Inform your doctor if you are scheduled for any medical imaging that requires contrast dye."
    },
    "Aspirin": {
        "Uses": "Used to reduce pain, fever, and inflammation. It is also a blood thinner and is often prescribed to reduce the risk of heart attacks and strokes.",
        "Side Effects": "Can cause stomach upset, nausea, and heartburn. It can also increase the risk of bleeding.",
        "Precautions": "Do not give to children or teenagers with viral infections due to the risk of Reye's syndrome. Consult a doctor before use if you are on other blood thinners."
    },
    "Omeprazole": {
        "Uses": "A proton pump inhibitor used to treat heartburn, acid reflux, and stomach ulcers by reducing the amount of acid the stomach produces.",
        "Side Effects": "Common side effects are headache, stomach pain, and nausea. Long-term use can affect vitamin B12 absorption.",
        "Precautions": "Take about 30 minutes before a meal. Do not crush or chew the capsule. Consult a doctor if symptoms do not improve."
    },
    "Hydrochlorothiazide": {
        "Uses": "A diuretic (water pill) used to treat high blood pressure and fluid retention (edema) caused by various medical conditions.",
        "Side Effects": "Can cause dizziness, lightheadedness, and an increase in urination. It can also cause a loss of potassium.",
        "Precautions": "Regularly monitor blood pressure and potassium levels. Do not stop taking this medication suddenly without consulting your doctor."
    },
    "Cetirizine": {
        "Uses": "An antihistamine used to treat symptoms of hay fever and other allergies, such as sneezing and itchy, watery eyes. It is also used to treat hives and itching.",
        "Side Effects": "Common side effects include drowsiness, dry mouth, and fatigue. It is generally well-tolerated.",
        "Precautions": "Use caution when driving or operating heavy machinery until you know how this medication affects you. Avoid alcohol consumption while on this drug."
    },
    "Levothyroxine": {
        "Uses": "A thyroid hormone replacement used to treat hypothyroidism (underactive thyroid). It restores hormone levels to a normal range.",
        "Side Effects": "Can cause heart palpitations, anxiety, sweating, and weight loss if the dose is too high. It is important to find the right dosage.",
        "Precautions": "Take on an empty stomach, at least 30-60 minutes before breakfast. Avoid taking it at the same time as iron or calcium supplements."
    }
}

mock_fitness_plans = {
    "Build Strength": [
        "**Warm-up:** 5 minutes of light cardio (jumping jacks or jogging in place).\n**Workout:** 3 sets of 10 reps each: Push-ups, Squats, Lunges, and Plank for 30 seconds.\n**Cool-down:** 5 minutes of stretching for arms and legs.",
        "**Warm-up:** 5 minutes of arm circles and leg swings.\n**Workout:** 3 sets of 8 reps each: Overhead Press, Bent-over Rows, Deadlifts, and Kettlebell Swings.\n**Cool-down:** 5 minutes of static stretching for all major muscle groups.",
        "**Warm-up:** 5 minutes on a stationary bike.\n**Workout:** 4 sets of 6 reps each: Bench Press, Pull-ups, Barbell Rows, and Leg Press.\n**Cool-down:** 5 minutes of foam rolling for back and legs.",
        "**Warm-up:** 5 minutes of light stretching.\n**Workout:** 3 sets of 12 reps each: Bicep Curls, Tricep Dips, Shoulder Press, and Calf Raises.\n**Cool-down:** 5 minutes of light cardio and a final stretch.",
        "**Warm-up:** 5 minutes of jumping rope.\n**Workout:** 4 sets of 8 reps each: Squats, Push-ups, Pull-ups, and Dips.\n**Cool-down:** 5 minutes of deep breathing and stretching for tired muscles.",
        "**Warm-up:** 5 minutes of jogging.\n**Workout:** 3 sets of 10 reps each: Bench press, Bicep curls, Tricep extensions, and Squats.\n**Cool-down:** 5 minutes of static stretches for all major muscle groups.",
        "**Warm-up:** 5 minutes of leg swings and arm circles.\n**Workout:** 3 sets of 10 reps each: Squats, Push-ups, Lunges, and Planks.\n**Cool-down:** 5 minutes of static stretches for legs and back.",
        "**Warm-up:** 5 minutes on the elliptical machine.\n**Workout:** 3 sets of 10 reps each: Overhead Press, Bent-over Rows, Deadlifts, and Dumbbell Curls.\n**Cool-down:** 5 minutes of foam rolling and a final stretch.",
        "**Warm-up:** 5 minutes of high-knees and butt kicks.\n**Workout:** 4 sets of 6 reps each: Bench Press, Pull-ups, Barbell Rows, and Leg Press.\n**Cool-down:** 5 minutes of static stretching for arms and legs.",
        "**Warm-up:** 5 minutes of dynamic stretching.\n**Workout:** 3 sets of 12 reps each: Bicep Curls, Tricep Dips, Shoulder Press, and Calf Raises.\n**Cool-down:** 5 minutes of light jogging and a final stretch."
    ],
    "Improve Cardio": [
        "**Warm-up:** 5 minutes of brisk walking.\n**Workout:** 30 minutes of jogging at a steady pace.\n**Cool-down:** 5 minutes of walking and stretching.",
        "**Warm-up:** 5 minutes of jumping jacks.\n**Workout:** 20 minutes of high-intensity interval training (HIIT) with burpees, mountain climbers, and squats.\n**Cool-down:** 5 minutes of light stretching and deep breathing.",
        "**Warm-up:** 5 minutes of light jogging.\n**Workout:** 30 minutes on an elliptical machine at a moderate pace.\n**Cool-down:** 5 minutes of walking and static stretching.",
        "**Warm-up:** 5 minutes of brisk walking.\n**Workout:** 25 minutes on a stationary bike with varied resistance levels.\n**Cool-down:** 5 minutes of walking and stretching for quads and hamstrings.",
        "**Warm-up:** 5 minutes of jumping rope.\n**Workout:** 30 minutes of swimming laps at a steady pace.\n**Cool-down:** 5 minutes of a gentle swim and stretching.",
        "**Warm-up:** 5 minutes of brisk walking.\n**Workout:** 30 minutes on a treadmill with varied incline and speed.\n**Cool-down:** 5 minutes of a slow walk and static stretching.",
        "**Warm-up:** 5 minutes of arm and leg swings.\n**Workout:** 20 minutes of HIIT with burpees, high knees, and mountain climbers.\n**Cool-down:** 5 minutes of deep breathing and stretching for quads and calves.",
        "**Warm-up:** 5 minutes of light jogging.\n**Workout:** 30 minutes of a steady jog in a park.\n**Cool-down:** 5 minutes of walking and static stretches for legs and back.",
        "**Warm-up:** 5 minutes of jumping jacks.\n**Workout:** 25 minutes on a stationary bike with varied resistance levels.\n**Cool-down:** 5 minutes of a slow pedal and a final stretch.",
        "**Warm-up:** 5 minutes of arm circles and leg swings.\n**Workout:** 30 minutes of a brisk walk on a treadmill with a slight incline.\n**Cool-down:** 5 minutes of a slow walk and static stretching."
    ],
    "Increase Flexibility": [
        "**Warm-up:** 5 minutes of light cardio (walking or jogging).\n**Workout:** 15 minutes of dynamic stretching, including leg swings, arm circles, and torso twists. Hold each for 30 seconds.\n**Cool-down:** 10 minutes of static stretching, holding each stretch for 30 seconds.",
        "**Warm-up:** 5 minutes of a gentle jog.\n**Workout:** 20 minutes of Yoga poses focusing on Hamstring and Hip stretches (e.g., Downward Dog, Warrior II).\n**Cool-down:** 5 minutes of a cool down stretch.",
        "**Warm-up:** 5 minutes of light cardio.\n**Workout:** 15 minutes of foam rolling for legs and back, followed by a series of stretches for the shoulders and chest.\n**Cool-down:** 5 minutes of deep breathing and relaxation.",
        "**Warm-up:** 5 minutes of brisk walking.\n**Workout:** 20 minutes of Pilates exercises focusing on core and flexibility.\n**Cool-down:** 5 minutes of a cool down stretch for quads and hamstrings.",
        "**Warm-up:** 5 minutes of jumping jacks.\n**Workout:** 15 minutes of dynamic stretching for hips and shoulders.\n**Cool-down:** 10 minutes of static stretching for all major muscle groups, holding each for 30 seconds.",
        "**Warm-up:** 5 minutes of a gentle jog.\n**Workout:** 20 minutes of static stretches for all major muscle groups, holding each for 30 seconds.\n**Cool-down:** 5 minutes of a cool down stretch.",
        "**Warm-up:** 5 minutes of light cardio.\n**Workout:** 15 minutes of dynamic stretches, including leg swings, torso twists, and arm circles.\n**Cool-down:** 10 minutes of static stretches for arms and legs, holding each for 30 seconds.",
        "**Warm-up:** 5 minutes of brisk walking.\n**Workout:** 20 minutes of yoga poses focusing on hip and shoulder flexibility.\n**Cool-down:** 5 minutes of deep breathing and relaxation.",
        "**Warm-up:** 5 minutes of jumping jacks.\n**Workout:** 15 minutes of foam rolling for back and legs, followed by a series of static stretches.\n**Cool-down:** 5 minutes of a cool down stretch for quads and hamstrings.",
        "**Warm-up:** 5 minutes of light jogging.\n**Workout:** 20 minutes of Pilates exercises focusing on core and flexibility.\n**Cool-down:** 5 minutes of a cool down stretch for all major muscle groups."
    ]
}

def show_page():
    """Renders the main dashboard page with AI features."""
    
    st.header("Welcome to the Dashboard!")
    st.markdown("---")

    # --- AI-Powered Features Section ---
    st.subheader("Your AI-Powered Health Tools ")
    st.info("These AI features are using basic, pre-canned data for demo purposes. They are not connected to a live AI model.")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["AI Health Assistant", "Symptom Checker", "Diet Plan Generator", "Drug Information", "Fitness Coach"])

    with tab1:
        st.subheader(" Talk to a Health Assistant")
        st.write("Ask any general health question, and our assistant will provide information.")
        user_query = st.text_input("Ask a question about health, wellness, or medicine:", key="ai_query")
        
        if st.button("Get Answer", key="ai_button"):
            if user_query:
                # Use a simple hash to provide a consistent 'random' response
                response_index = len(user_query) % len(mock_health_assistant_responses)
                st.markdown(f"**Answer:** {mock_health_assistant_responses[response_index]}")
            else:
                st.warning("Please enter a question to get a response.")

    with tab2:
        st.subheader(" Symptom Checker")
        st.write("Enter your symptoms to get a list of potential conditions and advice.")
        symptoms_input = st.text_area("Describe your symptoms (e.g., 'fever, cough, body aches'):", key="symptoms_input")
        
        if st.button("Check Symptoms", key="symptoms_button"):
            if symptoms_input:
                # Find the most relevant mock data entry
                found_match = False
                for symptoms_key, data in mock_symptom_data.items():
                    if all(s.strip().lower() in symptoms_input.lower() for s in symptoms_key.split(',')):
                        st.markdown(f"**Potential Conditions:** {', '.join(data['conditions'])}")
                        st.markdown(f"**Advice:** {data['advice']}")
                        found_match = True
                        break
                if not found_match:
                    st.markdown("**Potential Conditions:** Common Cold, Minor viral infection")
                    st.markdown("**Advice:** Your symptoms are general. Rest and stay hydrated. If they persist, see a medical professional.")
            else:
                st.warning("Please enter your symptoms to get a diagnosis.")

    with tab3:
        st.subheader(" Diet Plan Generator")
        st.write("Get a personalized daily diet plan based on your health goals.")
        goal_options = ["Weight Loss", "Muscle Gain", "General Wellness"]
        health_goal = st.selectbox("Select your goal:", goal_options, key="diet_goal")
        
        if st.button("Generate Diet Plan", key="diet_button"):
            if health_goal in mock_diet_plans:
                # Pick a random diet plan from the list
                plan = random.choice(mock_diet_plans[health_goal])
                st.markdown(f"**Your Personalized Diet Plan for {health_goal}:**\n\n{plan}")

    with tab4:
        st.subheader("Drug Information")
        st.write("Get a summary, side effects, and precautions for a medication.")
        drug_name = st.text_input("Enter a medication name (e.g., 'Paracetamol'):", key="drug_name").title()
        if st.button("Get Drug Info", key="drug_info_button"):
            if drug_name in mock_drug_info:
                info = mock_drug_info[drug_name]
                st.markdown(f"**Uses:** {info['Uses']}")
                st.markdown(f"**Side Effects:** {info['Side Effects']}")
                st.markdown(f"**Precautions:** {info['Precautions']}")
            else:
                st.warning(f"No information found for '{drug_name}'. Please try another one, such as Paracetamol or Ibuprofen.")

    with tab5:
        st.subheader(" AI Fitness Coach")
        st.write("Get a simple workout plan based on your fitness goals.")
        fitness_goal = st.selectbox("Select your fitness goal:", ["Build Strength", "Improve Cardio", "Increase Flexibility"], key="fitness_goal")
        if st.button("Generate Workout Plan", key="fitness_button"):
            if fitness_goal in mock_fitness_plans:
                # Pick a random workout plan from the list
                plan = random.choice(mock_fitness_plans[fitness_goal])
                st.markdown(f"**Your Personalized Workout Plan for {fitness_goal}:**\n\n{plan}")

    st.markdown("---")
    
    # --- Data Dashboard Section ---
    st.subheader("Health Dashboard & Information Hub ")
    col1, col2 = st.columns(2)
    with col1:
        blood_df = pd.DataFrame(urgent_blood_requirements)
        st.metric(label="Total Urgent Blood Requirements", value=len(blood_df))
    with col2:
        st.metric(label="Total Free Medical Camps", value=len(free_camps))
        
    st.markdown("---")

    # --- Urgent Blood Requirements Section with Filter ---
    st.subheader("🚨 Urgent Blood Requirements")
    st.write("The following is a live list of urgent blood needs across different regions.")
    blood_df = pd.DataFrame(urgent_blood_requirements)
    
    # Interactive Filter
    blood_types = ["All"] + sorted(list(blood_df["blood_type"].unique()))
    selected_blood_type = st.selectbox("Filter by Blood Type:", blood_types, key="blood_filter")
    
    if selected_blood_type != "All":
        filtered_blood_df = blood_df[blood_df["blood_type"] == selected_blood_type]
    else:
        filtered_blood_df = blood_df
        
    st.dataframe(filtered_blood_df, hide_index=True)
    
    st.markdown("---")

    # --- Free Medical Camps Section with Search ---
    st.subheader(" Free Medical Checkup Camps")
    with st.expander("View Upcoming Camps & Find One Near You"):
        search_camp = st.text_input("Search camps by location or type:", key="camp_search")
        filtered_camps = [c for c in free_camps if search_camp.lower() in c['location'].lower() or search_camp.lower() in c['type'].lower()]
        if filtered_camps:
            for camp in filtered_camps:
                st.info(f"**{camp['type']}** at **{camp['location']}** on **{camp['date']}**")
        else:
            st.warning("No camps found matching your search.")

    st.markdown("---")

    # --- Exclusive Discounts Section ---
    st.subheader("Exclusive Discounts on Medical Services")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Medical Scanning Center Discounts"):
            st.markdown("Avail special discounts on various medical scans and tests.")
            for discount in scanning_discounts:
                st.markdown(f"**{discount['center']}**")
                st.write(f"Address: {discount['address']}")
                st.write(f"Offer: **{discount['discount']}**")
                st.write(f"Valid Until: {discount['valid_until']}")
                st.markdown("---")
    with col2:
        with st.expander("Pharmacy Discounts & Offers"):
            st.markdown("Get discounts on your medicines and health products.")
            for offer in pharmacy_discounts:
                st.markdown(f"**{offer['store']}**")
                st.write(f"Address: {offer['address']}")
                st.write(f"Offer: **{offer['offer']}**")
                st.markdown("---")
    
    st.markdown("---")
    
    # --- Health News & Articles ---
    st.subheader(" Health News & Articles")
    with st.expander("Read the latest news"):
        for news in health_news:
            st.markdown(f"**{news['title']}**")
            st.write(f"*{news['summary']}*")
            st.caption(f"Source: {news['source']}")
            st.markdown("---")

    # --- General Health Tips Section ---
    st.subheader(" General Health Information")
    today_tip = general_tips[datetime.date.today().day % len(general_tips)]
    st.warning(f"**Daily Tip:** {today_tip}")
    
    st.markdown("---")
    st.subheader("Latest Announcements")
    st.info("The e-prescription feature will be available soon in your region. Stay tuned for updates!")
