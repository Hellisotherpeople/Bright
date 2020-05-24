# Bright
Measure how bright your github repo shines, and learn about interesting work that the people who were (or could have been) inspired by your repo have done

# What is Bright? 
It searches through all of the people who starred a particular repo, then looks at how many stars each of their repos have. It sums the total number of stars from each user to compute a "Brightness" score for a repo. It also creates a tree for visualizing what repos that your stargazers have made and which of those repos have a lot of stars. 

The intuition behind this is that a user who has a cumulative 1000 github stars is likely more experienced and knowledgable than a user with 0 github stars. Repositories which have thousands of stars from fake bot accounts (whose accounts would have 0 cumulative stars) would have a brightness score of zero, but a repository which seems unimportant but had a highly experienced developer star it would have a high brightness score. 

There is a tunable option for only visualizing other peoples repos who has more than `cut_off_number` number of stars. This defaults to 1

# Install Instructions

1. Clone the repo 
2. type `pip install -r requirements.txt`or `pip3 install -r requirments.txt` as needed. 
3. run the script as follows: `python3 github_bright.py <github_username> <github_password> <repo_name> <cut_off_number>`

Replace each bracketed expression with the corresponding string, the `cut_off_number` is optional.

Sample:
`python3 github_bright.py ghub_user ghub_pass Hellisotherpeople/Python-Cooperative-Synapse-NeuroEvolution 0`

# Example
