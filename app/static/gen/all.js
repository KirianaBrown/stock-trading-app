console.log("hello from the console");

function switchTabs(evt, action) {
    let i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    c;
    tablinks = document.getElementsByClassName("tab-links");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("tab-active", "");
    }

    document.getElementById(action).style.display = "block";
    evt.currentTarget.className += " tab-active";
}

const closePopUp = () => {
    let flashMessage = document.querySelector(".flash");
    flashMessage.style.display = "none";
};

function onReady(callback) {
    var intervalId = window.setInterval(function() {
        if (document.getElementsByTagName("body")[0] !== undefined) {
            window.clearInterval(intervalId);
            callback.call(this);
        }
    }, 1000);
}

function setVisible(selector, visible) {
    document.querySelector(selector).style.display = visible ? "block" : "none";
}

onReady(function() {
    setVisible(".dashboard-content-content", true);
    setVisible(".loader", false);
});

let acc = document.getElementsByClassName("accordion");
let i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("accordian-selected");

        let panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}