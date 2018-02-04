var quotes = [

    "Share your Projects",
    "Learn from Tutorials",
    "Brag about your Robots",
    "We are the future"
];

var i = -1;

setInterval(function() {
    $("#textslide").fadeOut(2000);
    var delay = 3000;
    setTimeout(function() {
        i++;
        $("#textslide").html(quotes[i]);
        $("#textslide").fadeIn(2000);
        if (i == quotes.length-1) {
            i = -1;
        }
    }, delay);   
}, 6 * 1000);