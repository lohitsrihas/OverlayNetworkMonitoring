<?php
$db =mysqli_connect("localhost","root" , "root", "authentication");
if(isset($_SESSION['Submit'])){
  session_start(); 
  $name = mysql_real_escape_string($_POST['name']);
  $password = mysql_real_escape_string($_POST['password']);
  $username = mysql_real_escape_string($_POST['username']);
  $mail = mysql_real_escape_string($_POST['email']);
  $sql="insert into users(name,password,username,mail) values('$name','$password','$username','$email')";
  mysqli_query($db,$sql);
header("location: login.html.html");
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Smart Net - Day 1 Sign Up</title>

<!-- Google Fonts -->
<link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700|Lato:400,100,300,700,900' rel='stylesheet' type='text/css'>

<link rel="stylesheet" href="/static/css/animate_signup.css">
<!-- Custom Stylesheet -->
<link rel="stylesheet" href="/static/css/akhi.css">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
</head>

<body>
<div class="container">
<div class="top">
<h1 id="title" class="hidden"><span id="logo">Smart <span>Net</span></span></h1>
	</div>
		<div class="login-box animated fadeInUp">
<div class="box-header">
<h2>Sign Up</h2>
</div>
<form method="post" action="signup.php">
<label for="name">Name<span class="req">*</span>
</label>

<input type="text" required autocomplete="off" />	
<br/>
<label for="username">Username<span class="req">*</span>
</label>

<input type="text" required autocomplete="off" />	
<br/>
<label for="mail">Emailaddress<span class="req">*</span>
</label>

<input type="text" required autocomplete="off" />			
<br/>			
<label for="password">Password</label>
<input type="password" id="password">
	<br/>
 
<input type="submit" name="Submit" value="Submit">
		<br/>
	<a href="/signup/login" target="parent"><p class="small">Already a member?</p></a>

		</div>
	</div>
</form>
</body>

<script>
	$(document).ready(function ()
 {
    	$('#logo').addClass('animated fadeInDown');
    	$("input:text:visible:first").focus();
	});
	$('#username').focus(function() 
{
		$('label[for="username"]').addClass('selected');
	});
	$('#username').blur(function()
 {
		$('label[for="username"]').removeClass('selected');
	});
	$('#password').focus(function() 
{
		$('label[for="password"]').addClass('selected');
	});
	$('#password').blur(function() 
{
		$('label[for="password"]').removeClass('selected');
	});

  
    </script>


  
       </html>
