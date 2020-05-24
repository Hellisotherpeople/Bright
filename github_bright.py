from github import Github
from treelib import Node, Tree
from treelib.exceptions import DuplicatedNodeIdError
import sys

##TODO: Make a way nicer dendogram visualization... 

##Example repo name: "Hellisotherpeople/Active-Explainable-Classification"


tree = Tree()

g = Github(sys.argv[1], sys.argv[2]) ## username and password


def get_starrgazers_for_repo(repo_name, star_cutoff = 1):
    print("Analyzing " + repo_name)
    print("---------------------------------------------------------------------------------")
    repo = g.get_repo(repo_name) ## start with a repo 
    stargazers = repo.get_stargazers() ## get the people who starred it
    total_stars = 0
    tree.create_node(repo_name, repo_name.lower()) ##Root node should be the repo
    for user in stargazers:
        if user.name is not None:
            tree.create_node(user.name, user.name.lower(), parent=repo_name.lower())
            repos = user.get_repos(type = "owner") ## get the user repos
            user_stars = 0 
            for repo in repos:
                total_stars += repo.stargazers_count 
                user_stars += repo.stargazers_count
                if repo.stargazers_count >= star_cutoff:
                    repo_with_stars = repo.name + " " + str(repo.stargazers_count) + " " + str(repo.html_url) 
                    try:
                        tree.create_node(repo_with_stars, repo.name.lower(), parent = user.name.lower())
                    except DuplicatedNodeIdError:
                        pass                        
            print(user.name + " Total Stars: " + str(user_stars))
    print("---------------------------------------------------------------------------------")
    print('\x1b[6;30;42m' + "Brightness Score (Total Stars): " + str(total_stars) + '\x1b[0m')
    tree.show(line_type="ascii-em")
    print('\x1b[6;30;42m' + "Brightness Score (Total Stars): " + str(total_stars) + '\x1b[0m') ## do the print at the bottom again so that it's obvious right at the end after a giant tree is generated

if len(sys.argv) > 4:
    stargazers = get_starrgazers_for_repo(sys.argv[3], int(sys.argv[4]))
else:
    stargazers = get_starrgazers_for_repo(sys.argv[3])

