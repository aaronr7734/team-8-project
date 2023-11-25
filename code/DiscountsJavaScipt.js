fetch('https://studentdiscountz.org/api/Discount/')
   .then((response) =>{

    return response.json();
   })
   .then(name => 
    //fetch the name
    document.getElementById("name").innerHTML = name)
    //fetch the businessname
    .then(businessName => document.getElementById("business_name").innerHTML = businessName)
    //fetch the description
    .then(descriptionText => document.getElementById("description").innerHTML = descriptionText)
    //fetch the url
    .then(urlText => document.getElementById("url").innerHTML = urlText)

    
   .catch(function(error) {
     console.log(error)
   });
   

    
   