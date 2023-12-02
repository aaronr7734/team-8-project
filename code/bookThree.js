$(function (){
    var $discounts = $('#bookThree')
   
    var discountsId = 13;
    
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
        var selectedDiscounts = discounts.find(function (discount){
            return discount.id  === discountsId;
        })
        if(selectedDiscounts){
            $discounts.append('<p class="deal-description"> <img src="' + selectedDiscounts.image + '" alt="gadget-image" class="img-fluid"> </p>');

            $discounts.append('<p class="deal-description">' + selectedDiscounts.name + '</p>');
            $discounts.append('<p class="deal-description">' + selectedDiscounts.description + '</p>');
            $discounts.append('<p class="deal-description">' + selectedDiscounts.location + '</p>');
            $discounts.append('<p > <a href="' + selectedDiscounts.url + '"  class="btn btn-primary"> View Deal </a></p>' );
            

        }
       
        }

    });  
    
});








