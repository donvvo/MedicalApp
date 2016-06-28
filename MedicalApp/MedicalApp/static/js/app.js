function acsSort (a, b) {
        if (a.getAttribute('data-name') < b.getAttribute('data-name')) {
            return -1;
        }
        else if (a.getAttribute('data-name') > b.getAttribute('data-name')) {
            return 1;
        }
        else {
            return 0;
        }
    }
function descSort (a, b) {
    return -1 * acsSort(a, b);
}

$(function() {
    var $successBtn = $('#success-btn');
    var $doctorSignupSuccess = $('#doctor-signup-success');
    $successBtn.click(function() {
        $doctorSignupSuccess.remove();
    });

    // Car crash animations
    $frontEndCollision = $('#front-end-collision');
    function frontEndLoop() {
        $frontEndCollision.delay(1000).css("left", "50px");
        $frontEndCollision.animate({"left": "-=50"}, 1000, frontEndLoop);
    }
    frontEndLoop();
    $sideEndCollision = $('#side-end-collision');
    function sideEndLoop() {
        $sideEndCollision.delay(1000).css("left", "0");
        $sideEndCollision.animate({"left": "+=50"}, 1000, sideEndLoop);
    }
    sideEndLoop();
    $sideSwipeCollision = $('#side-swipe-collision');
    function sideSwipeLoop() {
        $sideSwipeCollision.delay(1000).css("top", "30px");
        $sideSwipeCollision.animate({"top": "-=30"}, 1000, sideSwipeLoop);
    }
    sideSwipeLoop();
    $rearEndCollision = $('#rear-end-collision');
    function rearEndLoop() {
        $rearEndCollision.delay(1000).css("left", "0");
        $rearEndCollision.animate({"left": "+=50"}, 1000, rearEndLoop);
    }
    rearEndLoop();

    $('.time-input').timepicker({
        'minTime': '12:00am',
        'maxTime': '11:30pm'
    });

    $(".datepicker").datepicker();

    $('.validator-form .form-group input:not(.not-required),select').attr('required', 'true')
    $('.validator-form').validate();
});
