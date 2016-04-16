$(document).ready(function () {




    /*==================================
     Parallax Effect for Home page
     ====================================*/

    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    } else {



        // Tiny jQuery Plugin
        // by Chris Goodchild
        $.fn.exists = function (callback) {
            var args = [].slice.call(arguments, 1);

            if (this.length) {
                callback.call(this, args);
            }

            return this;
        };

        // Usage Parallax 
        $('.parallax-image-1').exists(function () {

            //alert('1 here');
            var offsetParallax1 = $(".parallax-image-1").offset().top;
            $('.parallax-image-1').parallax("50%", offsetParallax1, 0.1, true);

        });

        $('.parallax-image-2').exists(function () {

            //alert('2 here');
            var offsetParallax2 = $(".parallax-image-2").offset().top;
            $('.parallax-image-2').parallax("50%", offsetParallax2, 0.1, true);

        });


    } // mobile userAgent end 


}); // end Ready