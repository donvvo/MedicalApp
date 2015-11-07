$(function() {
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('.specialty-btn').click(function() {
        var specialty = $('.specialty-btn').text();
        $.ajax({
            type:"GET",
            url:"{% url 'medicalappointments:get_clinics' %}",
            data: {
                specialty: specialty
            },
          success: function(data){
            if (interest) {
              $('#project-content').html(data['project_modal_content']);
              // Open modal at the position on the page, instead of going back up
              var offset = $(document).scrollTop();
              $('#myModal').css('top', offset);
              $(window).resize(function() {
                var offset = $(document).scrollTop();
                $('#myModal').css('top', offset);
              });
              $('#myModal').modal();
            }
          }
        });


        $('#specialty-section').hide();
        $('#location-section').show();
    });

});