console.log("hello from the console");

function openCity(evt, action) {
    let i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tab-links");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("tab-active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(action).style.display = "block";
    evt.currentTarget.className += " tab-active";
}

const closePopUp = () => {
    let flashMessage = document.querySelector(".flash");
    flashMessage.style.display = "none";
};