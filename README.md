# Minimal Python Library Starter

A small Python 3.12+ starter for libraries managed with `uv`.

## What Is Included

- `uv` for environments, locking, building, and publishing
- `uv_build` as the PEP 517 build backend with a `src/` layout and `py.typed`
- mypy in strict mode
- Ruff for linting and formatting
- pytest for colocated tests (excluded from the wheel)
- Poe the Poet task runner for the script-style commands below
- pre-commit hooks for local format, lint, typecheck, test, build, and gitleaks checks
- GitHub Actions CI and gitleaks scans for push and pull request verification
- Grouped Dependabot updates for `uv` and GitHub Actions
- A single `src/py_lib_starter/__init__.py` library entrypoint

## Setup

```zsh
uv sync
uv run pre-commit install
```

## Scripts

```zsh
uv run poe verify
uv run poe build
uv run poe test
uv run poe lint
uv run poe typecheck
uv run poe format-check
uv run poe format
```

## Local Hooks

`uv run pre-commit install` installs both hook stages from `.pre-commit-config.yaml`.

- `pre-commit`: checks formatting, linting, mypy, and gitleaks
- `pre-push`: runs tests and verifies the build

## CI

`.github/workflows/ci.yml` runs `uv sync --locked` and `uv run poe verify` on every push and pull request.

## Publishing

`uv run poe build` cleans `dist/` and builds the sdist and wheel. `uv run poe publish` runs `verify` first, then `uv publish`.

## License

MIT. See [LICENSE.md](./LICENSE.md).
