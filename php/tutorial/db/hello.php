<?php
header("Content-Type: text/html; charset=utf-8");

//Create connection
$con=mysqli_connect("localhost","onerhao","hello","hust");
//Check connection
if(mysqli_connect_errno())
{
    echo "Failed to connect to MySQL:".mysqli_connect_error();
}

$charset=$con->get_charset();
$con->set_charset("utf8");
print $con->host_info."\n";
var_dump($charset);

$sql="SELECT * from students;";

//Execute query
if($result=mysqli_query($con,$sql))
{
    echo "select executed successfully\n";
}
else
{
    echo "Error creating table:".mysqli_error($con)."\n";
}

echo "结果:\n";
while($row=mysqli_fetch_array($result))
{
    echo utf8_encode($row['username'])." ".$row['name'];
    echo "<br>";
}

mysqli_close($con);
?>
