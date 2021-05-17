console.log("This is cart.");

var updateBtn = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateBtn.length; i++) {
  updateBtn[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("Product ID: ", productId, "Action: ", action);

    console.log("USER: ", user);
    if (user == "AnonymousUser") {
      console.log("User is Unauthenticated");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is Authenticated. Sending data . . .");
  var url = '/updateitem';

  fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ 'productId': productId, 'action': action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log('data: ', data);
      location.reload();
    });
}
