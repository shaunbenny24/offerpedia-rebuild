$(document).ready(function(){
	$(".products-list").addClass("new");

	$('.slick-gallery').slick({
		slidesToShow: 5,
		dots:true,
		slidesToScroll:2,
		responsive: [
			{
			breakpoint: 1280,
			settings: {
				slidesToShow: 4,
				slidesToScroll: 1,
			}
			},
			{
			breakpoint: 640,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
			}
			},
			{
			breakpoint: 480,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1
			}
			},

		// You can unslick at a given breakpoint now by adding:
		// settings: "unslick"
		// instead of a settings object
		]
	});
	$('.slick-category').slick({
	  slidesToShow: 7,
	  dots:true,
	  slidesToScroll:2,
	  responsive: [
	    {
	      breakpoint: 1280,
	      settings: {
	        slidesToShow: 5,
	        slidesToScroll: 1,
	      }
	    },
	    {
	      breakpoint: 980,
	      settings: {
	        slidesToShow: 4,
	        slidesToScroll: 1,
	      }
	    },
	     {
	      breakpoint: 640,
	      settings: {
	        slidesToShow: 3,
	        slidesToScroll: 1,
	      }
	    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
	  });
});