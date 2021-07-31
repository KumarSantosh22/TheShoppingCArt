var current = 0;
var slides = document.getElementsByClassName("slide-image");
var n = slides.length;
var prev = -1;
function displayNone() {
  for (var i = 0; i < n; i++) slides[i].style.display = "none";
}
function display() {
  if (prev > -1) {
    slides[prev].style.display = "none";
  }
  slides[current].style.display = "block";
}
function sliding(val) {
  prev = current;
  current += val;

  if (current > n - 1) {
    current = 0;
    prev = n - 1;
  } else if (current < 0) {
    current = n - 1;
    prev = 0;
  }

  display();
}
function automateSliding() {
  sliding(1);
}
displayNone();
display();
setInterval(automateSliding, 4000);
