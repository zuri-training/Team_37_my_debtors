const menu = document.getElementById("ham")
const mMenu = document.getElementById("mham")
const side = document.querySelector(".sidebar")
const cancel = document.querySelector(".fa-xmark")


menu.addEventListener("click", showBar)
mMenu.addEventListener("click", showBar)
cancel.addEventListener("click", hideBar)
function showBar() {
    side.style.display = "block"
}

function hideBar() {
    side.style.display = "none"
}
function MoveRectangle(){
    document.getElementById("rectangle").style.transform="translate(0px)";
    document.getElementById("Fullname").textContent="First Name"
    document.getElementById("id").textContent="ID"
    document.getElementById("phone").textContent="Phone"
    document.getElementById("gender").textContent="Gender"
    document.getElementsByClassName("personal")}
function MoveRectangleback(){
    document.getElementById("rectangle").style.transform="translate(250px)";
    document.getElementById("Fullname").textContent="School Name"
    document.getElementById("id").textContent="Address"
    document.getElementById("phone").textContent="Website"
    document.getElementById("gender").textContent="Proprietor"
    

    

}

   