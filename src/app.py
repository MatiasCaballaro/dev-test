from repository_summary import build_repository_summary
from settings import load_settings


def main() -> None:
    settings = load_settings()
    print(build_repository_summary(settings))


def version() -> str:
    return "wiki-fixture-e"


if __name__ == "__main__":
    main()
