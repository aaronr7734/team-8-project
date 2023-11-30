$.get("https://studentdiscountz.org/api/discounts/", 
function(data, status) {
    console.log(data, status);
})
$.post("https://studentdiscountz.org/api/discounts/",
{suggest: txt}, function(name){
    $("nameJs").html(name);
})
$.post("https://studentdiscountz.org/api/discounts/",
{suggest: txt}, function(description){
    $("descriptionJs").html(description);
})
$.post("https://studentdiscountz.org/api/discounts/",
{suggest: txt}, function(url){
    $("urlJs").html(url);
})