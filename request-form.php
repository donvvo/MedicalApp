<?php
	$to="demo@demo.com";/*Your Email*/
	$subject=$_REQUEST['subject'];

	$date=date("l, F jS, Y");
	$time=date("h:i A");

	$firstName=$_REQUEST['name'];
	$phone=$_REQUEST['phone'];
	$textMessage=$_REQUEST['textmessage'];

	$msg="
		Message sent from website form on date  $date, hour: $time.\n
		Name: $firstName\n
		Phone Number: $phone
		Message: $textMessage
		";
	if($email=="") {
	echo "<div class='alert alert-success'>
			  <a class='close' data-dismiss='alert'>×</a>
			  <strong>Thank you for your message!</strong>
		  </div>";
	} else {
	mail($to,$subject,$msg,"From:".$email);
	echo "<div class='alert alert-success'>
			  <a class='close' data-dismiss='alert'>×</a>
			  <strong>Thank you for your message!</strong>
		  </div>";
	}
?>
