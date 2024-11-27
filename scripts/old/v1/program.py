import os
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox

# Path to start looking for repositories
GIT_PATH = "/home/daniel/Git"

def is_broken_repo(repo_path):
    """ Check if a git repository is linked to a non-existent remote repository. """
    try:
        output = subprocess.check_output(
            ["git", "ls-remote"], cwd=repo_path, stderr=subprocess.STDOUT, text=True
        )
        # If the command returns output, it means the remote is reachable
        return False
    except subprocess.CalledProcessError:
        # If there is an error, it indicates an unreachable remote
        return True

def delete_broken_repos():
    deleted_count = 0

    for root, dirs, files in os.walk(GIT_PATH):
        if ".git" in dirs:
            repo_path = root
            if is_broken_repo(repo_path):
                shutil.rmtree(repo_path)
                deleted_count += 1

    messagebox.showinfo("Deletion Completed", f"Script run: {deleted_count} repositories deleted.")

def run_script():
    delete_broken_repos()

# Setting up the GUI
root = tk.Tk()
root.title("Git Repository Cleaner")
root.geometry("400x200")

label = tk.Label(root, text="Click the button to clean up broken Git repositories.")
label.pack(pady=20)

run_button = tk.Button(root, text="Run Script", command=run_script, bg="red", fg="white")
run_button.pack(pady=20)

root.mainloop()
