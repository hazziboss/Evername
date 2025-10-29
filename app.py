"""
EverName - Decentralized Identity & Legacy Platform
Flask application serving 35 screens for domain management, delegation, and legacy planning
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime, timedelta
import uuid
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Mock data storage (replace with database in production)
users = {}
domains = {}
delegates = {}
notifications = []

# ============================================
# 1. ONBOARDING & AUTH (3 screens)
# ============================================

@app.route('/')
def welcome():
    """Welcome / Intro screen"""
    return render_template('onboarding/welcome.html')

@app.route('/connect-wallet')
def connect_wallet():
    """Connect Wallet (multi-chain)"""
    return render_template('onboarding/connect_wallet.html')

@app.route('/nillion-login')
def nillion_login():
    """Nillion Login + Success"""
    return render_template('onboarding/nillion_login.html')

# ============================================
# 2. HOME & DASHBOARD (6 screens)
# ============================================

@app.route('/dashboard')
def dashboard():
    """Main Dashboard"""
    user_data = session.get('user', {})
    return render_template('dashboard/main.html', user=user_data)

@app.route('/quick-actions')
def quick_actions():
    """Quick Actions Panel"""
    return render_template('dashboard/quick_actions.html')

@app.route('/identity-health')
def identity_health():
    """Identity Liveness Meter + Health"""
    return render_template('dashboard/identity_health.html')

@app.route('/subscription')
def subscription():
    """Subscription / Renewal Status"""
    return render_template('dashboard/subscription.html')

@app.route('/cross-chain-summary')
def cross_chain_summary():
    """Cross-Chain Domains & Wallets Summary"""
    return render_template('dashboard/cross_chain_summary.html')

@app.route('/delegation-preview')
def delegation_preview():
    """Delegation / Legacy Status Preview"""
    return render_template('dashboard/delegation_preview.html')

# ============================================
# 3. NOTIFICATIONS (3 screens)
# ============================================

@app.route('/notification-settings')
def notification_settings():
    """Notification Settings (tier-based)"""
    return render_template('notifications/settings.html')

@app.route('/contact-bind')
def contact_bind():
    """Contact Bind Screen (Email/SMS/Push)"""
    return render_template('notifications/contact_bind.html')

@app.route('/delegate-notifications')
def delegate_notifications():
    """Delegate Notification History (read-only)"""
    return render_template('notifications/delegate_history.html')

# ============================================
# 4. DOMAIN SEARCH & REGISTRATION (5 screens)
# ============================================

@app.route('/search')
def domain_search():
    """Domain Search"""
    return render_template('domains/search.html')

@app.route('/availability')
def domain_availability():
    """Domain Availability"""
    query = request.args.get('q', '')
    return render_template('domains/availability.html', query=query)

@app.route('/marketplace')
def marketplace():
    """Premium / Suggested Names Marketplace"""
    return render_template('domains/marketplace.html')

@app.route('/checkout')
def checkout():
    """Checkout & Payment (NIL discount shown)"""
    domain = request.args.get('domain', '')
    return render_template('domains/checkout.html', domain=domain)

@app.route('/registration-success')
def registration_success():
    """Registration Success"""
    domain = request.args.get('domain', '')
    return render_template('domains/registration_success.html', domain=domain)

# ============================================
# 5. DOMAIN MANAGEMENT (6 screens)
# ============================================

@app.route('/my-domains')
def my_domains():
    """My Domains List"""
    return render_template('management/my_domains.html')

@app.route('/domain/<domain_name>')
def domain_details(domain_name):
    """Domain Details"""
    return render_template('management/domain_details.html', domain=domain_name)

@app.route('/domain/<domain_name>/wallets')
def linked_wallets(domain_name):
    """Linked Wallets & Resolvers"""
    return render_template('management/linked_wallets.html', domain=domain_name)

@app.route('/domain/<domain_name>/edit-records')
def edit_records(domain_name):
    """Edit Resolver Records"""
    return render_template('management/edit_records.html', domain=domain_name)

@app.route('/domain/<domain_name>/add-chain')
def add_chain(domain_name):
    """Add Chain Resolver (EVM / SOL / Sui / Aptos / BNB)"""
    return render_template('management/add_chain.html', domain=domain_name)

@app.route('/domain/<domain_name>/social-linking')
def social_linking(domain_name):
    """Social / Contact Linking (Email, WhatsApp, Telegram)"""
    return render_template('management/social_linking.html', domain=domain_name)

# ============================================
# 6. LEGACY / DELEGATION SETUP (6 screens)
# ============================================

@app.route('/legacy')
def legacy_overview():
    """Legacy Overview"""
    return render_template('legacy/overview.html')

@app.route('/legacy/add-delegate')
def add_delegate():
    """Add Delegate"""
    return render_template('legacy/add_delegate.html')

@app.route('/legacy/allocate-permissions')
def allocate_permissions():
    """Delegate Permission % Allocation"""
    return render_template('legacy/allocate_permissions.html')

@app.route('/legacy/delegate-tree')
def delegate_tree():
    """Multi-Delegate Tree View"""
    return render_template('legacy/delegate_tree.html')

@app.route('/legacy/upload-will')
def upload_will():
    """Upload Will (Video / Scan — premium)"""
    return render_template('legacy/upload_will.html')

@app.route('/legacy/confirm')
def confirm_legacy():
    """Confirm Legacy Plan & Lock"""
    return render_template('legacy/confirm.html')

# ============================================
# 7. LIVENESS & AUTOMATIC EXECUTION (3 screens)
# ============================================

@app.route('/liveness/inactive-warning')
def inactive_warning():
    """Inactivity Detected / Grace Countdown"""
    return render_template('liveness/inactive_warning.html')

@app.route('/liveness/im-alive')
def im_alive():
    """'I'm Alive' / Cancel Trigger Screen"""
    return render_template('liveness/im_alive.html')

@app.route('/liveness/execution-confirm')
def execution_confirm():
    """Legacy Execution Confirmation (assets distributed)"""
    return render_template('liveness/execution_confirm.html')

# ============================================
# 8. RECOVERY & ACCOUNT TOOLS (2 screens)
# ============================================

@app.route('/recovery')
def emergency_recovery():
    """Emergency Recovery / Backup Access"""
    return render_template('recovery/emergency_recovery.html')


# ============================================
# API ENDPOINTS FOR INTERACTIONS
# ============================================

@app.route('/api/connect', methods=['POST'])
def api_connect_wallet():
    """API endpoint to connect wallet"""
    data = request.json
    wallet_address = data.get('address')
    chain = data.get('chain')

    session['wallet'] = wallet_address
    session['chain'] = chain
    session['user_id'] = str(uuid.uuid4())

    return jsonify({'success': True, 'wallet': wallet_address})

@app.route('/api/search-domain', methods=['POST'])
def api_search_domain():
    """API endpoint to search domain"""
    data = request.json
    domain_name = data.get('name')

    # Mock availability check
    available = len(domain_name) > 3

    return jsonify({
        'available': available,
        'name': domain_name,
        'price': '10 NIL' if available else 'N/A'
    })

@app.route('/api/register-domain', methods=['POST'])
def api_register_domain():
    """API endpoint to register domain"""
    data = request.json
    domain_name = data.get('name')
    user_id = session.get('user_id')

    domain_id = str(uuid.uuid4())
    domains[domain_id] = {
        'name': domain_name,
        'owner': user_id,
        'created': datetime.now().isoformat(),
        'expiry': (datetime.now() + timedelta(days=365)).isoformat()
    }

    return jsonify({'success': True, 'domain_id': domain_id})

@app.route('/api/add-delegate', methods=['POST'])
def api_add_delegate():
    """API endpoint to add delegate"""
    data = request.json
    delegate_address = data.get('address')
    percentage = data.get('percentage')
    domain_id = data.get('domain_id')

    delegate_id = str(uuid.uuid4())
    delegates[delegate_id] = {
        'address': delegate_address,
        'percentage': percentage,
        'domain_id': domain_id,
        'created': datetime.now().isoformat()
    }

    return jsonify({'success': True, 'delegate_id': delegate_id})

@app.route('/api/confirm-alive', methods=['POST'])
def api_confirm_alive():
    """API endpoint to confirm user is alive"""
    user_id = session.get('user_id')

    return jsonify({
        'success': True,
        'message': 'Liveness confirmed',
        'next_check': (datetime.now() + timedelta(days=30)).isoformat()
    })

# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(e):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('error/500.html'), 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('templates/onboarding', exist_ok=True)
    os.makedirs('templates/dashboard', exist_ok=True)
    os.makedirs('templates/notifications', exist_ok=True)
    os.makedirs('templates/domains', exist_ok=True)
    os.makedirs('templates/management', exist_ok=True)
    os.makedirs('templates/legacy', exist_ok=True)
    os.makedirs('templates/liveness', exist_ok=True)
    os.makedirs('templates/recovery', exist_ok=True)
    os.makedirs('templates/error', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)

    app.run(debug=True, host='0.0.0.0', port=5001)
