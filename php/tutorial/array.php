<?php
$cars=array("Volvo","BMW","Toyota");
$arrlength=count($cars);

//indexed arrays
for ($x=0;$x<$arrlength;$x++)
{
    echo $cars[$x];
    echo "<br>";
}

//Associative arrays
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
echo "Peter is ".$age['Peter']. "year old.";

foreach($age as $x=>$x_value)
  {
  echo "Key=" . $x . ", Value=" . $x_value;
  echo "<br>";
  }

//Multidemensional arrays

?>
