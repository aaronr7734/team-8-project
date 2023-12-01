$(function (){
    var $discounts = $('#discounts');

    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function(data) {
            $.each(data, function(index, discount) {
                // Append name, description, location, and a link for each discount
                $discounts.append('<p><strong>Name:</strong> ' + discount.name + '</p>');
                $discounts.append('<p><strong>Description:</strong> ' + discount.description + '</p>');
                $discounts.append('<p><strong>Location:</strong> ' + discount.location + '</p>');
                $discounts.append('<a href="' + discount.url + '" class="btn btn-primary">Visit Website</a>');

                // Add a horizontal line for visual separation between discounts
                $discounts.append('<hr>');
            });
        },
        error: function(error) {
            console.log('Error loading discounts:', error);
        }
    });
});