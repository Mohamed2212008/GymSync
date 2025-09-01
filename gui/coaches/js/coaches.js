import { warningPopUp } from "../../shared/js/delete_warning.js";

let addCoachBtn = document.getElementById("add-coach");
let PopUp = document.getElementById("add-coach-form");
let addCoachForm = document.getElementById("coach-form");
let body = document.body;
let cancelBtn = document.getElementById("cancel");
let coachesDiv = document.getElementById("coaches-div");


loadCoaches();

// load coaches
function loadCoaches(){
    coachesDiv.innerHTML = "";
    eel.load_coaches()((result) => {
        result.forEach(coach => {
            let div = document.createElement("div");
            div.classList.add("card");
            div.innerHTML = `
                <div class="info">
                    <p class="c-name">${coach.name}</p>
                    <p class="c-phone-num">${coach.phone_num}</p>
                    <p class="c-specialty">${coach.specialty}</p>
                </div>
                <div class="btns">
                    <button class="btn edit" data-coach="${coach.name}">edit</button>
                    <button class="btn delete" data-coach="${coach.name}">delete</button>
                </div>
            `
            coachesDiv.append(div);
        });
    });
}


addCoachForm.addEventListener("submit", (e) => {
    e.preventDefault();
    let coachNameInput = document.getElementById("coach-name");
    let coachPhoneNumInput = document.getElementById("coach-phone-num");
    let coachSpecialtyInput = document.getElementById("coach-specialty");

    let coachName = coachNameInput.value;
    let coachPhoneNum = coachPhoneNumInput.value;
    let coachSpecialty = coachSpecialtyInput.value; 

    coachNameInput.value = '';
    coachPhoneNumInput.value = '';
    coachSpecialtyInput.value = '';

    eel.add_coach(coachName, coachPhoneNum, coachSpecialty)(() => {
        closePopUp();
        loadCoaches();
    });
});

// delete
coachesDiv.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete")) {
        warningPopUp().then((confirmed) => {
            if (confirmed) {
                let coach = e.target.getAttribute("data-coach");
                eel.remove_coach(coach);
                loadCoaches();
            }
        });
    }
});