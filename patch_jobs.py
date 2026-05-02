with open("app/automation/jobs.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'return {"status": "SUCCESS"}job_id' in line:
        new_lines.append('        return {"status": "SUCCESS"}\n')
    else:
        new_lines.append(line)

with open("app/automation/jobs.py", "w") as f:
    f.writelines(new_lines)
