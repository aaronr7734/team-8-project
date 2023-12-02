// Function to identify the major based on the HTML file name and return its ID
function getMajorIdFromFileName() {
  let path = window.location.pathname;
  let page = path.split("/").pop();

  let majorIds = {
    "computerScience.html": 3,
    "ArtHistory.html": 4,
    "PreMed.html": 5,
    "Business.html": 6,
    "Psychology.html": 7,
  };

  return majorIds[page];
}

// Function to create HTML content for a discount
function createDiscountHtml(discount) {
  return (
    '<div class="col-md-4 mb-3">' +
    '<div class="discount-card">' +
    '<img src="' +
    discount.image +
    '" alt="' +
    discount.name +
    '" class="img-fluid">' +
    '<div class="discount-info">' +
    '<h4 class="deal-name">' +
    discount.name +
    "</h4>" +
    '<p class="deal-business">' +
    discount.business_name +
    "</p>" +
    '<p class="deal-description">' +
    discount.description +
    "</p>" +
    '<a href="' +
    discount.url +
    '" class="btn btn-primary" target="_blank">View Deal</a>' +
    "</div>" +
    "</div>" +
    "</div>"
  );
}

// Function to fetch discounts for the identified major and render them on the page
function fetchDiscountsForMajor(majorId) {
  $.ajax({
    type: "GET",
    url:
      "https://studentdiscountz.org/api/categories/" +
      majorId +
      "/discounts_in_category/",
    success: function (discounts) {
      let discountsHtml = discounts
        .map((discount) => createDiscountHtml(discount))
        .join("");
      document.querySelector(".row.justify-content-center").innerHTML =
        discountsHtml;
    },
    error: function () {
      console.error("Error fetching discounts for major ID:", majorId);
    },
  });
}

// Initialization
document.addEventListener("DOMContentLoaded", function () {
  let majorId = getMajorIdFromFileName();
  if (majorId) {
    fetchDiscountsForMajor(majorId);
  } else {
    console.error("Major ID could not be determined.");
  }
});
