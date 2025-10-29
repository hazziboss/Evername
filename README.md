# EverName - Decentralized Identity & Legacy Platform

## 🌟 Overview

**EverName** is a revolutionary decentralized identity and legacy management platform that combines blockchain technology with privacy-preserving computation through **Nillion Network**. This comprehensive mockup demonstrates a full-featured application for managing digital identities, domain names, multi-chain wallet addresses, and automated legacy planning across various interactive screens.

---

## 🎯 Core Concept

EverName solves three critical problems in the Web3 ecosystem:

### 1. **Multi-Chain Identity Fragmentation**
- Users manage multiple wallet addresses across different blockchains (Ethereum, Solana, Sui, Aptos, BNB Chain, etc.)
- Each blockchain requires a different address format
- **EverName Solution**: Single `.ever` domain that resolves to all your wallet addresses across all supported chains

### 2. **Digital Asset Inheritance**
- Cryptocurrency and digital assets are often lost forever when owners become inactive or pass away
- Traditional inheritance systems don't work well with decentralized assets
- **EverName Solution**: Privacy-preserving, trustless, automatic delegation system that executes legacy plans based on provable inactivity

### 3. **Privacy in Legacy Planning**
- Delegation plans and will documents are sensitive information
- Traditional systems expose this data to centralized parties
- **EverName Solution**: Nillion Network's blind computation technology keeps legacy plans encrypted even during execution

---

## 🔐 Nillion Network Integration

### What is Nillion Network?

**Nillion** is a decentralized blind computation network that enables computations on encrypted data without ever decrypting it. This is achieved through advanced cryptographic techniques including:

- **Secure Multi-Party Computation (MPC)**
- **Secret Sharing**
- **Threshold Cryptography**

### How EverName Uses Nillion

#### 1. **Encrypted Legacy Plans**
```
User's Legacy Plan (Plaintext)
     ↓
Encrypted with Nillion
     ↓
Stored as Secret Shares
     ↓
Distributed Across Nillion Nodes
     ↓
Computation Without Decryption
     ↓
Automatic Execution on Trigger
```

**What Gets Encrypted:**
- Delegate wallet addresses and allocation percentages
- Liveness monitoring data and inactivity thresholds
- Will documents (video/scanned files in premium tiers)
- Contact information for notifications
- Asset distribution instructions

#### 2. **Blind Liveness Verification**
The system monitors user activity without exposing the monitoring logic:
- **Input**: User login timestamps (encrypted)
- **Computation**: Inactivity threshold checking (on encrypted data)
- **Output**: Trigger status (without revealing monitoring parameters)

#### 3. **Privacy-Preserving Delegation Execution**
When the system detects prolonged inactivity:
```
Encrypted Activity Data → Nillion MPC → Threshold Reached?
                              ↓
                          Grace Period
                              ↓
                    Automatic Asset Transfer
                              ↓
                      Delegates Notified
```

**Key Privacy Features:**
- Delegates don't know they're delegates until execution
- Other delegates don't know about each other
- Percentage allocations remain private
- The trigger mechanism is verifiable but encrypted

#### 4. **Decentralized Trust**
Unlike traditional escrow services:
- **No single party** can access your encrypted data
- **No centralized server** stores complete delegation plans
- **No manual claims** required from beneficiaries
- **Automatic execution** based on cryptographic proofs

---

## 📱 Complete Feature Set (30+ Screens)

### 🚀 1. Onboarding & Authentication (3 Screens)

#### Screen 1.1: Welcome Page
**Purpose**: Introduction to EverName ecosystem

**Key Features:**
- Platform overview and value proposition
- Feature highlights (Privacy-First, Multi-Chain, Legacy Planning)
- Benefits showcase with visual cards
- Call-to-action buttons

**Capabilities Demonstrated:**
- Brand presentation
- User education
- Conversion optimization

#### Screen 1.2: Connect Wallet
**Purpose**: Multi-chain wallet connection

**Supported Wallets:**
- MetaMask (Ethereum & EVM chains)
- WalletConnect (Universal)
- Coinbase Wallet
- Phantom (Solana)

**Capabilities:**
- Multi-wallet provider support
- Chain detection
- Session management
- Error handling

**Technical Integration:**
```javascript
// Web3 wallet connection via MetaMask
await window.ethereum.request({ method: 'eth_requestAccounts' })
```

#### Screen 1.3: Nillion Authentication
**Purpose**: Privacy layer initialization

**Process:**
1. Wallet connection verification
2. Nillion node ID generation
3. Encryption key creation
4. Blind computation setup
5. Success confirmation

**Encrypted Data Initialized:**
- User identity encryption keys
- Delegation plan storage preparation
- Liveness monitoring setup
- Contact information encryption

**Visual Feedback:**
- Progress bar (25%, 50%, 75%, 100%)
- Status messages at each step
- Nillion node ID display
- Encryption status indicator

---

### 🏠 2. Dashboard & Home (6 Screens)

#### Screen 2.1: Main Dashboard
**Purpose**: Central command center for user activity

**Metrics Displayed:**
- Active Domains: Count of registered `.ever` domains
- Linked Wallets: Number of blockchain addresses connected
- Active Delegates: Legacy beneficiaries configured
- Identity Health: Overall account status percentage

**Quick Stats Cards:**
- Domain ownership overview
- Wallet connection status
- Legacy plan completeness
- Subscription tier information

**Domain Management Table:**
| Domain | Status | Expiry Date | Chains | Actions |
|--------|--------|-------------|---------|---------|
| hazzi.ever | Active | Mar 15, 2026 | ⟠ ◎ ~ | View |
| myname.ever | Active | Jun 20, 2026 | ⟠ ◆ | View |
| crypto.ever | Expiring Soon | Nov 5, 2025 | ⟠ | Renew |

**Recent Notifications:**
- Domain renewal reminders
- Liveness confirmations
- Delegate activity logs

**Legacy Status Overview:**
- Active delegates count
- Allocation percentage
- Will upload status

#### Screen 2.2: Quick Actions Panel
**Purpose**: Fast access to common operations

**Action Cards:**
1. **Search Domains** - Find and register new `.ever` domains
2. **Manage Domains** - Edit existing domain configurations
3. **Link Wallet** - Add blockchain addresses to domains
4. **Add Delegate** - Configure legacy beneficiaries
5. **Renew Subscription** - Extend domain registrations
6. **Confirm Liveness** - Update activity status

**Design Pattern:**
- Icon-based navigation
- One-click access
- Contextual descriptions

#### Screen 2.3: Identity Liveness Meter
**Purpose**: Activity monitoring and health visualization

**Health Score Calculation:**
```
Health Score = (
    Recent Activity Weight × 40% +
    Login Frequency Weight × 30% +
    Liveness Streak Weight × 20% +
    Security Status Weight × 10%
)
```

**Metrics Tracked:**
- **Last Activity**: Timestamp of most recent login
- **Login Frequency**: Daily, Weekly, Monthly classification
- **Liveness Streak**: Consecutive days of activity
- **Next Check**: Scheduled liveness verification date

**Security Status Indicators:**
- Nillion Encryption: Active/Inactive
- Wallet Connection: Connected/Disconnected
- 2FA Status: Enabled/Disabled/Recommended
- Backup Status: Complete/Incomplete

**Activity Timeline:**
- Visual bar chart showing last 30 days activity
- Height represents activity level per day
- Color coding for activity intensity

**Privacy Note:**
All activity data is encrypted using Nillion Network before storage.

#### Screen 2.4: Subscription Management
**Purpose**: Tier-based feature access and renewal

**Subscription Tiers:**

| Feature | Free | Standard | Premium |
|---------|------|----------|---------|
| Domains | 1 | 5 | Unlimited |
| Chain Support | EVM | 5 chains | 10+ chains |
| Delegates | 1 | 3 | Unlimited |
| Video Will | ❌ | ❌ | ✅ |
| NIL Discount | 0% | 10% | 15% |
| Annual Cost | Free | $49 | $0 (1000+ NIL) |

**NIL Token Benefits:**
- **Registration Discount**: Up to 15% off domain prices
- **Staking Rewards**: Hold 1000+ NIL for Premium tier
- **Governance Rights**: Vote on platform decisions
- **Renewal Credits**: Automatic renewal fee offset

**Current Benefits Display:**
- Unlimited domains
- Multi-chain support (10+ chains)
- Advanced legacy features
- Multi-delegate support
- Video will upload
- Priority notifications
- 15% NIL token discount

**Renewal Information:**
- Next renewal date
- Days remaining
- Auto-renewal status
- Payment method (NIL Tokens)

#### Screen 2.5: Cross-Chain Summary
**Purpose**: Multi-blockchain wallet management

**Supported Blockchains:**

1. **Ethereum (EVM)**
   - Chain ID: 1
   - Address format: 0x...
   - Primary domain resolution
   - Gas token: ETH

2. **Solana**
   - Chain ID: 101
   - Address format: Base58
   - SPL token support
   - Gas token: SOL

3. **Sui**
   - Chain ID: sui-mainnet
   - Object-based architecture
   - Move VM integration
   - Gas token: SUI

4. **Aptos**
   - Chain ID: aptos-mainnet
   - Account-based model
   - Move VM integration
   - Gas token: APT

5. **BNB Chain**
   - Chain ID: 56
   - EVM compatible
   - BSC ecosystem
   - Gas token: BNB

6. **Polygon**
   - Chain ID: 137
   - Layer 2 scaling
   - EVM compatible
   - Gas token: MATIC

**Wallet Resolution Table:**
| Domain | Chain | Address | Status |
|--------|-------|---------|--------|
| hazzi.ever | Ethereum | 0x742d...4a5C | ✅ Active |
| hazzi.ever | Solana | 9mW3...xYz7 | ✅ Active |
| hazzi.ever | Sui | 0xa1b2...cd3e | ✅ Active |

**Features:**
- Add/remove chain resolvers
- Update wallet addresses
- Set primary resolution
- View transaction history

#### Screen 2.6: Delegation Preview
**Purpose**: Quick overview of legacy planning status

**Delegate Summary:**
```
Total Delegates: 2
Total Allocation: 100%
Liveness Check: Every 30 days
Last Confirmation: 2 hours ago
```

**Delegate Cards:**
1. **Primary Delegate**
   - Address: 0x1234...5678
   - Allocation: 60%
   - Status: Active
   - Added: Jan 15, 2025

2. **Secondary Delegate**
   - Address: 0x9abc...def0
   - Allocation: 40%
   - Status: Active
   - Added: Jan 20, 2025

**Will Status:**
- Upload Status: ✅ Completed
- Format: Video
- Encryption: Nillion secured
- Last Updated: Feb 1, 2025

**Quick Actions:**
- Manage Legacy Plan
- Add New Delegate
- Update Allocations
- View Full Tree

---

### 🔔 3. Notifications (3 Screens)

#### Screen 3.1: Notification Settings
**Purpose**: Tier-based communication preferences

**Notification Channels:**

1. **Email Notifications**
   - Domain renewal reminders (7, 3, 1 days before)
   - Liveness check reminders
   - Delegate activity alerts
   - Security notifications

2. **SMS Notifications** (Standard & Premium)
   - Critical security alerts
   - Urgent renewal notices
   - Liveness failure warnings

3. **Push Notifications** (Premium)
   - Real-time delegate actions
   - Instant liveness reminders
   - Price alerts for premium domains

4. **Telegram/WhatsApp** (Premium)
   - Daily activity summaries
   - Delegate dashboard access
   - Two-way interaction

**Tier-Based Features:**
- **Free**: Email only, 24-hour delay
- **Standard**: Email + SMS, 1-hour delay
- **Premium**: All channels, real-time

**Privacy Settings:**
- Encrypted notifications via Nillion
- Opt-out options per category
- Frequency controls
- Quiet hours configuration

#### Screen 3.2: Contact Binding
**Purpose**: Multi-channel contact verification

**Binding Process:**

1. **Email Verification**
   ```
   Enter Email → Send Code → Verify → Encrypt → Bind
   ```

2. **Phone/SMS**
   ```
   Enter Number → SMS OTP → Verify → Encrypt → Bind
   ```

3. **Telegram**
   ```
   @EverNameBot → Link Account → Verify Code → Bind
   ```

4. **WhatsApp**
   ```
   QR Code Scan → Verify → Grant Permissions → Bind
   ```

**Security Features:**
- All contact info encrypted via Nillion
- Two-factor authentication support
- Backup contact configuration
- Emergency contact designation

**Status Indicators:**
- ✅ Verified and Active
- ⏳ Pending Verification
- ❌ Unverified
- 🔒 Encrypted Storage Confirmed

#### Screen 3.3: Delegate Notification History
**Purpose**: Read-only audit log for delegates

**What Delegates See:**
- Notification of their delegation status (only after trigger)
- Percentage allocation they're entitled to
- Assets they'll receive
- Execution timeline

**What Delegates DON'T See (Until Execution):**
- Other delegates' identities
- Full asset inventory
- Owner's activity status
- Trigger conditions

**Notification Log Example:**
```
Date: Mar 15, 2025, 2:30 PM
Event: Delegation Assignment
Status: Encrypted - Will be revealed on execution
Your Allocation: [ENCRYPTED]
Assets: [ENCRYPTED]
```

**Post-Execution Notifications:**
```
Date: Mar 20, 2025, 10:15 AM
Event: Legacy Execution Initiated
Status: Active
Your Allocation: 60% of domain portfolio
Assets Received:
  - hazzi.ever → Transferred
  - 0x742d...4a5C (Ethereum) → Transferred
  - 3.5 ETH → Transferred
```

---

### 🔍 4. Domain Search & Registration (5 Screens)

#### Screen 4.1: Domain Search
**Purpose**: Discover and search for `.ever` domains

**Search Features:**
- Real-time availability checking
- Instant suggestions
- Similar domain recommendations
- Price estimations

**Search Interface:**
```
┌────────────────────────────────────────┐
│  Search for available .ever domains    │
│  [                              ] 🔍   │
└────────────────────────────────────────┘
```

**Trending Searches:**
- cryptowhale.ever - $25
- nftcollector.ever - $15
- defi.ever - $100
- blockchain-dev.ever - $12
- web3builder.ever - $10

**Search Filters:**
- Length (3-63 characters)
- Price range
- Premium vs. standard
- Category (Personal, Business, DeFi, NFT)

**Domain Name Rules:**
- Lowercase letters (a-z)
- Numbers (0-9)
- Hyphens (not at start/end)
- Minimum 3 characters
- Maximum 63 characters

#### Screen 4.2: Domain Availability
**Purpose**: Display search results and pricing

**Availability Response:**
```javascript
{
  "domain": "hazzi.ever",
  "available": true,
  "price": "10 NIL",
  "premium": false,
  "alternatives": [
    "hazzi-eth.ever",
    "hazzi-official.ever",
    "hazzi-xyz.ever"
  ]
}
```

**Displayed Information:**
- ✅ Available / ❌ Taken
- Base price in NIL tokens
- Premium markup (if applicable)
- Similar available domains
- Registration button

**Premium Domain Indicators:**
- Short names (< 5 characters): 10x base price
- Dictionary words: 5x base price
- Popular terms: 3x base price
- Numbers only: 2x base price

**Quick Actions:**
- Register Now
- Add to Cart
- View Marketplace Listing
- Check Similar Domains

#### Screen 4.3: Premium Marketplace
**Purpose**: Buy/sell premium domains

**Marketplace Listings:**

| Domain | Owner | Price | Category | Actions |
|--------|-------|-------|----------|---------|
| crypto.ever | 0x123... | 1000 NIL | Finance | Buy |
| nft.ever | 0x456... | 2500 NIL | Art | Bid |
| defi.ever | 0x789... | 5000 NIL | Finance | Offer |
| web3.ever | 0xabc... | 10000 NIL | Tech | View |

**Listing Features:**
- Fixed price sales
- Auction bidding
- Make offer functionality
- Escrow service (Nillion-secured)

**Seller Tools:**
- List domain for sale
- Set auction parameters
- Accept/reject offers
- Transfer management

**Buyer Protection:**
- Escrow via smart contracts
- Nillion-encrypted transfers
- Dispute resolution
- Ownership verification

**Featured Collections:**
- 3-Letter Domains
- DeFi & Finance Terms
- NFT & Art Terms
- Geographic Names
- Brand Names

#### Screen 4.4: Checkout & Payment
**Purpose**: Complete domain registration

**Order Summary:**
```
Domain: hazzi.ever
Registration Period: 1 year
Base Price: 10 NIL

Discounts:
- Premium Tier: -15% (-1.5 NIL)
- First Purchase Bonus: -10% (-1.0 NIL)

Subtotal: 7.5 NIL
Gas Fee: ~0.5 NIL (estimated)
Total: 8.0 NIL
```

**Payment Methods:**
1. **NIL Tokens** (Primary)
   - Instant confirmation
   - Lowest fees
   - Tier discounts applied

2. **ETH** (Secondary)
   - Converted to NIL
   - Standard exchange rate
   - Network gas fees apply

3. **USDC** (Stablecoin)
   - Fixed fiat value
   - Higher conversion fees
   - 24-hour settlement

**Transaction Security:**
- Smart contract escrow
- Nillion-encrypted transfer
- Automatic domain transfer
- Receipt generation

**Terms & Conditions:**
- Annual renewal required
- Transfer fees apply
- Privacy policy acceptance
- Nillion encryption consent

#### Screen 4.5: Registration Success
**Purpose**: Confirmation and next steps

**Success Message:**
```
✅ Congratulations!
You now own hazzi.ever

Transaction Hash: 0x7d3f...92a1
Domain ID: #12345
Registration Date: Mar 15, 2025
Expiry Date: Mar 15, 2026
```

**Next Steps:**

1. **Link Your Wallets**
   - Add Ethereum address
   - Add Solana address
   - Add other chains
   - Set primary resolution

2. **Configure Social Links**
   - Add email
   - Link Twitter/X
   - Connect Telegram
   - Add WhatsApp

3. **Set Up Legacy Plan**
   - Add delegates
   - Allocate percentages
   - Upload will (premium)
   - Confirm plan

**Quick Actions:**
- View Domain Dashboard
- Add Wallet Addresses
- Set Up Delegates
- Share Your Domain

---

### ⚙️ 5. Domain Management (6 Screens)

#### Screen 5.1: My Domains List
**Purpose**: Portfolio overview

**Domain Portfolio Stats:**
```
Total Domains: 3
Active: 2
Expiring Soon: 1
Total Value: 45 NIL
Linked Chains: 8
Total Delegates: 5
```

**Domain Cards:**
```
┌─────────────────────────────────────┐
│ hazzi.ever                     ✅   │
│ Expires: Mar 15, 2026               │
│ Chains: ⟠ ◎ ~ ◆                     │
│ Delegates: 2                        │
│ [Manage] [Renew] [Transfer]        │
└─────────────────────────────────────┘
```

**Bulk Operations:**
- Renew multiple domains
- Update all resolvers
- Export portfolio data
- Generate QR codes

**Sorting & Filtering:**
- By expiry date
- By number of linked chains
- By delegate count
- By registration date
- By alphabetical order

#### Screen 5.2: Domain Details
**Purpose**: Comprehensive domain configuration

**Domain Information:**
```
Domain: hazzi.ever
Owner: 0x742d...4a5C
Token ID: #12345
Registered: Jan 15, 2025
Expires: Jan 15, 2026
Status: Active
NFT Status: Minted on Ethereum
```

**Resolver Records:**
- Ethereum: 0x742d...4a5C ✅
- Solana: 9mW3...xYz7 ✅
- Sui: 0xa1b2...cd3e ✅
- Email: user@example.com ✅
- Twitter: @username ✅
- Website: https://example.com ✅

**Domain Management Actions:**
1. Edit Resolver Records
2. Add/Remove Chain Support
3. Link Social Accounts
4. Configure Subdomain (Premium)
5. Transfer Ownership
6. Renew Registration
7. List on Marketplace

**Security Settings:**
- Transfer lock: Enabled
- Resolver lock: Disabled
- Expiry protection: Enabled
- Auto-renewal: Active

**Analytics (Premium):**
- Total resolutions: 1,234
- Most resolved chain: Ethereum (45%)
- Geographic distribution
- Time-based analytics

#### Screen 5.3: Linked Wallets & Resolvers
**Purpose**: Multi-chain address management

**Chain Resolver Configuration:**

```
┌─────────────────────────────────────┐
│ Ethereum (EVM)                      │
│ Address: 0x742d...4a5C              │
│ Primary: Yes ✅                     │
│ Last Updated: Mar 15, 2025          │
│ [Edit] [Remove] [Set Primary]      │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Solana                              │
│ Address: 9mW3...xYz7                │
│ Primary: No                         │
│ Last Updated: Mar 10, 2025          │
│ [Edit] [Remove] [Set Primary]      │
└─────────────────────────────────────┘
```

**Resolver Record Types:**

1. **Cryptocurrency Addresses**
   - ETH, BTC, SOL, SUI, APT, BNB, MATIC
   - Auto-validation for each format
   - Checksum verification

2. **Content Records**
   - IPFS hash
   - Arweave transaction ID
   - Swarm hash

3. **Text Records**
   - Email
   - URL
   - Avatar
   - Description
   - Keywords

**Bulk Import:**
- CSV upload for multiple addresses
- JSON format support
- Validation before import
- Rollback on error

**Safety Features:**
- Address format validation
- Duplicate detection
- Confirmation dialogs
- Change history log

#### Screen 5.4: Edit Resolver Records
**Purpose**: Modify domain resolution data

**Record Editor Interface:**
```
Record Type: [Cryptocurrency Address ▼]
Chain: [Ethereum ▼]

Current Address:
0x742d35a8f91f7a45C

New Address:
[                              ]

☑ Validate address format
☑ Check address on blockchain
☑ Confirm ownership (sign message)

[Cancel] [Save Changes]
```

**Validation Steps:**
1. **Format Validation**
   - Correct length
   - Valid characters
   - Checksum verification

2. **Blockchain Verification**
   - Address exists on chain
   - Not a contract (if required)
   - Not blacklisted

3. **Ownership Proof**
   - Sign message with new address
   - Verify signature
   - Confirm in transaction

**Record History:**
- Timestamp of all changes
- Previous values
- Who made the change
- Revert capability (24-hour window)

**Batch Editing:**
- Update multiple records at once
- Apply same address to multiple chains
- Scheduled updates
- Conditional updates

#### Screen 5.5: Add Chain Resolver
**Purpose**: Extend domain to new blockchains

**Supported Chains:**

**EVM Compatible:**
- ✅ Ethereum
- ✅ Polygon
- ✅ BNB Chain
- ✅ Arbitrum
- ✅ Optimism
- ✅ Avalanche C-Chain
- ✅ Fantom

**Non-EVM:**
- ✅ Solana
- ✅ Sui
- ✅ Aptos
- ✅ Cosmos
- ✅ Polkadot
- ✅ Cardano
- ✅ Near

**Add Chain Workflow:**
```
1. Select Blockchain
   [Solana ▼]

2. Enter Address
   [9mW3...xYz7              ]

3. Verify Ownership
   Sign message with this address:
   "I own this Solana address and want to link it to hazzi.ever"

   Signature:
   [                         ]

4. Set as Primary (Optional)
   ☐ Make this the primary resolver

5. Confirm & Submit
   [Add Chain Resolver]
```

**Address Verification Methods:**
1. **Sign Message** (Preferred)
   - Sign with private key
   - Verify signature on-chain
   - Instant verification

2. **Test Transaction** (Alternative)
   - Send 0.0001 tokens
   - Verify transaction
   - Refunded automatically

3. **Smart Contract Call** (Advanced)
   - Call verification contract
   - Prove ownership
   - Gas fees apply

**Chain-Specific Settings:**
- Custom derivation path
- Memo/tag support
- Multi-sig configuration
- Proxy/delegation setup

#### Screen 5.6: Social & Contact Linking
**Purpose**: Connect Web2 identities to Web3 domain

**Social Platform Integration:**

**Communication:**
- 📧 Email Address
- 📱 WhatsApp
- ✈️ Telegram
- 💬 Discord
- 📞 Phone/SMS

**Social Media:**
- 🐦 Twitter/X
- 📸 Instagram
- 💼 LinkedIn
- 🎮 Twitch
- 📺 YouTube

**Professional:**
- 🌐 Website/Blog
- 💻 GitHub
- 📝 Medium
- 🎨 Behance
- 🎭 OpenSea

**Linking Process:**
```
1. Select Platform
   [Twitter/X]

2. Enter Handle
   @username

3. Verification
   Method 1: Post verification code
   Method 2: OAuth authentication

4. Privacy Settings
   ☑ Show publicly on profile
   ☐ Share with delegates
   ☑ Encrypt with Nillion

5. Confirm
   [Link Account]
```

**Profile Display:**
```
┌─────────────────────────────────────┐
│ hazzi.ever                          │
│                                     │
│ 🌐 https://hazzi.com                │
│ 🐦 @hazzi                           │
│ 📧 contact@hazzi.com                │
│ 💬 @hazzicrypto                     │
│ 💻 github.com/hazzi                 │
│                                     │
│ [QR Code]  [Share]  [Edit]         │
└─────────────────────────────────────┘
```

**Privacy Controls:**
- Public vs. private display
- Selective sharing with delegates
- Encryption options
- Visibility toggles per platform

**Verification Badges:**
- ✅ Verified Email
- ✅ Verified Twitter
- ⏳ Pending Instagram
- ❌ Unverified GitHub

---

### 👥 6. Legacy & Delegation Setup (6 Screens)

#### Screen 6.1: Legacy Overview
**Purpose**: Introduction to delegation system

**How It Works:**

```
1. Configure Delegates
   ↓
2. Set Percentage Allocations
   ↓
3. System Monitors Your Activity
   ↓
4. Prolonged Inactivity Detected
   ↓
5. Grace Period Begins
   ↓
6. Automatic Asset Distribution
```

**Current Legacy Status:**
```
✅ Delegation Plan: Active
✅ Total Delegates: 2
✅ Total Allocation: 100%
✅ Will Document: Uploaded (Video)
✅ Liveness Check: Every 30 days
⏰ Next Check: Apr 15, 2025
✅ Last Activity: 2 hours ago
```

**Asset Inventory:**
- 3 `.ever` domains
- 5 linked wallet addresses
- Estimated portfolio value
- Legacy-eligible assets

**Delegate Summary:**
| Delegate | Allocation | Status | Added |
|----------|-----------|--------|-------|
| 0x1234...5678 | 60% | Active | Jan 15 |
| 0x9abc...def0 | 40% | Active | Jan 20 |

**Privacy Guarantee:**
```
🔒 All delegation data encrypted via Nillion
🔒 Delegates notified only on execution
🔒 Zero-knowledge proof of allocation
🔒 Trustless automatic execution
```

#### Screen 6.2: Add Delegate
**Purpose**: Configure legacy beneficiaries

**Add Delegate Form:**
```
Delegate Information:
─────────────────────────────────────

Wallet Address:
[0x                                    ]
☑ Validate address format

Delegate Name (Optional):
[John Doe                              ]

Relationship (Optional):
[Family Member ▼]

Allocation Percentage:
[60] %
Remaining: 40%

Notification Preferences:
☑ Email notification on execution
☐ SMS notification (Premium)
☑ Include personal message

Personal Message (Encrypted):
┌────────────────────────────────────┐
│ If you're reading this...          │
│                                    │
└────────────────────────────────────┘

[Cancel] [Add Delegate]
```

**Validation Rules:**
- Valid wallet address format
- Not your own address
- Not already a delegate
- Total allocation ≤ 100%
- Minimum 1% per delegate

**Security Confirmations:**
```
⚠️ Important Security Notices:

1. This delegate will receive 60% of:
   - All .ever domains
   - All linked wallet contents
   - Associated NFTs and tokens

2. Delegation is encrypted via Nillion
   - Delegate won't know until execution
   - Cannot be claimed manually
   - Automatic on inactivity trigger

3. You can modify/remove at any time
   - Changes take effect immediately
   - Nillion re-encrypts data
   - Delegates not notified of changes

Do you want to proceed?
[Yes, Add Delegate] [Cancel]
```

**Delegate Types:**
1. **Individual Wallet**
   - Single address
   - Direct transfer
   - Simple allocation

2. **Multi-Sig Wallet**
   - Requires multiple signatures
   - Enhanced security
   - Shared control

3. **Smart Contract**
   - Programmable distribution
   - Conditional logic
   - Advanced use cases

#### Screen 6.3: Allocate Permissions
**Purpose**: Distribute assets among delegates

**Allocation Interface:**
```
Total Allocation: 100%
Remaining: 0%

┌────────────────────────────────────┐
│ Delegate 1: 0x1234...5678          │
│ John Doe (Family)                  │
│                                    │
│ [━━━━━━━━━━━━━━━━━━━━━━━━━━━] 60% │
│                                    │
│ Assets Included:                   │
│ ☑ All domains                      │
│ ☑ All wallets                      │
│ ☑ NFTs & tokens                    │
│ ☐ Social accounts (Premium)        │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│ Delegate 2: 0x9abc...def0          │
│ Jane Smith (Friend)                │
│                                    │
│ [━━━━━━━━━━━━━━] 40%               │
│                                    │
│ Assets Included:                   │
│ ☑ Selected domains only            │
│   - crypto.ever                    │
│ ☑ Ethereum wallet only             │
│ ☐ Other assets                     │
└────────────────────────────────────┘

[Reset] [Save Allocations]
```

**Allocation Methods:**

1. **Equal Split**
   - Divide evenly among all delegates
   - Automatic recalculation
   - One-click setup

2. **Percentage-Based**
   - Manual slider control
   - Real-time validation
   - Visual feedback

3. **Asset-Specific**
   - Allocate specific domains
   - Allocate specific wallets
   - Granular control (Premium)

**Visual Allocation:**
```
Total Assets: $10,000 USD

Delegate 1 (60%): $6,000
├─ hazzi.ever
├─ myname.ever
└─ 2 ETH wallets

Delegate 2 (40%): $4,000
├─ crypto.ever
└─ 1 SOL wallet
```

**Allocation Rules:**
- Total must equal 100%
- Minimum 1% per delegate
- Maximum 10 delegates (Free: 1, Standard: 3, Premium: Unlimited)
- Can leave some assets unallocated (revert to owner)

#### Screen 6.4: Multi-Delegate Tree View
**Purpose**: Visualize complex delegation structures

**Tree Visualization:**
```
                    You (Owner)
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   Delegate 1      Delegate 2      Delegate 3
    (60%)           (30%)           (10%)
        │               │
    ┌───┴───┐       ┌───┴───┐
    │       │       │       │
Sub-Del  Sub-Del  Sub-Del  Sub-Del
  (30%)   (30%)   (15%)   (15%)
```

**Hierarchical Delegation (Premium):**
- Primary delegates can set their own delegates
- Cascading allocation
- Conditional triggers
- Time-based unlocking

**Delegation Conditions (Advanced):**
```
Delegate 1 receives 60% IF:
✓ Owner inactive for 90 days
✓ Grace period (30 days) expires
✓ No "I'm Alive" confirmation

Delegate 2 receives 30% IF:
✓ Owner inactive for 90 days
✓ Delegate 1 also inactive for 60 days
✓ Secondary trigger activated

Delegate 3 receives 10% IF:
✓ Date reaches Jan 1, 2030
✓ OR all primary delegates decline
```

**Interactive Features:**
- Drag-and-drop to reorganize
- Click delegate to edit
- Add/remove connections
- Export tree as image

**Execution Simulator:**
```
Simulate Scenario:
─────────────────────────────────────
Inactive Period: [90] days
Current Date: Mar 15, 2025
Trigger Date: Jun 15, 2025

Run Simulation →

Results:
✓ Grace period: Jun 15 - Jul 15
✓ Delegate 1 notified: Jul 15
✓ Assets transferred: Jul 16
✓ Transaction fees: 0.02 ETH
```

#### Screen 6.5: Upload Will (Premium)
**Purpose**: Attach legal documents to delegation

**Upload Options:**

**1. Video Will**
```
┌────────────────────────────────────┐
│                                    │
│         📹 Record Video            │
│                                    │
│     Max Duration: 10 minutes       │
│     Format: MP4, WebM              │
│     Max Size: 500 MB               │
│                                    │
│  [Start Recording] [Upload File]  │
│                                    │
└────────────────────────────────────┘
```

**2. Document Scan**
```
Supported Formats:
- PDF (max 50 pages)
- Images: JPG, PNG
- Office: DOCX, DOC

Security Features:
✓ Encrypted with Nillion
✓ Tamper-proof hash
✓ Timestamped on blockchain
✓ Multi-signature verification
```

**3. Text-Based Will**
```
┌────────────────────────────────────┐
│ Last Will and Testament            │
│                                    │
│ I, [Your Name], being of sound    │
│ mind, declare this to be my       │
│ digital asset distribution plan:  │
│                                    │
│ 1. hazzi.ever → Delegate 1        │
│ 2. All ETH → Delegate 1           │
│ 3. crypto.ever → Delegate 2       │
│                                    │
│ Signed: [Digital Signature]       │
│ Date: March 15, 2025              │
└────────────────────────────────────┘
```

**Encryption Process:**
```
Upload File
   ↓
Nillion Encryption
   ↓
Secret Sharing (5-of-9)
   ↓
Distributed Storage
   ↓
Blockchain Hash Anchor
   ↓
Completion Confirmation
```

**Access Controls:**
- Only viewable after execution
- Delegates receive access
- Owner can update anytime
- Version history maintained

**Legal Compliance:**
- Jurisdiction selection
- Witness signature support
- Notarization integration
- Legal template library

#### Screen 6.6: Confirm Legacy Plan
**Purpose**: Final review and activation

**Legacy Plan Checklist:**
```
☑ Delegation Plan
  ✓ 2 delegates configured
  ✓ 100% allocated
  ✓ Addresses validated

☑ Asset Inventory
  ✓ 3 domains mapped
  ✓ 5 wallets linked
  ✓ Estimated value: $10,000

☑ Will Document
  ✓ Video uploaded
  ✓ Encrypted via Nillion
  ✓ Blockchain hash: 0x7d3f...

☑ Liveness Configuration
  ✓ Check interval: 30 days
  ✓ Grace period: 30 days
  ✓ Notification setup: ✓

☑ Contact Verification
  ✓ Email verified
  ✓ SMS verified (Premium)
  ✓ Telegram linked

☐ Legal Review (Optional)
  ○ Jurisdiction: [Select]
  ○ Witness signatures: 0/2
```

**Activation Summary:**
```
⚠️ Important: Once activated, your legacy plan:

✓ Monitors your activity every 30 days
✓ Encrypts all data via Nillion Network
✓ Automatically executes on prolonged inactivity
✓ Cannot be manually claimed by delegates
✓ Reversible only by you (via "I'm Alive")

Estimated Costs:
- Nillion encryption: One-time 5 NIL
- Liveness monitoring: 1 NIL/year
- Execution gas: ~0.05 ETH (paid from estate)

Total Initial Cost: 5 NIL + 1 NIL/year
```

**Final Confirmation:**
```
I understand and agree to:
☑ All delegates and allocations are correct
☑ Nillion will encrypt my legacy data
☑ The system will monitor my activity
☑ Execution is automatic and trustless
☑ I can modify or cancel at any time

Digital Signature:
[Sign with Wallet]

[Cancel] [Activate Legacy Plan]
```

**Post-Activation:**
```
✅ Legacy Plan Activated!

Plan ID: #LP-12345
Activation Date: Mar 15, 2025
Nillion Encryption: ✓ Complete
Monitoring Status: ✓ Active

Next Steps:
1. Confirm liveness regularly
2. Update plan as needed
3. Inform delegates (optional)
4. Keep emergency contacts updated

[View Dashboard] [Download Certificate]
```

---

### 💓 7. Liveness & Automatic Execution (3 Screens)

#### Screen 7.1: Inactivity Warning
**Purpose**: Alert user of potential legacy trigger

**Warning Display:**
```
⚠️ INACTIVITY DETECTED

Last Activity: Dec 15, 2024
Days Inactive: 85 days
Threshold: 90 days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Grace Period Countdown:
┌────────────────────────────────┐
│                                │
│        5 DAYS REMAINING        │
│                                │
│     Until Legacy Execution     │
│                                │
└────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If you don't confirm liveness by:
📅 Mar 20, 2025 at 11:59 PM

Your legacy plan will execute:
• Delegates will be notified
• Assets will be distributed
• Process is irreversible

[I'M ALIVE - CANCEL TRIGGER]
```

**Notification History:**
```
Reminders Sent:
✓ Day 70: Email reminder sent
✓ Day 80: SMS alert sent (Premium)
✓ Day 85: Urgent email & SMS
✓ Day 87: Final warning

Attempts to Reach You:
✓ 5 emails sent
✓ 3 SMS messages (Premium)
✓ 2 push notifications
✓ 1 Telegram message
```

**Grace Period Details:**
```
Grace Period: 30 days (Mar 15 - Apr 15)

During this time:
• Delegates are NOT yet notified
• You can still cancel
• Assets remain under your control
• Daily reminders continue

After Grace Period:
• Automatic execution begins
• Delegates receive notification
• Asset transfer initiated
• Process cannot be stopped
```

**Emergency Actions:**
```
Quick Actions:
┌────────────────────────────────┐
│ [I'm Alive - Stop Process]     │
│ Large, prominent button        │
└────────────────────────────────┘

Alternative Methods:
• Call emergency hotline
• Contact delegate directly
• Use recovery wallet
• Email support with code
```

#### Screen 7.2: "I'm Alive" Confirmation
**Purpose**: Cancel legacy execution

**Confirmation Interface:**
```
✋ CONFIRM YOU'RE ALIVE

To cancel the legacy execution:

1. Verify Your Identity
   ──────────────────────────────
   Connect Wallet:
   [MetaMask] [WalletConnect] [Other]

2. Sign Liveness Message
   ──────────────────────────────
   Message to Sign:
   "I am alive and wish to cancel
    legacy execution for hazzi.ever
    Timestamp: 2025-03-15T10:30:00Z"

   [Sign Message]

3. Complete Verification
   ──────────────────────────────
   ☐ I am the rightful owner
   ☐ I want to cancel legacy execution
   ☐ I will remain active

4. Optional: Update Settings
   ──────────────────────────────
   New Check Interval:
   [30 days ▼] [60 days] [90 days]

   Grace Period:
   [30 days ▼] [15 days] [45 days]

[Confirm I'm Alive]
```

**Verification Steps:**
```
Step 1: Wallet Connection
   ✓ Connected: 0x742d...4a5C
   ✓ Matches domain owner

Step 2: Signature Verification
   ✓ Message signed
   ✓ Signature valid
   ✓ Timestamp within window

Step 3: Blockchain Confirmation
   ✓ Transaction submitted
   ✓ Confirmation: 1/3
   ⏳ Waiting for finality...

Step 4: Nillion Update
   ✓ Liveness data encrypted
   ✓ Monitoring reset
   ✓ Next check: Apr 15, 2025
```

**Success Confirmation:**
```
✅ LIVENESS CONFIRMED

Status: Active
Last Confirmed: Mar 15, 2025, 10:35 AM
Next Check: Apr 15, 2025

Your legacy execution has been cancelled.

Updated Settings:
• Monitoring interval: 30 days
• Grace period: 30 days
• Notifications: Email + SMS

Reminders:
• You'll receive a reminder 7 days before next check
• You can confirm liveness anytime
• Multiple confirmations reset the timer

[Return to Dashboard]
```

**Alternative Verification Methods:**
```
Can't Access Wallet?

Emergency Recovery Options:
1. Recovery Phrase Verification
2. Backup Email Code
3. SMS OTP (if linked)
4. Delegate Attestation (Premium)
5. Video Verification (Premium)

[Use Alternative Method]
```

#### Screen 7.3: Legacy Execution Confirmation
**Purpose**: Post-execution status and audit trail

**Execution Summary:**
```
🔔 LEGACY PLAN EXECUTED

Execution Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Trigger Date: Mar 20, 2025
Execution Date: Apr 20, 2025
Grace Period: 30 days (completed)
Final Confirmations Sent: 15

Owner Inactivity:
Last Activity: Dec 15, 2024
Days Inactive: 125 days
Threshold Met: ✓ Yes

Delegates Notified:
✓ Delegate 1: Apr 20, 2025, 9:00 AM
✓ Delegate 2: Apr 20, 2025, 9:00 AM
```

**Asset Distribution:**
```
┌─────────────────────────────────────┐
│ Delegate 1 (60% - 0x1234...5678)    │
│                                     │
│ Domains Transferred:                │
│ ✓ hazzi.ever                        │
│ ✓ myname.ever                       │
│                                     │
│ Wallets Transferred:                │
│ ✓ Ethereum: 2.1 ETH                 │
│ ✓ Solana: 45 SOL                    │
│                                     │
│ Total Value: ~$6,000 USD            │
│ Transaction Hash: 0x9d7e...          │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Delegate 2 (40% - 0x9abc...def0)    │
│                                     │
│ Domains Transferred:                │
│ ✓ crypto.ever                       │
│                                     │
│ Wallets Transferred:                │
│ ✓ Sui: 100 SUI                      │
│                                     │
│ Total Value: ~$4,000 USD            │
│ Transaction Hash: 0x3f2a...          │
└─────────────────────────────────────┘
```

**Execution Timeline:**
```
Timeline of Events:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dec 15, 2024  Last owner activity
  ↓ 70 days
Feb 23, 2025  First reminder sent
  ↓ 10 days
Mar 5, 2025   Urgent alert sent
  ↓ 10 days
Mar 15, 2025  Grace period begins
  ↓ 5 days
Mar 20, 2025  Daily reminders start
  ↓ 30 days
Apr 20, 2025  Execution triggered
  ↓
Apr 20, 2025  Nillion decryption
  ↓
Apr 20, 2025  Delegates notified
  ↓
Apr 20, 2025  Assets transferred
  ↓
Apr 20, 2025  ✓ Complete
```

**Will Document Access:**
```
📄 Will Document Released

The encrypted will has been decrypted
and made available to delegates.

Document Type: Video Will
Uploaded: Jan 15, 2025
Nillion Hash: 0x7d3f...
Access Link: [Secure Portal]

Delegates can now view:
✓ Personal messages
✓ Distribution instructions
✓ Special requests
✓ Contact information
```

**Audit Trail:**
```
Blockchain Proofs:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Liveness Monitoring:
- Smart Contract: 0xABC...
- Proof of Inactivity: 0x123...
- Grace Period Hash: 0x456...

Asset Transfers:
- Domain NFT Transfer: 0x789...
- Wallet Delegation: 0xDEF...
- Execution Receipt: 0x012...

All records are permanently stored
on-chain and verifiable by anyone.

[View on Explorer] [Download Report]
```

**Delegate Notifications Sent:**
```
Notification Log:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Delegate 1 (John Doe):
✓ Email: Sent Apr 20, 9:00 AM
✓ SMS: Sent Apr 20, 9:01 AM
✓ Access Portal: Created
✓ Asset Guide: Delivered

Delegate 2 (Jane Smith):
✓ Email: Sent Apr 20, 9:00 AM
✓ Access Portal: Created
✓ Asset Guide: Delivered
```

**Post-Execution Support:**
```
For Delegates:
• Access your inheritance portal
• View step-by-step asset guides
• Contact support if needed
• Join delegate community

[Access Delegate Portal]
```

---

### 🔧 8. Recovery & Account Tools (1 Screen)

#### Screen 8.1: Emergency Recovery
**Purpose**: Account access restoration

**Recovery Methods:**

**1. Seed Phrase Recovery**
```
┌────────────────────────────────────┐
│ Enter 12/24-word Recovery Phrase   │
│                                    │
│ Word 1:  [         ]               │
│ Word 2:  [         ]               │
│ Word 3:  [         ]               │
│ ...                                │
│ Word 12: [         ]               │
│                                    │
│ [Validate & Recover]               │
└────────────────────────────────────┘
```

**2. Social Recovery (Premium)**
```
Request Recovery from Trusted Contacts:

Guardian 1: friend@email.com
Status: ⏳ Pending approval

Guardian 2: family@email.com
Status: ✓ Approved (1/3)

Guardian 3: colleague@email.com
Status: ✓ Approved (2/3)

Threshold: 2 of 3 guardians needed
Current: 2/3 ✓

[Complete Recovery]
```

**3. Backup Email Code**
```
A recovery code has been sent to:
recovery@example.com

Enter 6-digit code:
┌───┬───┬───┬───┬───┬───┐
│   │   │   │   │   │   │
└───┴───┴───┴───┴───┴───┘

Code expires in: 15:00

[Verify Code]
[Resend Code]
```

**4. Hardware Key Recovery**
```
Insert YubiKey or Security Key

Detected: YubiKey 5 NFC
Serial: 12345678

[Verify with Hardware Key]
```

**5. Delegate Attestation (Advanced)**
```
If you cannot access any recovery method,
your configured delegates can attest to
your identity.

Minimum 1 delegate must verify:
- Your identity (video call)
- Ownership proof (documents)
- Legal authorization

This is a last-resort option and may
take 3-7 business days.

[Request Delegate Attestation]
```

**Account Security Settings:**
```
Two-Factor Authentication:
☑ Email OTP
☑ SMS OTP (Premium)
☑ Authenticator App
☐ Hardware Key

Recovery Options Configured:
✓ Seed phrase (backed up)
✓ 3 Social guardians
✓ Backup email
✓ Hardware key registered

Last Security Audit: Mar 15, 2025
Risk Level: 🟢 Low

[Update Security Settings]
```

---

## 🔐 Nillion Network Integration - Technical Deep Dive

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    EverName Application Layer                │
│  (Flask Frontend + Web3 Wallet Integration + UI/UX)          │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                   Smart Contract Layer                       │
│  (Domain Registry + NFT + Delegation Logic on Ethereum)      │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                    Nillion Network Layer                     │
│  (Blind Computation + Secret Sharing + MPC Protocol)         │
│                                                              │
│  Components:                                                 │
│  • Nilchain (Nillion Blockchain)                            │
│  • Secret Shares (Distributed across nodes)                  │
│  • Computation Nodes (MPC participants)                      │
│  • Storage Nodes (Encrypted data persistence)                │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow for Legacy Plan Creation

```
1. User Creates Delegation Plan
   ├─ Delegate addresses
   ├─ Percentage allocations
   ├─ Liveness thresholds
   └─ Will documents

2. Data Preparation
   plaintext_data = {
     "delegates": [
       {"address": "0x123...", "percentage": 60},
       {"address": "0xabc...", "percentage": 40}
     ],
     "threshold_days": 90,
     "grace_period": 30,
     "will_ipfs": "Qm..."
   }

3. Nillion Encryption
   ├─ Generate random polynomial
   ├─ Create secret shares (e.g., 5-of-9 threshold)
   ├─ Distribute shares across Nillion nodes
   └─ Store commitment on Nilchain

4. Smart Contract Recording
   ├─ Store Nillion computation ID
   ├─ Record commitment hash
   ├─ Link to domain NFT
   └─ Initialize liveness monitor

5. Monitoring Active
   ├─ Off-chain oracle checks activity
   ├─ Encrypted comparison via Nillion MPC
   ├─ Trigger recorded if threshold met
   └─ Grace period countdown begins
```

### Liveness Monitoring with Blind Computation

**Problem**: How to check if someone is inactive without revealing:
- When they last logged in
- How the threshold is calculated
- Who is monitoring them

**Nillion Solution**:

```python
# Pseudocode for blind liveness check

# Step 1: User activity encrypted and stored
last_activity_timestamp = encrypt_with_nillion(
    current_timestamp
)

# Step 2: Threshold comparison (encrypted)
result = nillion_mpc_compare(
    encrypted_current_time - encrypted_last_activity,
    encrypted_threshold_days
)
# Result is encrypted boolean: true if inactive, false if active

# Step 3: Grace period computation (encrypted)
if nillion_decrypt_result(result, owner_only=False):
    grace_expiry = nillion_mpc_add(
        encrypted_trigger_time,
        encrypted_grace_period
    )

# Step 4: Execution trigger (automatic)
if nillion_mpc_compare(
    encrypted_current_time,
    encrypted_grace_expiry
) == true:
    nillion_decrypt_secrets()  # Reveals delegate info
    execute_legacy_plan()
```

**Key Privacy Properties**:
- Nobody knows the exact last activity time
- Threshold is never revealed
- Comparison happens on encrypted data
- Only the boolean result ("trigger" or "not trigger") is revealed
- Delegates' identities stay secret until execution

### Secret Sharing Example

**Input Data**:
```
Delegate 1: 0x742d35a8f91f7a45C (60%)
Delegate 2: 0x9abc123def456789 (40%)
```

**Shamir's Secret Sharing**:
```
Secret: S (the delegation plan)
Polynomial: P(x) = S + a₁x + a₂x² + ... + aₜ₋₁xᵗ⁻¹

Shares created:
Share 1: P(1) → Node 1
Share 2: P(2) → Node 2
Share 3: P(3) → Node 3
Share 4: P(4) → Node 4
Share 5: P(5) → Node 5
Share 6: P(6) → Node 6
Share 7: P(7) → Node 7
Share 8: P(8) → Node 8
Share 9: P(9) → Node 9

Threshold: Any 5 shares can reconstruct S
          Any 4 or fewer shares reveal NOTHING
```

**Reconstruction on Trigger**:
```
When legacy execution is triggered:
1. Smart contract broadcasts execution signal
2. Nillion nodes verify trigger authenticity
3. 5+ nodes combine their shares
4. Original secret is reconstructed:
   S = Delegate 1: 0x742d... (60%)
       Delegate 2: 0x9abc... (40%)
5. Delegates are notified
6. Assets are transferred
```

### Privacy Guarantees

**What Nillion Network Ensures**:

1. **Confidentiality**
   - Delegates don't know they're delegates (until execution)
   - Other delegates are unknown to each other
   - Percentage allocations are secret
   - Liveness thresholds are encrypted

2. **Integrity**
   - Computations are verifiable
   - No single party can manipulate results
   - Blockchain anchors prevent tampering
   - Audit trail is immutable

3. **Availability**
   - Distributed storage across nodes
   - No single point of failure
   - Automatic failover
   - Censorship resistant

4. **Programmability**
   - Complex logic in encrypted domain
   - Conditional triggers
   - Multi-party computation
   - Zero-knowledge proofs

### Comparison with Traditional Systems

| Aspect | Traditional Escrow | Nillion + EverName |
|--------|-------------------|-------------------|
| **Privacy** | Escrow company knows everything | Nobody knows full picture |
| **Trust** | Must trust central party | Trustless cryptography |
| **Manual Claims** | Beneficiaries must file claims | Automatic execution |
| **Single Point of Failure** | Yes (escrow company) | No (distributed) |
| **Verification** | Hidden process | Publicly verifiable |
| **Cost** | High fees (lawyers, executors) | Low gas fees |
| **Censorship** | Can be blocked | Censorship resistant |

---

## 🎨 Design & User Experience

### Design System

**Color Palette**:
```css
--primary-color: #6366f1 (Purple)
--secondary-color: #10b981 (Green)
--danger-color: #ef4444 (Red)
--bg-dark: #0f172a (Dark Blue)
--text-primary: #f1f5f9 (Light Gray)
```

**Typography**:
- Font Family: Inter, -apple-system, BlinkMacSystemFont
- Headings: 600-800 weight
- Body: 400-500 weight
- Monospace: For addresses and hashes

**Component Library**:
- Cards with subtle shadows
- Gradient buttons
- Progress bars and meters
- Badge indicators
- Interactive tables
- Modal dialogs
- Dropdown menus
- Form elements

### Responsive Design

**Breakpoints**:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

**Mobile Optimizations**:
- Touch-friendly buttons (min 44px)
- Simplified navigation
- Collapsible sections
- Swipe gestures
- Bottom sheet modals

### Accessibility

**WCAG 2.1 AA Compliance**:
- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatibility
- Color contrast ratios > 4.5:1
- Focus indicators
- Alt text for images

---

## 🔗 Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with custom properties
- **JavaScript (ES6+)** - Interactive functionality
- **Web3.js** - Blockchain interaction

### Backend
- **Flask 3.0.2** - Python web framework
- **Jinja2** - Template engine
- **Session Management** - User state
- **RESTful APIs** - Data exchange

### Blockchain
- **Ethereum** - Primary chain for domain NFTs
- **EVM Compatible** - Polygon, BNB, Arbitrum, Optimism
- **Solana** - Alternative chain support
- **Sui/Aptos** - Next-gen blockchain support

### Privacy Layer
- **Nillion Network** - Blind computation
- **MPC (Multi-Party Computation)** - Secure calculations
- **Secret Sharing** - Distributed storage
- **Zero-Knowledge Proofs** - Privacy verification

### Storage
- **On-Chain** - Domain ownership, delegation commitments
- **Nillion** - Encrypted legacy plans, will documents
- **IPFS** - Decentralized file storage (optional)

---

## 💡 Use Cases & User Stories

### Use Case 1: Crypto Investor Estate Planning

**User**: Alex, 35-year-old crypto investor

**Problem**:
- Owns 10 ETH, 100 SOL, various NFTs
- Worried about family accessing funds if something happens
- Doesn't trust centralized solutions
- Wants privacy (doesn't want family to know holdings yet)

**Solution with EverName**:
1. Register `alex.ever` domain
2. Link all wallet addresses to the domain
3. Add spouse as 100% delegate
4. Set 90-day inactivity threshold
5. Upload video explaining wallet access
6. Nillion encrypts everything

**Outcome**:
- If inactive for 90 days → automatic transfer to spouse
- Spouse doesn't know they're a delegate until needed
- No lawyers, no probate, no manual claims
- Fully private and automated

### Use Case 2: DAO Founder Succession Planning

**User**: Sarah, founder of a DeFi DAO

**Problem**:
- Controls DAO multisig as primary signer
- Needs succession plan for project continuity
- Multiple team members should inherit different roles
- Community doesn't know about succession (could cause panic)

**Solution with EverName**:
1. Register `sarahdao.ever`
2. Configure 3 delegates:
   - CTO: 40% (technical control)
   - COO: 30% (operational control)
   - Community Lead: 30% (governance control)
3. Set 180-day threshold (longer for DAO founder)
4. Link multisig address, admin keys, social accounts
5. Upload operational playbook (encrypted)

**Outcome**:
- Gradual, automatic transition of control
- No single point of failure
- Community doesn't panic (smooth transition)
- Each delegate gets appropriate access

### Use Case 3: Digital Nomad Multi-Chain Identity

**User**: Miguel, travels full-time, uses multiple chains

**Problem**:
- Different wallets for different chains (ETH, SOL, Sui)
- Hard to share one identity across platforms
- Wants single name for payments/communication
- Needs emergency access if phone is lost

**Solution with EverName**:
1. Register `miguel.ever`
2. Link 6 different chain addresses
3. Add email, Telegram, Twitter
4. Set emergency recovery guardians (3 trusted friends)
5. Enable social recovery

**Outcome**:
- Single identity: `miguel.ever`
- Receives payments on any chain
- Social links accessible to anyone
- Can recover account via friends if needed

---

## 📈 Future Roadmap (Concepts)

### Phase 1: Foundation (Current Mockup)
✅ 30+ screens covering core features
✅ Nillion integration concept
✅ Multi-chain support framework
✅ Legacy delegation system

### Phase 2: Production Implementation
- Smart contract development (Solidity)
- Nillion SDK integration (Python/JS)
- Database backend (PostgreSQL)
- Production-grade security

### Phase 3: Advanced Features
- Subdomain support (premium.user.ever)
- Programmable delegation rules
- Cross-chain atomic swaps
- DAO integration toolkit

### Phase 4: Ecosystem Expansion
- Mobile app (iOS/Android)
- Browser extension
- API for third-party integration
- Marketplace for premium domains

---

## 🔒 Security Considerations

### Current Mockup Security
- Mock data (in-memory, non-persistent)
- Session-based authentication
- No real blockchain integration
- Demonstration-only encryption

### Production Requirements
**Essential**:
- Hardware wallet support
- Multi-signature capabilities
- Rate limiting and DDoS protection
- Secure key management (HSM)
- Regular security audits

**Nillion-Specific**:
- Proper MPC implementation
- Secret sharing threshold configuration
- Node reputation system
- Encrypted channel establishment
- Stake-based security

---

## 📊 Metrics & Analytics (Conceptual)

### User Metrics
- Domain registrations per day
- Active users (DAU/MAU)
- Delegation plan completion rate
- Liveness confirmation frequency

### Platform Metrics
- Total domains registered
- Total value locked (delegated assets)
- Number of delegates configured
- Legacy executions triggered

### Nillion Metrics
- Encryption operations per day
- MPC computations completed
- Storage node utilization
- Decryption events (executions)

---

## 🌐 Cross-Chain Resolver Specifications

### Supported Address Formats

**Ethereum (EVM)**:
```
Format: 0x + 40 hex characters
Example: 0x742d35a8f91f7a45C8E9e5f6B9c2D3e4F5a6B7c8
Checksum: EIP-55 mixed case
Validation: Keccak-256 hash
```

**Solana**:
```
Format: Base58, 32-44 characters
Example: 9mW3x7b2N5Y4K8r6V3c1Q7z5T4H8L6M9P2F1D3J8
Validation: Ed25519 public key
```

**Sui**:
```
Format: 0x + 64 hex characters
Example: 0xa1b2c3d4e5f67890...
Validation: Blake2b hash
```

**Bitcoin**:
```
Format: 1/3/bc1 + Base58/Bech32
Example: bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
Validation: Checksum + script type
```

### Resolution Process

```
User requests: miguel.ever on Ethereum
    ↓
1. DNS-like query to EverName registry
2. Registry returns resolver contract address
3. Query resolver for ETH address
4. Return: 0x742d35a8f91f7a45C...
    ↓
Send payment to resolved address
```

---

## 💰 NIL Token Economics (Conceptual)

### Token Utility

**1. Domain Registration**
- Payment currency
- Discounts for holders (0-15%)
- Staking for premium features

**2. Tier Access**
```
Free: 0 NIL
Standard: 500 NIL staked
Premium: 1000+ NIL staked
Enterprise: 5000+ NIL staked
```

**3. Governance**
- Vote on feature proposals
- Fee structure changes
- Nillion integration parameters
- Ecosystem fund allocation

**4. Liveness Monitoring Fees**
- 1 NIL per year per domain
- Auto-deducted from stake
- Funds Nillion compute costs

### Token Distribution (Example)
```
Total Supply: 100,000,000 NIL

Allocation:
• Community Rewards: 40%
• Development Fund: 25%
• Initial Liquidity: 15%
• Team & Advisors: 10%
• Ecosystem Grants: 10%
```

---

## 🤝 Integration Possibilities

### Wallet Integration
- MetaMask Snaps
- WalletConnect v2
- Coinbase Wallet SDK
- Phantom (Solana)
- Sui Wallet
- Martian (Aptos)

### DeFi Integration
- Uniswap (domain as trading identity)
- Aave (credit score via domain history)
- ENS interoperability
- Lens Protocol (social graph)

### Social Integration
- Twitter verification
- Discord bots (resolve .ever to wallet)
- Telegram payments
- Farcaster integration

### Enterprise Integration
- Corporate succession planning
- DAO tooling
- Payroll systems (pay via .ever)
- Identity verification (KYC via .ever)

---

## 📚 Educational Resources (Mockup Context)

### For Users
- Getting started guide
- Video tutorials
- FAQs
- Best practices for delegation

### For Developers
- API documentation
- Smart contract specs
- Nillion integration guide
- Frontend component library

### For Delegates
- What to expect
- How to claim assets
- Legal considerations
- Support resources

---

## 🏁 Conclusion

This comprehensive mockup demonstrates **EverName** as a next-generation decentralized identity and legacy platform that solves critical problems in Web3:

✅ **Multi-chain identity fragmentation** → Single `.ever` domain for all chains

✅ **Digital asset inheritance** → Trustless, automatic legacy execution

✅ **Privacy in legacy planning** → Nillion-powered blind computation

The screens cover the complete user journey from onboarding to legacy execution, showcasing:
- Intuitive UX for complex blockchain operations
- Privacy-preserving delegation via Nillion
- Multi-chain wallet management
- Automated, trustless asset distribution

**Key Innovation**: By combining blockchain-based domain ownership with Nillion Network's blind computation, EverName enables truly private and automatic legacy planning without trusted intermediaries.

This mockup serves as a blueprint for implementing a production-ready platform that could fundamentally change how we manage digital identity and inheritance in the decentralized web.

---

**Last Updated**: March 2025
**Version**: 1.0.0
**Status**: UI/UX Mockup & Concept Demonstration
**Technology**: Flask + HTML/CSS/JavaScript
**Blockchain Concept**: Ethereum + Nillion Network

---

## 🔗 Quick Links

- **Run the App**: `python evername_app.py`
- **Learn More**: Read individual template files for detailed features
- **Nillion Network**: https://nillion.com

