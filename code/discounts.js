$(function (){
    var $discounts = $('#discounts')
    var $name = $('#nameID')
    var $locationJs = $('#locationJs')
    var $urlJs = $('#urlJs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(name){
            $.each(name, function(data){
                $name.append('<p>' + data.name + '</p>');
            });

        },
        success: function(discounts){
            $.each(discounts, function(data){
                $discounts.append('<p>' +description.description + '</p>');

            });

        },
        success: function(locationJs){
            $.each(locationJs, function(data){
                $locationJs.append('<p>' + description.location + '</p>');
            });
            
        },
        success: function(urlJs){
            $.each(discounts, function(data){
                 $urlJs.append('<a href=">' + description.url + '" class="btn btn-primary" >' + '</a>');
                    
    
                });

        }

    });
});






