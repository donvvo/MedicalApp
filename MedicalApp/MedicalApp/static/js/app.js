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

    var filterHTML = '<li><a href="#" class="btn btn-color-border-solid-3" data-filter=""></a></li>';
    var addFilterItem = function(city) {
        var $filterItem = $(filterHTML);
        var $filterLink = $filterItem.find('a');
        $filterLink.attr('data-filter', '.' + city);
        $filterLink.text(city);
        $('#city_filter').append($filterItem);
    };

    var clinicHTML = '<div class="gallery-grid-item">' +
                        '<figure class="effect-chico">' +
                            '<img src="'+ img + '" alt="">' +
                            '<figcaption>' +
                            '<h4></h4>' +
                            '<p>Health Care</p>' +
                            '<a href="#"></a>' +
                            '</figcaption>' +
                        '</figure>' +
                    '</div>';
    var addClinic = function(clinic) {
        var $clinicItem = $(clinicHTML);
        $clinicItem.attr('class', $clinicItem.attr('class') + ' ' + clinic.fields.city);
        $clinicItem.find('h4').text(clinic.pk);
        $('#clinics').isotope('insert', $clinicItem);
    };

    $('.specialty-btn').click(function() {
        var specialty = $(this).text();
        $.ajax({
            type:"GET",
            url:url,
            data: {
                specialty: specialty
            },
            success: function(data){
                var cities = [];
                data.forEach(function(clinic) {
                    addClinic(clinic);
                    var city = clinic.fields.city;
                    if ($.inArray(city, cities) === -1) {
                        cities.push(city);
                    }
                });
                cities.forEach(function(city) {
                    addFilterItem(city);
                });

                // cache container
                var $container = $('.gallery-grid');
                $container.isotope({ });
                // filter items when filter link is clicked
                $('.filters a').click(function(){
                    $('.filters a').removeClass('active');
                    $(this).addClass('active');

                    var selector = $(this).attr('data-filter');
                    $container.isotope({ filter: selector });
                    return false;
                });

                $('#specialty-section').hide();
                $('#location-section').show();

                console.log($('.filter'));
                $('#show_all').click();
            }
        });
    });

});