<?php
$pos[1]=array("gpio"=>26,"temp_serial"=>"28-041771124ff");
$pos[2]=array("gpio"=>19);
$pos[3]=array("gpio"=>10);
$pos[4]=array("gpio"=>22);
$pos[5]=array("gpio"=>27);
$pos[6]=array("gpio"=>17);
$pos[7]=array("gpio"=>9);
$pos[8]=array("gpio"=>7); 
file_put_contents("/opt/fermenters/ferm_pos",json_encode($pos));
?>
