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

        # UI Elements
        self.start_button = tk.Button(root, text="Start Cleaning", command=self.clean_repos)
        self.start_button.pack(pady=10)

        self.output_box = scrolledtext.ScrolledText(root, width=70, height=20)
        self.output_box.pack(pady=10)

    def log(self, message):
        """Log messages to the UI output box."""
        self.output_box.insert(tk.END, message + "\n")
        self.output_box.see(tk.END)
        self.root.update()

    def clean_repos(self):
        """Clean up Git repositories without valid remotes."""
        base_dir = "/home/daniel/Git"  # Change this path as needed
        deleted_count = 0

        for root_dir, dirs, files in os.walk(base_dir):
            if ".git" in dirs:
                repo_path = root_dir

                try:
                    repo = git.Repo(repo_path)

                    # Check if repository has remotes and if they are valid
                    if len(repo.remotes) == 0:
                        # No remotes at all
                        self.log(f"No remotes found for: {repo_path}")
                        shutil.rmtree(repo_path)
                        deleted_count += 1
                        self.log(f"Deleted repository: {repo_path}")
                    else:
                        # Check if all remotes are invalid (e.g., disconnected or deleted)
                        all_remotes_invalid = True
                        for remote in repo.remotes:
                            try:
                                remote.fetch()  # Try fetching from the remote to check validity
                                all_remotes_invalid = False  # If fetch succeeds, the remote is valid
                                break
                            except Exception as e:
                                self.log(f"Invalid remote '{remote.name}' in {repo_path}: {e}")

                        if all_remotes_invalid:
                            shutil.rmtree(repo_path)
                            deleted_count += 1
                            self.log(f"Deleted repository with invalid remotes: {repo_path}")
                        else:
                            self.log(f"Repository has valid remotes, skipping: {repo_path}")

                except git.InvalidGitRepositoryError:
                    self.log(f"Invalid Git repository, skipping: {repo_path}")
                except Exception as e:
                    self.log(f"Error processing {repo_path}: {e}")

                # Prevent recursion into .git directories
                dirs.remove(".git")

        # Display confirmation message
        messagebox.showinfo("Cleanup Complete", f"Script run complete: {deleted_count} repositories deleted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GitRepoCleaner(root)
    root.mainloop()