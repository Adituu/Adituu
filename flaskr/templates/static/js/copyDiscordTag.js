const discordContactButton = document.getElementById("discordContact");

discordContactButton.addEventListener("click", () => {
	navigator.clipboard.writeText("notRat#2588");
	alert("Discord tag copied to clipboard.\n\nnotRat#2588");
});
