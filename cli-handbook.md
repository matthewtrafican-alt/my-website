# Advanced CLI Handbook — Windows (PowerShell & CMD)
> Covering: Shell & File System · Git & Version Control · Dev Tools (Node, Python, Docker)

---

## Table of Contents
1. [PowerShell vs CMD — When to Use What](#powershell-vs-cmd)
2. [Navigation & File System](#navigation--file-system)
3. [File Operations](#file-operations)
4. [Text & Output Manipulation](#text--output-manipulation)
5. [Environment Variables](#environment-variables)
6. [Processes & System](#processes--system)
7. [Networking](#networking)
8. [Scripting & Automation](#scripting--automation)
9. [Git & Version Control](#git--version-control)
10. [Node.js & npm](#nodejs--npm)
11. [Python & pip](#python--pip)
12. [Docker](#docker)
13. [Tips, Tricks & Power Moves](#tips-tricks--power-moves)

---

## PowerShell vs CMD

| Feature | PowerShell | CMD |
|---|---|---|
| Objects | Yes (rich .NET objects) | No (plain text) |
| Scripting | `.ps1` scripts | `.bat` / `.cmd` scripts |
| Piping | Objects between cmdlets | Text only |
| Use case | Modern dev, automation | Legacy, quick tasks |
| Launch | `pwsh` or `powershell` | `cmd` |

**Rule of thumb**: Use PowerShell for everything new. Use CMD only for legacy batch scripts or when PS isn't available.

---

## Navigation & File System

```powershell
# Print current directory
pwd                         # PowerShell
cd                          # CMD (no args shows current path)

# Change directory
cd C:\Users\You\Projects
cd ..                       # Go up one level
cd ..\..                    # Go up two levels
cd ~                        # Home directory (PowerShell)
cd /                        # Root of current drive

# List files
ls                          # PowerShell alias (like Unix)
dir                         # CMD and PowerShell
Get-ChildItem               # Full PowerShell cmdlet
ls -Force                   # Show hidden files
ls -Recurse                 # Recursive listing
ls *.txt                    # Filter by extension
ls | Sort-Object LastWriteTime  # Sort by date modified

# Change drives
D:                          # Switch to D drive
cd D:\Projects              # Switch drive and path

# Open Explorer in current directory
explorer .
```

---

## File Operations

```powershell
# Create files and directories
New-Item file.txt           # Create empty file (PS)
New-Item -ItemType Directory myfolder  # Create directory
mkdir myfolder              # Shortcut (works in PS and CMD)
echo "" > file.txt          # Quick file create (CMD style)
ni file.txt                 # Alias for New-Item

# Copy
Copy-Item file.txt backup.txt           # PS
copy file.txt backup.txt                # CMD
Copy-Item -Recurse src\ dst\            # Copy folder recursively
cp -r src/ dst/                         # Unix-style alias (PS)

# Move / Rename
Move-Item old.txt new.txt               # Move or rename (PS)
move old.txt new.txt                    # CMD
Rename-Item file.txt renamed.txt        # Explicit rename

# Delete
Remove-Item file.txt                    # PS
Remove-Item -Recurse -Force myfolder\   # Delete folder + contents
del file.txt                            # CMD
rmdir /s /q myfolder                    # CMD recursive delete

# Read file contents
Get-Content file.txt                    # PS (like cat)
cat file.txt                            # PS alias
type file.txt                           # CMD
Get-Content file.txt -Tail 20           # Last 20 lines
Get-Content file.txt -Wait              # Live tail (like tail -f)

# Write to file
"Hello World" | Out-File file.txt       # Write (overwrites)
"Hello World" | Add-Content file.txt    # Append
"Hello" > file.txt                      # Redirect (overwrites)
"Hello" >> file.txt                     # Redirect (append)

# Search in files
Select-String "pattern" file.txt        # Like grep (PS)
Select-String -Recurse "TODO" *.js      # Recursive grep
findstr "pattern" file.txt              # CMD equivalent

# File info
Get-Item file.txt | Select-Object *     # Full file metadata
(Get-Item file.txt).Length              # File size in bytes
```

---

## Text & Output Manipulation

```powershell
# Piping (chain commands)
ls | Where-Object { $_.Length -gt 1MB }        # Files > 1MB
ls | Select-Object Name, Length | Sort-Object Length -Descending
Get-Content log.txt | Select-String "ERROR"

# Count lines / items
(Get-Content file.txt).Count            # Line count
ls | Measure-Object                     # Count files

# Format output
ls | Format-Table Name, Length, LastWriteTime   # Table view
ls | Format-List                                # List view
ls | ConvertTo-Json                             # JSON output
ls | Export-Csv output.csv -NoTypeInformation   # CSV export

# Redirect output
command > output.txt                    # Stdout to file
command 2> errors.txt                   # Stderr to file
command > out.txt 2>&1                  # Both to same file
command | Tee-Object output.txt         # Print AND save

# String operations
"hello world".ToUpper()
"  trim me  ".Trim()
"a,b,c" -split ","                      # Split string
"hello" -replace "ell","ELL"            # Replace in string

# Filter and search
ls | Where-Object Name -like "*.log"
ls | Where-Object LastWriteTime -gt (Get-Date).AddDays(-7)  # Modified last 7 days
```

---

## Environment Variables

```powershell
# View variables
$env:PATH                               # Print PATH
$env:USERNAME                           # Current user
Get-ChildItem Env:                      # List ALL env vars
[System.Environment]::GetEnvironmentVariables()  # Full list

# Set (current session only)
$env:MY_VAR = "hello"
$env:PATH += ";C:\new\path"            # Append to PATH

# Set permanently (user-level)
[System.Environment]::SetEnvironmentVariable("MY_VAR","value","User")

# Set permanently (system-level, requires admin)
[System.Environment]::SetEnvironmentVariable("MY_VAR","value","Machine")

# Delete variable
Remove-Item Env:MY_VAR

# CMD equivalents
set                                     # List all
set MY_VAR=hello                        # Set (session)
setx MY_VAR "hello"                     # Set permanently (user)
echo %MY_VAR%                           # Read in CMD
```

---

## Processes & System

```powershell
# List processes
Get-Process                             # All processes
Get-Process chrome                      # Filter by name
Get-Process | Sort-Object CPU -Desc | Select-Object -First 10  # Top 10 by CPU

# Kill processes
Stop-Process -Name chrome               # Kill by name
Stop-Process -Id 1234                   # Kill by PID
taskkill /F /IM chrome.exe             # CMD forceful kill
taskkill /F /PID 1234

# System info
systeminfo                              # Full system info
Get-ComputerInfo                        # PS system info
hostname                                # Computer name
whoami                                  # Current user

# Services
Get-Service                             # List services
Start-Service wuauserv                  # Start Windows Update
Stop-Service wuauserv
Restart-Service wuauserv

# Disk usage
Get-PSDrive                             # Drive usage summary
Get-ChildItem -Recurse | Measure-Object -Sum Length  # Folder size

# Check what's using a port
netstat -ano | findstr :3000            # Who's on port 3000
Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess
```

---

## Networking

```powershell
# Basic connectivity
ping google.com
ping -n 4 google.com                    # 4 pings only
tracert google.com                      # Trace route
nslookup google.com                     # DNS lookup
Resolve-DnsName google.com              # PS DNS lookup

# HTTP requests (PowerShell)
Invoke-WebRequest https://api.example.com           # Like curl
(Invoke-WebRequest https://api.example.com).Content # Just body
Invoke-RestMethod https://api.example.com/data      # Auto-parse JSON
curl https://api.example.com                        # If curl installed

# Download files
Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile "file.zip"
curl -o file.zip https://example.com/file.zip

# Network info
ipconfig                                # IP addresses
ipconfig /all                           # Full network details
ipconfig /flushdns                      # Flush DNS cache
Get-NetIPAddress                        # PS network addresses
netstat -an                             # Active connections

# Firewall
Get-NetFirewallRule                     # List rules
New-NetFirewallRule -DisplayName "App" -Direction Inbound -Port 8080 -Action Allow
```

---

## Scripting & Automation

```powershell
# PowerShell script basics (.ps1)

# Variables
$name = "World"
$count = 42
$items = @("a", "b", "c")              # Array
$map = @{ key = "value" }              # Hashtable

# Conditionals
if ($count -gt 10) {
    Write-Host "Big number"
} elseif ($count -eq 10) {
    Write-Host "Exactly ten"
} else {
    Write-Host "Small number"
}

# Comparison operators
# -eq  -ne  -gt  -lt  -ge  -le
# -like  -match  -contains  -in

# Loops
foreach ($item in $items) { Write-Host $item }
for ($i = 0; $i -lt 10; $i++) { Write-Host $i }
1..10 | ForEach-Object { Write-Host $_ }
while ($true) { break }

# Functions
function Greet($name) {
    return "Hello, $name!"
}
Greet "Alice"

# Error handling
try {
    Get-Item "nonexistent.txt" -ErrorAction Stop
} catch {
    Write-Host "Error: $_"
} finally {
    Write-Host "Always runs"
}

# Running scripts
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned  # Allow scripts
.\myscript.ps1
powershell -File myscript.ps1

# Profiles (run on PS startup)
notepad $PROFILE                        # Edit your profile
```

---

## Git & Version Control

```powershell
# Setup
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"   # VS Code as editor
git config --list                               # View all config

# Initialize & clone
git init                                # New repo in current folder
git clone https://github.com/user/repo.git
git clone https://... myfolderName      # Clone to custom folder

# Status & history
git status                              # Current state
git log                                 # Commit history
git log --oneline --graph               # Visual branch graph
git log --oneline -10                   # Last 10 commits
git diff                                # Unstaged changes
git diff --staged                       # Staged changes
git diff main..feature                  # Branch comparison

# Staging & committing
git add file.txt                        # Stage one file
git add .                               # Stage all changes
git add -p                              # Interactive stage (chunk by chunk)
git commit -m "Your message"
git commit -am "Stage + commit tracked files"
git commit --amend --no-edit            # Amend last commit (keep message)

# Branches
git branch                              # List branches
git branch -a                           # All branches (including remote)
git branch feature/login               # Create branch
git checkout feature/login             # Switch branch
git switch feature/login               # Modern switch
git checkout -b feature/login          # Create + switch
git switch -c feature/login            # Modern create + switch
git branch -d feature/login            # Delete merged branch
git branch -D feature/login            # Force delete

# Merging & rebasing
git merge feature/login                # Merge into current branch
git merge --no-ff feature/login        # Always create merge commit
git rebase main                        # Rebase current branch onto main
git rebase -i HEAD~3                   # Interactive rebase last 3 commits
git cherry-pick abc1234                # Apply specific commit

# Remote
git remote -v                          # List remotes
git remote add origin https://...      # Add remote
git fetch                              # Download without merging
git pull                               # Fetch + merge
git pull --rebase                      # Fetch + rebase (cleaner)
git push origin main
git push -u origin feature/login       # Push + track upstream
git push --force-with-lease            # Safe force push

# Stashing
git stash                              # Stash changes
git stash save "WIP: login form"       # Named stash
git stash list                         # List stashes
git stash pop                          # Apply + remove latest
git stash apply stash@{2}              # Apply specific stash
git stash drop stash@{0}               # Delete a stash

# Undoing
git restore file.txt                   # Discard unstaged changes
git restore --staged file.txt          # Unstage a file
git reset HEAD~1                       # Undo last commit (keep changes)
git reset --hard HEAD~1                # Undo last commit (discard changes)
git revert abc1234                     # Safe undo via new commit
git clean -fd                          # Delete untracked files/folders

# Tags
git tag v1.0.0                         # Lightweight tag
git tag -a v1.0.0 -m "Release v1.0.0" # Annotated tag
git push origin --tags                 # Push all tags
```

---

## Node.js & npm

```powershell
# Version management
node --version
npm --version
npx --version

# Install nvm-windows for managing Node versions
# https://github.com/coreybutler/nvm-windows
nvm list                               # Installed versions
nvm list available                     # Available versions
nvm install 20.0.0                     # Install specific version
nvm use 20.0.0                         # Switch version
nvm current                            # Active version

# Project setup
npm init                               # Interactive setup
npm init -y                            # Auto-accept defaults
npm install                            # Install from package.json
npm install express                    # Add dependency
npm install -D jest                    # Add dev dependency
npm install -g nodemon                 # Global install
npm uninstall express
npm update                             # Update all packages

# Running scripts (from package.json)
npm start
npm test
npm run build
npm run dev

# Useful npm commands
npm list                               # Installed packages
npm list -g --depth=0                  # Global packages
npm outdated                           # Show outdated packages
npm audit                              # Security audit
npm audit fix                          # Auto-fix vulnerabilities
npm cache clean --force                # Clear cache
npm ci                                 # Clean install (for CI)

# npx — run without installing
npx create-react-app myapp
npx create-next-app@latest myapp
npx ts-node script.ts

# package.json scripts example
# {
#   "scripts": {
#     "start": "node server.js",
#     "dev": "nodemon server.js",
#     "build": "tsc",
#     "test": "jest --watch"
#   }
# }

# pnpm (faster alternative to npm)
npm install -g pnpm
pnpm install
pnpm add express
pnpm run dev
```

---

## Python & pip

```powershell
# Check versions
python --version
python3 --version
pip --version

# Virtual environments (ALWAYS use these)
python -m venv venv                    # Create virtualenv
.\venv\Scripts\activate                # Activate (Windows)
deactivate                             # Deactivate

# With Poetry (recommended for modern projects)
pip install poetry
poetry new myproject
poetry install
poetry add requests
poetry add --dev pytest
poetry run python script.py
poetry shell                           # Activate venv

# pip basics
pip install requests                   # Install package
pip install requests==2.28.0           # Specific version
pip install -r requirements.txt        # Install from file
pip uninstall requests
pip list                               # Installed packages
pip show requests                      # Package details
pip freeze > requirements.txt          # Export dependencies
pip install --upgrade pip              # Update pip itself

# Running Python
python script.py
python -m module_name                  # Run as module
python -c "print('hello')"             # One-liner
python -i script.py                    # Interactive after running

# Common tools
pip install black                      # Code formatter
pip install flake8                     # Linter
pip install mypy                       # Type checker
pip install pytest                     # Test runner
pytest                                 # Run tests
pytest -v                              # Verbose
pytest tests/test_auth.py             # Specific file
pytest -k "test_login"                 # Filter by name

# pyenv-win (Node version manager equivalent)
# Install from https://github.com/pyenv-win/pyenv-win
pyenv install 3.12.0
pyenv global 3.12.0
pyenv local 3.11.0                     # Per-project version
```

---

## Docker

```powershell
# Check Docker
docker --version
docker info
docker ps                              # Running containers
docker ps -a                           # All containers (including stopped)

# Images
docker images                          # List local images
docker pull nginx                      # Download image
docker pull node:20-alpine             # Specific tag
docker rmi nginx                       # Remove image
docker image prune                     # Remove dangling images
docker image prune -a                  # Remove all unused images

# Running containers
docker run nginx                       # Run (foreground)
docker run -d nginx                    # Detached (background)
docker run -d -p 8080:80 nginx         # Map port host:container
docker run -d -p 8080:80 --name myapp nginx  # Named container
docker run -it ubuntu bash             # Interactive terminal
docker run --rm ubuntu echo "hello"    # Auto-remove after exit
docker run -v C:\data:/app/data nginx  # Mount volume

# Container management
docker stop myapp
docker start myapp
docker restart myapp
docker rm myapp                        # Remove stopped container
docker rm -f myapp                     # Force remove running container
docker logs myapp                      # View logs
docker logs -f myapp                   # Follow logs (like tail -f)
docker exec -it myapp bash             # Shell into running container
docker exec myapp ls /app              # Run command in container
docker inspect myapp                   # Full container info
docker stats                           # Live resource usage

# Building images
docker build -t myapp:latest .         # Build from Dockerfile
docker build -t myapp:v1.0 -f custom.Dockerfile .
docker tag myapp:latest myapp:v1.0     # Add tag

# Docker Compose
docker-compose up                      # Start services
docker-compose up -d                   # Detached
docker-compose up --build              # Rebuild before starting
docker-compose down                    # Stop & remove containers
docker-compose down -v                 # Also remove volumes
docker-compose logs -f                 # Follow all logs
docker-compose ps                      # Service status
docker-compose exec app bash           # Shell into service
docker-compose build                   # Build images only

# Volumes
docker volume ls
docker volume create mydata
docker volume rm mydata
docker volume prune

# Networks
docker network ls
docker network create mynet
docker run --network mynet myapp

# Cleanup everything
docker system prune                    # Remove unused resources
docker system prune -a --volumes       # Nuclear cleanup (careful!)

# Dockerfile quick reference
# FROM node:20-alpine
# WORKDIR /app
# COPY package*.json ./
# RUN npm ci
# COPY . .
# EXPOSE 3000
# CMD ["node", "server.js"]
```

---

## Tips, Tricks & Power Moves

### PowerShell Profile
```powershell
# Edit your profile (~\.config\powershell\profile.ps1 or similar)
notepad $PROFILE

# Useful profile additions:
Set-Alias g git
Set-Alias k kubectl
function proj { cd C:\Users\You\Projects\$args }
function gs { git status }
function glog { git log --oneline --graph -20 }
```

### Useful Shortcuts
| Shortcut | Action |
|---|---|
| `Tab` | Autocomplete |
| `Ctrl+R` | Reverse history search |
| `Ctrl+C` | Kill current command |
| `Ctrl+L` | Clear screen |
| `Up/Down` | Navigate history |
| `Alt+.` | Insert last argument (PS) |

### Finding Things Fast
```powershell
# Find files
Get-ChildItem -Recurse -Filter "*.log"
Get-ChildItem -Recurse | Where-Object Name -like "*config*"

# Find command history
Get-History
Get-History | Select-String "git"      # Search history

# Where is a command?
Get-Command node                       # Find executable
(Get-Command node).Source              # Full path
where.exe node                         # CMD equivalent
```

### Working Smarter
```powershell
# Chain commands
cd myproject; npm install; npm run dev   # Run sequentially
npm run build && npm start               # Run second only if first succeeds
npm run build || echo "Build failed"     # Run second only if first fails

# Background jobs (PS)
Start-Job { npm run build }
Get-Job
Receive-Job 1

# Measure execution time
Measure-Command { npm run build }

# Clipboard
"text" | Set-Clipboard                 # Copy to clipboard
Get-Clipboard                          # Paste from clipboard
cat output.txt | clip                  # CMD: copy file to clipboard

# Common aliases to know
ls = Get-ChildItem
cat = Get-Content  
rm = Remove-Item
cp = Copy-Item
mv = Move-Item
echo = Write-Output
pwd = Get-Location
clear = Clear-Host
```

---

*Generated for Windows PowerShell / CMD — May 2026*
