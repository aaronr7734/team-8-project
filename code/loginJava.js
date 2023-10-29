const formEl = document.querySelector('.form');

formEl.addEventListener('submit', event => {
    event.preventDefault(); 

    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData);

    if (data.password !== data.confirm_password) {
        alert("Passwords don't match!");
        return;
    }

    fetch('OUR_API_ENDPOINT_HERE',{
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
         },
         body: JSON.stringify(data)
    }).then(res => res.json())
      .then(data => console.log(data))
      .catch(error => console.log(error));
});

