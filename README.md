# 533-GithubProject
The goal of this project is to see how the number of contributors to a software project affects the project's development. 

With the advent of more open development tools such as Git, the number of contributors to any one project can exceed some professional developer teams. This calls to mind an old saying: "Too many cooks spoil the pot." It may be that having open-source development contributed to by numerous developers of varying skills and experiences could actually harm development. This project analyzes the question of "How does the number of contributors affect a project's development?" by taking a number of statistics from several public repositories on Github.

A Python file is used to get the repositories from Github, calling Github repositories for a given repo to retrieve statistics about them.  

The measured statistics for each repository are:
* [✓] Number of Commits
* [✓] Average time between Commits
* [✓] Number of Contributors
* [✓] Number of Lurkers (< 10% of max contributor's commits)
* [✓] Repository file size
* Number of Repository releases
* Average time between Repository releases