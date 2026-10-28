# Git cheatsheet

| Task | Command |
| --- | --- |
| New branch | `git switch -c feature` |
| Stage all | `git add -A` |
| Commit | `git commit -m "message"` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| See history | `git log --oneline --graph` |
| Update from main | `git pull --rebase origin main` |
