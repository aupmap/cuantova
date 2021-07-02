//Main
const parallax = document.getElementById("parallax");

window.addEventListener("scroll", function()
{
    let offset = window.pageYOffset;
    parallax.style.backgroundPositionY = offset
    * 0.7 + "px";
})


/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon
function myFunction() {
    var x = document.getElementById("menu");
    if (x.className === "menu") {
      x.className += " responsive";
    } else {
      x.className = "menu";
    }
  } 
*/
