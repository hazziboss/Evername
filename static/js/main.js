/**
 * EverName - Main JavaScript
 * Handles wallet connections, API interactions, and UI updates
 */

// Global state
let wallet = {
    connected: false,
    address: null,
    chain: null
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    checkWalletConnection();
    initializeEventListeners();
    initializeDropdown();
});

/**
 * Check if wallet is already connected
 */
function checkWalletConnection() {
    const storedWallet = sessionStorage.getItem('wallet');
    if (storedWallet) {
        wallet = JSON.parse(storedWallet);
        updateWalletUI();
    }
}

/**
 * Connect to MetaMask or other Web3 wallet
 */
async function connectWallet(provider = 'metamask') {
    try {
        if (typeof window.ethereum === 'undefined') {
            alert('Please install MetaMask or another Web3 wallet!');
            return;
        }

        const accounts = await window.ethereum.request({
            method: 'eth_requestAccounts'
        });

        const chainId = await window.ethereum.request({
            method: 'eth_chainId'
        });

        wallet.connected = true;
        wallet.address = accounts[0];
        wallet.chain = chainId;

        // Store in session
        sessionStorage.setItem('wallet', JSON.stringify(wallet));

        // Send to backend
        await fetch('/api/connect', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                address: wallet.address,
                chain: wallet.chain
            })
        });

        updateWalletUI();
        showNotification('Wallet connected successfully!', 'success');

        // Redirect to dashboard if on connect page
        if (window.location.pathname === '/connect-wallet') {
            setTimeout(() => {
                window.location.href = '/nillion-login';
            }, 1000);
        }

    } catch (error) {
        console.error('Wallet connection error:', error);
        showNotification('Failed to connect wallet', 'error');
    }
}

/**
 * Disconnect wallet
 */
function disconnectWallet() {
    wallet = {
        connected: false,
        address: null,
        chain: null
    };
    sessionStorage.removeItem('wallet');
    updateWalletUI();
    showNotification('Wallet disconnected', 'info');
}

/**
 * Update wallet UI
 */
function updateWalletUI() {
    const walletAddressEl = document.getElementById('wallet-address');
    const statusIndicator = document.querySelector('.status-indicator');

    if (wallet.connected && wallet.address) {
        const shortAddress = `${wallet.address.slice(0, 6)}...${wallet.address.slice(-4)}`;
        if (walletAddressEl) walletAddressEl.textContent = shortAddress;
        if (statusIndicator) statusIndicator.classList.add('connected');
    } else {
        if (walletAddressEl) walletAddressEl.textContent = 'Not Connected';
        if (statusIndicator) statusIndicator.classList.remove('connected');
    }
}

/**
 * Search for domain availability
 */
async function searchDomain(domainName) {
    try {
        const response = await fetch('/api/search-domain', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: domainName })
        });

        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Domain search error:', error);
        return null;
    }
}

/**
 * Register a domain
 */
async function registerDomain(domainName) {
    try {
        const response = await fetch('/api/register-domain', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: domainName })
        });

        const result = await response.json();
        if (result.success) {
            showNotification('Domain registered successfully!', 'success');
            return result;
        }
    } catch (error) {
        console.error('Domain registration error:', error);
        showNotification('Failed to register domain', 'error');
    }
}

/**
 * Add a delegate
 */
async function addDelegate(delegateAddress, percentage, domainId) {
    try {
        const response = await fetch('/api/add-delegate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                address: delegateAddress,
                percentage: percentage,
                domain_id: domainId
            })
        });

        const result = await response.json();
        if (result.success) {
            showNotification('Delegate added successfully!', 'success');
            return result;
        }
    } catch (error) {
        console.error('Add delegate error:', error);
        showNotification('Failed to add delegate', 'error');
    }
}

/**
 * Confirm user is alive (liveness check)
 */
async function confirmAlive() {
    try {
        const response = await fetch('/api/confirm-alive', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        const result = await response.json();
        if (result.success) {
            showNotification('Liveness confirmed! Next check: ' + new Date(result.next_check).toLocaleDateString(), 'success');
            return result;
        }
    } catch (error) {
        console.error('Confirm alive error:', error);
        showNotification('Failed to confirm liveness', 'error');
    }
}

/**
 * Show notification toast
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#6366f1'};
        color: white;
        border-radius: 0.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        z-index: 9999;
        animation: slideIn 0.3s ease;
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Initialize event listeners
 */
function initializeEventListeners() {
    // Connect wallet buttons
    const connectButtons = document.querySelectorAll('[data-action="connect-wallet"]');
    connectButtons.forEach(btn => {
        btn.addEventListener('click', () => connectWallet());
    });

    // Domain search form
    const searchForm = document.querySelector('[data-form="domain-search"]');
    if (searchForm) {
        searchForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const input = searchForm.querySelector('input[name="domain"]');
            const result = await searchDomain(input.value);
            if (result) {
                window.location.href = `/availability?q=${input.value}`;
            }
        });
    }

    // Register domain button
    const registerButtons = document.querySelectorAll('[data-action="register-domain"]');
    registerButtons.forEach(btn => {
        btn.addEventListener('click', async () => {
            const domainName = btn.dataset.domain;
            await registerDomain(domainName);
        });
    });

    // Add delegate form
    const delegateForm = document.querySelector('[data-form="add-delegate"]');
    if (delegateForm) {
        delegateForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const address = delegateForm.querySelector('input[name="address"]').value;
            const percentage = delegateForm.querySelector('input[name="percentage"]').value;
            const domainId = delegateForm.querySelector('input[name="domain_id"]').value;
            await addDelegate(address, percentage, domainId);
        });
    }

    // Confirm alive button
    const aliveButtons = document.querySelectorAll('[data-action="confirm-alive"]');
    aliveButtons.forEach(btn => {
        btn.addEventListener('click', async () => {
            await confirmAlive();
        });
    });
}

/**
 * Initialize dropdown menu for better accessibility
 */
function initializeDropdown() {
    const dropdown = document.querySelector('.nav-dropdown');
    const dropdownBtn = document.querySelector('.nav-dropdown-btn');
    const dropdownContent = document.querySelector('.nav-dropdown-content');

    if (!dropdown || !dropdownBtn || !dropdownContent) return;

    // Toggle dropdown on click
    dropdownBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdown.classList.toggle('active');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!dropdown.contains(e.target)) {
            dropdown.classList.remove('active');
        }
    });

    // Keep dropdown open when hovering over content
    dropdownContent.addEventListener('mouseenter', () => {
        dropdown.classList.add('active');
    });

    // Close dropdown when clicking a link
    const dropdownLinks = dropdownContent.querySelectorAll('a');
    dropdownLinks.forEach(link => {
        link.addEventListener('click', () => {
            dropdown.classList.remove('active');
        });
    });
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
