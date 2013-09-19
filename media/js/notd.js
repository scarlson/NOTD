var ws = new WebSocket("ws://" + location.host + "/ws/");
var canvas = document.getElementById('board');
//canvas.width = document.width;
//canvas.height = document.height;
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var ctx = canvas.getContext('2d');
var tileimg = new Image();
tileimg.src = "static/images/Grass.png";
var rockimg = new Image();
rockimg.src = "static/images/rock.png";
var treeimg = new Image();
treeimg.src = "static/images/tree.png";
var playerimg = new Image();
playerimg.src = "static/images/player.png";
var zombieimg = new Image();
zombieimg.src = "static/images/zombie.png";
var beansimg = new Image();
beansimg.src = "static/images/Beans.png";
var unarmedimg = new Image();
unarmedimg.src = "static/images/Unarmed.png";
var batimg = new Image();
batimg.src = "static/images/Bat.png";
var swordimg = new Image();
swordimg.src = "static/images/Sword.png";
items = {
    'Unarmed': "static/images/Unarmed.png",
    'Bat': "static/images/Bat.png",
    'Beans': "static/images/Beans.png",
    'Sword': "static/images/Sword.png"
};

function tile(x, y) {
    var sourceX = 0;
    var sourceY = 0;
    var sourceWidth = 108;
    var sourceHeight = 122;
    var destinationWidth = 52;
    var destinationHeight = 60;
    ctx.drawImage(tileimg, sourceX, sourceY, sourceWidth, sourceHeight,
        x, y, destinationWidth, destinationHeight);
};

function tree(x, y) {
    var sourceX = 0;
    var sourceY = 0;
    var sourceWidth = 52;
    var sourceHeight = 82;
    var destinationWidth = 39;
    var destinationHeight = 61;
    wx = x + 25 - (destinationWidth / 2);
    wy = y + 30 - (destinationHeight / 2) - 10;
    ctx.drawImage(treeimg, sourceX, sourceY, sourceWidth, sourceHeight,
        wx, wy, destinationWidth, destinationHeight);
    wx = x + 25 - (destinationWidth / 2) - 10;
    wy = y + 30 - (destinationHeight / 2) + 10;
    ctx.drawImage(treeimg, sourceX, sourceY, sourceWidth, sourceHeight,
        wx, wy, destinationWidth, destinationHeight);
    wx = x + 25 - (destinationWidth / 2) + 10;
    wy = y + 30 - (destinationHeight / 2) + 10;
    ctx.drawImage(treeimg, sourceX, sourceY, sourceWidth, sourceHeight,
        wx, wy, destinationWidth, destinationHeight);
};

function rock(x, y) {
    var sourceX = 0;
    var sourceY = 0;
    var sourceWidth = 66;
    var sourceHeight = 61;
    var destinationWidth = 49;
    var destinationHeight = 45;
    x = x + 25 - (destinationWidth / 2);
    y = y + 30 - (destinationHeight / 2);
    ctx.drawImage(rockimg, sourceX, sourceY, sourceWidth, sourceHeight,
        x, y, destinationWidth, destinationHeight);
};

function player(x, y) {
    ctx.drawImage(playerimg, x, y);
};

function zombie(x, y) {
    var sourceX = 0;
    var sourceY = 0;
    var sourceWidth = 329;
    var sourceHeight = 571;
    var destinationWidth = 33;
    var destinationHeight = 57;
    x = x + 25 - (destinationWidth / 2);
    y = y + 30 - (destinationHeight / 2);
    ctx.drawImage(zombieimg, sourceX, sourceY, sourceWidth, sourceHeight,
        x, y, destinationWidth, destinationHeight);
};

$(document).keypress(function (event) {
    if ($("#chatin").is(":focus") == false) {
        if (event.which == 49) {
            var key = '1'
            $('.aitem').removeClass('aitem');
            $('#eq0').addClass('aitem')
        }
        if (event.which == 50) {
            var key = '2'
            $('.aitem').removeClass('aitem');
            $('#eq1').addClass('aitem')
        }
        if (event.which == 51) {
            var key = '3'
            $('.aitem').removeClass('aitem');
            $('#eq2').addClass('aitem')
        }
        if (event.which == 52) {
            var key = '4'
            $('.aitem').removeClass('aitem');
            $('#eq3').addClass('aitem')
        }
        if (event.which == 53) {
            var key = '5'
            $('.aitem').removeClass('aitem');
            $('#eq4').addClass('aitem')
        }
        if (event.which == 54) {
            var key = '6'
            $('.aitem').removeClass('aitem');
            $('#eq5').addClass('aitem')
        }
        if (event.which == 119) {
            var key = 'w'
            ws.send(JSON.stringify({
                key: key,
                room: room
            }));
        }
        if (event.which == 97) {
            var key = 'a'
            ws.send(JSON.stringify({
                key: key,
                room: room
            }));
        }
        if (event.which == 115) {
            var key = 's'
            ws.send(JSON.stringify({
                key: key,
                room: room
            }));
        }
        if (event.which == 100) {
            var key = 'd'
            ws.send(JSON.stringify({
                key: key,
                room: room
            }));
        }
        if (event.which == 101) {
            var key = 'e'
            var item = $('.aitem').attr('id')
            ws.send(JSON.stringify({
                key: key,
                room: room,
                item: item
            }));
        }
        if (event.which == 113) {
            var key = 'q'
            ws.send(JSON.stringify({
                key: key,
                room: room
            }));
        }
        if (event.which == 122) {
            var key = 'z'
            ws.send(JSON.stringify({
                key: key,
                room: room
            }));
        }
        if (event.which == 120) {
            var key = 'x'
            var item = $('.aitem').attr('id')
            ws.send(JSON.stringify({
                key: key,
                room: room,
                item: item
            }));
        }
        if (event.which == 32) {
            event.preventDefault();
            var key = 'space'
            var item = $('.aitem').attr('id')
            ws.send(JSON.stringify({
                key: key,
                room: room,
                item: item
            }));
        }
        console.log(event.which);
    }
});
ws.onopen = function () {
    ws.send(JSON.stringify({
        open: room
    }));
};
ws.onmessage = function (evt) {
    msg = JSON.parse(evt.data);
    if (msg.text != null) {
        var text = msg.text;
        var ps = $("#chat > .msg").size();
        if (ps > 2) {
            $('#chat .msg:first-child').remove();
            $('#chat').html($('#chat').html() + text);
        } else {
            $('#chat').html($('#chat').html() + text);
        }
    }
    if (msg.playa != null) {
        canvas.width = canvas.width;
        var p = msg.playa;
        var centerx = p.x * 52
        var centery = p.y * 45 + 10
        var playerx = p.x
        var playery = p.y
        $('#player-' + p.uid + " #health").html("HP: " + p.health);
        $('#player-' + p.uid + " #exp").html("XP: " + p.xp);
        $('.eq').html("")
        for (var j = 0; j < p.eq.length; j++) {
            $('#eq' + j).html('<img src="' + items[p.eq[j].name] + '"/>')
        }
        var fov = p.fov
        for (var j = 0; j < fov.length; j++) {
            var t = fov[j]
            var yoffset = (t.y - playery) * -26;
            var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
            var destinationY = (t.y * 45) - centery + (canvas.height / 2);
            tile(destinationX, destinationY);
        }
        for (var j = 0; j < fov.length; j++) {
            var t = fov[j]
            console.log(t)
            if (fov[j].type === "Tree") {
                var yoffset = (t.y - playery) * -26;
                var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
                var destinationY = (t.y * 45) - centery + (canvas.height / 2);
                tree(destinationX, destinationY);
            }
            if (fov[j].type === "Rock") {
                var yoffset = (t.y - playery) * -26;
                var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
                var destinationY = (t.y * 45) - centery + (canvas.height / 2);
                rock(destinationX, destinationY);
            }
            if (fov[j].item != null) {
                if (fov[j].item.name === "Unarmed") {
                    var sourceX = 0;
                    var sourceY = 0;
                    var sourceWidth = 256;
                    var sourceHeight = 256;
                    var destinationWidth = 48;
                    var destinationHeight = 48;
                    var yoffset = (t.y - playery) * -26;
                    var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
                    var destinationY = (t.y * 45) - centery + (canvas.height / 2);
                    destinationX = destinationX + 25 - (destinationWidth / 2);
                    destinationY = destinationY + 30 - (destinationHeight / 2);
                    ctx.drawImage(unarmedimg, sourceX, sourceY, sourceWidth, sourceHeight,
                        destinationX, destinationY, destinationWidth, destinationHeight);
                }
                if (fov[j].item.name === "Bat") {
                    var sourceX = 0;
                    var sourceY = 0;
                    var sourceWidth = 128;
                    var sourceHeight = 128;
                    var destinationWidth = 48;
                    var destinationHeight = 48;
                    var yoffset = (t.y - playery) * -26;
                    var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
                    var destinationY = (t.y * 45) - centery + (canvas.height / 2);
                    destinationX = destinationX + 25 - (destinationWidth / 2);
                    destinationY = destinationY + 30 - (destinationHeight / 2);
                    ctx.drawImage(batimg, sourceX, sourceY, sourceWidth, sourceHeight,
                        destinationX, destinationY, destinationWidth, destinationHeight);
                }
                if (fov[j].item.name === "Sword") {
                    var sourceX = 0;
                    var sourceY = 0;
                    var sourceWidth = 128;
                    var sourceHeight = 128;
                    var destinationWidth = 48;
                    var destinationHeight = 48;
                    var yoffset = (t.y - playery) * -26;
                    var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
                    var destinationY = (t.y * 45) - centery + (canvas.height / 2);
                    destinationX = destinationX + 25 - (destinationWidth / 2);
                    destinationY = destinationY + 30 - (destinationHeight / 2);
                    ctx.drawImage(swordimg, sourceX, sourceY, sourceWidth, sourceHeight,
                        destinationX, destinationY, destinationWidth, destinationHeight);
                }
                if (fov[j].item.name === "Beans") {
                    var sourceX = 0;
                    var sourceY = 0;
                    var sourceWidth = 190;
                    var sourceHeight = 307;
                    var destinationWidth = 31;
                    var destinationHeight = 50;
                    var yoffset = (t.y - playery) * -26;
                    var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
                    var destinationY = (t.y * 45) - centery + (canvas.height / 2);
                    destinationX = destinationX + 25 - (destinationWidth / 2);
                    destinationY = destinationY + 30 - (destinationHeight / 2);
                    ctx.drawImage(beansimg, sourceX, sourceY, sourceWidth, sourceHeight,
                        destinationX, destinationY, destinationWidth, destinationHeight);
                }
            }
            player(canvas.width / 2, canvas.height / 2);
        }

    }
    if (msg.npcs != null) {
        var npcs = msg.npcs
        for (var j = 0; j < npcs.length; j++) {
            var t = npcs[j]
            var yoffset = (t.y - playery) * -26;
            var destinationX = ((t.x * 52) - centerx + (canvas.width / 2)) + yoffset;
            var destinationY = (t.y * 45) - centery + (canvas.height / 2);
            zombie(destinationX, destinationY);
        }
    }
};
ws.onclose = function () {
    ws.send(JSON.stringify({
        close: room
    }));
};

function chat(message) {
    var msg = $.trim($('#chatin').val());
    $('#chatin').val("");
    if (msg != "") {
        ws.send(JSON.stringify({
            chat: msg,
            room: room
        }));
    }
};
