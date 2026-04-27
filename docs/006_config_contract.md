# Configuration Contract

Configuration must be strictly typed, validated at startup, and loaded in a predictable precedence order. The application must crash immediately on startup if configuration is invalid.

## Environment Profiles
The system supports distinct profiles via the `ENV` variable:
1.  **`dev`**: Local development, connects to local SQLite, uses mock data or testnet.
2.  **`paper`**: Paper trading. Connects to live Binance data feeds but executes via the internal simulation engine.
3.  **`testnet`**: Connects to Binance official testnet for both data and execution.
4.  **`live`**: Production. Connects to Binance live for data and execution. Requires explicit confirmation flags.

## Secret Handling
*   **Rule:** NO SECRETS IN CODE OR CONFIG FILES.
*   API keys, Telegram tokens, and database passwords must be provided exclusively via Environment Variables or a local `.env` file (which is strictly `.gitignore`d).
*   Env Var Naming Rule: Prefix with `BINANCE_`, `TG_`, or `DB_` (e.g., `BINANCE_API_KEY_LIVE`).

## Configuration Structure
We use hierarchical configuration (e.g., Pydantic Settings).

### 1. `ExecutionConfig`
*   `mode`: (enum: paper, testnet, live)
*   `exchange`: "binance"
*   `market_type`: (enum: spot, margin, futures)
*   `dry_run_safety_flag`: boolean (Must be explicitly False to allow real orders).

### 2. `RiskConfig`
*   `max_account_drawdown_pct`: float (e.g., 0.20)
*   `max_gross_leverage`: float (e.g., 2.0)
*   `daily_loss_limit_usd`: float
*   `max_order_notional_usd`: float
*   `fat_finger_buffer_pct`: float (e.g., 0.05)

### 3. `UniverseConfig`
*   `symbols`: List[str] (e.g., ["BTCUSDT", "ETHUSDT"])
*   `base_asset`: str (e.g., "USDT")

### 4. `TelegramConfig`
*   `bot_token`: str (secret)
*   `chat_id`: str (secret)
*   `alert_level`: str (INFO, WARN, ERROR)

## Precedence Order
When resolving configuration values, the system respects the following order (highest to lowest priority):
1.  **Environment Variables** (e.g., `export RISK_MAX_DRAWDOWN=0.15`)
2.  **Local `.env` file**
3.  **Configuration files** (e.g., `config/paper.yaml` or `config/live.yaml`)
4.  **Hardcoded Python defaults** (Defined in Pydantic models)

## Static vs. Dynamic Config
*   **Static:** Loaded once at startup (e.g., API keys, database paths, core risk limits). Changing these requires a process restart.
*   **Dynamic:** Parameters that can be hot-reloaded (e.g., strategy weights, specific indicator parameters). Dynamic config must be fetched from a designated local file or DB table, but never external APIs to ensure offline resilience.

## Feature Toggles
Use boolean flags in config to enable/disable specific modules (e.g., `ENABLE_TELEGRAM=True`, `ENABLE_ML_PREDICTOR=False`).
