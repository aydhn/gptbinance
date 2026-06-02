# Executable Plans and Concurrency Policy

- **Plan != Execution:** Plan onaylanmış olabilir ama safe completion garanti değildir.
- **Dependencies & Gates:** Her adım policy/readiness/approval/beneficiary safety gatelerinden geçmelidir.
- **Handoffs:** Opaque handoff yasaktır; tüm geçişlerde sahibi belli olmalıdır.
