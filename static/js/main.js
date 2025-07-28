const btn = document.getElementById("menu-toggle");
const menu = document.getElementById("menu");

btn.addEventListener("click", () => {
  menu.classList.toggle("hidden");
});


const modal = document.getElementById("modal");
  document.getElementById("abrirModal").onclick = () => modal.style.display = "block";
  function cerrarModal() {
    modal.style.display = "none";
  }

    window.onclick = function(event) {
        if (event.target == modal) {
        modal.style.display = "none";
        }
    }

    window.addEventListener("click", function(event) {
      if (!menu.classList.contains("hidden") && !btn.contains(event.target) && !menu.contains(event.target)) {
        menu.classList.add("hidden");
      }
    });


document.addEventListener("DOMContentLoaded", function () {
      const currentUrl = encodeURIComponent(window.location.href);

      const fb = document.getElementById("share-facebook");
      const pin = document.getElementById("share-pinterest");

      if (fb) {
        fb.href = `https://www.facebook.com/sharer/sharer.php?u=${currentUrl}`;
      }

      if (pin) {
        pin.href = `https://pinterest.com/pin/create/button/?url=${currentUrl}`;
      }
    });


// Código para el botón de "like"

    
