---
layout: post
title:  "Bash Shell For Working"
date:   2022-05-30
categories: unknown
author: ntnhaatj
tags: work unix
---

# Settings rc files
```sh
# .zshrc, .bashrc
$ cat .zshrc

# add identify key to ssh client
ssh-add ~/.ssh/ntnhaatj >/dev/null 2>&1

# alias to search service logs
alias s=journalclt | grep ssh
```

# vim
### Display
- `:set hlsearch` - highlight any matched from searching
- `:nohlsearch` - disable highlight
- `:set number` - show line number
- `:set relativenumber` - show relative line number with cursor
- set default settings
```sh
$ cat ~/.vimrc 
set number
set relativenumber
set hlsearch
```

### Navigation
- by word: `W, E, B, Option + nav`
- by line: 
    - `0` - start
    - `$` - end
    - `:<linenumber>` - go to line number
- by file:
    - `gg` - start of file
    - `G` - end of file 

### Editing
- `u` undo
- `^r` redo
- `5dd` delete 5 lines
- `yy` - copy line, `dd` - cut line, `p` - paste, `vy` - enter visual block and copy
- `:%s/foo/bar/g` - globally replace foo to bar 

### Searching
- `/str` - search str, `n` - next match, `N` - next match in opposite direction

### Windows
- `^wn` - new window, `:w <name>` - save new file as name
- `^wj` or `^wk` - switch among windows


# Useful Unix commands for ETL pipeline
### awk
- scan file by lines
- output matched pattern
- useful for transforming structured data from stdin

```sh
# output all USER, PID of processes
$ ps aux | awk '{print $1,$2}'
```

### uniq combine with sort
- to aggregate (count) the unique values

```sh
$ ps aux | \
    awk '{print $1}' | \    # get the first column from stdin
    sort | \                # sort alphabetically
    uniq -c                 # count two adjacent lines are the same
```
