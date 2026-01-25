// API Configuration
const API_BASE_URL = '';

// Token management
const TokenManager = {
    getToken() {
        return localStorage.getItem('access_token');
    },
    
    setToken(token) {
        localStorage.setItem('access_token', token);
    },
    
    removeToken() {
        localStorage.removeItem('access_token');
    },
    
    isAuthenticated() {
        return !!this.getToken();
    }
};

// API utility functions
const API = {
    async request(endpoint, options = {}) {
        const url = `${API_BASE_URL}${endpoint}`;
        const token = TokenManager.getToken();
        
        const defaultHeaders = {
            'Content-Type': 'application/json',
        };
        
        if (token) {
            defaultHeaders['Authorization'] = `Bearer ${token}`;
        }
        
        const config = {
            ...options,
            headers: {
                ...defaultHeaders,
                ...options.headers,
            },
        };
        
        try {
            const response = await fetch(url, config);
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || `HTTP error! status: ${response.status}`);
            }
            
            return data;
        } catch (error) {
            throw error;
        }
    },
    
    async post(endpoint, body) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(body),
        });
    },
    
    async get(endpoint) {
        return this.request(endpoint, {
            method: 'GET',
        });
    }
};

// Auth functions
const Auth = {
    async login(email, password) {
        const data = await API.post('/auth/login', { email, password });
        TokenManager.setToken(data.access_token);
        return data;
    },
    
    async register(email, password) {
        return await API.post('/users', { email, password });
    },
    
    async getProfile() {
        return await API.get('/users/me');
    },
    
    logout() {
        TokenManager.removeToken();
        window.location.href = '/index.html';
    }
};

// Utility functions
const Utils = {
    showError(element, message) {
        element.textContent = message;
        element.style.display = 'block';
        
        // Scroll to error
        element.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    },
    
    hideError(element) {
        element.style.display = 'none';
    },
    
    showSuccess(element, message) {
        element.textContent = message;
        element.style.display = 'block';
    },
    
    hideSuccess(element) {
        element.style.display = 'none';
    },
    
    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    },
    
    setLoading(button, isLoading) {
        if (isLoading) {
            button.disabled = true;
            button.innerHTML = '<span class="spinner"></span>Processing...';
        } else {
            button.disabled = false;
            button.innerHTML = button.getAttribute('data-original-text') || 'Submit';
        }
    }
};

// Protected route check
function requireAuth() {
    if (!TokenManager.isAuthenticated()) {
        window.location.href = '/index.html';
        return false;
    }
    return true;
}

// Public route check (redirect if already authenticated)
function requireGuest() {
    if (TokenManager.isAuthenticated()) {
        window.location.href = '/dashboard.html';
        return false;
    }
    return true;
}
