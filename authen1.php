<?php      
    include('connection.php');  
  
    $username = $_POST['Uname'];  
    $password = $_POST['Pass'];  
    $r="1";
      
        //to prevent from mysqli injection  
        $username = stripcslashes($username);  
        $password = stripcslashes($password);  
        $username = mysqli_real_escape_string($con, $username);  
        $password = mysqli_real_escape_string($con, $password);  
        $number1=1;
        if(isset($_POST['log'])){
        if(!empty($_POST['Uname']) && !empty($_POST['Pass'])) 
    {
        $sql = "select *from mydatabase.customer where username = '$username' and password1 = '$password'";  
        $result = mysqli_query($con, $sql);  
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);  
        $count = mysqli_num_rows($result);  
          
        if($count >= 1){ 
            header("location: http://localhost:8501"); 
            $query="INSERT INTO mydatabase.current VALUES('$username','$r')";  
            $result=mysqli_query($con,$query); 
            echo "<h1><center> Login successful </center></h1>"; 

        }  
        else{ 
             echo '<script>alert("Login Unsuccessful! Invalid Username / Password: Please try again")</script>';
             } 
     }else{echo '<script>alert("Fields are left empty! Try again.")</script>';}
   
      }
    
      if(isset($_POST['reg'])){
      header("location: register.html");} 

?>  