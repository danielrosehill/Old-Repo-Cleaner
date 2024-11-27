import os
import shutil
import git
import tkinter as tk
from tkinter import scrolledtext, messagebox

class GitRepoCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Repository Cleaner")
        self.root.geometry("600x400")

        self.start_button = tk.Button(root, text="Start Cleaning", command=self.clean_repos)
        self.start_button.pack(pady=10)

        self.output_box = scrolledtext.ScrolledText(root, width=70, height=20)
        self.output_box.pack(pady=10)

    def log(self, message):
        self.output_box.insert(tk.END, message + "\n")
        self.output_box.see(tk.END)
        self.root.update()

    def clean_repos(self):
        base_dir = "/home/daniel/Git"
        deleted_count = 0

        for root, dirs, files in os.walk(base_dir):
            if ".git" in dirs:
                repo_path = root
                try:
                    repo = git.Repo(repo_path)
                    if not repo.remotes:
                        # No remote found, delete the repository
                        shutil.rmtree(repo_path)
                        deleted_count += 1
                        self.log(f"Deleted repository: {repo_path}")
                    else:
                        self.log(f"Repository has a remote, skipping: {repo_path}")
                except git.InvalidGitRepositoryError:
                    self.log(f"Invalid Git repository, skipping: {repo_path}")
                dirs.remove(".git")  # Do not recurse into .git directories

        # Display confirmation message
        messagebox.showinfo("Cleanup Complete", f"Script run: {deleted_count} repositories deleted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GitRepoCleaner(root)
    root.mainloop()
