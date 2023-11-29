function signUpForm() {
    const firstName = document.getElementById('firstname').value;
    const lastName = document.getElementById('lastname').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match. Please try again');
        return;
    }

    const userData = {
        firstName: firstName,
        lastName: lastName,
        email: email,
        password: password,
    };

	fetch('https://studentdiscountz.org/api/register/', {
	    method: 'POST',
	    headers: {
	        'Content-Type': 'application/json'
	    },
	    body: JSON.stringify(userData),
	})
	    .then(response => {
	        if (!response.ok) {
	            throw new Error('Network response was not ok');
	        }
	        return response.json();
	    })
	    .then(data => {
	        if (data.success) {
	            alert("Account Successfully Created!");
	            console.log("Test:", data);
	            window.location.href = 'index.html';
	        } else {
	            console.error('Error: ', data.error);
	        }
	    })
	    .catch(error => {
	        console.error('Fetch error:', error);
	        alert('Sign Up Incomplete');
	    });
	}

