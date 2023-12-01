$(function (){
    var $discounts = $('#discounts')
    var discountsId = 1;
    //var $name = $('#nameID')
   // var $locationJs = $('#locationJs')
    //var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
        var selectedDiscounts = discounts.find(function (discount){
            return discount.id  === discountsId;
        })
        if(selectedDiscounts){
            $discounts.append('<p>' + selectedDiscounts.name + '</p>');
            $discounts.append('<p>' + selectedDiscounts.description + '</p>');
            $discounts.append('<p>' + selectedDiscounts.url + '</p>');
            $discounts.append('<p>' + selectedDiscounts.location + '</p>');

        }
       
        }

    });  
    
});






