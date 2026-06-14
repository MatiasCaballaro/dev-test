from settings import FixtureSettings


def build_repository_summary(settings: FixtureSettings) -> str:
    return f"{settings.name} on {settings.branch}: {settings.purpose}"
