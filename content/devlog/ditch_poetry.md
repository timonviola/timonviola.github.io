+++
title = "Why am I ditching Poetry?"
date = 2024-11-24
description = "Motivation to change Python workflow from Poetry."

[taxonomies]
tags = ["python", "rant"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++
`TL;DR; switch to Hatch+uv, pip is the best.`

I like writing code. I don't like to relearn package managers, neither do I want to make a hobby out of learning a new one every year.

This is a short rant on why I am starting all my new Python projects with [Hatch 🐣](https://github.com/pypa/hatch) instead of [Poetry](https://github.com/python-poetry/poetry).

# why poetry
I started using Poetry when it was around `v0.4.0`. It was the first package manager which I started using after pip and it had some awesome benefits:
- virtual environment handling
- lock file

(The CLI was never intuitive to me.)

# reasons to switch
## environment isolation
The `venv` switching was never seamless. Countless times I ended up debugging a `virtual environment`. Time after time I need to manually destroy Poetry's `venv`s and completely rebuild the environment.

## speed
I work daily with a large project (600+ dependencies), let's call the project Apache Airflow.

Building the base Airflow image, with constraints file respected it takes somewhere around `600 sec` to build it. That is a lot of time.

```bash
🎄 airflow ❯ poetry lock
Updating dependencies
Resolving dependencies... (71.3s)

Writing lock file
```

## ease of use
I spent my fair share of time explaining Poetry. Maybe it was a mistake moving away from *low-tech* `pip` and `virtualenv`.

# the alternative
## speed
I start all my new projects with Hatch and [uv](https://docs.astral.sh/uv/) build backend. The comparison of the two tools/workflows are quite unfair, I am ditching the lock file as well.

However, I can build Apache Airflow in `5 sec` range. In the below case, it's a `30x` speed up.

```bash
🎄 airflow ❯ uv pip install --constraint constraints.txt -r requirements.txt
Resolved 203 packages in 1.96s
```

## environment isolation
I can isolate my `docs`, `tests` and other environments instead of relying on `dependency groups`.

## ease of use
To me, the simplicity of Hatch and the speed of uv are finally making it worthwhile to switch. After 6 years of Poetry, I have no regrets, switching it.

I don't like going back to projects, where poetry is used, but there is no value in switching if your dependencies resolve fast enough and CD pipelines perform reasonably.


# the future
`pip` is king. Luckily uv support most of the commands, so it makes it extremely easy to switch to `uv pip` If you are new to Python packaging, library development - get familiar with `pip` commands first and then the tools on top of it. The [packaging user guide](https://packaging.python.org/en/latest/) is really well written.

I will consider switching from hatch if there will be a [`cargo`](https://github.com/rust-lang/cargo) like tool for python.

