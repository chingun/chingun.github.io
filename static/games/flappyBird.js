var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

// load images
var bird = new Image();
var bg = new Image();
var fg = new Image();
var pipeNorth = new Image();
var pipeSouth = new Image();
bird.src = "images/bird.png";
bg.src = "images/bg.png";
fg.src = "images/fg.png";
pipeNorth.src = "images/pipeNorth.png";
pipeSouth.src = "images/pipeSouth.png";

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
document.addEventListener("keydown",moveUp);
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
draw();
