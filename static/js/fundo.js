function alterarEstilosBody() {
    var bodyElement = document.body;
    bodyElement.style.backgroundImage = "url('/static/img/solar.jpg')";
    bodyElement.style.backgroundPosition = "center";
    bodyElement.style.backgroundSize = "cover";

    var footerElement = document.getElementById('footer');     
    if (footerElement) {
        footerElement.parentNode.removeChild(footerElement);
    }


}
    

document.addEventListener("DOMContentLoaded", function() {
    alterarEstilosBody();
});
