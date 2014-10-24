$(document).ready(function() {
    /* http://demo.solemone.de/overflow-image-with-vertical-centering-for-responsive-web-design/ */
    if ($(".image-bg").length > 0){
        var imageHeight, wrapperHeight, overlap, container = $('.image-bg');  
     
        function centerImage() {
            imageHeight = container.find('img').height();
            wrapperHeight = container.height();
            overlap = (wrapperHeight - imageHeight) / 2;
            container.find('img').css('margin-top', overlap);
        }
         
        $(window).on("load resize", centerImage);
         
        var el = document.getElementById('image-bg');
        if (el.addEventListener) {  
            el.addEventListener("webkitTransitionEnd", centerImage, false); // Webkit event
            el.addEventListener("transitionend", centerImage, false); // FF event
            el.addEventListener("oTransitionEnd", centerImage, false); // Opera event
        }
    }
 
});