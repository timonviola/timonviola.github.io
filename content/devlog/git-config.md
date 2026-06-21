+++
title = "gitconfig gems"
date = 2025-06-23
description = "A not so simple gitconfig"
draft = false

[taxonomies]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++
my gitconfig is not the simplest and I use some lesser known gems:
- multiple files with `IncludeIf` directive to set up *overlays*
```config
[includeIf "gitdir:~/pumba/"]
    path = .gitconfig-overlay
```

So everytime I work on something under `~/pumba/`, I have git configured for those projects in a different manner.

## Why?
Github does not allow you to have multiple e-mails/profiles configured.

`.gitconfig`
```config
[user]
    name = Timon Viola
    email = timon@timon.com
```

`.gitconfig-overlay`
```config
[user]
    name = Timon
    email = pumba@pumba.org
    signingkey = 1234ABCD

[commit]
    gpgsign = true
```


