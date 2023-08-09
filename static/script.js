function calculate() {
    const lambdaValue = document.getElementById('lambda').value;
    const muValue = document.getElementById('mu').value;
    const serversValue = document.getElementById('servers').value;
    const capacityValue = document.getElementById('capacity').value;

    const data = {
        lambda: lambdaValue,
        mu: muValue,
        servers: serversValue,
        capacity: capacityValue
    };

    axios.post('/api/calculate', data)
        .then(response => {
            document.getElementById('system-title').innerText = "System " + response.data.system_name;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function toggleServerInput() {
    const contServerInput = document.getElementById('input_servers');
    const systemName = document.getElementById('system_name');
    const serverInput = document.getElementById('servers');
    const switchElement = document.getElementById('server-switch');
    console.log(switchElement)
    serverInput.disabled = !switchElement.checked;
    systemName.textContent = serverInput.disabled ? 'M/M/1' : 'M/M/S';
    serverInput.value = serverInput.disabled ? 1 : '';
    contServerInput.style.opacity = serverInput.disabled ? 0.5 : 1;
    contServerInput.style.opacity = serverInput.disabled ? 'none' : 'auto';
}

function validateNumber(input) {

    var value = parseFloat(input.value);
    var errorMessage = "Este campo es obligatorio y debe ser mayor o igual a 1.";

    if (input.classList.contains('optional-number') && (isNaN(value) || value >= 1)) {
        input.setCustomValidity('');
    } else if (!isNaN(value) && value >= 1) {
        input.setCustomValidity('');
    } else {
        input.setCustomValidity(errorMessage);
    }
}

function showErrorMessage(input, message) {
    var errorElement = input.nextElementSibling;
    if (!errorElement || !errorElement.classList.contains('error-message')) {
        errorElement = document.createElement('span');
        errorElement.className = 'error-message';
        input.insertAdjacentElement('afterend', errorElement);
    }
    errorElement.textContent = message;
}

function hideErrorMessage(input) {
    var errorElement = input.nextElementSibling;
    if (errorElement && errorElement.classList.contains('error-message')) {
        errorElement.remove();
    }
}


document.addEventListener("DOMContentLoaded", function () {
    toggleServerInput();
});

var inputs = document.querySelectorAll('.required-number, .optional-number');
inputs.forEach(function (input) {
    input.addEventListener('input', function () {
        validateNumber(input);
    });
});