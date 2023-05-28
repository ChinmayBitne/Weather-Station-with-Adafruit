<?php 
    //Creates new record as per request
    //Connect to database
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "sensor";


    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Database Connection failed: " . $conn->connect_error);
    }


    //Get current date and time
    date_default_timezone_set('Asia/Kolkata');
    $d = date("Y-m-d");
    //echo " Date:".$d."<BR>";
    $t = date("H:i:s");
    echo $d;
    echo $t;

    if(!empty($_POST['Temperature']) || !empty($_POST['Humidity']))
    {
        if(($_POST['Temperature']!=0) || ($_POST['Humidity']!=0))
        {
            $Temperature = $_POST['Temperature'];
            $Humidity = $_POST['Humidity'];


            //$sql = "INSERT INTO logs (Temperature, Humidity, Date, Time) VALUES (".$Temperature.",".$Humidity.", ".$d.", ".$t.")";
            $sql = "insert into logs(Temperature, Humidity, Date, Time) values('".$Temperature."','".$Humidity."','".$d."','".$t."')";


            if ($conn->query($sql) === TRUE) {
                echo "OK";
            } else {
                echo "Error: " . $sql . "<br>" . $conn->error;
            }
        }
	}
	$conn->close();
?>