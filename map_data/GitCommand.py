"""
course: CI103
lab section: 071
date: 05/21/2020
id: aw3338
name: Ao Wang
description: The module holds the class AutomateCommit, which helps committing and pushing to Github automatically.
"""

import subprocess


class AutomateCommit:
    """
    The AutomateCommit object helps with self-automating commits for the self-updating
    wildfire map, statistics page, and news feed.

    :param commit_message: The commit message for the commit command
    :type commit_message: str
    :param repo_dir: The destination for the file/folder you want to commit
    :type repo_dir: str
    """

    def __init__(self, commit_message="Update webpage", repo_dir=""):
        self.commit_message = commit_message
        self.repo_dir = repo_dir

    def set_commit_message(self, message):
        self.commit_message = message

    def get_commit_message(self):
        return self.commit_message

    def set_repo_dir(self, repo):
        self.repo_dir = repo

    def get_repo_dir(self):
        return self.repo_dir

    # The git command for Python were from:
    # https://www.ivankrizsan.se/2017/03/19/interacting-with-github-using-python/

    def execute_shell_command(self, cmd):
        """Executes a shell command in a subprocess, waiting until it has completed.

        :param cmd: Command to execute.
        :param work_dir: Working directory path.
        """
        pipe = subprocess.Popen(
            cmd,
            shell=True,
            cwd=self.repo_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        (out, error) = pipe.communicate()
        print(out, error)
        pipe.wait()

    def git_commit(self):
        """Commits the Git repository located in supplied repository directory with the supplied commit message.

        :param commit_message: Commit message.
        :param repo_dir: Directory containing Git repository to commit.
        """
        cmd = 'git commit -am "%s"' % self.commit_message
        self.execute_shell_command(cmd)

    def git_push(self):
        """Pushes any changes in the Git repository located in supplied repository directory to remote git repository.

        :param repo_dir: Directory containing git repository to push.
        """
        cmd = 'git push '
        self.execute_shell_command(cmd)
