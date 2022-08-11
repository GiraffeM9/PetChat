var test = "test message";

function draw_canvas(canvas_id){
    // main game screen
    var canvas = document.getElementById(canvas_id);
    var ctx = canvas.getContext("2d");
    var heightRatio = 0.5;
    var daisy = document.getElementById("Daisy_img");
    var moonlight = document.getElementById("Moonlight_img");
    var house = document.getElementById("pet_house_img");
    canvas.height = canvas.width * heightRatio;
    ctx.fillStyle = "#4493ed";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    draw_house(ctx, house);
    draw_pet(ctx, moonlight);
    ctx.imageSmoothingEnabled = false;
};

function draw_house(ctx, image){
    ctx.drawImage(image, 0, 0);
};

function draw_pet(ctx, image){
    ctx.drawImage(image, 95, 20);
};

function minigame(ctx, pet){
    console.log(test);
};

function messages(ctx, pet){
    console.log(test);
};

function Time() {
    var date = new Date();
    var hour = date.getHours();
    var minute = date.getMinutes();
    hour = update(hour);
    minute = update(minute);
    document.getElementById("clock").innerText = hour + " : " + minute;
    setTimeout(Time, 60000);
   };
   
function update(t) {
    if (t < 10) {
    return "0" + t;
    }
    else {
    return t;
    }
};

