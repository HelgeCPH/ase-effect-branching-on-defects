import argparse


def main(project, force_recollection=False):
    # Implement me!!!
    pass


if __name__ == "__main__":

    msg = "Collect issues from JIRA."
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite previously collected issue dumps.",
    )
    parser.add_argument("project")
    args = parser.parse_args()

    main(project=args.project, force_recollection=args.force)
