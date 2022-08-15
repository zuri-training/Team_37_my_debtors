const menu = document.getElementById("ham")
const mMenu = document.getElementById("mham")
const side = document.querySelector(".sidebar")
const cancel = document.querySelector(".fa-xmark")


mMenu.addEventListener("click", showBar)
cancel.addEventListener("click", hideBar)
function showBar() {
    side.style.display = "block"
}

function hideBar() {
    side.style.display = "none"
}