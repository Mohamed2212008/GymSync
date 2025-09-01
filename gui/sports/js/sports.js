// loading sports
import { warningPopUp } from "../../shared/js/delete_warning.js"
loadSports();

let form = document.getElementById("sport-form");
let sportsDev = document.getElementById("sportsDev");

function loadSports() {
    eel.load_sports()((result) => {
        sportsDev.innerHTML = "";
        result.forEach(sport => {
            let sportCard = document.createElement('div');
            sportCard.classList.add("card");
            sportCard.innerHTML = `
                <div class="info">
                    <p class="name">${sport.sport_name}</p>
                    <p class="type">${sport.sport_type}</p>
                    <p class="players">${sport.trainees} trainees</p>
                    <p class="coaches">${sport.coaches} coaches</p>
                </div>
                <div class="btns">
                    <button class="btn edit" data-sport="${sport.sport_name}">edit</button>
                    <button class="btn delete" data-sport="${sport.sport_name}">delete</button>
                </div>
            `;
            sportsDev.append(sportCard);
        });
    });
}

// adding new sport
form.addEventListener("submit", (e) => {
    e.preventDefault();
    let sportNameInput = document.getElementById("sport-name");
    let sportTypeInput = document.getElementById("sport-type");

    let sportName = sportNameInput.value;
    let sportType = sportTypeInput.value;

    sportNameInput.value = '';
    sportTypeInput.value = '';

    eel.add_sport(sportName, sportType)(function() {
        closePopUp();
        loadSports();
    });
})

// delete sport
sportsDev.addEventListener("click", (e) => {
    if(e.target.classList.contains("delete")) {
        warningPopUp().then((confirmed) => {
            if (confirmed) {
                let sport = e.target.getAttribute("data-sport");
                eel.delete_sport(sport);
                loadSports()
            }
        });
    }
});



// change the scrollbar style
// add multiple languages En, Ar
// 