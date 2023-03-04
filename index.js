// function showUrl() {
//   var urlInput = document.getElementById("url");
//   var urlValue = urlInput.value;
//   alert("The URL you entered is: " + urlValue);
// }
function checkImage() {
  var urlInput = document.getElementById("url");
  var urlValue = urlInput.value;

  var img = new Image();
  img.src = urlValue;
  img.onload = function () {
    alert("Success! The URL points to an image.");
  };
  img.onerror = function () {
    document.write("false");
  };
}
