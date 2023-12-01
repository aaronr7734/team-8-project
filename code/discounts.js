$(function (){
    var $discounts = $('#discounts')
    var $discountsId = 1;
    //var $name = $('#nameID')
   // var $locationJs = $('#locationJs')
    //var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        data: {id : discountId},
        success: function(data){
            if(data.length > 0){
                var item = data[0];
                $discounts.append('<p>' + item.name + '</p>');
                $discounts.append('<p>' + item.description + '</p>');
                $discounts.append('<p>' + item.url + '</p>');
                $discounts.append('<p>' + item.location + '</p>');
    
            }
            else{
                $discounts.append('<p> Nothing to show </p>');
            }
        
        
        }

    });  
    
});






