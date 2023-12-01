$(function (){
    
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
            $.each(discounts, function(name, desciption, url, business_name, location){
                $discounts.append('<li>' + discounts.name + discounts.desciption + discounts.url + desciption.location + '</li>');

            });

        }
    });
});






