/* console.log('hello world') */
$('.navbar').removeClass("sticky"); 
$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY >50){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky"); 
        }
    })
});

$('.navbar .menu li a').click(function(){
    // applying again smooth scroll on menu items click
    $('html').css("scrollBehavior", "smooth");
});


$(document).ready(function(){
    $('#nepse-market').on('change',function(){
        if(this.value=='top-losers')
        {
            $("#top-losers").show();
            $("#top-gainers").hide();
        }
        if(this.value=='top-gainers')
        {
            $("#top-gainers").show();
            $("#top-losers").hide();
        }
        
    });
});
