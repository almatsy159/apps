

//a coded poem - also on medium(unmetered): //https://medium.com/@sophiawood/to-remind-ourselves-b7d66da90ca4
function setup() {
    //we make these spaces for creation
    createCanvas(600, 600);
    }

function draw() {
    const can = document.getElementById("can")
    const ctx = can.getContext("2d");
    ctx.fillRect("150,0,0,75")
}


//document.getElementById("login")
divs = document.querySelector("div")

for(let d=0;d<divs.length;d++){
    d.style.background = "red"
}


//idea getting all child of body , getting all css property (style,pos,mvt) and for all childs 


// body.[childs]

// c as child :
//    c <block> => all child of c that is <block>