import re

with open('app/main.py', 'r') as f:
    content = f.read()

parser_patch = """
    parser.add_argument("--disarm-live-session", action="store_true", help="Manually disarm live start gates")

    # Derivatives
    parser.add_argument("--product-type", type=str, choices=["spot", "margin", "futures"], default="spot")
    parser.add_argument("--execution-symbol", type=str, help="Target symbol")
    parser.add_argument("--set-leverage", type=int, help="Set leverage multiplier")
    parser.add_argument("--set-margin-mode", type=str, choices=["isolated", "cross"])
    parser.add_argument("--set-position-mode", type=str, choices=["one_way", "hedge"])
    parser.add_argument("--show-liquidation-risk", action="store_true")
    parser.add_argument("--show-funding-summary", action="store_true")
    parser.add_argument("--show-borrow-summary", action="store_true")
    parser.add_argument("--show-derivatives-summary", action="store_true")
    parser.add_argument("--run-derivatives-paper-session", action="store_true")
    parser.add_argument("--run-derivatives-testnet-smoke", action="store_true")
    parser.add_argument("--paper-symbols", type=str)
"""

content = content.replace('    parser.add_argument("--disarm-live-session", action="store_true", help="Manually disarm live start gates")', parser_patch)

with open('app/main.py', 'w') as f:
    f.write(content)
