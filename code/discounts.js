
// Function to fetch discounts for a specific category
function fetchDiscountsForCategory(categoryName, categoryId) {
    $.ajax({
        type: 'GET',
        url: 'https://studentdiscountz.org/api/categories/' + categoryId + '/discounts_in_category/',
        success: function(discounts) {
            // Randomly select six discounts to display
            var selectedDiscounts = selectRandomDiscounts(discounts, 6);

            // Update the HTML for the given category tab
            updateCategoryTabWithDiscounts(categoryName, selectedDiscounts);
        },
        error: function() {
            console.error('Error fetching discounts for category:', categoryName);
        }
    });
}


// Function to randomly select a given number of discounts from a list or display all if fewer than the count
function selectRandomDiscounts(discounts, count) {
    if (discounts.length === 0) {
        // If there are no discounts, display a "Coming Soon" message
        return [{ description: 'Coming Soon', imageUrl: '', url: '#' }];
    } else if (discounts.length <= count) {
        // If the number of discounts is less than or equal to the count, display all
        return discounts.sort(() => 0.5 - Math.random());
    } else {
        // Shuffle the array of discounts and select the first 'count' number of elements
        return discounts.sort(() => 0.5 - Math.random()).slice(0, count);
    }
}

function selectRandomDiscounts(discounts, count) {
    // Shuffle the array of discounts
    var shuffledDiscounts = discounts.sort(() => 0.5 - Math.random());

    // Select the first 'count' number of elements
    return shuffledDiscounts.slice(0, count);
}

// Function to update the HTML content of a category tab with selected discounts
function updateCategoryTabWithDiscounts(categoryName, discounts) {
    var tabContent = $('#' + categoryName + ' .discount-content');
    tabContent.empty(); // Clear existing content

    discounts.forEach(function(discount) {
        // Create HTML content for each discount
        var discountHtml = createDiscountHtml(discount);
        // Append the discount HTML to the tab content
        tabContent.append(discountHtml);
    });
}

// Function to create HTML content for a discount
function createDiscountHtml(discount) {
    return '<div class="discount-card">' +
                '<img src="' + discount.imageUrl + '" alt="Discount Image" class="img-fluid">' +
                '<div class="discount-info">' +
                    '<p class="deal-description">' + discount.description + '</p>' +
                    '<a href="' + discount.url + '" class="btn btn-primary" target="_blank">View Deal</a>' +
                '</div>' +
            '</div>';
}

$(document).ready(function() {
    // Initialize the process of fetching and displaying discounts when the webpage loads
    fetchDiscountsForCategory('gadget-deals-tab', 8);
    fetchDiscountsForCategory('dorm-deals-tab', 9);
    fetchDiscountsForCategory('book-deals-tab', 10);
    fetchDiscountsForCategory('food-deals-tab', 11);
    fetchDiscountsForCategory('fun-deals-tab', 12);

    
});
