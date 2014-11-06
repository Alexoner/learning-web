<?php
$x=5;
$y=10;

function myTest()
{
    global $x,$y;
    $y=$x+$y;
    $GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y'];
}

myTest();
echo $y; //outputs 15
?>
