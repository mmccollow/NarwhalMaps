$(function() {
	$('#slides').slides({
		play: 15000,
		pause: 2500,
		animationStart: function(current) {
			$('.caption').animate({
				bottom:-35
			}, 100);
		},
		animationComplete: function(current) {
			$('.caption').animate({
				bottom:0
			}, 200);
		},
		slidesLoaded: function() {
			$('.caption').animate({
				bottom:0
			}, 200);
		}
	});
});
