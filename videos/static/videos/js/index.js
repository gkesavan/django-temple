var listofallvideos = [];
var video_index     = 0;
var video_player    = null;
var main_immage      = null;
var filestringarray = "";

function loadAllCurrentVideos(){
	 jQuery.get("/temple/videolist/", function(data) {
	 	listofallvideos = data.fileslist;
	 }) ;
};

function onload(){
    jQuery.get("/temple/videolist/", function(data) {
        listofallvideos = data.fileslist;
        filestringarray = listofallvideos[video_index].split(':')
        if(filestringarray[1] == "video" ){
            $("#maindiv").html("<video playsinline autoplay muted id='homevideo' onended='onVideoEnded();'></video>");
            video_player        = document.getElementById("homevideo");
            video_player.setAttribute("src", "/mediafile/"+filestringarray[0]);
            video_player.play();
        } else {
            $("#maindiv").html('<img id="homeimmage" alt="Temple Image" class="center fit">');
            main_immage = document.getElementById("homeimmage");
            console.log("Setting the immage");
            main_immage.setAttribute("src", "/mediafile/"+filestringarray[0]);
            setTimeout(function(){
                console.log("Setting the immage");
                onVideoEnded();
             }, filestringarray[2] * 1000);
        }
    }) ;
 }

function onVideoEnded(){
    if(video_index < listofallvideos.length - 1){
        video_index++;
    }
    else{
        loadAllCurrentVideos();
        video_index = 0;
    }
    filestringarray = listofallvideos[video_index].split(':')
    if(filestringarray[1] == "video" ){
        $("#maindiv").html('<video playsinline autoplay muted id="homevideo" onended="onVideoEnded();"></video>');
        video_player        = document.getElementById("homevideo");
        video_player.setAttribute("src", "/mediafile/"+filestringarray[0]);
        video_player.play();
    } else {
        $("#maindiv").html('<img id="homeimmage" alt="Temple Image" class="center fit">');
        main_immage = document.getElementById("homeimmage");
        main_immage.setAttribute("src", "/mediafile/"+filestringarray[0]);
        setTimeout(function(){
        console.log("Setting the immage");
        onVideoEnded();
        }, filestringarray[2] * 1000);
    }
}

$(document).ready(function () {
});