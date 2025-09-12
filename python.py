import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("eHospital Implementation Dashboard")

# Our HTML Dashboard
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>eHospital Implementation Dashboard</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
  <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
  <script src="https://code.highcharts.com/maps/highmaps.js"></script>
  <script src="https://code.highcharts.com/mapdata/countries/in/in-all.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
  <style>
    body {
      background: linear-gradient(to right, #d9f0ff, #e6f7ff);
      font-family: Arial, sans-serif;
    }
    .status-box {
      background: white;
      padding: 15px;
      border-radius: 10px;
      margin-bottom: 10px;
      box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    .map-container {
      height: 500px;
      margin-top: 20px;
    }
    .top-buttons {
      margin: 20px;
    }
    .btn-custom {
      margin: 3px;
      border-radius: 20px;
    }
    .table-section {
      margin-top: 40px;
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }
  </style>
</head>
<body>
  <div class="container-fluid">
    <!-- Top Navigation -->
    <div class="top-buttons text-center">
      <button class="btn btn-primary btn-custom">State wise Dashboard</button>
      <button class="btn btn-primary btn-custom">Instance wise Dashboard</button>
      <button class="btn btn-primary btn-custom">ABDM Dashboard</button>
      <button class="btn btn-primary btn-custom">Other Dashboard</button>
    </div>

    <div class="row">
      <!-- Left Panel -->
      <div class="col-md-4">
        <h4 class="text-center mb-3">eHospital Status</h4>
        <div class="status-box">Today's Active Hospitals : <b>246</b></div>
        <div class="status-box">Patient Registration : <b>51,25,77,594</b></div>
        <div class="status-box">Admission : <b>4,02,31,262</b></div>
        <div class="status-box">Prescription : <b>1,18,01,002</b></div>
        <div class="status-box">Laboratory Report : <b>2,20,73,926</b></div>
        <div class="status-box">Radiology Report : <b>7,71,552</b></div>
        <div class="status-box">Discharge Summary : <b>1,64,07,381</b></div>
        <div class="status-box">ABHA Created : <b>24,62,094</b></div>
        <div class="status-box">Health Record Link Request : <b>3,52,27,554</b></div>
      </div>

      <!-- Right Panel (Map) -->
      <div class="col-md-8">
        <h4 class="text-center">eHospital Implementation</h4>
        <div id="india-map" class="map-container"></div>
      </div>
    </div>

    <!-- State Data Table -->
    <div class="table-section">
      <h4 class="text-center mb-3">State-wise eHospital Data</h4>
      <table id="stateTable" class="display" style="width:100%">
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

  <!-- Highcharts Map -->
  <script>
    Highcharts.mapChart('india-map', {
      chart: { map: 'countries/in/in-all' },
      title: { text: '' },
      legend: { title: { text: 'No of active hospitals' } },
      colorAxis: {
        dataClasses: [
          { to: 5, color: '#d9f0ff', name: '<= 5' },
          { from: 6, to: 10, color: '#a6d9ff', name: '6 to 10' },
          { from: 11, to: 50, color: '#4da6ff', name: '11 to 50' },
          { from: 51, color: '#0059b3', name: '> 50' }
        ]
      },
      series: [{
        data: [
          ['in-ap', 50],
          ['in-dl', 25],
          ['in-ka', 75],
          ['in-mp', 60],
          ['in-as', 15]
        ],
        keys: ['hc-key', 'value'],
        joinBy: 'hc-key',
        name: 'Active Hospitals',
        states: { hover: { color: '#ff9933' } },
        dataLabels: { enabled: true, format: '{point.name}' }
      }]
    });

    // Activate DataTable
    $(document).ready(function () {
      $('#stateTable').DataTable();
    });
  </script>
</body>
</html>
"""

# Render the HTML inside Streamlit
components.html(html_code, height=1200, scrolling=True)