const firstBox = document.getElementById('box1');
const secondBox = document.getElementById('box2');
const thirdBox = document.querySelector("#box3");
const containerBox = document.getElementById('container1');
const newBox = document.createElement('div');
newBox.classList.add('box');

let friends = ["Kristian", "Sam", "Michael"];
let ages = [3, 10, 18];

for (i = 0; i < friends.length; i++) {
    textNode = document.createTextNode(friends[i]);
    containerBox.children[i].innerHTML = friends[i];
}

function checkAdult(age) {
    return age >= 18;
}

firstBox.addEventListener('mouseenter', () => {
    firstBox.style.backgroundColor = "blue";
});

firstBox.addEventListener('mouseout', () => {
    firstBox.style.backgroundColor = "red";
});

secondBox.addEventListener('mouseenter', () => {
    secondBox.style.backgroundColor = "green";
    secondBox.classList.add('box2');
});

secondBox.addEventListener('mouseout', () => {
    secondBox.style.backgroundColor = "pink";
    secondBox.classList.remove('box2');
});

thirdBox.addEventListener('mouseenter', () => {
    thirdBox.style.backgroundColor = "purple";
    thirdBox.classList.add('box3');
});

thirdBox.addEventListener('mouseout', () => {
    thirdBox.style.backgroundColor = "orange";
    thirdBox.classList.remove('box3');
});