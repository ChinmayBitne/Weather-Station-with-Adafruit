
<?php 
//connect to localhost if not exists
	$servername = "localhost";
	$username = "root";
	$password = "";


	// Create connection
	$conn = new mysqli($servername, $username, $password);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}


	// Create database
	if($sql = "CREATE DATABASE sensor"){
	    echo "Database created successfully";
	} else {
	    echo "Error creating database: " . $conn->error;
	}


	$conn->close();


	echo "<br>";
//Connect to database and create table
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "sensor";


	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}


	
	$sql = "CREATE TABLE logs (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	Temperature VARCHAR(30),
	Humidity VARCHAR(30),
	'Date' DATE ,
	'Time' TIME , 
	'TimeStamp' TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)";


	if ($conn->query($sql) === TRUE) {
	    echo "Table logs created successfully";
	} else {
	    echo "Error creating table: " . $conn->error;
	}


	$conn->close();
?>