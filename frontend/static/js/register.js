// Check if user is already logged in
if (requireGuest && typeof requireGuest === 'function') {
    requireGuest();
}

document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const errorMessage = document.getElementById('errorMessage');
    const successMessage = document.getElementById('successMessage');
    
    registerForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        Utils.hideError(errorMessage);
        Utils.hideSuccess(successMessage);
        
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const submitButton = registerForm.querySelector('button[type="submit"]');
        
        // Store original button text
        if (!submitButton.getAttribute('data-original-text')) {
            submitButton.setAttribute('data-original-text', submitButton.textContent);
        }
        
        // Validate inputs
        if (!email || !password || !confirmPassword) {
            Utils.showError(errorMessage, 'Please fill in all fields');
            return;
        }
        
        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            Utils.showError(errorMessage, 'Please enter a valid email address');
            return;
        }
        
        // Password validation
        if (password.length < 8) {
            Utils.showError(errorMessage, 'Password must be at least 8 characters long');
            return;
        }
        
        // Password confirmation
        if (password !== confirmPassword) {
            Utils.showError(errorMessage, 'Passwords do not match');
            return;
        }
        
        try {
            Utils.setLoading(submitButton, true);
            
            await Auth.register(email, password);
            
            Utils.setLoading(submitButton, false);
            Utils.showSuccess(successMessage, 'Account created successfully! Redirecting to login...');
            
            // Redirect to login after 2 seconds
            setTimeout(() => {
                window.location.href = '/index.html';
            }, 2000);
        } catch (error) {
            Utils.setLoading(submitButton, false);
            Utils.showError(errorMessage, error.message || 'Registration failed. Please try again.');
        }
    });
});
