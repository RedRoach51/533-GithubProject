import requests;
import json;

#some resources for reference:
#https://stackoverflow.com/questions/27931139/how-to-use-github-v3-api-to-get-commit-count-for-a-repo


def getGithubCommits(repo = "SSW-567-HW04", user = "redroach51"):
    commits = requests.get("https://api.github.com/repos/"+ user + "/" + repo + "/commits")
    commits = commits.json();
    return len(commits);

def main():
    user_name = input("Input GitHub repo's owner: ")
    user_repo = input("Input GitHub repo's name: ")
    if (user_name == "" or user_repo == ""):
        print("Default test API set to creator RedRoach51's host repo.")
        user_name = "redroach51"
        user_repo = "SSW-567-HW04"
    commits = getGithubCommits(user_repo,user_name)
    print(user_repo + ", Commits: " + str(commits))

if __name__ == '__main__':
    main()