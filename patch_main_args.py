with open("app/main.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == "args =":
        continue
    new_lines.append(line)

with open("app/main.py", "w") as f:
    f.writelines(new_lines)
