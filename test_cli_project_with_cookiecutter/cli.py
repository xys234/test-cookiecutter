"""Console script for test_cli_project_with_cookiecutter."""
import argparse
import sys


def main():
    """Console script for test_cli_project_with_cookiecutter."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("This is the main function")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
