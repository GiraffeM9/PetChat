// javascript code for the majority of front end (game and game ui)

var test = "test message";
var canvas = document.getElementById("game_screen");
var ctx = canvas.getContext("2d");
var heightRatio = 0.5;
var moonlight = document.getElementById("Moonlight_img");
var house = new Image();
house.src = "http://127.0.0.1:5000/static/images/pet_house.png"
var start_screen = new Image();
start_screen.src = "http://127.0.0.1:5000/static/images/start_screen.png"
const game_start_event = new Event('start_game');

function home_screen(){
    // main game screen
    phone_div.className = "show"
    canvas.height = canvas.width * heightRatio;
    ctx.fillStyle = "#4493ed";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    draw_bg(ctx, house);
    draw_pet(ctx, moonlight);
    ctx.imageSmoothingEnabled = false;
};

function start_s(){
    // prepares for minigamegame start screen
    clear_screen();
    ctx.drawImage(start_screen, 0, 0, 310, 150)
    phone_div.className = "hide"
};

function clear_screen(){
    canvas.height = canvas.width * heightRatio;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};


function draw_bg(ctx, image){
    ctx.drawImage(image, 0, 0);
};

function draw_pet(ctx, image){
    ctx.drawImage(image, 95, 20);
};

function messages(ctx, pet){
    console.log(test);
};

function update_clock() {
    // manages in game clock
    var now = new Date();
    var months = ["January", "February", 
        "March", "April", "May", "June", "July", "August", "September", "October",
        "November", "December"];

    if (now.getMinutes() < 10){
        var time = now.getHours() + ':' + '0' + now.getMinutes();
    }
    else {
        var time = now.getHours() + ':' + now.getMinutes();
    }

        // a cleaner way than string concatenation
    var date = [now.getDate(), 
                months[now.getMonth()],].join(' ');
    
    
    document.getElementById('clock').innerHTML = time
    document.getElementById('date').innerHTML = date


    // call this function again in 1000ms/1s
    setTimeout(update_clock, 1000);
};

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
};

