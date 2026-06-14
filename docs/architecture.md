# Dev Test Architecture

This repository is a small fixture used to validate repository ingestion, wiki generation, and incremental reingestion.

## Components

- `src/app.py` exposes the command-line entrypoint.
- `src/settings.py` defines environment-aware fixture settings.
- `src/repository_summary.py` builds a small summary that can be used by wiki and search tests.

## Runtime Flow

1. The application loads fixture settings.
2. The entrypoint asks the summary module for repository metadata.
3. The summary is printed for smoke-test visibility.

## Testing Intent

The files are intentionally small, readable, and cross-referenced so ingestion can detect code and documentation changes clearly.
