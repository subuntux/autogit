#!/usr/bin/env python3

import os 
import subprocess
import sys 
import getpass

banner = """
[Auto Git, Git Client [v.1.0]]
[subuntux 2024]
"""

def function(argument):
    
    if argument == '--help':
        print_help()
    elif argument == '--h':
        print_help()
    elif argument == '--gh-push':
        gh_push()
    elif argument == '--re-push':
        re_push()
    elif argument == '--push':
        push()
    elif argument == '--git':
        subprocess.run(["pkg", "install", "git", "-y"])
    elif argument == '--gh':
        subprocess.run(["pkg", "install", "gh", "-y"])
    else:
        print_help()
        
def print_help():
    print(banner)
    print("Usage")
    print("autogit --help or --h for help")
    print("autogit --gh-push after using gh")
    print("autogit --re-push for push an reinit repository")
    print("autogit --push every time after --gh-push and/or --re-push")
    print("autogit --git for download git")
    print("autogit --gh for download gh")
    
def gh_push():
    name = input("Username-| ")
    mail = input("E-Mail-| ")
    
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "config", "--global", "user.email", f'"{mail}"'])
    subprocess.run(["git", "config", "--global", "user.name", f'"{name}"'])
    subprocess.run(["git", "checkout", "-b",  "main"])
    subprocess.run(["git", "commit", "-m", "create"])
    subprocess.run(["git", "push", "--set-upstream", "origin", "main"])
    subprocess.run(["git", "push", "-u", "origin"])
    
def re_push():
    name = input("Username-| ")
    token = getpass.getpass("Token-| ")
    repo = input("Repo-| ")
    
    url = f"https://{name}:{token}@github.com/{name}/{repo}"
    
    subprocess.run(["git", "init"])
    subprocess.run(["git", "remote", "set-url", "origin", url])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "update"])
    subprocess.run(["git", "push", "-u", "origin"])
    
def push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "update"])
    subprocess.run(["git", "push", "-u", "origin"])
    
if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Only one arg")
        sys.exit(1)
        
argument = sys.argv[1]
function(argument)