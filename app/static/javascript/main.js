document.getElementById('wash-form').addEventListener('submit', function(event) {
    event.preventDefault();
    fetchStages();
});

function fetchStages() {
    fetch('/wash_status')
        .then(response => response.json())
        .then(stages => {
            let statusElement = document.getElementById('current-status');

            stages.forEach((stage, index) => {
                setTimeout(() => {
                    statusElement.textContent = stage.status;
                }, index * 2000);
            });
        })
        .catch(error => console.error('Error:', error));
}
