var listofallimmages = [];
var video_index     = 0;
var main_immage      = null;
var filestringarray = "";
var immagelooptime  = 4;


function loadAllCurrentImmages(){
	 jQuery.get("/temple/imagelist", function(data) {
	    console.log(data);
	 	listofallimages = data.imagelist;
	 }) ;
};

function onload(){
    jQuery.get("/temple/imagelist", function(data) {
        console.log(data);
        listofallimages = data.imagelist;
        console.log(listofallimages.length);
        console.log(video_index);
        $("#maindiv").html('<img id="homeimmage" alt="Temple Image" class="center fit">');
        main_immage = document.getElementById("homeimmage");
        main_immage.setAttribute("src", "/mediafile/images/"+listofallimages[video_index]);
        setTimeout(function(){
            console.log("Setting the immage");
            onImageEnded();
         }, immagelooptime * 1000);
    }) ;
 }

function onImageEnded(){
    console.log(listofallimages.length);
    console.log(video_index);
    if(video_index < listofallimages.length - 1){
        video_index++;
    }
    else{
        loadAllCurrentImmages();
        video_index = 0;
    }

    $("#maindiv").html('<img id="homeimmage" alt="Temple Image" class="center fit">');
    main_immage = document.getElementById("homeimmage");
    main_immage.setAttribute("src", "/mediafile/images/"+listofallimages[video_index]);
    setTimeout(function(){
    onImageEnded();
    }, immagelooptime * 1000);
}

$(document).ready(function () {
});