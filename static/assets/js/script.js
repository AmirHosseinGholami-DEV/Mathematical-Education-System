// ====== Window Scroll , Header ======
$(function() {
    $(window).scroll(function(event) {
        if ($(document).scrollTop() < 1) {

            $('.header-area').removeClass('fixed');
            $('.header-area').removeClass('active');

        } else if ($(document).scrollTop() > 100) {

            $('.header-area').removeClass('fixed');
            $('.header-area').addClass('active');
        } else {

            $('.header-area').addClass('fixed');
        }
    });
});

/* =========================
        Typing js           
============================ */

/* =========================
        Progress Bar js           
============================ */
$(function() {

    $('.skill').waypoint(function() {

        $('.progres').each(function() {
            $(this).animate({
                width: $(this).attr('aria-valuenow') + '%'
            }, 200);
        });

        this.destroy();

    }, {
        offset: 'bottom-in-view'
    });
});

/* =========================
          Isotop Js           
============================ */
$(window).on('load', function() {
    $('.gallery').isotope({
        //options
        isOriginLeft: false,
    });

    $('.filtering').on('click', 'button', function() {
        var filterValue = $(this).attr('data-filter');
        $('.gallery').isotope({
            filter: filterValue
        });
        $('.filtering').find('.active').removeClass('active');
        $(this).addClass('active')
    });
});


/* ===============================
         Magnific Pop-up          
================================== */
$(function() {
    $('.gallery').magnificPopup({
        delegate: ".img-fluid",
        type: 'image',
        gallery: {
            enabled: true
        }
    });
})


/* =========================
       Counterup Js           
============================ */
$(function() {
    $('.integers').counterUp({
        delay: 10,
        time: 2000
    });
});

/* =========================
       Owl Carousel Js           
============================ */
$(function() {
    $(".owl-carousel").owlCarousel({
        loop: true,
        stagePadding: 10,
        margin: 30,
        nav: false,
        rtl: true,
        autoplay: true,
        center: false,
        dots: true,
        mouseDrag: true,
        touchDrag: true,
        smartSpeed: 1000,
        autoplayHoverPause: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 1,
            },
            991: {
                margin: 30,
                items: 2,
            },
        }
    });
});

/* =========================
        Preloader Js           
============================ */
$(window).on('load', function() {
    $('#status').fadeOut(8000);
    $('#preloader').delay(800).fadeOut('slow');
});

/* ===============================
    Scrolling jQuery eesing js          
================================== */
$(function() {
    $('a.smooth-scroll').click(function(event) {
        event.preventDefault();
        var sectionId = $(this).attr('href');

        $('html, body').animate({
            scrollTop: $(sectionId).offset().top
        }, 1250);
    })
})