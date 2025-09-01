function fetchComponent() {
    return fetch('../../shared/components/delete_warning.html')
    .then(Response => Response.text())
    .then(html => {
        let parser = new DOMParser();
        let doc = parser.parseFromString(html, 'text/html');
        let deleteWarningDev = document.getElementById("delete-warning");
        deleteWarningDev.innerHTML = '';
        deleteWarningDev.append(...doc.body.children);
    })
}


export function warningPopUp() {
    return fetchComponent().then(() => {
        let promise = new Promise((resolve) => {
        let body = document.body
        let deleteWarning = document.getElementById("delete-warning");
        deleteWarning.style.display = 'block';
        body.classList.add('body');
    
        deleteWarning.addEventListener('click', (e) => {
            if (e.target.id == 'confirm-btn') {
                deleteWarning.style.display = 'none';
                body.classList.remove('body');
                resolve(true);
            }
            else {
                deleteWarning.style.display = 'none';
                body.classList.remove('body');
                resolve(false);
            }
        }, {once: true});
    });
        return promise  
    })
}