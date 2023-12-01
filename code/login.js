function loginForm() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value; 

    const userData = {
        username: username,
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
                    alert("Account Successfully Logged in!");
                    window.location.href = 'index.html';
                } else {
                    alert('Error. ' + data.message);
                    console.error('Error: ', data.error);
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
                alert('Login Up Incomplete');
            });
        }
n
