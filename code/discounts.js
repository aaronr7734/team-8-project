$(function (){
    var $discounts = $('#discounts')
    var $name = $('#nameID')
   // var $locationJs = $('#locationJs')
    //var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
        $('tr td:nth-child(2)').each(discounts, function(index, description){
            $discounts.append('<p>' + description.name + '</p>');
            $discounts.append('<p>' +description.description + '</p>');
            $discounts.append('<p>' + description.url + '</p>');
            $discounts.append('<p>' + description.location + '</p>');


         });
        
        }

    });  
    
});






