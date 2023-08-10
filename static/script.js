function calculate() {
    const lambdaValue = document.getElementById('lambda').value;
    const muValue = document.getElementById('mu').value;
    const serversValue = document.getElementById('servers').value;
    const capacityValue = document.getElementById('capacity').value;

    const main = document.getElementById('main_content');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const result_graphic = document.getElementById('result_graphic');
    const upButton = document.getElementById('upButton');
    const downButton = document.getElementById('downButton');

    const requestBody = {
        lambda: parseFloat(lambdaValue),
        mu: parseFloat(muValue),
        servers: parseInt(serversValue),
        capacity: parseInt(capacityValue) || 0
    };
    
    // main.style.display = 'none';
    result.style.display = 'flex';
    result_graphic.style.display = 'flex';

    axios.post('/api/calculate', requestBody)
        .then(response => {
            window.location.href = '#result';
            upButton.style.display = 'block';
            document.getElementById('result_system_name').innerText = "System " + response.data.system_name;
            document.getElementById('result_lambda').innerText = response.data.lamb;
            document.getElementById('result_mu').innerText = response.data.mu;
            document.getElementById('no_servers').innerText = response.data.s;
            document.getElementById('r_capacity').innerText = response.data.k;
            document.getElementById('u_factor').innerText = response.data.rho;
            document.getElementById('ls').innerText = response.data.l;
            document.getElementById('ws').innerText = response.data.w;
            document.getElementById('lq').innerText = response.data.lq;
            document.getElementById('wq').innerText = response.data.wq;
            graphic(response.data.pn);
        })
        .catch(error => {
            // main.style.display = 'flex';
            result.style.display = 'none';
            window.location.href = '#main_content';
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

function graphic(probabilityValues) {
    var ctx = document.getElementById('probabilityNoCustomer').getContext('2d');

    const nValues = probabilityValues.map( function (value, index) { return index});

    const probabilityNoCustomer = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: nValues.map(function (n) {
                return 'n=' + n;
            }),
            datasets: [{
                label: 'Customer probability in the system',
                data: probabilityValues,
                backgroundColor: 'rgba(75, 192, 192, 0.6)', // Color de las barras
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}


document.addEventListener("DOMContentLoaded", function () {
    toggleServerInput();
    var errorMessage = document.querySelector('.error-message');
    var inputs = document.querySelectorAll('.required-number, .optional-number');
    console.log(inputs)
    inputs.forEach(input => {
        input.addEventListener('input', () => validateNumber(input, errorMessage))
    });
    
    let chartStatus = Chart.getChart('probabilityNoCustomer');
    
    var form = document.getElementById('form');
    form.addEventListener('submit', (event) => {
        event.preventDefault()

        if (form.checkValidity()) {
            if (chartStatus != undefined) {
                chartStatus.destroy();
            }
            calculate();
        }
    })
});