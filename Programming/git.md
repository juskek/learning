
### Git hangs after writing objects and never pushes to origin
https://stackoverflow.com/questions/15843937/git-push-hangs-after-total-line

1. git config --global http.postBuffer 157286400
2. git commit and push
3. git config --global http.postBuffer 1048576


## Squash up to a certain commit 
```
git reset --soft HEAD~3
OR
git reset --soft <commit_hash>

git commit
```
## Squash all commits on current branch into one
- WARNING: squashes ALL commits including the original branch commits the current branch was created from.
- Check git log 
```
git reset $(git commit-tree HEAD^{tree} -m "A new start")
```


Semantic Versioning
https://semver.org/