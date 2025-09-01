let body = document.body;
let addBtn = document.getElementById("add-btn");
let popUp = document.getElementById("pop-up");
let cancelBtn = document.getElementById("cancel");

export function closePopUp(){
    popUp.style.display = "None";
    body.classList.remove("body");
}

addBtn.addEventListener("click", () => {
    popUp.style.display = "block";
    body.classList.add("body");

    cancelBtn.onclick = closePopUp;
});
