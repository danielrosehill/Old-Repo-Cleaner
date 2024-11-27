Generate an attractive GUI that will work on the Linux desktop (OpenSUSE) and which will do the following:

Iterate through this directory, recursing into every subdirectory:
/home/daniel/Git

Each folder is a Github repository.

Some repositories belong to old remote repositories which no longer exist.

Your tasks are to:

- 1) Determine if this repository is linked to an old repo ("linked" means that the local repository does not have a remote repository because it has been deleted)
- If that is the case, delete the local repository

The UI should include a terminal output which displays a verbose output showing what the script is doing.

After you have finished deleting the empty repositories, display a confirmation message using this format:

Script run: {number} repositories deleted.

Where: {number} represents the total number of repositories that you deleted.