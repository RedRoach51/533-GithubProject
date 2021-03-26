import requests;
import json;
import os;
#import github;
#import datetime;
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

#some resources for reference:
#https://stackoverflow.com/questions/27931139/how-to-use-github-v3-api-to-get-commit-count-for-a-repo

# Make sure to set your own GITHUBTOKEN env key!
token = os.getenv('GITHUBTOKEN')


def getGithubCommits(repo = "SSW-567-HW04", user = "redroach51"):
    commits_orig = requests.get("https://api.github.com/repos/" + user + "/" + repo + 
                                    "/commits?simple=yes&per_page=100&page=1",
                                headers={"Authorization": token})
    commits = commits_orig.json();
    total_commits = len(commits)
    
    while 'next' in commits_orig.links.keys():
        commits_orig = requests.get(commits_orig.links['next']['url'],
                        headers={"Authorization": token})
        commits.extend(commits_orig.json())
 
    total_commits = len(commits)
    
    output(commits);
    return len(commits);

def output(json_object):
   with open('TempOutput.txt','w') as outfile:
       json.dump(json_object,outfile)

def main():
    user_name = input("Input GitHub repo's owner: ")
    user_repo = input("Input GitHub repo's name: ")
    if (user_name == "" or user_repo == ""):
        print("Default test API set to creator RedRoach51's host repo.")
        user_name = "redroach51"
        user_repo = "SSW-567-HW04"
    commits = getGithubCommits(user_repo,user_name)
    print(user_repo + " Commits: " + str(commits))

if __name__ == '__main__':
    main()