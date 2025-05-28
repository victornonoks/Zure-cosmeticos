document.getElementById('cart-toggle').addEventListener('click', function () {
  let cartSidebar = new bootstrap.Offcanvas(document.getElementById('cartSidebar'));
  cartSidebar.show();
});

function editInput() {
  const inputs = document.querySelectorAll("input.input");
    inputs.forEach(input => {
      input.disabled = false
    });
}

  function saveInput() {
    const inputs = document.querySelectorAll(".input")
    inputs.forEach(input => 
      input.disabled = true
    )
  }