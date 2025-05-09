  document.getElementById('cart-toggle').addEventListener('click', function () {
    var cartSidebar = new bootstrap.Offcanvas(document.getElementById('cartSidebar'));
    cartSidebar.show();
  });