var mymap = L.map('mapid');
let xhr = new XMLHttpRequest();
xhr.onreadystatechange = function (){
	if(this.readyState == 4 && this.status == 200){
		var obj = JSON.parse(this.responseText);
		mymap.setView([20.5937,78.9629],6);
		for(var i=0;i< obj.length;i++){
			var marker = L.marker([obj[i].lat,obj[i].long]).addTo(mymap);
		}
	}
}

xhr.open("GET","/api/points",true);
xhr.send();

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox/streets-v11',
	tileSize: 512,
	zoomOffset: -1,
	accessToken: 'pk.eyJ1IjoiZ2Vla3lwYW5kZXkiLCJhIjoiY2s2bTBucXdjMGo1ejNqcWcxdnF4bXVqcyJ9.Edq3ZxO9C_DmsyYvsPtrEA'
	}).addTo(mymap);


var circle = L.circle([18.453471,73.849960], {
	color: 'red',
	fillColor: '#f03',
	fillOpacity: 0.5,
	radius: 20
	}).addTo(mymap);

//marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
