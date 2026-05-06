with open("app/main.py", "r") as f:
    content = f.read()

content = content.replace(
"""    parser.add_argument("--show-redaction-summary", action="store_true", help="Show redaction summary")
""",
"""    parser.add_argument("--show-redaction-summary", action="store_true", help="Show redaction summary")
    args = parser.parse_args()
""")

with open("app/main.py", "w") as f:
    f.write(content)
