$(function () {
    var $discounts = $('#discounts');
    var discountIdsToShow = [1, 2, 3]; // Change these IDs to the ones you want to display

    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/discounts/',
        success: function (discounts) {
            // Loop through each ID in the array
            discountIdsToShow.forEach(function (discountId) {
                // Find the discount with the current ID
                var selectedDiscount = discounts.find(function (discount) {
                    return discount.id === discountId;
                });

                if (selectedDiscount) {
                    // Display the selected discount
                    $discounts.append('<p> ' + selectedDiscount.name + '</p>');
                    $discounts.append('<p> ' + selectedDiscount.description + '</p>');
                    $discounts.append('<p> ' + selectedDiscount.url + '</p>');
                    $discounts.append('<p>' + selectedDiscount.location + '</p>');
                    $discounts.append('<hr>'); // Add a horizontal line between discounts
                }
            });
        }
    });
});
