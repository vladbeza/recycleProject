
$(document).ready(function() {
     var elements = $('input[type=radio]');
    for (var i = 0; i < elements.length; i++)
    elements[i].onclick=radioClicked;
    });

//$(document).ready(function(){
//    var url = "https://api.novaposhta.ua/v2.0/json/";
//    var params = "modelName=Address&calledMethod=getCities&apiKey=44af01e2069a132543ab95299cb4ea7d";
//    var response = httpGet(url+"?"+params, parseCitiesResponse);
//});
//
//$.post(
//    "https://api.novaposhta.ua/v2.0/json/",
//    {'modelName' : 'Address', 'calledMethod' : 'getCities', "methodProperties": {
//        "Ref": "ebc0eda9-93ec-11e3-b441-0050568002cf"}, 'apiKey': '44af01e2069a132543ab95299cb4ea7d'},
//    function(data) {
//       alert('page content: ' + JSON.stringify(data));
//    }
//);

$(function() {
  var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://api.novaposhta.ua/v2.0/json/",
  "method": "POST",
  "headers": {
    "content-type": "application/json",

  },
  "processData": false,
  "data": "{\r\n\"apiKey\": \"44af01e2069a132543ab95299cb4ea7d\",\r\n \"modelName\": \"Address\",\r\n \"calledMethod\": \"getCities\"}"
}

$.ajax(settings).done(function (response) { console.log(response);
});
});

//function parseCitiesResponse(response){
//    console.log(response);
//}

function radioClicked() {

    var inputTextAddress = document.getElementById("input_text_address");
    var selectAddress = document.getElementById("select_text_address");
    var radioNovaPoshta = document.getElementById("radioNovaPoshtaDelivery");
    var radioHome = document.getElementById("radioHomeDelivery");

    if (this.id == "radioHomeDelivery") {
        inputTextAddress.style.display = "block";
        inputTextAddress.name = "address";
        selectAddress.style.display = "none";
        selectAddress.name = "";
        radioNovaPoshta.checked = false;
   }
   else
   {
        inputTextAddress.style.display = "none";
        inputTextAddress.name = "";
        selectAddress.style.display = "block";
        selectAddress.name = "address";
        radioHome.checked = false;
   }
};

//function httpGet(theUrl, callback)
//{
//    var xmlHttp = new XMLHttpRequest();
//    xmlHttp.open( "GET", theUrl, true );
//    xmlHttp.onreadystatechange = function()
//    {
//    if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
//        callback(xmlHttp.responseText);
//    }
//    }
//    xmlHttp.send( null );
//}