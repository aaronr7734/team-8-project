$(function (){
    var $discounts = $('#discounts')
    //var $name = $('#nameID')
   // var $locationJs = $('#locationJs')
    //var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(data){
        $.each(data, function(index, item){
            $discounts.append('<p>' + item.name + '</p>');
            $discounts.append('<p>' + item.description + '</p>');
            $discounts.append('<p>' + item.url + '</p>');
            $discounts.append('<p>' + item.location + '</p>');


         });
        
        }

    });  
    
});






