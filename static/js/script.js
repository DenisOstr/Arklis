$(document).ready(function() {
	$('.menu-btn').click(function() {
		$('#menu-list').toggle('active');
	});

	$('.user-btn').click(function() {
		$('.dropdown-content').toggle('dropdown-active')
	});

	$("#owl-crl").owlCarousel({
		info: false,
		loop: true,
		autoplay: true,
		autoplayTimeout: 2500,

		items: 4,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1030: {
				items: 3
			},
			1100: {
				items: 4
			},

		}
	});
})