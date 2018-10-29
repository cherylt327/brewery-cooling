<?php
$stdin = fopen('php://stdin','r'); 

$recipes = json_decode(file_get_contents("recipes"),true);
foreach($recipes as $no=>$recipe); 
{
	$screen.=$recipe['name']." - ".$no."\r\n"; 
}
$screen.="Enter Recipe No#:\r\n"; 
echo $screen; 
$recipe_no = trim(fgets($stdin)); 

echo "Enter Fermenter Pos 1-4:\r\n"; 
$ferm_pos = trim(fgets($stdin));


$fermenting=json_decode(file_get_contents("fermenting"),true);
$fermenting[]=array("start_date"=>date("Y-m-d"),"recipe_no"=>$recipe_no,"ferm_pos"=>$ferm_pos);

file_put_contents("/opt/fermenters/fermenting",json_encode($fermenting)); 
?>
