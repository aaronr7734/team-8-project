function loginForm() {
  const username = document.getElementById('email').value
  const email = document.getElementById('email').value
  const password = document.getElementById('password').value;

  const userData = {
    username,
    email,
    password,
  };

console.log(JSON.stringify(userData));

  fetch('https://studentdiscountz.org/api/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  })
    .then(response => response.json())
    .then(data => {
       alert('Welcome Back!');
       window.location.href = 'index.html';
    })
    .catch(error => {
      alert('Login Up Incomplete');
    });

const form = document.getElementById('login');
form.addEventListener('submit', function (event) {
  event.preventDefault();

  setTimeout(function () {
    window.location.href = 'index.html';
  }, 2000);
});

}
