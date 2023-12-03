function signUpForm() {
  const first_name = document.getElementById('first_name').value;
  const last_name = document.getElementById('last_name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;
  const form = document.getElementById('Signup');

  form.addEventListener('submit', function (event) {
    event.preventDefault();
});
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
      setTimeout(function () {
       window.location.href = 'index.html';
     }, 1000);
    })
    .catch(error => {
      alert('Sign Up Incomplete');
    });
}
