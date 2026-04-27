# Security Baseline

## Secrets Policy
*   **No Hardcoding:** API keys, secret keys, database credentials, and Telegram tokens must NEVER be hardcoded in Python files.
*   **Environment Variables:** All secrets must be loaded via environment variables.
*   **`.env` File:** Local development secrets belong in a `.env` file in the project root.
*   **Git Ignore:** The `.env` file is strictly ignored in `.gitignore`. A safe `.env.example` is provided for reference.

## API Key Least Privilege
*   **Testnet Keys:** Used exclusively for `testnet` and `paper` execution modes where applicable.
*   **Live Keys (Read-Only):** Create a separate Binance API key with ONLY "Read Info" permissions for purely observational tasks or data collection.
*   **Live Keys (Trading):** Create a dedicated API key for live trading.
    *   Enable Spot & Margin Trading (if needed).
    *   Enable Futures Trading (if needed).
    *   **CRITICAL:** Ensure "Enable Withdrawals" is **UNCHECKED**. The system must never have withdrawal capability.
    *   **IP Restriction:** Restrict the API key to the static IP address of the machine running the bot.

## Local Machine Hygiene
*   The machine running the live bot should be dedicated or securely compartmentalized (e.g., a specific user account with restricted permissions).
*   Avoid running unknown or untrusted scripts on the same machine.

## File Permissions
*   The `.env` file must be readable only by the user executing the bot (`chmod 600 .env`).
*   SQLite database files in `storage/state/` should be restricted similarly to prevent unauthorized tampering with account state records.

## Logging Redaction
*   The logging system MUST NOT print raw API Secret Keys to standard output or log files.
*   Log filters should be applied to mask sensitive headers or payloads in `DEBUG` mode if necessary.

## Emergency Key Rotation
*   The operator must know how to quickly regenerate API keys on Binance and update the `.env` file or environment variables, followed by a system restart, in case of suspected compromise.

## Forbidden Practices
*   Committing `.env` files.
*   Printing API keys in error messages.
*   Running the live bot as the `root` user on a Linux system.
