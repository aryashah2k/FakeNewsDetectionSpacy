<?php      
    // $host = "localhost";  
    // $user = "root";  
    // $password = "";  
    // $db_name = "mydatabase";  

    $host = "remotemysql.com";  
    $user = "ywNaDEUMs0";  
    $password = "z3FwsBlKs8";  
    $db_name = "ywNaDEUMs0"; 
      
    $con = mysqli_connect($host, $user, $password, $db_name);  
    if(mysqli_connect_errno()) {  
        die("Failed to connect with MySQL: ". mysqli_connect_error());  
    }  
?>  