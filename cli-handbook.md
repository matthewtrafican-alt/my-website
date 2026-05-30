# Advanced CLI Handbook — Windows (PowerShell & CMD)
> Plain English → Command → What It Does

---

## How to use this handbook

Every entry follows this pattern:

**When you want to...** → `the command` → *what actually happens*

You don't need to memorize commands. You need to know what you're trying to do — then look it up here.

---

## Table of Contents
1. [Navigation & Files](#navigation--files)
2. [Working with Text & Output](#working-with-text--output)
3. [Environment Variables](#environment-variables)
4. [Processes & System](#processes--system)
5. [Networking](#networking)
6. [Scripting](#scripting)
7. [Git & Version Control](#git--version-control)
8. [Node.js & npm](#nodejs--npm)
9. [Python & pip](#python--pip)
10. [Docker](#docker)
11. [Quick Reference — Copy & Paste Prompts](#quick-reference--copy--paste-prompts)

---

## Navigation & Files

**When you want to see where you are** → `pwd` → *prints the full path of your current folder*

**When you want to move into a folder** → `cd foldername` → *changes your location to that folder*

**When you want to go back up one level** → `cd ..` → *moves you to the parent folder*

**When you want to go home** → `cd ~` → *takes you to your user home directory*

**When you want to switch drives** → `D:` → *switches to the D drive*

**When you want to see what's in a folder** → `ls` → *lists all files and folders*

**When you want to see hidden files too** → `ls -Force` → *shows everything including hidden items*

**When you want to search inside a folder recursively** → `ls -Recurse` → *lists everything including subfolders*

**When you want to open the folder in File Explorer** → `explorer .` → *opens the current folder visually*

**When you want to open a file in VS Code** → `code filename.js` → *opens or creates the file in VS Code*

**When you want to open the whole project in VS Code** → `code .` → *opens the entire current folder as a VS Code project*

**When you want to create a new folder** → `mkdir foldername` → *creates a new empty folder*

**When you want to create a new file** → `New-Item file.txt` or `ni file.txt` → *creates an empty file*

**When you want to copy a file** → `Copy-Item file.txt backup.txt` → *makes a copy with a new name*

**When you want to copy a whole folder** → `Copy-Item -Recurse src\ dst\` → *copies folder and all its contents*

**When you want to rename or move a file** → `Move-Item old.txt new.txt` → *renames or moves the file*

**When you want to delete a file** → `Remove-Item file.txt` → *permanently deletes the file*

**When you want to delete a whole folder** → `Remove-Item -Recurse -Force myfolder\` → *deletes folder and everything in it*

**When you want to read a file** → `cat file.txt` → *prints the file contents to the terminal*

**When you want to see just the last few lines** → `Get-Content file.txt -Tail 20` → *shows the last 20 lines*

**When you want to watch a file update live** → `Get-Content file.txt -Wait` → *like tail -f, refreshes as file changes*

**When you want to write to a file** → `"Hello" | Out-File file.txt` → *creates or overwrites the file with that text*

**When you want to append to a file** → `"Hello" | Add-Content file.txt` → *adds to the end without overwriting*

**When you want to search for text inside files** → `Select-String "pattern" file.txt` → *like grep, finds matching lines*

**When you want to search recursively** → `Select-String -Recurse "TODO" *.js` → *searches all matching files in all subfolders*

**When you want to open a file in the browser** → `start index.html` → *opens the file with its default program*

---

## Working with Text & Output

**When you want to filter results** → `ls | Where-Object Name -like "*.log"` → *shows only items matching your condition*

**When you want to sort results** → `ls | Sort-Object Length -Descending` → *sorts by any property*

**When you want to count things** → `ls | Measure-Object` → *counts files or lines*

**When you want to save output to a file** → `command > output.txt` → *redirects stdout to a file*

**When you want to save errors too** → `command > out.txt 2>&1` → *captures both stdout and stderr*

**When you want to print AND save** → `command | Tee-Object output.txt` → *shows output and saves it at once*

**When you want to export as CSV** → `ls | Export-Csv output.csv -NoTypeInformation` → *saves results as a spreadsheet*

**When you want to copy something to clipboard** → `"text" | Set-Clipboard` → *copies to clipboard*

**When you want to paste from clipboard** → `Get-Clipboard` → *reads clipboard contents*

---

## Environment Variables

**When you want to read a variable** → `$env:PATH` → *prints the value of that variable*

**When you want to list all variables** → `Get-ChildItem Env:` → *shows every environment variable*

**When you want to set a variable for this session** → `$env:MY_VAR = "hello"` → *sets it until you close the terminal*

**When you want to add to PATH** → `$env:PATH += ";C:\new\path"` → *appends a path to your PATH variable*

**When you want to set a variable permanently** → `[System.Environment]::SetEnvironmentVariable("MY_VAR","value","User")` → *persists across sessions*

---

## Processes & System

**When you want to see what's running** → `Get-Process` → *lists all running processes*

**When you want to kill an app** → `Stop-Process -Name chrome` → *force-closes that process*

**When you want to kill by process ID** → `Stop-Process -Id 1234` → *kills specific process*

**When you want to see who's using a port** → `netstat -ano | findstr :3000` → *shows what process is on that port*

**When you want to kill what's on a port** → `Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess` → *finds the process using that port*

**When you want system info** → `systeminfo` → *full hardware and OS details*

**When you want to know who you're logged in as** → `whoami` → *prints your username*

**When you want to measure how long something takes** → `Measure-Command { npm run build }` → *times any command*

---

## Networking

**When you want to check if a site is reachable** → `ping google.com` → *sends test packets and shows response time*

**When you want to trace a network path** → `tracert google.com` → *shows every hop between you and the destination*

**When you want to look up a DNS address** → `nslookup google.com` → *resolves a domain to its IP*

**When you want to see your IP address** → `ipconfig` → *shows all network interface info*

**When you want to flush DNS cache** → `ipconfig /flushdns` → *clears cached DNS entries*

**When you want to make an HTTP request** → `Invoke-RestMethod https://api.example.com` → *like curl, auto-parses JSON*

**When you want to download a file** → `Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile "file.zip"` → *downloads to current folder*

**When you want to see active connections** → `netstat -an` → *lists all open network connections*

---

## Scripting

**When you want to allow scripts to run** → `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` → *unlocks PowerShell scripting for your user*

**When you want to run a script** → `.\myscript.ps1` → *executes a PowerShell script file*

**When you want to edit your shell profile** → `notepad $PROFILE` → *opens your startup config file*

**When you want to chain commands** → `cmd1 && cmd2` → *runs second only if first succeeds*

**When you want to run commands regardless** → `cmd1; cmd2` → *runs both no matter what*

**When you want to run something if the first fails** → `cmd1 || cmd2` → *runs second only if first fails*

---

## Git & Version Control

**When you want to start tracking a project** → `git init` → *creates a hidden .git folder that tracks all changes*

**When you want to download someone's project** → `git clone https://github.com/user/repo.git` → *downloads the full repo to your machine*

**When you want to see what changed** → `git status` → *shows modified, staged, and untracked files*

**When you want to see the history** → `git log --oneline --graph` → *visual timeline of all commits*

**When you want to save your work** → `git add . && git commit -m "what I changed"` → *snapshots your current state*

**When you want to save just one file** → `git add file.txt && git commit -m "updated file"` → *commits only that file*

**When you want to stage changes interactively** → `git add -p` → *lets you review each change chunk by chunk*

**When you want to push to GitHub** → `git push` → *uploads your commits to the remote*

**When you want to pull the latest** → `git pull --rebase` → *downloads and integrates remote changes cleanly*

**When you want to create a new branch** → `git switch -c feature/my-feature` → *creates and switches to a new branch*

**When you want to switch branches** → `git switch main` → *moves to that branch*

**When you want to merge a branch** → `git merge feature/my-feature` → *combines that branch into your current one*

**When you want to temporarily save uncommitted work** → `git stash` → *shelves changes so you can switch context*

**When you want to restore stashed work** → `git stash pop` → *brings back your shelved changes*

**When you want to undo your last commit** → `git reset HEAD~1` → *removes the commit but keeps your file changes*

**When you want to discard file changes** → `git restore file.txt` → *throws away unstaged changes to that file*

**When you want to unstage a file** → `git restore --staged file.txt` → *removes it from the staging area*

**When you want to connect to GitHub** → `git remote add origin https://github.com/USER/REPO.git` → *links your local repo to GitHub*

**When you want to ignore node_modules** → `echo node_modules/ > .gitignore` → *tells Git to never track that folder*

**When you want to remove a folder from GitHub but keep it locally** → `git rm -r --cached foldername` → *untracks it without deleting it*

---

## Node.js & npm

**When you want to start a new Node project** → `npm init -y` → *creates package.json with default settings*

**When you want to install all dependencies** → `npm install` → *reads package.json and installs everything*

**When you want to add a package** → `npm install express` → *installs and adds to dependencies*

**When you want to add a dev-only package** → `npm install -D jest` → *installs but marks as development only*

**When you want to install globally** → `npm install -g nodemon` → *makes the command available anywhere*

**When you want to run your app** → `node server.js` → *executes your JS file with Node*

**When you want to run a script** → `npm run dev` → *runs whatever "dev" is defined as in package.json*

**When you want to check for security issues** → `npm audit fix` → *automatically fixes known vulnerabilities*

**When you want to see installed packages** → `npm list` → *lists all packages in current project*

**When you want to run a tool without installing** → `npx create-next-app@latest myapp` → *downloads and runs once*

**When you want to manage Node versions** → `nvm install 20.0.0 && nvm use 20.0.0` → *switches between Node versions*

---

## Python & pip

**When you want to create an isolated environment** → `python -m venv venv` → *creates a folder with its own Python + packages*

**When you want to activate it** → `.\venv\Scripts\activate` → *switches your terminal to use that environment*

**When you want to leave it** → `deactivate` → *switches back to global Python*

**When you want to install a package** → `pip install requests` → *downloads and installs into active environment*

**When you want a specific version** → `pip install requests==2.28.0` → *pins to exact version*

**When you want to install from a file** → `pip install -r requirements.txt` → *installs everything listed in the file*

**When you want to save your dependencies** → `pip freeze > requirements.txt` → *exports all installed packages and versions*

**When you want to run your script** → `python app.py` → *executes the Python file*

**When you want to run tests** → `pytest -v` → *runs all test files verbosely*

**When you want to format your code** → `black .` → *auto-formats all Python files*

---

## Docker

**When you want to run a container** → `docker run -d -p 8080:80 --name myapp nginx` → *starts a detached container with port mapping*

**When you want to see what's running** → `docker ps` → *lists active containers*

**When you want to see all containers** → `docker ps -a` → *includes stopped containers*

**When you want to get inside a container** → `docker exec -it myapp bash` → *opens a shell inside the running container*

**When you want to follow container logs** → `docker logs -f myapp` → *streams live output from the container*

**When you want to stop a container** → `docker stop myapp` → *gracefully stops it*

**When you want to force remove a container** → `docker rm -f myapp` → *stops and deletes it*

**When you want to build an image** → `docker build -t myapp:latest .` → *builds from Dockerfile in current folder*

**When you want to start all services** → `docker-compose up -d` → *starts everything defined in docker-compose.yml*

**When you want to stop everything** → `docker-compose down -v` → *stops and removes containers and volumes*

**When you want to follow all service logs** → `docker-compose logs -f` → *streams logs from all services*

**When you want to clean up everything unused** → `docker system prune` → *removes stopped containers, dangling images, unused networks*

---

## Quick Reference — Copy & Paste Prompts

### Start a project from scratch
```powershell
mkdir my-project
cd my-project
git init
code .
```

### The daily Git loop (do this every time you change something)
```powershell
git add .
git commit -m "describe what you changed"
git push
```

### Set up a Node project
```powershell
npm init -y
npm install express
node server.js
```

### Set up a Python project
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install requests
python app.py
```

### Push a project to GitHub for the first time
```powershell
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/YOU/REPO.git
git branch -M main
git push -u origin main
```

### Fix node_modules accidentally committed
```powershell
echo node_modules/ > .gitignore
git rm -r --cached node_modules
git add .gitignore
git commit -m "remove node_modules"
git push
```

### Check everything is installed
```powershell
git --version && node --version && python --version
```

---

*Advanced CLI Handbook — Windows Edition · May 2026*
*Plain English → Command → What It Does*
