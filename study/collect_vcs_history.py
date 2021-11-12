import argparse


def main(repo):
    # Implement me!!!
    pass


if __name__ == "__main__":

    msg = "Collect commits from Git."
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("repo")
    args = parser.parse_args()

    main(args.repo)
