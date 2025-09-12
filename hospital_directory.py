import streamlit as st
import streamlit.components.v1 as components

def show_page():
    """
    Renders the complete eHospital Implementation Dashboard.
    All logic and UI components are compiled within this single function.
    """
    st.title("eHospital Implementation Dashboard")

    # --- New Streamlit UI elements in the sidebar ---
    st.sidebar.markdown(
        """
        <style>
            .sidebar-title {
                font-size: 1.5rem;
                font-weight: bold;
                color: #007bff;
                margin-bottom: 20px;
                text-align: center;
            }
            .stMetric label {
                color: #333;
                font-size: 1.1rem;
            }
        </style>
        <div class="sidebar-title">Key Metrics</div>
        """, unsafe_allow_html=True
    )
    st.sidebar.metric(label="Total Active Hospitals (Today)", value="246")
    st.sidebar.metric(label="Total Patient Registrations", value="51.25 Crore", delta="1.2% daily increase")
    st.sidebar.metric(label="ABHA Created", value="24.62 Lakhs")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Filter Dashboard (Work in Progress)")
    st.sidebar.selectbox("Select State", ["All States", "ANDHRA PRADESH", "ASSAM", "DELHI", "KARNATAKA"], key="state_filter")
    st.sidebar.date_input("Select Date Range", value=())

    # --- End of new Streamlit UI elements ---

    # Our HTML Dashboard
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>eHospital Dashboard</title>
      <script src="https://cdn.tailwindcss.com"></script>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
      <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
      <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
      <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
      <script src="https://code.highcharts.com/maps/highmaps.js"></script>
      <script src="https://code.highcharts.com/mapdata/countries/in/in-all.js"></script>
      <style>
        body {
          font-family: 'Inter', sans-serif;
        }
        .dataTables_wrapper .dataTables_filter input {
            border-radius: 9999px !important;
            padding: 8px 16px !important;
            border: 1px solid #e5e7eb !important;
        }
        .dataTables_wrapper .dataTables_length select {
            border-radius: 9999px !important;
            border: 1px solid #e5e7eb !important;
        }
      </style>
    </head>
    <body class="bg-gray-100 p-4 sm:p-8">
      <div class="max-w-7xl mx-auto">
        <!-- Top Navigation Buttons -->
        <div class="flex flex-wrap justify-center gap-2 sm:gap-4 mb-8">
          <button class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-full shadow-md transition-transform transform hover:scale-105">State wise Dashboard</button>
          <button class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-full shadow-md transition-transform transform hover:scale-105">Instance wise Dashboard</button>
          <button class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-full shadow-md transition-transform transform hover:scale-105">ABDM Dashboard</button>
          <button class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-full shadow-md transition-transform transform hover:scale-105">Other Dashboard</button>
        </div>

        <!-- Main Dashboard Content: Status Boxes and Map -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 mb-8">
          <!-- Left Panel: eHospital Status -->
          <div class="lg:col-span-1 p-6 bg-white rounded-xl shadow-md">
            <h4 class="text-xl font-semibold mb-4 text-center text-gray-800">eHospital Status</h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 gap-4">
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Today's Active Hospitals : <b class="text-blue-600">246</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Patient Registration : <b class="text-blue-600">51,25,77,594</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Admission : <b class="text-blue-600">4,02,31,262</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Prescription : <b class="text-blue-600">1,18,01,002</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Laboratory Report : <b class="text-blue-600">2,20,73,926</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Radiology Report : <b class="text-blue-600">7,71,552</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Discharge Summary : <b class="text-blue-600">1,64,07,381</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">ABHA Created : <b class="text-blue-600">24,62,094</b></div>
              <div class="p-4 bg-gray-50 rounded-lg shadow-inner">Health Record Link Request : <b class="text-blue-600">3,52,27,554</b></div>
            </div>
          </div>

          <!-- Right Panel: Map -->
          <div class="lg:col-span-2 p-6 bg-white rounded-xl shadow-md flex flex-col items-center justify-center">
            <h4 class="text-xl font-semibold mb-4 text-center text-gray-800">eHospital Implementation</h4>
            <div id="india-map" class="w-full h-[500px] rounded-xl shadow-inner"></div>
          </div>
        </div>

        <!-- State Data Table -->
        <div class="p-6 bg-white rounded-xl shadow-md overflow-x-auto">
          <h4 class="text-xl font-semibold mb-4 text-center text-gray-800">State-wise eHospital Data</h4>
          <table id="stateTable" class="w-full display" style="width:100%">
            <thead>
              <tr>
                <th>State</th>
                <th>Last Active On</th>
                <th>Patient Registration</th>
                <th>ADT</th>
                <th>Billing</th>
                <th>Clinic</th>
                <th>Lab</th>
                <th>Radiology</th>
                <th>ABHA Created</th>
                <th>ABHA Linked</th>
              </tr>
            </thead>
            <tbody>
              <tr><td>ANDAMAN AND NICOBAR ISLAND</td><td>26/03/2025</td><td>12,59,947</td><td>74,650</td><td>0</td><td>0</td><td>1,51,727</td><td>0</td><td>388</td><td>62,907</td></tr>
              <tr><td>ANDHRA PRADESH</td><td>26/03/2025</td><td>2,94,56,192</td><td>24,70,788</td><td>15,738</td><td>66,95,384</td><td>51,00,848</td><td>3,46,835</td><td>2,75,307</td><td>91,79,298</td></tr>
              <tr><td>ASSAM</td><td>26/03/2025</td><td>89,26,587</td><td>4,48,566</td><td>24,849</td><td>19</td><td>0</td><td>0</td><td>3,118</td><td>1,72,650</td></tr>
              <tr><td>DELHI</td><td>26/03/2025</td><td>6,40,03,583</td><td>25,19,435</td><td>21,780</td><td>11,68,549</td><td>20,28,657</td><td>74,614</td><td>2,985</td><td>8,58,168</td></tr>
              <tr><td>KARNATAKA</td><td>26/03/2025</td><td>13,45,91,590</td><td>1,11,29,036</td><td>4,83,91,345</td><td>17,72,314</td><td>82,52,068</td><td>2,24,607</td><td>18,39,125</td><td>91,15,002</td></tr>
              <tr><td>MADHYA PRADESH</td><td>26/03/2025</td><td>8,12,82,006</td><td>1,28,35,724</td><td>91,48,872</td><td>294</td><td>48,80,573</td><td>40</td><td>24,264</td><td>2,03,345</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Highcharts Map and DataTable Activation -->
      <script>
        Highcharts.mapChart('india-map', {
          chart: { map: 'countries/in/in-all' },
          title: { text: '' },
          legend: { title: { text: 'No of active hospitals', style: { fontWeight: 'bold' } } },
          colorAxis: {
            dataClasses: [
              { to: 5, color: '#dbeafe', name: '<= 5' },
              { from: 6, to: 10, color: '#93c5fd', name: '6 to 10' },
              { from: 11, to: 50, color: '#3b82f6', name: '11 to 50' },
              { from: 51, color: '#1d4ed8', name: '> 50' }
            ]
          },
          series: [{
            data: [
              ['in-ap', 50],
              ['in-dl', 25],
              ['in-ka', 75],
              ['in-mp', 60],
              ['in-as', 15],
              ['in-tn', 40],
              ['in-up', 5]
            ],
            keys: ['hc-key', 'value'],
            joinBy: 'hc-key',
            name: 'Active Hospitals',
            states: { hover: { color: '#fcd34d' } },
            dataLabels: { enabled: true, format: '{point.name}' }
          }]
        });

        $(document).ready(function () {
          $('#stateTable').DataTable();
        });
      </script>
    </body>
    </html>
    """

    # Render the HTML inside Streamlit
    components.html(html_code, height=1200, scrolling=True)

if __name__ == "__main__":
    show_page()
