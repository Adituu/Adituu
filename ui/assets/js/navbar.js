var navToggled = false;

var navToggler = document.getElementById("navbarToggle");

navToggler.addEventListener("click", function (event) {
	var navList = document.getElementById("navbarList");

	if (navToggled == false) {
		navList.classList.add("visible");
		navList.classList.remove("hidden");

		navToggled = true;
	} else {
		navList.classList.remove("visible");
		navList.classList.add("hidden");

		navToggled = false;
	}
});
