// https://bfl-centr.ru/ - main source

// load DOM for the first step:

document.addEventListener('DOMContentLoaded', function() {

    const form = document.getElementById('form'); // variable to connect with form

    form.addEventListener('submit', sendData); // event listener to send data if user submit the form (press Enter or click the button)

    async function sendData(event) {
        event.preventDefault; // cancel page reload
    }
})

