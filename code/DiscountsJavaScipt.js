$.get('https://studentdiscountz.org/api/Discounts'), function(name,description,business_name, url) {
  alert(name + "\n" + description + "\n" + business_name + "\n" + url + "\n" );
}

// update the html to class
$('nameD')
.fail(function(){
  console.error('Error getting data');
});  

   

    