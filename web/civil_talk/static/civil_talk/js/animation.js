document.addEventListener("DOMContentLoaded", function() {
    var button = document.getElementById('submit-button');

    button.onmouseover = function() {
        button.style.transform = "scale(5)";
        button.style.transition = "transform 0.3s ease";
    };

    button.onmouseout = function() {
        button.style.transform = "scale(1)";
    };
});
