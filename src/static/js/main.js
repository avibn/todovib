var menu_toggle = document.getElementById('menu-toggle');
var side_nav = document.getElementById('side-nav');
var side_nav_main = document.getElementById('side-nav-main');

function menu_on() {
    side_nav.classList.toggle('side-nav__open');
    side_nav_main.classList.toggle('side-nav-main__open');
}

menu_toggle.onclick = menu_on
var max_width = window.matchMedia("(max-width: 578px)")
max_width.addEventListener("change", () => {
    side_nav.classList.remove('side-nav__open');
    side_nav_main.classList.remove('side-nav-main__open');
})