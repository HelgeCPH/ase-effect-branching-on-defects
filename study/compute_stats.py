import argparse


def main(project):
    # Implement me!!!
    pass


if __name__ == "__main__":
    msg = "Compute statistics for projects."
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("project")
    args = parser.parse_args()

    main(args.project)
