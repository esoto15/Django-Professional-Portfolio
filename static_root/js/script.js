var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}


document.addEventListener("DOMContentLoaded", function () {
  var stickyLine = document.getElementById("sticky-line");

  window.addEventListener("scroll", function () {
      var scrollPosition = window.scrollY;

      if (scrollPosition >= 0) {
          stickyLine.style.display = "block";
          stickyLine.style.top = scrollPosition + "px";
      } else {
          stickyLine.style.display = "none";
      }
  });
});