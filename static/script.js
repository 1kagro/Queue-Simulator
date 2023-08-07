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
document.addEventListener("DOMContentLoaded", function () {
    toggleServerInput();
});

