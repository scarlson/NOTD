// oh god I have no idea what I'm doing
//

var d = new Date()
var offset = d.getTimezoneOffset()
var timeField = $(".time")
var dafuq = timeField.html()
var hours = parseInt(dafuq[0] + dafuq[1])
if (dafuq[0] == "0") {
    hours = parseInt(dafuq[1])
}
if (dafuq[5] == 'P') {
    hours = hours + 12
}

if (offset == 360) {
    hours = hours - 1
}
if (offset == 420) {
    hours = hours + 1
}

rebuild = "01/01/2000 " + String(hours) + ":" + dafuq[3] + dafuq[4] + ":00"
tz = String(String(d).split("(")[1]).split(")")[0]

timeField.html(formatDate(rebuild) + " " + tz)

function formatDate(date) {
    var d = new Date(date);
    var hh = d.getHours();
    var m = d.getMinutes();
    var s = d.getSeconds();
    var dd = "AM";
    var h = hh;
    if (h >= 12) {
        h = hh-12;
        dd = "PM";
    }
    if (h == 0) {
        h = 12;
    }
    m = m<10?"0"+m:m;
    s = s<10?"0"+s:s;

    /* if you want 2 digit hours:
    *     h = h<10?"0"+h:h; */

    var pattern = new RegExp("0?"+hh+":"+m+":"+s);

    var repalcement = h+":"+m;
    /* if you want to add seconds
    *     repalcement += ":"+s;  */
    repalcement += dd;    

    return repalcement;
}
