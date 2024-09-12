+++
title = "serene theme test"
date = 2024-09-12
description = "random content"
draft = true

[taxonomies]
tags = ["general"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++
Trying out a set of theme features.

# Callouts
{% note(header="Note") %}
note text
{% end %}

{% important(header="Note") %}
important text
{% end %}

# Code snippets
## rust
```rust,linenos,linenostart=20
use highlighter::highlight;
let code = "...";
highlight(code);
```

## python
```python,linenos,hl_lines=1 4-5 7
import sys
import time

code = "..."
for i in code:
    print(code)
    time.sleep(1)
sys.exit(0)
```
