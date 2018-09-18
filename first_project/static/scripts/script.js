$(document).ready(function(){
    $("td").hover(function(){
    if ($(this).text() == "True") {
        $(this).text(1);}
   	else if ($(this).text() == "False") {
    	$(this).text(0);}
        }, function(){
    if ($(this).text() == 1) {
        $(this).text("True");}
   	else if ($(this).text() == 0) {
    	$(this).text("False");}
    });
});
