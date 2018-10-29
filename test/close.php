<?php
require '../php-gpio/vendor/autoload.php'; 
use PhpGpio\Gpio; 
$pin = 26; 
$gpio = new GPIO(); 
$gpio->setup($pin, "out"); 
$gpio->output($pin,1); 
?>
