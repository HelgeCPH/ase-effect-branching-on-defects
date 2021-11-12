import os
from pydriller import Repository


repo_name = "ignite"
gh_repo = f"https://github.com/apache/{repo_name}.git"
repo_path = os.path.join("data", "repositories", repo_name)
repo = Repository(path_to_repo=gh_repo, clone_repo_to=repo_path)
for commit in repo.traverse_commits():
    print(f"{commit.hash[:10]}")
