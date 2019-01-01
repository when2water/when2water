<?php

/* Error Codes
 * 0: Valid
 * 1: Invalid
 * 2: Zip Not Sent
 * 3: Request/JSON Decode failed
*/

ob_start();
if (isset($_GET['zip'])) {
	try {
		$ch = curl_init("http://api.zippopotam.us/us/" . $_GET['zip']);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		// ob_start();
		$response = curl_exec($ch);
		// ob_end_clean();
		curl_close($ch);
		
		$json = json_decode($response, true);
		// var_dump($json);
		
		if (isset($json['post code']) && $json['country']==="United States") {
			$code = 0;
		}
		else {
			$code = 1;
		}
	}
	catch (Exception $e) {
		$code = 3;
	}
}
else {
	$code = 2;
}
ob_end_clean();

echo $code;

?>