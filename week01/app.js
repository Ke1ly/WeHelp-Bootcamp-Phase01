function showSideMenu() {
  let sidemenu = document.querySelector(".hamburger-menu");
  sidemenu.style.display = "block";
}
function hideSideMenu() {
  let sidemenu = document.querySelector(".hamburger-menu");
  sidemenu.style.display = "none";
}

function SideMenu() {
  if (window.innerWidth > 600) {
    hideSideMenu();
  }
}

window.addEventListener("resize", SideMenu);
