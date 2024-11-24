+++
title = "Why am I ditching Poetry?"
date = 2024-11-24
description = "Motivation to change Python workflow from Poetry."
draft = true

[taxonomies]
tags = ["python"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++
I like writing code and if I have to wrestle with my build tool/package manager, that's valuable development time wasted. This is a short rant on why I am starting all my new Python projects with [Hatch 🐣](https://github.com/pypa/hatch) instead of [Poetry](https://github.com/python-poetry/poetry).

# ease of use
Countless times I ended up debugging a my or a colleagues `virtual environment`. I am not sure why, but time after time I need to manually destroy Poetry's `venv`s.

Broken package installations, breaking changes - I need something simpler.

# speed
I work daily with Apache Airflow, this means custom OCI/Docker file and building the image in CI/CD.

Building the base Airflow image, with constraints file respected it takes somewhere around `600 sec` to build it. That is a lot of time.

# the alternative
I start all my new projects with Hatch and [uv](https://docs.astral.sh/uv/) build backend. The comparison of the two tools/workflows are quite unfair, I am ditching the lock file as well.

However, I can build Apache Airflow in `50 sec` range.

I can isolate my `docs`, `tests` and other environments instead of relying on `dependency groups`.

To me, the simplicity of Hatch and the speed of uv are finally making it worthwhile to switch. After 6 years of Poetry, I have no regrets (so far), switching it.

# one last thing
`pip` is king. Pip is the go-to tool, no matter what. Luckily uv support most of the commands, so it makes it extremely easy to swith to `uv pip` If you are new to Python packaging, library development - consider learning `pip` API first and then the tools on top of it.

`uv` might become a game changer, when/if it becomes a cargo like tool, I will switch again, probably.


