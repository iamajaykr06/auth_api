// Check if user is already logged in
if (requireGuest && typeof requireGuest === 'function') {
    requireGuest();
}

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const errorMessage = document.getElementById('errorMessage');
    
    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        Utils.hideError(errorMessage);
        
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        const submitButton = loginForm.querySelector('button[type="submit"]');
        
        // Store original button text
        if (!submitButton.getAttribute('data-original-text')) {
            submitButton.setAttribute('data-original-text', submitButton.textContent);
        }
        
        // Validate inputs
        if (!email || !password) {
            Utils.showError(errorMessage, 'Please fill in all fields');
            return;
        }
        
        // Basic email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            Utils.showError(errorMessage, 'Please enter a valid email address');
            return;
        }
        
        try {
            Utils.setLoading(submitButton, true);
            
            await Auth.login(email, password);
            
            // Redirect to dashboard on success
            window.location.href = '/dashboard.html';
        } catch (error) {
            Utils.setLoading(submitButton, false);
            Utils.showError(errorMessage, error.message || 'Login failed. Please check your credentials.');
        }
    });
});
