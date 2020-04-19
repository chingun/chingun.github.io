/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
// **************************************************
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;
var keep_down = false;
for (i = 0; i < dropdown.length; i++){  // Gets each Dropdown variable and changes them one by one.
  if(keep_down){
    dropdownContent.style.display = "block";
  }
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "";
      keep_down = false;
    } else {
      dropdownContent.style.display = "block";
      keep_down = true;
    }
  });
}
// **************************************************
// Moving image Javascript
var i = 0;
// var txts = ["if !false: ", '\n', "  return \"it is funny", '\n', "  because it is true\""];
var speed = 100;
var txt = "if not false:\n\ return \"it is funny\n\ because it is true\"";
var checker = false;
function typeWriter() {
    if (i < txt.length) {
        if(txt.charAt(i)=='\"'){
          checker = !checker;
        }
        else if(txt.charAt(i)=='\n'){
          document.getElementById("message-box").innerHTML += "<br />&nbsp";
        }
        if (checker){
          document.getElementById("message-box").innerHTML += txt.charAt(i);
        }
        else{
          document.getElementById("message-box").innerHTML += txt.charAt(i);
        }
        i++;
        setTimeout(typeWriter, speed);
    }
    if (i == txt.length){
      document.getElementById("message-box").innerHTML += "<div class=\"blinking\">|</div>";
      i++;
    }
}
// ****************************************************
// ************ Flappy Bird Not finished **************
// ****************************************************
var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");
// load images
var bird = new Image();
var bg = new Image();
var fg = new Image();
var pipeNorth = new Image();
var pipeSouth = new Image();
bird.src = "/static/flappy_images/bird.png";
bg.src = "/static/flappy_images/bg.png";
fg.src = "/static/flappy_images/fg.png";
pipeNorth.src = "/static/flappy_images/pipeNorth.png";
pipeSouth.src = "/static/flappy_images/pipeSouth.png";
// Constant Variables to allow physics
var gap = 120;
var constant;
var bird_x_loc = 10;
var bird_y_loc = 150;
var gravity = 9.8;
var score = 0;
var deltaT = 0.15;
var vel = 0;
// Audio Files for Immersion
// var fly = new Audio();
// var scor = new Audio();
// fly.src = "sounds/fly.mp3";
// scor.src = "sounds/score.mp3";
// on key down
document.addEventListener("keydown", moveUp);
function moveUp(){
    vel = -40;
    // fly.play();
}
// pipe coordinates
var pipe = [];
pipe[0] = {
    x : cvs.width,
    y : 0
};
// draw images
function draw(){
    ctx.drawImage(bg,0,0);
    for(var i = 0; i < pipe.length; i++){
        constant = pipeNorth.height+gap;
        ctx.drawImage(pipeNorth,pipe[i].x,pipe[i].y);
        ctx.drawImage(pipeSouth,pipe[i].x,pipe[i].y+constant);
        pipe[i].x--;
        if( pipe[i].x == 150 ){
            pipe.push({
                x : cvs.width,
                y : Math.floor(Math.random()*pipeNorth.height)-pipeNorth.height
            }); 
        }
        // detect collision
        if( bird_x_loc + bird.width >= pipe[i].x && bird_x_loc <= pipe[i].x + pipeNorth.width && 
            (bird_y_loc <= pipe[i].y + pipeNorth.height || bird_y_loc+bird.height >= pipe[i].y+constant) 
            || bird_y_loc + bird.height >=  cvs.height - fg.height){
            location.reload(); // reload the page
        }
        if(pipe[i].x == 5){
            score++;
            // scor.play();
        }
    }
    ctx.drawImage(fg,0,cvs.height - fg.height);
    ctx.drawImage(bird,bird_x_loc,bird_y_loc);
    vel += gravity * deltaT;
    bird_y_loc += gravity * deltaT * deltaT / 2 + vel * deltaT;
    ctx.fillStyle = "#000";
    ctx.font = "20px Verdana";
    ctx.fillText("Score : "+score,10,cvs.height-20);
    requestAnimationFrame(draw);
  }