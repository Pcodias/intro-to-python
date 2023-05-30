# Best practices for when you are working on exercises

## Shortcuts

### Commenting out shortcut:
- Select the lines you want to comment and press:
    - Windows: ```Ctrl + / ```
    - Mac: ```Command + /```


### Bash shortcuts
- TAB - autocompletes commands, file names, or directory names for you​.

- UP/DOWN Arrows - Scroll backward and forwards through previous commands you’ve typed in the current session. ​

- F3 - Repeat the previous command​.

- CTRL + C -  Abort the current line you’re typing or a command that is currently executing​.


---


## When you start:
First, make sure you are using the Shell 🐚 (not the console). 

While using the bash Shell, navigate the folders using the command-line and make sure you are in the same folder as the files you want to access. Ex: In order to access `exercises_1.py`, you have to be in `intro-to-python/session_01`.

Here are some CLI commands to help you out:

```bash
pwd # Prints to the console the path of your current working directory

ls # Lists the files in the directory you are in


cd <directory_name> # Gets in a given directory

cd .. # Gets out of the directory you are in

```

---

## How do you run a python file?
1. Make sure that you are using the Shell 🐚.
1. Verify that you are in the folder containing the file you want to run. You can use `pwd` to check the current folder and `ls` to see the files in the current folder.
2. Run `python <file_name.py>` (ex: `python exercises_1.py`).

---

## Before you go:

When you are done for the day, don't forget to commit and push your work using the git commands:

```shell

git add . # Adds ALL changes to the staging area in preparation for committing them to the repository.​

git commit -m "<Short description of what you have worked on.>" #  Saves changes to the local repository, along with your commit message, usually describing the changes.

git push origin main # Uploads local changes to your remote repository, on the main branch.
```