const formEl = document.querySelector('.form');

formEl.addEventListener('submit', event => {
    event.preventDefault(); 

    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData);

    if (data.password !== data.confirm_password) {
        alert("Passwords don't match!");
        return;
    }

    // Remove the confirm_password field before sending
    delete data.confirm_password;

    fetch('https://studentdiscountz.org/api/register',{
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
         },
         body: JSON.stringify(data)
    }).then(res => {
        if (res.status === 201) {
            return res.json();
        } else {
            return Promise.reject(res.json());
        }
    })
    .then(data => {
        alert("Account successfully created!");
        window.location.href = "LoginPage.html";
    })
    .catch(errorPromise => {
        errorPromise.then(errorData => {
            alert(JSON.stringify(errorData));
        });
    });
});
