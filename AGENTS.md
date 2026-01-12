# AGENTS.md - Development Guidelines for Play Directory

This is a **playground/experimental directory** for testing and prototyping. No existing codebase patterns have been established yet.

---

## Build / Lint / Test Commands

**Status**: No build system configured yet.

As code is added, establish the appropriate commands here:

### Build Commands
- *None configured yet*

### Linting
- *None configured yet*

### Testing
- *None configured yet*
- When adding tests, document how to run single tests (e.g., `pytest tests/test_foo.py::test_bar`)

---

## Code Style Guidelines

Since this is a new project, establish patterns as you add code. Keep these principles in mind:

### General Principles
1. **Follow the framework/language conventions** - If using a specific framework (React, Next.js, Express, etc.), follow its official style guide
2. **Be consistent** - Once a pattern is established, stick to it across all new code
3. **Update this file** - When patterns are established, document them here

### Language-Specific Guidelines (to be filled as code is added)

#### Python
- Use type hints for all function signatures
- Follow PEP 8 formatting
- Use `ruff` for linting, `mypy` for type checking
- Package manager: `uv`

#### TypeScript/JavaScript
- Use explicit return types on exports
- Organize imports: external libraries → internal modules → relative imports
- Package manager: Detect automatically (npm/yarn/pnpm/bun)
- Linting: ESLint
- Formatting: Prettier

### Error Handling
- **Never use empty catch blocks** - All errors must be logged or handled
- Provide meaningful error messages
- Propagate errors appropriately (don't swallow them)

### Naming Conventions
- Use descriptive, self-documenting names
- Follow language conventions (snake_case for Python, camelCase for JS/TS)
- Avoid abbreviations unless widely understood

### Testing
- Write focused tests for core user flows and critical paths
- Mock external dependencies (APIs, databases, file systems)
- Deferr edge case testing until explicitly required
- Use descriptive test names

### Documentation
- Add one-line docstrings/comments for functions that aren't self-documenting
- Comment "why", not "what"
- Keep documentation in sync with code changes

---

## Project Structure

**Current Status**: Empty playground directory

```
play/
├── .opencode/          # OpenCode managed resources
└── (to be populated)  # Your code goes here
```

---

## Notes for Agentic Coding

1. **Before starting implementation**: Check if patterns exist in the codebase
2. **If patterns don't exist**: Propose an approach before implementing
3. **After establishing patterns**: Update this file with the conventions used
4. **Always use diagnostics**: Run `lsp_diagnostics` on changed files before marking tasks complete
