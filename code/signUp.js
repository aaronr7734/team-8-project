function signUpForm() {
  const first_name = document.getElementById('first_name').value;
  const last_name = document.getElementById('last_name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  if (password !== confirmPassword) {
    alert('Passwords do not match. Please try again');
    return;
  }

  const userData = {
    first_name,
    last_name,
    email,
    password,
  };

console.log(JSON.stringify(userData));

  fetch('https://studentdiscountz.org/api/register/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  })
    .then(response => response.json())
    .then(data => {
       alert('Account Successfully Created!');
    })
    .catch(error => {
      alert('Sign Up Incomplete');
    });
}

const form = document.getElementById('Signup');
form.addEventListener('submit', function (event) {
  event.preventDefault();

  setTimeout(function () {
    window.location.href = 'index.html';
  }, 2000);
});

