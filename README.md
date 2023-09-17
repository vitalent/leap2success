
# Git push without commit history

git checkout --orphan new-branch
git add -A
git commit -am "Initial commit"
git branch -D main
git branch -m main

git push -f origin main

# Github > Settings > Branches 
click "add branch protection rule"
add main
add master