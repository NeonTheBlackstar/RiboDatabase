function initMap() {
  var uluru = {lat: 52.4669812, lng: 16.9241726};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: uluru
  });
  var infowindow = new google.maps.InfoWindow({
    content: "<p>Adam Mickiewicz University</p>" + "<p>Laboratory of Computational Genomics</p>" + "<p>Umultowska 89, Poznan</p>"
  });
  var marker = new google.maps.Marker({
    position: uluru,
    map: map
  });
  infowindow.open(map,marker);
}