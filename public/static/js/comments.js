function changeObjective(e) {
  var hidden = document.getElementsByName("span-answer");
  var span = document.getElementById("span-answer");
  var button = document.querySelector(".remove-comment");
  e.preventDefault();

  if (hidden.value === "post" || hidden.value == undefined) {
    button.classList.toggle("activado");
  }

  var x = e.target.dataset.pk;
  hidden.value = x;
  span.innerHTML = "#" + x;
}

function removeObjective(e) {
  e.preventDefault();
  var hidden = document.getElementsByName("span-answer");
  var span = document.getElementById("span-answer");
  var button = document.querySelector(".remove-comment");
  button.classList.toggle("activado");
  hidden.value = "post";
  span.innerHTML = "";
}
