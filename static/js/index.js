// // function showUrl() {
// //   var urlInput = document.getElementById("url");
// //   var urlValue = urlInput.value;
// //   alert("The URL you entered is: " + urlValue);
// // }
// function checkImage() {
//   var urlInput = document.getElementById("url");
//   var urlValue = urlInput.value;

//   var img = new Image();
//   img.src = urlValue;
//   img.onload = function () {
//     alert(checkImage);
//   };
//   img.onerror = function () {
//     alert("Error! The URL does not points to an image.");
//   };
// }

function runPythonFunction() {
  var url = document.getElementById("url").value;
  $.ajax({
    url: "/run_python_function",
    type: 'POST',
    data: {url: url},
    success: function(result) {
      // const objStr = JSON.stringify(result);
      alert(result.result);
      console.log(result);
    },
    error: function(xhr, status, error) {
      alert("Error: " + error);
      console.log(xhr.responseText);
    }
  });
}