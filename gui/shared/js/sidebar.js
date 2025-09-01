let currentScript = document.currentScript;
let currentPage = currentScript.getAttribute("data-page");

fetch('../shared/components/sidebar.html')
    .then(Response => Response.text())
    .then(html => {
        let parser = new DOMParser();
        let doc  = parser.parseFromString(html, 'text/html');

        let activePage = doc.getElementById(currentPage);
        activePage.classList.add("active");

        let sidebar = document.getElementById("sidebar");
        sidebar.innerHTML = '';
        sidebar.append(...doc.body.children);
})