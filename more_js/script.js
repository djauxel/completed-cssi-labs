var red, green, blue;
var clickCount = 0;
const batteryBar = document.getElementById('first');

function rgb(r, g, b){
  return "rgb("+r+","+g+","+b+")";
}

batteryBar.addEventListener('click', ()=> {
  clickCount++;
  console.log(clickCount);

  red = Math.round(Math.random() * 255);
  green = Math.round(Math.random() * 255);
  blue = Math.round(Math.random() * 255);
  console.log("rgb(" + red + ", " + green + ", " + blue + ")"); // print the rgb codes

  batteryBar.style.background = rgb(red, green, blue);

  let cell = document.createElement('div');
  cell.classList.add('cell');
  batteryBar.append(cell);
});