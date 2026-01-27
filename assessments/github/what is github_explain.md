
# What is GitHub and Git?

## GitHub Definition

GitHub is a web-based platform and cloud service that hosts Git repositories and provides collaboration tools for software development. It allows developers to store, manage, track, and collaborate on code projects using Git version control. GitHub also provides features like issue tracking, pull requests, code reviews, team collaboration, CI/CD integration, and project management tools.

### Key Features of GitHub
- **Repository Hosting**: Cloud-based storage for code
- **Version Control**: Track changes and history
- **Collaboration**: Multiple users working on same project
- **Pull Requests**: Code review before merging
- **Issue Tracking**: Bug reports and feature requests
- **Actions**: Continuous Integration/Continuous Deployment (CI/CD)
- **Code Search**: Find code across repositories
- **Documentation**: Wiki and README support
- **Security**: Vulnerability scanning and protection

---

## Git Definition

Git is a free, open-source, distributed version control system designed to handle projects of any size with speed and efficiency. Git tracks changes in source code during development and maintains a complete history of every modification. It allows multiple developers to work independently and merge their changes back together.

### Key Characteristics of Git
- **Distributed**: Full copy of repository on each machine
- **Version Control**: Tracks all file changes over time
- **Branching**: Create independent development branches
- **Merging**: Combine changes from different branches
- **Open Source**: Free to use and modify
- **Fast**: Optimized for speed
- **Local**: Works offline with local repository
- **Staging Area**: Control exactly what gets committed

---

## Git Commands

### Configuration Commands

#### 1. **git config**
Set up Git configuration (user name, email, etc.)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list                           # List all configuration settings
git config user.name                        # Check specific setting
git config --global user.name "New Name"    # Change name globally
```

#### 2. **git help**
Get help about Git commands
```bash
git help                    # General help
git help <command>          # Help for specific command
git <command> -h            # Quick help for command
```

---

### Repository Initialization & Cloning

#### 3. **git init**
Initialize a new Git repository
```bash
git init                    # Initialize current directory as Git repository
git init <directory-name>   # Initialize a new directory as Git repository
```

#### 4. **git clone**
Clone (copy) an existing repository
```bash
git clone <repository-url>              # Clone repository to current directory
git clone <repository-url> <directory>  # Clone to specific directory
git clone --depth 1 <repository-url>    # Shallow clone (faster)
```

---

### Checking Status & History

#### 5. **git status**
Show the current status of working directory
```bash
git status                  # Show status with detailed output
git status -s               # Short status format
git status --porcelain      # Machine-readable format
```

#### 6. **git log**
View commit history
```bash
git log                             # View all commits
git log --oneline                   # One-line commit summary
git log --graph --oneline --all     # Visual branch graph
git log -n 5                        # Show last 5 commits
git log --author="Name"             # Filter by author
git log --since="2 weeks ago"       # Show commits from last 2 weeks
git log --grep="keyword"            # Filter by commit message
git log <file>                      # Show commits for specific file
git log -p                          # Show detailed changes in each commit
```

#### 7. **git show**
Display details of a specific commit
```bash
git show                    # Show last commit details
git show <commit-hash>      # Show specific commit
git show <commit-hash>:<file-path>  # Show file at specific commit
```

#### 8. **git diff**
Compare changes between versions
```bash
git diff                            # Show unstaged changes
git diff --staged                   # Show staged changes
git diff <branch1> <branch2>        # Compare branches
git diff <commit1> <commit2>        # Compare commits
git diff HEAD~1                     # Compare with previous commit
```

---

### Staging & Committing

#### 9. **git add**
Stage files for commit
```bash
git add <file>              # Stage specific file
git add .                   # Stage all changes
git add *.txt               # Stage all .txt files
git add --all               # Stage all changes (newer syntax)
git add -p                  # Interactive staging (choose hunks)
```

#### 10. **git commit**
Create a commit (save changes)
```bash
git commit -m "Commit message"          # Commit with message
git commit -am "Message"                # Stage and commit tracked files
git commit --amend                      # Modify last commit
git commit --amend --no-edit            # Amend without changing message
git commit -m "Title" -m "Description"  # Multi-line commit message
```

#### 11. **git restore**
Restore files to previous state
```bash
git restore <file>                      # Discard changes in working directory
git restore --staged <file>             # Unstage file
```

#### 12. **git reset**
Reset staging area or commits
```bash
git reset                               # Unstage all files
git reset <file>                        # Unstage specific file
git reset --soft HEAD~1                 # Undo last commit (keep changes staged)
git reset --mixed HEAD~1                # Undo last commit (keep changes unstaged)
git reset --hard HEAD~1                 # Undo last commit (discard changes)
git reset HEAD~3                        # Go back 3 commits
```

---

### Branching

#### 13. **git branch**
Manage branches
```bash
git branch                              # List local branches
git branch -a                           # List all branches (local + remote)
git branch <branch-name>                # Create new branch
git branch -d <branch-name>             # Delete branch (safe)
git branch -D <branch-name>             # Delete branch (force)
git branch -m <old-name> <new-name>     # Rename branch
git branch -v                           # Show branches with last commit
```

#### 14. **git checkout**
Switch between branches or restore files
```bash
git checkout <branch-name>              # Switch to branch
git checkout -b <branch-name>           # Create and switch to new branch
git checkout <commit-hash>              # Detached HEAD state
git checkout -- <file>                  # Discard changes in file
```

#### 15. **git switch**
Modern alternative to checkout for branch switching
```bash
git switch <branch-name>                # Switch to branch
git switch -c <branch-name>             # Create and switch to new branch
git switch -                            # Switch to previous branch
```

---

### Merging & Rebasing

#### 16. **git merge**
Merge one branch into another
```bash
git merge <branch-name>                 # Merge branch into current branch
git merge --no-ff <branch-name>         # Create merge commit
git merge --squash <branch-name>        # Squash commits before merging
git merge --abort                       # Cancel merge in progress
```

#### 17. **git rebase**
Reapply commits on top of another branch
```bash
git rebase <branch-name>                # Rebase current branch
git rebase -i HEAD~3                    # Interactive rebase last 3 commits
git rebase --continue                   # Continue after resolving conflicts
git rebase --abort                      # Cancel rebase
```

#### 18. **git cherry-pick**
Apply specific commits to current branch
```bash
git cherry-pick <commit-hash>           # Apply single commit
git cherry-pick <commit1> <commit2>     # Apply multiple commits
git cherry-pick --continue              # Continue after conflict resolution
```

---

### Remote Repository Operations

#### 19. **git remote**
Manage remote repositories
```bash
git remote                              # List remotes
git remote -v                           # List remotes with URLs
git remote add <name> <url>             # Add new remote
git remote remove <name>                # Remove remote
git remote rename <old> <new>           # Rename remote
git remote show <name>                  # Show remote details
git remote set-url <name> <new-url>     # Change remote URL
```

#### 20. **git fetch**
Download objects and refs from remote
```bash
git fetch                               # Fetch from default remote (origin)
git fetch <remote>                      # Fetch from specific remote
git fetch --all                         # Fetch from all remotes
git fetch <remote> <branch>             # Fetch specific branch
```

#### 21. **git pull**
Fetch and merge changes from remote
```bash
git pull                                # Fetch and merge from origin/default branch
git pull <remote> <branch>              # Pull from specific remote/branch
git pull --rebase                       # Pull with rebase instead of merge
git pull --no-ff                        # Always create merge commit
```

#### 22. **git push**
Upload commits to remote repository
```bash
git push                                # Push to default remote
git push <remote> <branch>              # Push to specific remote/branch
git push --all                          # Push all branches
git push --tags                         # Push all tags
git push <remote> --delete <branch>     # Delete remote branch
git push -u origin <branch>             # Push and set upstream
```

---

### Stashing

#### 23. **git stash**
Temporarily save changes without committing
```bash
git stash                               # Stash current changes
git stash save "Description"            # Stash with description
git stash list                          # List all stashes
git stash show                          # Show latest stash changes
git stash apply                         # Apply latest stash (keep stash)
git stash apply stash@{n}               # Apply specific stash
git stash pop                           # Apply and remove latest stash
git stash drop                          # Delete latest stash
git stash drop stash@{n}                # Delete specific stash
git stash clear                         # Delete all stashes
```

---

### Tagging

#### 24. **git tag**
Create, list, and manage tags (version markers)
```bash
git tag                                 # List tags
git tag <tag-name>                      # Create lightweight tag
git tag -a <tag-name> -m "Message"      # Create annotated tag
git tag -d <tag-name>                   # Delete local tag
git push origin <tag-name>              # Push specific tag to remote
git push origin --delete <tag-name>     # Delete remote tag
git show <tag-name>                     # Show tag details
```

---

### Undoing Changes

#### 25. **git revert**
Create new commit that undoes changes
```bash
git revert <commit-hash>                # Create revert commit for specific commit
git revert HEAD                         # Revert last commit
git revert --no-edit <commit-hash>      # Revert without editing message
```

#### 26. **git clean**
Remove untracked files
```bash
git clean -n                            # Show what would be deleted (dry run)
git clean -f                            # Force delete untracked files
git clean -fd                           # Delete untracked files and directories
git clean -fX                           # Delete ignored files
```

---

### Searching & Inspecting

#### 27. **git grep**
Search for text within tracked files
```bash
git grep "keyword"                      # Search for keyword
git grep "keyword" <branch>             # Search in specific branch
git grep -n "keyword"                   # Show line numbers
git grep -i "keyword"                   # Case-insensitive search
```

#### 28. **git blame**
Show who changed each line
```bash
git blame <file>                        # Show author of each line
git blame -L10,20 <file>                # Show lines 10-20
git blame --date=short <file>           # Show dates in short format
```

#### 29. **git bisect**
Find commit that introduced a bug
```bash
git bisect start                        # Start bisect session
git bisect bad                          # Mark current commit as bad
git bisect good <commit-hash>           # Mark specific commit as good
git bisect reset                        # End bisect session
```

---

### Advanced Operations

#### 30. **git reflog**
Show reference logs (undo almost anything)
```bash
git reflog                              # Show recent operations
git reflog <branch-name>                # Show reflog for specific branch
git reset --hard HEAD@{n}               # Go back to specific state
```

#### 31. **git format-patch**
Create patches from commits
```bash
git format-patch -1 HEAD                # Create patch for last commit
git format-patch -3                     # Create patches for last 3 commits
```

#### 32. **git apply**
Apply patches
```bash
git apply <patch-file>                  # Apply patch
git apply --check <patch-file>          # Check if patch applies cleanly
```

#### 33. **git archive**
Create file archive of repository
```bash
git archive HEAD -o archive.zip         # Create zip archive
git archive --format=tar HEAD | gzip > archive.tar.gz
```

---

### Collaboration & Pull Requests

#### 34. **git request-pull**
Create pull request message
```bash
git request-pull <base-branch> <remote-url> <branch-name>
```

#### 35. **git am**
Apply patches from email (mailing list workflow)
```bash
git am <patch-file>                     # Apply patch from email
git am --continue                       # Continue after conflict
git am --abort                          # Cancel patch application
```

---

### Inspection & Analysis

#### 36. **git fsck**
File system check - verify repository integrity
```bash
git fsck                                # Check repository integrity
git fsck --lost-found                   # Find lost commits
```

#### 37. **git gc**
Garbage collection - optimize repository
```bash
git gc                                  # Optimize repository
git gc --aggressive                     # More aggressive optimization
```

#### 38. **git verify-commit**
Verify cryptographic signature of commits
```bash
git verify-commit <commit-hash>         # Verify commit signature
```

---

### Working with Submodules

#### 39. **git submodule**
Manage Git submodules (repositories within repositories)
```bash
git submodule add <url> <path>          # Add submodule
git submodule init                      # Initialize submodules
git submodule update                    # Update submodules
git clone --recurse-submodules <url>    # Clone with submodules
```

---

### Signing Commits

#### 40. **git config (GPG signing)**
Configure commit signing
```bash
git config --global user.signingkey <key-id>
git config --global commit.gpgsign true
git commit -S -m "Signed commit"        # Create signed commit
```

---

## Git Workflow Commands Summary

### Basic Workflow
```bash
git init                    # 1. Initialize repository
git add <files>             # 2. Stage changes
git commit -m "Message"     # 3. Commit changes
git push                    # 4. Push to remote
```

### Feature Branch Workflow
```bash
git checkout -b feature/new-feature         # Create feature branch
# Make changes
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature      # Push branch to remote
# Create pull request on GitHub
git checkout main                           # Switch back to main
git pull                                    # Update local main
git merge feature/new-feature               # Merge feature locally (optional)
```

### Collaborative Workflow
```bash
git pull                    # Get latest changes
# Make changes
git add .
git commit -m "Message"
git push                    # Push changes
git fetch                   # Check for remote changes
```

---

## Quick Reference Table

| Command | Purpose |
|---------|---------|
| `git init` | Initialize new repository |
| `git clone` | Copy existing repository |
| `git add` | Stage files for commit |
| `git commit` | Save changes |
| `git push` | Upload to remote |
| `git pull` | Download and merge from remote |
| `git branch` | Manage branches |
| `git checkout` | Switch branches |
| `git merge` | Combine branches |
| `git status` | Show repository status |
| `git log` | View commit history |
| `git diff` | Compare changes |
| `git stash` | Temporarily save changes |
| `git tag` | Mark versions |
| `git revert` | Undo commits |

---

## Difference Between Git and GitHub

| Feature | Git | GitHub |
|---------|-----|--------|
| **Type** | Version control system | Hosting platform |
| **Installation** | Installed locally | Web-based service |
| **Access** | Local or networked | Cloud/Internet |
| **Collaboration** | Manual coordination | Built-in tools |
| **Cost** | Free & open source | Free (with paid tiers) |
| **Features** | Core version control | Additional: PR, Issues, Actions, Wiki |
| **Repository Storage** | Local machine | Cloud servers |
| **Interface** | Command-line | Web interface + Git CLI |

