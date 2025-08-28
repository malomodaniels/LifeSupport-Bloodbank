const searchIcon = document.getElementById("searchIcon");
const searchContainer = document.getElementById("searchContainer");

searchIcon.addEventListener("click", () => {
  searchContainer.classList.toggle("d-none"); // show/hide search bar
});
