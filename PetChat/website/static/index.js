var test = "test message";
var canvas = document.getElementById("game_screen");
var ctx = canvas.getContext("2d");
var heightRatio = 0.5;
var daisy = document.getElementById("Daisy_img");
var moonlight = document.getElementById("Moonlight_img");
var house = new Image();
house.src = "http://127.0.0.1:5000/static/images/pet_house.png"


function home_screen(){
    // main game screen
    canvas.height = canvas.width * heightRatio;
    ctx.fillStyle = "#4493ed";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    draw_house(ctx, house);
    draw_pet(ctx, moonlight);
    ctx.imageSmoothingEnabled = false;
};

function clear_screen(){
    canvas.height = canvas.width * heightRatio;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};


function draw_house(ctx, image){
    ctx.drawImage(image, 0, 0);
};

function draw_pet(ctx, image){
    ctx.drawImage(image, 95, 20);
};

function messages(ctx, pet){
    console.log(test);
};

function update_clock() {
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

