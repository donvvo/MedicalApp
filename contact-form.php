<?php
	$to="demo@demo.com";/*Your Email*/
	$subject="Message from the website";

	$date=date("l, F jS, Y");
	$time=date("h:i A");

	$firstName=$_REQUEST['name'];
	$email=$_REQUEST['email'];
	$lastName=$_REQUEST['lastname'];
	$phone=$_REQUEST['phone'];

	$msg="
		Message sent from website form on date  $date, hour: $time.\n	
		First Name: $firstName\n
		Last Name: $lastName\n
		Email: $email\n	
		Phone Number: $phone
		";
	if($email=="") {
	echo "<div class='alert alert-danger'>
			  <a class='close' data-dismiss='alert'>×</a>
			  <strong>Warning!</strong> Please fill all the fields.
		  </div>";
	} else {
	mail($to,$subject,$msg,"From:".$email);
	echo "<div class='alert alert-success'>
			  <a class='close' data-dismiss='alert'>×</a>
			  <strong>Thank you for your message!</strong>
		  </div>";
	}
?>
