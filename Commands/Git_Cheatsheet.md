## Git & Github

### Introduction of Git    
   
`Git` is a version control system for tracking changes in computer files and cordinating work on those files among multiple people.
  
`Github` is a provider of Internet hosting for software deveploment and version control using Git. It offers the distributed version control and source code managementfunctionality of Git.

`Bitbucket` is a Git based source code repository hosting service. Bitbucked offers both commercial plans and tree accounts with an unlimited number of private repositories.
 
`Gitlab` is a open - core company that provides Gitlab a DevOps software package that combines the ability to develop, secure, and operate software in a single applacation. 

### Your Identity
   
Configuring Name & Email in Git
   
`git config` that lets you get and set configuration variables that control all aspects of how Git looks and operates.

The first thing you should do when you install Git is to set your username and email address.

`git config --global user.name "Username"` &&
`git config --global user.email "Email"`

you need to do this only if you pass the "--global" option,
because then Git will always use that infomation for anything
you do on that system.
  
Checking the Username & Email:
    
`git config --global user.name` &&
`git config --global user.email`

### Initializing Git Repository or Reinitializing an exiting one 
    
`git init` - create an empty Git repository or reinitialize an exiting one.
   
Description
    
This command creates an empty Git repository basically a `.git` directory with subdirectories for object, `refs/heads`, `refs/tags`, and template files.

**Setup for SSH for Git**
     
`ssh-keygen` - you can create a new public and private key pair with the following command, Enter and re-enter a passphrase when prompted, or leave it empty.

`eval "$(ssh-agent -s)"` - Add you SSH key to the ssh-agent. Notice that you'll need to replace id_rsa in the command with the name of your private key file
     
`ssh-add ~/.ssh/id_rsa`  - Key

**check online** : [Connecting to Github with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

    
### Staging Area

Unlike the other systems, Git has something called the `staging area` or `index`. This is an intermediate area where commits can be formatted and reviewed before completing the commit. 
Working Directory > UnModified > Modified > Staging Area > Remote Repository .

### Git Add Command
   
The `git add` command adds content from the working directory
into the staging area (or “index”) for the next commit. 
When the git commit command is run, by default it only looks
at this staging area, so git add is used to craft what 
exactly you would like your next commit snapshot to look like.
   
`git add -A` - stages all

`git add .` - stages new and modified, without deleted
  
`git add -u` - stages modified and deleted,without new

### Git Checkout Command

Updates files in the working tree to match the version in the index or the specified tree. If no pathspec was given, git checkout will also update HEAD to set the specified branch as the current branch.
  
`git checkout` - switch branches or restore working tree files
  
`git checkout -f` - all

### Git Logs Command 
 
List commits that are reachable by following the parent links from the given commit(s), but exclude commits that are reachable from the one(s) given with a ^ in front of them. The output is given in reverse chronological order by default

`git log` - show commit logs

`git log -p` -( number of commit) - to see recently commits

### Git Diff Command

Show changes between the working tree and the index or a tree, changes between the index and a tree, changes between two trees, changes resulting from a merge, changes between two blob objects, or changes between two files on disk.

`git diff` - show changes between commits,commit and working tree, etc

`git diff --staged` - comparing working to staging area

### Removing File

The  `git rm` command is used to remove files from the staging area and working directory for Git. It is similar to git add in that it staged a removal of a file for the next commit
   
`git rm (filename)` - Remove files from the working tree and from the staging area
   
`git rm --cached (filename)` - File only remove from staging area

### Checking Status
    
Displays paths that have differences between the index file and the current HEAD commit, paths that have differences between the working tree and the index file, and paths in the working tree that are not tracked by Git (and are not ignored by gitignore).
   
`git status` - Show the working tree status

`git status -s` - short for git status
    
### Ignoring files and directory
  
A `.gitignore` file specifies intentionally untracked files that Git should ignore. Files already tracked by Git are not affected; see the NOTES below for details.
    
`gitignore` - Specifies intentionally untracked files to ignore

### Branches 
 
A branch represents an independent line of development. Branches serve as an abstraction for the edit/stage/commit process. You can think of them as a way to request a brand new working directory, staging area, and project history. New commits are recorded in the history for the current branch, which results in a fork in the history of the project.
    
`git branch --list` - Listing a branches

`git branch (branch_name)` - Creating a branch
    
`git branch -d (branch_name)` - Deleting a branch

### Github 

GitHub, Inc. is a provider of Internet hosting for software development and version control using Git. It offers the distributed version control and source code management (SCM) functionality of Git, plus its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, continuous integration, and wikis for every project.

### Remote Repository
   
Remote repositories are versions of your project that are hosted on the Internet or network somewhere. You can have several of them, each of which generally is either read-only or read/write for you.

### Pushing repo from local repository to remote repository
 
The `git push` command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo.

`git push` (origin master) -  origin is by default remote and master is by default branch

### Pulling repo form remote repository to local repository
 
The `git pull` command is used to fetch and download content from a remote repository and immediately update the local repository to match that content.    
    
`git pull` - by default

### Cloning repo 
    
The `git clone` command is used to copy an existing Git repository from a server to the local machine.
