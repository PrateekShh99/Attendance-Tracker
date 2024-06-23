document.getElementById('attendanceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const checkedRadios = document.querySelectorAll('input[type="radio"]:checked');
    const attendanceArray = [];
    checkedRadios.forEach(radio => {
        attendanceArray.push(radio.value);
    });

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ attendance: attendanceArray })
    });
});
