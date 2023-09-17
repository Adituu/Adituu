document.addEventListener("DOMContentLoaded", function (event) {
	var currentDate = new Date();

	var copyrightYear = document.getElementById("copyright_date");
	copyrightYear.innerText = `${currentDate.getFullYear()}`;
});

// var discordContactButton = document.getElementById("discordContact");

// discordContactButton.addEventListener("click", function (event) {
// 	navigator.clipboard.writeText("discord#tag");

// });
