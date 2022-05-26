# General Git Snippets

## Unsorted

### Find Base Folder

```shell
git rev-parse --show-toplevel
```

### Branch names

```shell
git branch
```

#### options

- add `-r` to only get remote branches
- add `-a` to get remote and local branches

### Delete Branch

#### locally

```shell
git branch -d [branch_name]
```

#### options

- replace `-d` with `-D` to force deletion. `-d` fails if the branch has not been pushed.

#### remote

```shell
git push -d [origin] [branch_name]
```

### Branch info

```shell
git show [OPTIONAL: branch_name]
```

### ASCII Tree

```shell
git log --graph --oneline
```

#### options

- add `-all` to get the tree of all branches

### Backup

```shell
git bundle create <file_name or file_path>.bundle --all
```
