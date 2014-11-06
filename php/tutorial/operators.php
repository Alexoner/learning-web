<?php
$x=10;
$y=6;
echo ($x + $y); // outputs 16
echo ($x - $y); // outputs 4
echo ($x * $y); // outputs 60
echo ($x / $y); // outputs 1.6666666666667
echo ($x % $y); // outputs 4

$x=10;
echo $x; // outputs 10

$y=20;
$y += 100;
echo $y; // outputs 120

$z=50;
$z -= 25;
echo $z; // outputs 25

$i=5;
$i *= 6;
echo $i; // outputs 30

$j=10;
$j /= 5;
echo $j; // outputs 2

$k=15;
$k %= 4;
echo $k; // outputs 3

$x=10;
echo ++$x; // outputs 11

$y=10;
echo $y++; // outputs 10

$z=5;
echo --$z; // outputs 4

$i=5;
echo $i--; // outputs 5

var_dump($x == $y);
echo "<br>";
var_dump($x === $y);
echo "<br>";
var_dump($x != $y);
echo "<br>";
var_dump($x !== $y);
echo "<br>";

$x = array("a" => "red", "b" => "green");
$y = array("c" => "blue", "d" => "yellow");
$z = $x + $y; // union of $x and $y
var_dump($z);
var_dump($x == $y);
var_dump($x === $y);
var_dump($x != $y);
var_dump($x <> $y);
var_dump($x !== $y);
?>
