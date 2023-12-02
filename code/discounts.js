$(function (){
    var $discounts = $('#discounts')
   
    var discountsId = 1;
    
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(discounts){
        var selectedDiscounts = discounts.find(function (discount){
            return discount.id  === discountsId;
        })
        if(selectedDiscounts){
            $discounts.append('<p class="deal-description> <img src="' + selectedDiscounts.image+ '" alt="gadget-image" class="img-fluid"> </p>');
            $discounts.append('<p class="deal-description">' + selectedDiscounts.name + '</p>');
            $discounts.append('<p class="deal-description">' + selectedDiscounts.description + '</p>');
            
            $discounts.append('<p class="btn btn-primary "> <a href="' + selectedDiscounts.url + '" target="_blank"> View Deal </a></p>' );
            $discounts.append('<p class="deal-description">' + selectedDiscounts.location + '</p>');

        }
       
        }

    });  
    
});








