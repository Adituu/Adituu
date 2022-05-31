const changeButton = document.getElementById('change-theme');

var currentTheme = 'blue';

changeButton.addEventListener('click', function() {
    if (currentTheme == 'blue') {
        currentTheme = 'red';
        document.getElementById('main-style').href = '/static/css/themes/main.red.css';
    } else {
        currentTheme = 'blue';
        document.getElementById('main-style').href = '/static/css/main.css';
    }
});
