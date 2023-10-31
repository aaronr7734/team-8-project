// I only know the very basics of javascript
// So I'm not sure if this is the best way to do this.
document.addEventListener("DOMContentLoaded", function() {
    const loginFormEl = document.querySelector('.signupBox'); 

    loginFormEl.addEventListener('submit', event => {
        event.preventDefault(); 

        const formData = new FormData(loginFormEl);
        const loginData = Object.fromEntries(formData);

        fetch('https://studentdiscountz.org/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginData)
        }).then(res => res.json())
        .then(data => {
            if (data.token) {
                // Redirect to home page.
                window.location.href = "https://studentdiscountz.org/";
            } else {
                // Show error // this is the part I'm not sure is safe.
                alert(JSON.stringify(data));
            }
        })
        .catch(error => console.log(error));
    });
});