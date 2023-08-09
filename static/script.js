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
    const value = parseFloat(input.value);
    const isOptional = input.classList.contains('optional-number');
    const errorMessage = isOptional ? "El número opcional debe ser mayor o igual a 1." : "Este campo es obligatorio y debe ser mayor o igual a 1.";

    if (document.activeElement === input) {
        if ((!isOptional && (isNaN(value) || value < 1)) || (isOptional && !isNaN(value) && value < 1)) {
            showError(input, errorMessage);
        } else {
            hideError(input);
        }
    }
}

function showError(input, message) {
    input.classList.add('error');
    let errorElement = input.nextElementSibling;

    if (!errorElement || !errorElement.classList.contains('error-message')) {
        errorElement = document.createElement('span');
        errorElement.className = 'error-message';
        input.insertAdjacentElement('afterend', errorElement);
    }

    errorElement.textContent = message;
}

function hideError(input) {
    input.classList.remove('error');
    const errorElement = input.nextElementSibling;

    if (errorElement && errorElement.classList.contains('error-message')) {
        errorElement.remove();
    }
}


document.addEventListener("DOMContentLoaded", function () {
    toggleServerInput();

    // var inputs = document.querySelectorAll('.required-number, .optional-number');
    // console.log(inputs)
    // inputs.forEach(input => {
    //     input.addEventListener('input', () => validateNumber(input))
    // });
});