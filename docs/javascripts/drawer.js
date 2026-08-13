/* Override Material's desktop drawer reset so the hamburger toggle works at any width */
document.addEventListener("DOMContentLoaded", function () {
  var drawer = document.getElementById("__drawer");
  if (!drawer) return;

  var hamburger = document.querySelector('label[for="__drawer"]');
  if (!hamburger) return;

  hamburger.addEventListener("click", function (e) {
    e.preventDefault();
    drawer.checked = !drawer.checked;
    drawer.dispatchEvent(new Event("change"));
  });

  var overlay = document.querySelector(".md-overlay");
  if (overlay) {
    overlay.addEventListener("click", function () {
      drawer.checked = false;
      drawer.dispatchEvent(new Event("change"));
    });
  }
});
