
// Hide Django flash message after a few seconds (give or take)


var message_timeout = document.getElementById("message-timer");

setTimeout(function()

{

    message_timeout.style.display = "none";

}, 5000);