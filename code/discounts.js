$(function (){
    var $discounts = $('#discounts')
    var $name = $('#nameID')
    var $locationJs = $('locationJs')
    var urlJs = $('urljs')
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(name){
            $.each(name, function(data){
                $discounts.append('<p>' + data.name + '</p>');
            });

        },
        success: function(discounts){
            $.each(discounts, function(data){
                $discounts.append('<p>' + data.name + '</p>');
                $discounts.append('<p>' +description.description + '</p>');
                $discounts.append('<p>' + description.location + '</p>');
                $discounts.append('<a href=">' + description.url + '" class="btn btn-primary" >' + '</a>');
                

            });

        },
        success: function(locationJs){
            $.each(locationJs, function(data){
                $discounts.append('<p>' + description.location + '</p>');
            });
            
        },
        success: function(urlJs){
            $.each(discounts, function(data){
                 $discounts.append('<a href=">' + description.url + '" class="btn btn-primary" >' + '</a>');
                    
    
                });

        }

    });
});






