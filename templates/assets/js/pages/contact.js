var Contact = function () {

    return {
        
        //Map
        initMap: function () {
			var map;
			$(document).ready(function(){
			  map = new GMaps({
				div: '#map',
				lat: 37.86534,
				lng: -122.254147
			  });
			   var marker = map.addMarker({
					lat: 37.86534,
					lng: -122.254147,
		            title: 'Lean Consulting, LLC'
		        });
			});
        }

    };
}();