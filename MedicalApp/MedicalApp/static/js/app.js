$(function() {
    var $successBtn = $('#success-btn');
    console.log($successBtn);
    var $doctorSignupSuccess = $('#doctor-signup-success');
    console.log($doctorSignupSuccess);
    $successBtn.click(function() {
        $doctorSignupSuccess.remove();
    });
});