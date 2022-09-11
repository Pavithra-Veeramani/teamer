
$(document).ready(function(){

    $(".nav-item .nav-link").on("click", function(){
        $(".nav").find(".active").removeClass("active");
        $(this).addClass("active");
     });

});