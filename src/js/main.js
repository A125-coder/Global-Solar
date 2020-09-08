function myMap() {
    let mapCanvas = document.querySelector(".mapContact");
    var myCenter = new google.maps.LatLng(50.4869837, 30.4596262);
    var mapOptions = { center: myCenter, zoom: 14 };


    let map = new google.maps.Map(mapCanvas, mapOptions);
    let marker = new google.maps.Marker({
        position: myCenter,
        animation: google.maps.Animation.BOUNCE,
        icon:'../img/img/Vector-Smart-Object_map.png',
    });
    marker.setMap(map);
}