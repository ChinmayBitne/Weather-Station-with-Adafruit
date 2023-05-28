<?php
$conn = mysqli_connect("localhost", "root", "", "sensor");
$rows = mysqli_query($conn, "SELECT * FROM logs");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System</title>
    <link rel="stylesheet" href='style.css'></link> 
</head>
<body>
<table border = 1 cellpadding ="0" cellspacing="0" id="table">
    <tr id="heading">
        <td>Sr. No.</td>
        <td>Temperature</td>
        <td>Humidity</td>
        <td>Date</td>
        <td>Time</td>
    </tr>
    <?php $i =1; ?>
    <?php foreach($rows as $row) : ?>
        <tr>
            <td><?php echo $i++; ?></td>
            <td><?php echo $row["Temperature"]; ?></td>
            <td><?php echo $row["Humidity"]; ?></td>
            <td><?php echo $row["Date"]; ?></td>
            <td><?php echo $row["Time"]; ?></td>
            
        </tr>
    <?php endforeach; ?>
</body>
</html>
