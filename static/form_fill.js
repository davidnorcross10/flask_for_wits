var countries = ["Japan","Germany","Gabon","Guatemala","Tanzania","Tunisia","Mongolia","Nicaragua","El Salvador","Ecuador","USA"];
//document.getElementById("test").innerHTML = {{countryList|tojson}};
//var countries = Object.keys(countryJSON)

function autocomplete(inp,arr) {
var currentFocus = -1;
inp.addEventListener("input",function(e){
  var val = this.value;
  closeAllLists();
  if (!val) {
    currentFocus = -1;
    return false;
  }
  a = document.createElement("DIV");
  a.setAttribute("id",this.id+"autocomplete-list");
  a.setAttribute("class","autocomplete-items");
  this.parentNode.appendChild(a);
  for (i=0;i<arr.length;i++) {
    if (arr[i].substr(0,val.length).toUpperCase()==val.toUpperCase()) {
      b=document.createElement("DIV");
      b.setAttribute("class","menu-item");
      b.innerHTML = "<strong>" + arr[i].substr(0,val.length) + "</strong>";
      b.innerHTML += arr[i].substr(val.length);
      a.appendChild(b);
    }
  }
});
inp.addEventListener("keydown",function(e){
  var x = document.getElementById(this.id+"autocomplete-list");
  if (x) {
    x = x.getElementsByTagName("div");
  }
  if (e.keyCode == 40) { //down arrow
    currentFocus ++;
    addActive(x);
  } else if (e.keyCode == 38) { //up arrow
    e.preventDefault();
    currentFocus --;
    addActive(x);
  }
});
function addActive(x){
  if (!x) { return false;}
  removeActive(x);
  if (currentFocus < 0) {currentFocus = (x.length - 1);}
  if (currentFocus >= x.length) {currentFocus = 0;}
  x[currentFocus].classList.add("autocomplete-active");
}
function removeActive(x){
  for (var i = 0;i<x.length;i++) {
    x[i].classList.remove("autocomplete-active");
  }
}
function closeAllLists(elmnt){
  var x = document.getElementsByClassName("autocomplete-items");
  var total = x.length;
  for (var i=0;i<total;i++) {
    if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
document.addEventListener("click",function(e){
  closeAllLists(e.target);
});
}
autocomplete(document.getElementById("country-input"),countries);
