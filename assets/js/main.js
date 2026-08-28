jQuery(document).ready(function($) {

   if ($('.ds-testimonials-section').length) {
		$('.ds-testimonials-slider').slick({
		  	infinite: true,
		  	arrows: true,
		  	autoplay: true,
		  	autoplaySpeed: 4000,
		  	prevArrow:"<button type='button' class='slick-prev slick-arrow'><i class='ri-arrow-left-line'></i></button>",
		  	nextArrow:"<button type='button' class='slick-next slick-arrow'><i class='ri-arrow-right-line'></i></button>"
		});
    }

   // AOS - Animate on Scroll
   if (typeof AOS !== 'undefined') {
      // Remove the fallback style so AOS can control opacity/transforms
      $('head style').each(function() {
         if ($(this).text().indexOf('[data-aos]') !== -1) {
            $(this).remove();
         }
      });
      AOS.init({
         duration: 800,
         easing: 'ease-in-out',
         once: true,
         offset: 100
      });
   }

   // Back to Top button
   var $backToTop = $('.back-to-top');
   $(window).on('scroll', function() {
      if ($(this).scrollTop() > 400) {
         $backToTop.addClass('visible');
      } else {
         $backToTop.removeClass('visible');
      }
   });
   $backToTop.on('click', function() {
      $('html, body').animate({ scrollTop: 0 }, 600);
   });

});
