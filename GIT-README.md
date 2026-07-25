# Git & GitHub Quick Steps

This repository contains a minimal Python script to practice basic Git and GitHub workflows.

Run the script locally:

```powershell
python pyscripts/myscript.py
python pyscripts/myscript.py --name Alice
```

Basic Git workflow:

```bash
# initialize repository (if not already)
git init

# check status
git status

# stage files and commit
git add .
git commit -m "Add simple demo script"

# add remote and push
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

Tips:
- Create a branch for changes: `git checkout -b my-feature`
- Use small commits and clear messages.
- On GitHub, create a repository and copy its URL into the `git remote add` command above.
