document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting by default

    let isValid = true;
    const email = document.getElementById('email');
    const phone = document.getElementById('phone');
    const errorMessage = document.getElementById('errorMessage');

    // Reset styles and error message
    email.style.borderColor = '';
    phone.style.borderColor = '';
    errorMessage.style.display = 'none';

    // Check email validity
    if (!email.value || !email.checkValidity()) {
        isValid = false;
        email.style.borderColor = 'red';
    }

    // Check phone validity
    if (!phone.value || !phone.checkValidity()) {
        isValid = false;
        phone.style.borderColor = 'red';
    }

    if (!isValid) {
        errorMessage.style.display = 'block';
    } else {
        this.submit(); // Submit the form if all fields are valid
    }
});