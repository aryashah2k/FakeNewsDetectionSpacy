<?php  
  include('connection.php');   
    $username=$_POST['Uname'];  
    $password=$_POST['Pass'];  

      if(isset($_POST['reg'])){
    $username = stripcslashes($username);  
    $password = stripcslashes($password);  
    $username = mysqli_real_escape_string($con, $username);  
    $password = mysqli_real_escape_string($con, $password);  
    if(!empty($_POST['Uname']) && !empty($_POST['Pass'])) 
    {
    	$sql = "select * from ywNaDEUMs0.customer where username = '$username'";  
    	$result = mysqli_query($con, $sql);  
    	$row = mysqli_fetch_array($result, MYSQLI_ASSOC);  
    	$count = mysqli_num_rows($result);  
    	if($count >= 1){ 
          echo '<script>alert("Username is already taken, Please try again with a different username!")</script>';
        }  
         else{ 
             $query="INSERT INTO ywNaDEUMs0.customer(username,password1) VALUES('$username','$password')";  
              $result=mysqli_query($con,$query);  
              if($result){  
               echo "Account Successfully Created"; 
               header("location: login.html"); 
               } 
               else {  
                   echo "Failure!";  
                     }  
              }}
           else
           { 
              echo '<script>alert("Fields are left empty! Try again.")</script>';
            }

}






?>  