<?php
function sum($x,$y=0)
{
    $z=$x+$y;
    return $z;
}

echo "5 + 10 = ". sum(5,10) ."<br>";
echo "7 + 13 = ".sum(7,13) . "<br>";
echo "2 + 4 = ".sum(2,4)."<br>";
echo "9 + 0 = ".sum(9)."<br>";
?>
