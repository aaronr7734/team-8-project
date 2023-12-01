$(document).ready(function () {
    $.get("https://studentdiscountz.org/api/discounts/", 
    function(data, status) {
        console.log(data, status);
    });
    $.post("https://studentdiscountz.org/api/discounts/", {user: "la", body: "0"}, 
    function(data, status) {
        console.log(data, status); 
    });
});


