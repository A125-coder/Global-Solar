function myMap() {
  let mapCanvas = document.querySelector(".mapContact");
  var myCenter = new google.maps.LatLng(50.4869837, 30.4596262);
  var mapOptions = { center: myCenter, zoom: 14 };

  let map = new google.maps.Map(mapCanvas, mapOptions);
  let marker = new google.maps.Marker({
    position: myCenter,
    animation: google.maps.Animation.BOUNCE,
    icon: "../img/img/Vector-Smart-Object_map.png",
  });
  marker.setMap(map);
}

let aboutCompany = document.querySelectorAll('.faq-question_0');
let aboutCompanyP = document.querySelectorAll('.faq-question_');
let aboutCompany_textP = document.querySelectorAll('.faq-question_1');

  for (let i = 0; i < aboutCompany.length; i++) {

    
    aboutCompany[i].addEventListener('click', () => {
      if (aboutCompany_textP[i].innerHTML == "") {
      aboutCompany[i].style.height = "inherit";
      aboutCompany[i].style.borderColor="#ffddc6";
      aboutCompanyP[i].style.marginTop = "25px";
      aboutCompany_textP[i].style.marginTop = "40px";
        // aboutCompany_text.style.animation = "about_animation 2s 1";
        switch (i) {
            case 0:
                aboutCompany_textP[i].innerHTML = 'З точки зору продуктивності,монокристалічні панелі демонструють кращі показники виробітку, ніж полікристалічні. Крім цього, дані фотодулі повільніше деградують. Але нижча ціна робить полікристалічні панелі економічно доцільнішими. Загальна вартість станції на основі полікристалічних панелей буде меншою, а от степінь виробітку буде залишатися на високому рівні.';
                break;
            case 1:
                aboutCompany_textP[i].innerHTML = '«Зелений» тариф – це державна програма, яка стимулює розвиток відновлювальних джерел енергії. Держава зобов\'язується купувати згенеровану електроенергію у власників відновлювальних джерел енергії за фіксованою сумою.';
                break;
            case 2:
                aboutCompany_textP[i].innerHTML = 'Станом на 2019 рік, ціна зеленого тарифу складає 0.18 євроцентів. При укладені угоди цього року, Ви продаватимете надлишки електроенергії державі за даною ціною до 2030 року.';
                break;
            case 3:
                aboutCompany_textP[i].innerHTML = 'Звернутися в нашу компанію (: Спершу варто визначити технічне завдання ( Мета встановлення, тип станції, потужність, місце встановлення і ін. ) .';
                break;
            case 4:
                aboutCompany_textP[i].innerHTML = 'Це зележить від потужності станції і комплектуючих. Станції потужністю в 30 кВт окупляються найшвидше. Приблизний термін окупності станції на 30 кВт – 4 роки.';
                break;
            case 5:
                aboutCompany_textP[i].innerHTML = 'Можете, але дана процедура потребує спеціальних знань, тому краще скористатися послугами компанії, яка займається цим професійно.';
                break;
            case 6:
                aboutCompany_textP[i].innerHTML = 'Ваша інвестиція залежить від потужності – вона може складати від 3 до 25 тис. $. Більші інвестиції – швидший і більший прибуток.';
                break;
            case 7:
                aboutCompany_textP[i].innerHTML = 'Монокристалічні модулі - більше 30 років\n Полікристалічні модулі - більше 25 років\n Модулі з аморфного кремнію - 7-20 років.';
                break;

        }
      }
      else{
        aboutCompany_textP[i].innerHTML = '';
        aboutCompanyP[i].style.marginTop = "0";
        aboutCompany[i].style.borderColor="#f2f2f2";
        aboutCompany[i].style.height = "80px";
      }
    })
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

