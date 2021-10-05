// 初始化視窗大小
$(document).ready(function () {
    window.resizeTo(450, 250);
});

let number = document.getElementById("number");
let search = document.getElementById("search");
let random = document.getElementById("random");

search.addEventListener("click", Search);
number.addEventListener("keypress", e => {if (e.key == "Enter") Search()});

function Search() {eel.download(number.value)};

let max = 375615;    // 隨機漫畫的最大值

getRandom = max => {return String(Math.floor(Math.random() * max) + 1)};

random.addEventListener("click", () => {eel.download(getRandom(max))});