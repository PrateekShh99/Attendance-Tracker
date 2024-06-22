document.getElementById('attendanceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const checkedRadios = document.querySelectorAll('input[type="radio"]:checked');
    const attendanceArray = [];
    for (let i = 0; i < checkedRadios.length; i++) {
        attendanceArray.push(checkedRadios[i].value);
    }
    return attendanceArray;
});