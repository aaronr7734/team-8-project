$(function (){
    var $discounts = $('#discounts')
   //var $name = $('#nameID')
   // var $locationJs = $('#locationJs')
    //var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
        $.each(discounts, function(data){
            $discounts.append('<p>' + data.name + '</p>');
            $discounts.append('<p>' +data.description + '</p>');
            $discounts.append('<p>' + data.url + '</p>');
            $discounts.append('<p>' + data.location + '</p>');


        });
    }

    });
});






