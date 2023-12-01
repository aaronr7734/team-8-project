$(function (){
    var $discounts = $('#discounts')
   //var $name = $('#nameID')
   // var $locationJs = $('#locationJs')
    //var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
        $.each(discounts, function(name, description, url, business_name, location){
            $discounts.append('<p>' + name.name + '</p>');
            $discounts.append('<p>' +description.description + '</p>');
            $discounts.append('<p>' + url.url + '</p>');
            $discounts.append('<p>' + location.location + '</p>');


        });
    }

    });
});






