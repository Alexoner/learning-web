<?php
//POSTING from PHP curl
$data = array("name" => "Hagrid", "age" => "36");                                                                    
$data_string = json_encode($data);                                                                                   
 
$ch = curl_init('http://api.local/rest/users');                                                                      
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);                                                                  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($data_string))                                                                       
);                                                                                                                   
 
$result = curl_exec($ch);
 
$response = curl_exec($ch);
curl_close($ch);

//POSTING from Pecl_http
$url = 'http://api.flickr.com/services/xmlrpc/';
 
$response = http_post_data($url, $xml);

//POSTING from pecl_http:the OO interface
$url = 'http://api.flickr.com/services/xmlrpc/';
 
$request = new HTTPRequest($url, HTTP_METH_POST);
$request->setRawPostData($xml);
$request->send();
$response = $request->getResponseBody();

php>
