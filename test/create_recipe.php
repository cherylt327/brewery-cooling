<?php
$recipes[1]=array(
	"name"=>"Expressway IPA"
); 
$recipes[1]['segments'][1]['start_temp']=64; 
$recipes[1]['segments'][1]['end_temp']=64; 
$recipes[1]['segments'][1]['days']=21; 
file_put_contents("/opt/fermenters/recipes",json_encode($recipes)); 
?>
