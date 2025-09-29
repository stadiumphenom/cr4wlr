from github import Github
import os
from datetime import datetime

def create_github_issue(repo_name, title, body, token=None):
    token = token or os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GitHub token required.")
    g = Github(token)
    repo = g.get_repo(repo_name)
    issue = repo.create_issue(title=title, body=body)
    return issue.html_url

def prepare_issue_body(error_file='last_error.txt'):
    with open(error_file) as f:
        error_log = f.read()
    timestamp = datetime.now().isoformat()
    # Get last commit hash
    commit = os.popen('git rev-parse HEAD').read().strip()
    body = f"Error log from {error_file} at {timestamp}\nCommit: {commit}\n\n{error_log}"
    return body
