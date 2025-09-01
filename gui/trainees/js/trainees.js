import {closePopUp} from "../../shared/js/modal.js";
import { warningPopUp } from "../../shared/js/delete_warning.js";

let traineeForm = document.getElementById("add-trainee-form");
let contentDiv = document.getElementById("content");
loadTrainees();

function loadTrainees() {
    contentDiv.innerHTML = "";
    eel.load_trainees()((result) => {
        result.forEach(trainee => {
            let card = document.createElement("div");
            card.classList.add("card");
            card.innerHTML = `
                <div class="info t-info">
                    <p class="name">${trainee.name}</p>
                    <p class="age">${trainee.age}</p>
                    <p class="gender">${trainee.gender}</p>
                    <p class="phone_num">${trainee.phone_num}</p>
                    <p class="sport">${trainee.sport}</p>
                    <p class="coach">${trainee.coach}</p>
                </div>
                <div class="btns">
                    <button class="btn edit" data-trainee="${trainee.name}">edit</button>
                    <button class="btn delete" data-trainee="${trainee.name}">delete</button>
                </div>          
            `
            contentDiv.append(card);
        });
    });
}

traineeForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let traineeNameInput = document.getElementById("t-name");
    let traineeAgeInput = document.getElementById("t-age");
    let traineePhoneNumInput = document.getElementById("t-phone-num");
    let traineeGender = document.getElementById("gender-select");
    let sport = document.getElementById("sport-select");
    let coach = document.getElementById("coach-select");

    let traineeName = traineeNameInput.value;
    let traineeAge = traineeAgeInput.value;
    let traineePhoneNum = traineePhoneNumInput.value;

    traineeNameInput.value = "";
    traineeAgeInput.value = "";
    traineePhoneNumInput.value = "";
    
    let gender = false
    if (traineeGender.value == "1"){
        gender = true
    }
    eel.add_trainee(traineeName, traineeAge, gender, traineePhoneNum, sport.value, coach.value)(() => {
        closePopUp();
        loadTrainees();
    });
});

contentDiv.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete")) {
        warningPopUp().then((confirmed) => {
            if (confirmed) {
                let trainee = e.target.getAttribute("data-trainee");
                console.log(trainee);
                eel.remove_trainee(trainee);
                loadTrainees();
            }
        });
    }
});