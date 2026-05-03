with open("app/main.py", "r") as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if line.strip() == "if args.run_replay:":
        skip = True
    if skip and line.strip() == "if args.run_governance:":
        skip = False

    if not skip:
        new_lines.append(line)

with open("app/main.py", "w") as f:
    f.writelines(new_lines)
