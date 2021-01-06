(function($) {
	$.fn.d3SimpleBarChart = function(opts) {
		// default configuration
		var config = $.extend({}, {
			opt1: null
		}, opts);
		// main function
		function init(obj) {
			function draw(data) {
				d3.select('.barChart') 
				.selectAll('div') 
				.data(data) 
				.enter() 
				.append('div') 
				.attr('class','item clearfix') 
				.text(function(d){return d.text}) 
				.append('div') 
				.text(function (data) {
					return data.count; 
				})			
				.attr('class','bar') 
				.style('width', function(d){ 
					return (d.count*15)  + 'px'
				});
			};
			
			d3.json("/static/json/rankapi.json", draw); 
		}
		// initialize every element
		this.each(function() {
			init($(this));
		});
		return this;
	};
	// start
	$(function() {
		$('.barChart').d3SimpleBarChart();
	});
})(jQuery);