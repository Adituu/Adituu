const navTogglerButton = document.getElementById("navToggler");
const navList = document.getElementById("navList");

function showNavList() {
	navList.classList.remove("hidden");
	navList.classList.add("visible");
}

function hideNavList() {
	navList.classList.remove("visible");
	navList.classList.add("hidden");
}

navTogglerButton.addEventListener("click", () => {
	if (navList.classList.contains("hidden")) {
		showNavList();
		return;
	}

	hideNavList();
});
