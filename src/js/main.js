function myMap() {
  let mapCanvas = document.querySelector(".mapContact");
  var myCenter = new google.maps.LatLng(50.4869837, 30.4596262);
  var mapOptions = { center: myCenter, zoom: 14 };

  let map = new google.maps.Map(mapCanvas, mapOptions);
  let marker = new google.maps.Marker({
    position: myCenter,
    animation: google.maps.Animation.BOUNCE,
    icon: "../img/img/Vector-Smart-Object_map.png"
  });
  marker.setMap(map);
}
let imgProduct = [];

for (let i = 0; i < 4; i++) {
    imgProduct[i] = src = "../img/img/product_" + [i+1] + ".jpg";
}
for (let i = 0; i < 4; i++) {
  document.querySelector('.product_img_'+[i+1]+'').src = imgProduct[i];
}
document.querySelector('.product_img_0').src = imgProduct[0];
for (let i = 0; i < 4; i++) {
  document.querySelector('.product_img_'+[i+1]+'').addEventListener('click', () => {
    document.querySelector(".product_img_0").src = imgProduct[i];
  })
}
