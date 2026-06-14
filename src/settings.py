from dataclasses import dataclass


@dataclass(frozen=True)
class FixtureSettings:
    name: str = "dev-test"
    branch: str = "main"
    purpose: str = "incremental ingestion and wiki generation fixture"


def load_settings() -> FixtureSettings:
    return FixtureSettings()
