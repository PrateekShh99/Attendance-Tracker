document.getElementById('attendanceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const checkedRadios = document.querySelectorAll('input[type="radio"]:checked');
    const attendanceArray = [];
    checkedRadios.forEach(radio => {
        attendanceArray.push({ name: radio.name, value: radio.value });
    });

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ attendance: attendanceArray })
    });
});

window.onload = function() {
    const peopleSections = document.querySelectorAll('.person-info');
    peopleSections.forEach(section => {
        const radios = section.querySelectorAll('input[type="radio"]');
        let isSelected = false;
        
        radios.forEach(radio => {
            if (radio.checked) {
                isSelected = true;
            }
        });
        
        if (!isSelected && radios.length > 0) {
            radios[0].checked = true;
        }
    });
}
