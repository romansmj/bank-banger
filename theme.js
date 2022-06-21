let changeTheme = document.getElementById('theme-button');

changeTheme.onclick = function() {

    let currentTheme = document.getElementById('theme');

    if (currentTheme.getAttribute('href') == '../front/style/main.css') {
        
        currentTheme.href = '../front/style/light.css';
        
    } else {
        
        currentTheme.href = '../front/style/main.css';
    }
}