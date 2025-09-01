let select = document.getElementById("coach-select");

eel.load_coaches()((result) => {
    result.forEach(coach => {
        let option = document.createElement("option");
        console.log(coach);
        option.value = coach.name;
        option.textContent = coach.name;
        select.append(option);
    });
});