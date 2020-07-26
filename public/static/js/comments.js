function getCookieValue(a) {
  var b = document.cookie.match("(^|;)\\s*" + a + "\\s*=\\s*([^;]+)");
  return b ? b.pop() : "";
}

function changeObjective(e) {
  /*
  var hidden = document.getElementsByName("span-answer");
  var span = document.getElementById("span-answer");
  var button = document.querySelector(".remove-comment");
  e.preventDefault();

  if (hidden.value === "post" || hidden.value == undefined) {
    button.classList.toggle("activado");
  }

  
  hidden.value = x;
  span.innerHTML = "#" + x;*/

  e.preventDefault();
  var x = e.target.dataset.pk;
  var comment =
    '<div class="comment-reply"><form method="post"><input type="hidden" name="csrfmiddlewaretoken" value="' +
    getCookieValue("csrftoken") +
    '" /> <input type="hidden" name="span-answer" value="' +
    x +
    '" /><div class="form-group row"><textarea placeholder="Ingresa tu comentario..." class="col-sm-12" name="body" id="body" rows="3" required></textarea></div><button type="submit" class="btn btn-warning">Enviar</button></form></div>';
  var parent = e.target.parentNode.parentNode.parentNode.parentNode.parentNode;
  var elem = parent.children[2];

  elem.insertAdjacentHTML("beforeend", comment);
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
