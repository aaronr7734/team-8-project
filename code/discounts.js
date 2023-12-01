$(function (){
    var $discounts = $('#discounts')
   
    var discountsIdShow = [1,2,3] ;
    //var $name = $('#nameID')
   // var $locationJs = $('#locationJs')
    //var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
            discountIdsToShow.forEach(function (discountId) {
                // Find the discount with the current ID
                var selectedDiscount = discounts.find(function (discount) {
                    return discount.id === discountId;
                });
            if(selectedDiscounts){
                $discounts.append('<p>' + selectedDiscounts.name + '</p>');
                $discounts.append('<p>' + selectedDiscounts.description + '</p>');
                $discounts.append('<p>' + selectedDiscounts.url + '</p>');
                $discounts.append('<p>' + selectedDiscounts.location + '</p>');

            }
       
        });
    }
    });

});  
    






