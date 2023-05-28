
<?php
$conn = mysqli_connect("localhost", "root", "", "sensor");
$rows = mysqli_query($conn, "SELECT * FROM logs ORDER BY id DESC LIMIT 1");
$row = mysqli_fetch_assoc($rows);
$refreshInterval = 5; // Refresh interval in seconds
?>

<!DOCTYPE html>
    <html lang="en">
    <html>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" rel="stylesheet">
        <style>
          html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
          }
          h1 { font-size: 2.0rem; }
          p { font-size: 2.0rem; }
          .units { font-size: 1.2rem; }
          .dht-labels{
            font-size: 1.5rem;
            vertical-align:middle;
            padding-bottom: 15px;
          }
        </style>
        <meta http-equiv="refresh" content="<?php echo $refreshInterval; ?>">
      </head>
      <body>
        <h1>NodeMCU ESP8266 Monitoring Weather Station</h1>
        <p>
          <i class="fa fa-thermometer-half" style="font-size:3.0rem;color:#62a1d3;"></i>
          <span class="dht-labels">Temperature : </span>
          <span id="TemperatureValue"><?php echo $row["Temperature"]; ?></span>
          <sup class="units">&deg;C</sup>
        </p>
        <p>
          <i class="fa fa-tint" style="font-size:3.0rem;color:#75e095;"></i>
          <span class="dht-labels">Humidity : </span>
          <span id="HumidityValue"><?php echo $row["Humidity"]; ?></span>
          <sup class="units">%</sup>
        </p>
        <p>
          <i class="far fa-clock" style="font-size:1.0rem;color:#e3a8c7;"></i>
          <span style="font-size:1.0rem;">Time </span>
          <span id="time" style="font-size:1.0rem;"></span>
          
          <i class="far fa-calendar-alt" style="font-size:1.0rem;color:#f7dc68";></i>
          <span style="font-size:1.0rem;">Date </span>
          <span id="date" style="font-size:1.0rem;"></span>
        </P>
        <div class="container">
    <script type="text/javascript">
        function table()
        {
            const xhttp = new XMLHttpRequest();
            xhttp.onload = function()
            {
                document.getElementById("table").innerHTML = this.responseText;
            }
            xhttp.open("GET","system.php");
            xhttp.send();
        }

        setInterval(function() {
           table(); 
        }, 1);

    </script>
    <div id="table">

    </div>
        <script>
          setInterval(function() {
            // Call a function repetatively with 2 Second interval
            getTemperatureData();
            getHumidityData();
          }, 2000); 
          
          setInterval(function() {
            // Call a function repetatively with 1 Second interval
            Time_Date();
          }, 1000); 
    
          function getTemperatureData() {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
              if (this.readyState == 4 && this.status == 200) {
                document.getElementById("TemperatureValue").innerHTML =
                this.responseText;
              }
            };
            xhttp.open("GET", "readTemperature", true);
            xhttp.send();
          }
    
          function getHumidityData() {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
              if (this.readyState == 4 && this.status == 200) {
              document.getElementById("HumidityValue").innerHTML =
              this.responseText;
              }
            };
            xhttp.open("GET", "readHumidity", true);
            xhttp.send();
          }
          function Time_Date() {
            var t = new Date();
            document.getElementById("time").innerHTML = t.toLocaleTimeString();
            var d = new Date();
            const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"];
            const monthNames = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"];
            document.getElementById("date").innerHTML = dayNames[d.getDay()] + ", " + d.getDate() + "-" + monthNames[d.getMonth()] + "-" + d.getFullYear();
          }
        </script>
      </body>
    </html>

    
