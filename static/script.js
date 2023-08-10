function calculate() {
    const lambdaValue = document.getElementById('lambda').value;
    const muValue = document.getElementById('mu').value;
    const serversValue = document.getElementById('servers').value;
    const capacityValue = document.getElementById('capacity').value;

    const requestBody = {
        lambda: parseFloat(lambdaValue),
        mu: parseFloat(muValue),
        servers: parseInt(serversValue),
        capacity: parseInt(capacityValue) || 0
    };

    axios.post('/api/calculate', requestBody)
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
    serverInput.disabled = !switchElement.checked;
    systemPrefix = serverInput.disabled ? 'M/M/1' : 'M/M/S';
    systemName.textContent = `${systemPrefix}${systemName.textContent.substring(5)}`
    serverInput.value = serverInput.disabled ? 1 : '';
    contServerInput.style.opacity = serverInput.disabled ? 0.5 : 1;
    contServerInput.style.opacity = serverInput.disabled ? 'none' : 'auto';
}

function validateNumber(input, errorMessage) {
    const systemName = document.getElementById('system_name');
    const value = parseFloat(input.value);
    const isOptional = input.classList.contains('optional-number');
    const message = isOptional ? "El número debe ser mayor que cero" : "Este campo es obligatorio y debe ser mayor que cero";

    if (document.activeElement === input) {
        if ((!isOptional && (isNaN(value) || value <= 0)) || (isOptional && !isNaN(value) && value <= 0)) {
            showError(input, message, errorMessage);
            return false;
        } else {
            hideError(input, errorMessage);
        }

    }
    
    if (input.id == 'capacity') {
        if (input.value === '') {
            systemName.textContent = systemName.textContent.replace('/K', '');
        } else if (!systemName.textContent.includes('/K')) {
            systemName.textContent += '/K';
        }
        // const serversInput = document.getElementById('servers');
        // const capacityValue = parseInt(input.value);
        // const serversValue = parseInt(serversInput.value);
        // if (capacityValue < serversValue) {
        //     showError(input, "La capacidad debe ser mayor o igual que el número de servidores", errorMessage);
        // } else {
        //     hideError(input, errorMessage);
        // }
    }
}

function showError(input, message, errorMessage) {
    const parentContainer = input.closest('.input_section_data');
    parentContainer?.classList.add('error', 'error-shake');

    errorMessage.textContent = message;
    errorMessage.style.opacity = 1;

    setTimeout(() => {
        errorMessage.style.opacity = 0;
    }, 5000);
}

function hideError(input, errorMessage) {
    input.classList.remove('error', 'error-shake');
    errorMessage.style.opacity = 0;
}


document.addEventListener("DOMContentLoaded", function () {
    toggleServerInput();
    var errorMessage = document.querySelector('.error-message');
    var inputs = document.querySelectorAll('.required-number, .optional-number');
    console.log(inputs)
    inputs.forEach(input => {
        input.addEventListener('input', () => validateNumber(input, errorMessage))
    });

    var form = document.getElementById('form');
    form.addEventListener('submit', (event) => {
        event.preventDefault()

        if (form.checkValidity()) {
            calculate();
        }

    })
});