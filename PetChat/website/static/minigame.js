var myGamePiece;
var myObstacles = [];
var minigame_coins = 0;
var myScore;
var myCoins;
var myBackground;
var start_screen;
var game_over;

function start_game() {
    //myGamePiece = new component(30, 30, "red", 10, 120);
    myGamePiece = new component(75, 30, "http://127.0.0.1:5000/static/images/moonlight_mini.png", 10, 120, "image");
    myCoins = new component("12px", "Lucida Console", "yellow", 220, 14, "text");
    myScore = new component("12px", "Consolas", "blue", 220, 24, "text");
    myBackground = new component(652, 150, "http://127.0.0.1:5000/static/images/Minigame_bgt.png", 0, 0, "background");
    myGameArea.start();
};

var myGameArea = {
    canvas: document.getElementById("game_screen"),
    start: function () {
        //this.canvas.width = 480;
        //this.canvas.height = 270;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        window.addEventListener('keydown' || 's', function (e) {
            e.preventDefault();
            myGameArea.key = e.keyCode;
        })
        window.addEventListener('keyup' || 'w', function (e) {
            myGameArea.key = false;
        })
        this.frameNo = 0;
        this.interval = setInterval(updateGameArea, 10);
    },
    clear: function () {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    stop: function () {
        clearInterval(this.interval);
    },

};

class component {
    constructor(width, height, color, x, y, type, name) {
        this.type = type;
        if (type == "image" || type == "background") {
            this.image = new Image();
            this.image.src = color;
        };
        this.color = color;
        this.width = width;
        this.height = height;
        this.speedX = 0;
        this.speedY = 0;
        this.x = x;
        this.y = y;
        this.name = name;
        this.update = function () {
            ctx = myGameArea.context;
            if (this.type == "text") {
                ctx.font = this.width + " " + this.height;
                // font width + " " + font name
                ctx.fillStyle = color;
                ctx.fillText(this.text, this.x, this.y);
            } 
            else if (type == "image" || type == "background") {
                ctx.drawImage(this.image,
                    this.x,
                    this.y,
                    this.width, this.height);
                if (type == "background") {
                    ctx.drawImage(this.image, this.x + this.width, this.y, this.width, this.height);
                };
            }
            else {
                ctx.fillStyle = color;
                ctx.fillRect(this.x, this.y, this.width, this.height);
            };
        };
        this.newPos = function () {
            this.x += this.speedX;
            this.y += this.speedY;
            if (this.type == "background") {
                if (this.x == -(this.width)) {
                  this.x = 0;
                };
            };
        };
        this.crashWith = function (otherobj) {
            var myleft = this.x;
            var myright = this.x + (this.width);
            var mytop = this.y;
            var mybottom = this.y + (this.height);
            var otherleft = otherobj.x;
            var otherright = otherobj.x + (otherobj.width);
            var othertop = otherobj.y;
            var otherbottom = otherobj.y + (otherobj.height);
            var crash = true;
            if ((mybottom < othertop) || (mytop > otherbottom) || (myright < otherleft) || (myleft > otherright)) {
                crash = false;
            };
            return crash;
        };
    };
};

function updateGameArea() {
    var x, y;
    for (i = 0; i < myObstacles.length; i += 1) {
        if (myGamePiece.crashWith(myObstacles[i])) {
            if (myObstacles[i].name != "coin") {
                myGameArea.stop();
                return;
            }
            myObstacles.splice(i, 1);
            minigame_coins++;
            console.log("coins: ", minigame_coins);
            return;
        };
    };
    myGameArea.clear();
    myGameArea.frameNo += 1;
    myBackground.speedX = -1;
    myBackground.newPos();    
    myBackground.update();
    if (myGameArea.frameNo == 1 || everyinterval(80)) {
        x = myGameArea.canvas.width;
        h = myGameArea.canvas.height
        i = getRandomInt(1, 3);
        console.log(i);
        if (i == 1) {
            y = myGameArea.canvas.height - (h * 1 / 3) + 9
        }
        else if (i == 2) {
            y = myGameArea.canvas.height - (h * 2 / 3) + 9
        }
        else if (i == 3) {
            y = myGameArea.canvas.height - (h * 3 / 3) + 9
        };
        console.log("height", y);
        o = getRandomInt(1, 5);
        if (o % 5 == 0) {
            myObstacles.push(new component(20, 20, "http://127.0.0.1:5000/static/images/coin.png", x, y, "image", "coin"));
        }
        else {
            obstacle_img = getRandomInt(1, 3);
            console.log("obstacle image", obstacle_img);
            if (obstacle_img == 1){
                myObstacles.push(new component(30, 30, "http://127.0.0.1:5000/static/images/poop.png", x, y, "image"));
            }
            else if (obstacle_img == 2){
                myObstacles.push(new component(30, 30, "http://127.0.0.1:5000/static/images/plastic_bag.png", x, y, "image"));
            }
            else if(obstacle_img == 3){
                myObstacles.push(new component(30, 30, "http://127.0.0.1:5000/static/images/chip_bag.png", x, y, "image"));
            };
            //myObstacles.push(new component(30, 30, "green", x, y, "obstacle"));
        };
    };
    for (i = 0; i < myObstacles.length; i += 1) {
        myObstacles[i].x += -2.4;
        myObstacles[i].update();
    };
    myGamePiece.speedX = 0;
    myGamePiece.speedY = 0;
    if (myGameArea.key && myGameArea.key == 38) { myGamePiece.speedY = -2; }
    if (myGameArea.key && myGameArea.key == 40) { myGamePiece.speedY = 2; }
    myScore.text = "Score: " + myGameArea.frameNo;
    myScore.update();
    myCoins.text = "Coins: " + minigame_coins;
    myCoins.update();
    myGamePiece.newPos();
    myGamePiece.update();
};

function everyinterval(n) {
    if ((myGameArea.frameNo / n) % 1 == 0) { return true; }
    return false;
};