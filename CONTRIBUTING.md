# Contributing to AI-PMS RAG Bootcamp

We welcome contributions to the project! Please review the following guidelines before submitting a Pull Request.

## Contribution Guides & Ownership

For detailed contribution tracking, credit claiming, and specific engineering practices for Phase 1 & 2 of this project, please refer to the developer guides:
- 🎓 **K. Bala Chowdappa** (Guide, Mentor, and Architecture Design) — See task logs and architectural progress in [`docs/BALU_tasks/`](docs/BALU_tasks/)
- 💻 **Donthi Nishitha** (Core Development, Advanced RAG Track) — 📖 [Nishitha's Contribution Guide](docs/Nishitha_Contribution_Guide.md)

This guide is highly recommended to understand how we separate experiments and assign credit.

## Development Workflow

1. Clone the repository and set up your virtual environment:
```bash
git clone https://github.com/balacsegprec/aipms-rag-bootcamp.git
cd aipms-rag-bootcamp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a feature branch:
```bash
git checkout -b feature/your-feature
```

3. Make your changes and ensure all tests pass:
```bash
python3 -m pytest tests/ -v
```

4. Commit your changes with descriptive messages:
```bash
git commit -m "Add feature: [description]"
```

5. Push to your branch and open a Pull Request!

## Code Standards
- Ensure all new features have accompanying unit or integration tests in the `tests/` directory.
- New scripts inside `scripts/` should appropriately handle path traversal (`sys.path.append`) to access the `src/` directory.
- Follow the architectural boundaries (do not mix experimental notebooks with production `src/core/` code).
