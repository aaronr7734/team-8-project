$(function (){
    var $discounts = $('#discounts')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
            $.each(discounts, function(name, description, url, business_name, location){
                $discounts.append('<p>' + discounts.name + '</p>');
                $discounts.append('<p>' +discounts.description + '</p>');
                $discounts.append('<p>' + discounts.url + '</p>');
                $discounts.append('<p>' + discounts.location + '</p>');
                

            });

        }
    });
});






