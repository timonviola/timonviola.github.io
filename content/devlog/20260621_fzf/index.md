+++
title = "fzf everything"
date = 2026-06-21
description = "Use fzf for everything"
draft = false

[taxonomies]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++

Lately I have been using [`fzf`](https://github.com/junegunn/fzf), a cli fuzzy finder, for more and more things. There are a plethora of really
complex examples, but I am more or less stuck at the stage where I write my own terminal
helpers and shell scripts.

One of the motivation was to reduce complexity, I rather use a 4 line shell script than
yet another full fledged `go` or `rust` ~~slop~~ tool. Below I am only showing the
`fzf` part of the scripts, there is usually some ceremony around them e.g. wrapping it
into a `function`.


{{ asciinema(src="cast.txt", autoPlay=true, loop=true, controls=false) }}

## dswitch
[Directory switch](https://github.com/timonviola/config/blob/df12e0d106ddedff8fc5276548f9b2ef4bcfd06d/scripts/dswitch). I have been using this handy little tool for years now. It allows you to hop into a `dir` in your filesystem quite easily.
```bash
selected=$(find ~/Documents ~/work -mindepth 1 -maxdepth 1 -type d | fzf)
```

## aswitch
[AWS context switch](https://github.com/timonviola/config/blob/df12e0d106ddedff8fc5276548f9b2ef4bcfd06d/scripts/aswitch). I use `aswitch` to switch between `aws` profiles:
```bash
selected=$(aws configure list-profiles | fzf)
```
## cswitch
[(Kubernetes) Context switch](https://github.com/timonviola/config/blob/df12e0d106ddedff8fc5276548f9b2ef4bcfd06d/scripts/cswitch) (kswitch is taken apperently, maybe I should just overwrite it):
```bash
kubectl config get-contexts -o=name | fzf | xargs -r kubectl config use-context
```

Some would prefer to switch the kube-context always together with the `aws` context,
quite a valid need, and easily doable with a simple shell script. Probably I will make
cook up a script to do this.

It's a lot of fun making these pickers, I also have a script to delete multiple git branches in one go. I should make one for switching/working with git-worktrees as well!
