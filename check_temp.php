<?php
$today = date("Y-m-d"); 
$fermenting = json_decode(file_get_contents("/opt/fermenters/fermenting"),true);
$ferm_pos = json_decode(file_get_contents("/opt/fermenters/ferm_pos"),true);
$recipes = json_decode(file_get_contents("/opt/fermenters/recipes"),true);
$dev_folder="/sys/bus/w1/devices/"; 
foreach($fermenting as $ferm) {
	$recipe=$recipes[$ferm['recipe_no']]; 
	$segments=$recipe['segments'];
	$days = 0; 
	$old_days=0; 
	$gpio = $ferm_pos[$ferm['ferm_pos']]['gpio']; 
	$gpio_lock_file="/opt/fermenters/gpio_".$gpio.".lock"; 
	$temp_serial = $ferm_pos[$ferm['ferm_pos']]['temp_serial']; 
	foreach($segments as $segment) {
		$days=$days+$segment['days'];
		$start=new DateTime($ferm['start_date']); 
		$end=new DateTime($today);
		$interval = $start->diff($end); 
		$interval = $interval->format('%a');
		if($interval <= $days && $interval >= $old_days) { 
			$f=$dev_folder.$temp_serial."/w1_slave";
			$lines = file($f); 
			$c=0; 
			foreach($lines as $line) {
				$line=trim($line);
				if(substr($line, -3)=='YES') { 
					$temp_line=$lines[$c+1]; 
					$temp_line_split=explode(" ", $temp_line); 
					$searchword="t="; 
					foreach($temp_line_split as $search_field) {
						if(strpos($search_field,$searchword)!== false) { 
							$search_exp=explode("=",$search_field); 
							$degrees_c=$search_exp[1]/1000; 
							$degrees_f=$degrees_c*9/5+32;
							if($degrees_f > $segment['end_temp'] && !is_file($gpio_lock_file)) { 
								exec('sudo ./php-gpio/openvalve '.$gpio.' open');
								file_put_contents($gpio_lock_file,"1"); 
							} else if($degrees_f < $segment['end_temp']){ 
									exec('sudo ./php-gpio/openvalve '.$gpio.' close'); 
									if(is_file($gpio_lock_file)) { 
										unset($gpio_lock_file);
									}
							}	
						}
					}
				}
			$c++; 
			}
		}
		$old_days=$days; 
		if($c == count($segments) && $interval > $old_days) { 
						if(is_file($gpio_lock_file)) { 
							exec('sudo ./php-gpio/openvalve '.$gpip.' close'); 
							unset($gpio_lock_file); 
						}
		}
	}	
}
?>
