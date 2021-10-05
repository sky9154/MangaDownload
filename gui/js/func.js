// 初始化視窗大小
$(document).ready(function () {
    window.resizeTo(450, 250);
});

let number = document.getElementById("number");
function Search() {
    eel.download(number.value);
}
number.addEventListener("keypress", e => {if (e.key == "Enter") Search();});