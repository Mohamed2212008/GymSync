let selectElement = document.getElementById("sport-select");

eel.load_sports()((result) => {
    result.forEach(sport => {
       let option = document.createElement("option");
       option.value = sport.sport_name;
       option.textContent = sport.sport_name;
       selectElement.append(option);
    });
});