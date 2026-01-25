// Check authentication
if (requireAuth && typeof requireAuth === 'function') {
    if (!requireAuth()) {
        // Redirect will happen in requireAuth
        return;
    }
}

document.addEventListener('DOMContentLoaded', async function() {
    const loadingMessage = document.getElementById('loadingMessage');
    const errorMessage = document.getElementById('errorMessage');
    const userInfo = document.getElementById('userInfo');
    const logoutBtn = document.getElementById('logoutBtn');
    
    // Load user profile
    try {
        const profile = await Auth.getProfile();
        
        // Hide loading, show user info
        loadingMessage.style.display = 'none';
        userInfo.style.display = 'block';
        
        // Populate user data
        document.getElementById('userId').textContent = profile.id;
        document.getElementById('userEmail').textContent = profile.email;
        document.getElementById('userCreatedAt').textContent = Utils.formatDate(profile.created_at);
    } catch (error) {
        loadingMessage.style.display = 'none';
        Utils.showError(errorMessage, error.message || 'Failed to load profile. Please try again.');
        
        // If token is invalid, redirect to login
        if (error.message.includes('token') || error.message.includes('401')) {
            setTimeout(() => {
                Auth.logout();
            }, 2000);
        }
    }
    
    // Logout handler
    logoutBtn.addEventListener('click', function() {
        Auth.logout();
    });
});
