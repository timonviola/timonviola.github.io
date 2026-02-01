+++
title = "Python Enums and Literals"
date = 2026-02-01
description = "Some thoughts on Enums vs Literals in Python 3.11+"
draft = false

[taxonomies]
tags = ["python"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++
C, Rust, TypeScript and almost all programming languages offer 'enums' as a way of expressing, that a variable can have a certain set of values. Python is no exception, [Enums](https://docs.python.org/3/library/enum.html) are supposed to fulfill the same purpose, but many times it is more practical to rely on [Literals](https://docs.python.org/3/library/typing.html#typing.Literal). At this point I am starting to think that Python's enums are the [coriander](https://www.britannica.com/story/why-does-cilantro-taste-like-soap-to-some-people) of Python. 

The type checker set-up:
- python 3.11+
- mypy with `strict` mode
- basedpyright with `strict` mode

Let's take a look at a use-case, where `StrEnum` and `Literal` can be directly compared:
```python
from enum import StrEnum, auto

class Environment(StrEnum):
    STAGING = auto()
    PRODUCTION = auto()

```

```python
from typing import Literal

EnvironmentProduction = Literal["PRODUCTION"]
EnvironmentStaging = Literal["STAGING"]
Environment = EnvironmentStaging | EnvironmentProduction
```

Enums have the advantage of
- runtime safety
- maintainability.

Parsing user input, API responses with an Enum, gives you a runtime error. With Literals, it will be just another string at runtime, and you may not notice the error until much later. Using static type checkers, as above, does help you mitigate this, but it is not the same as runtime safety.

Enums also help to avoid polluting the code with string literals. This helps avoid typos and makes refactoring easier (i.e. renaming). With Literals, you have to use `== "production"` and so on and perform a global search and replace, which is error-prone. I guess with LLMs and agentic coding, this is less of an issue, but still...

Another plus on maintainability is that, Enums do not let you inherit, but Literals do.


Alright, so looking at literals, I have to repeat the strings:
```python
def literal_function(this: Environment):
    match this:
        case "PRODUCTION":
            print("a")
        case "STAGING":
            print("b")
        case _:
            print("something else")
```
But with Enums, I can simply refer to the enum members:
```python
def enum_function(this: EnumEnvironment):
    match this:
        case EnumEnvironment.PRODUCTION:
            print("a")
        case EnumEnvironment.STAGING:
            print("b")
        case _:
            print("panic!")
```

I get
- proper LSP completion (not only 'Text')
- I can easily rename members with LSP rename action
- I can easily look for anything in the code that uses `EnumEnvironment.PRODUCTION` with LSP "find references", as opposed to literals, where I have to search for string occurrences.

The nice thing is that in both cases, mypy and pyright are able to check exhaustiveness of the match statement. They indicate, that the final `case _:` is unreachable code.[^1]


And adding a new member - let's say - `Test` to the variants, and removing the wildcard `case _:`, also works consistently in both cases. Nevertheless, I have to type out the new literal member on the 'case' again.[^2]
> 🛑 Cases within match statement do not exhaustively handle all values
  Unhandled type: "Literal[EnumEnvironment.TEST]"
  If exhaustive handling is not intended, add "case _: pass"  (reportMatchNotExhaustive)
```python
class EnumEnvironment(StrEnum):
    PRODUCTION = auto()
    STAGING = auto()
    TEST = auto()


def enum_function(this: EnumEnvironment):
    match this:
        case EnumEnvironment.PRODUCTION:
            print("a")
        case EnumEnvironment.STAGING:
            print("b")
```

## Why not to use Enums then?
However, literals are more transportable e.g. using an ORM, it is easier to map Literal to database values, than Enums. If that's your use-case, most likely, you are better off with Literals.

Another argument can be that if you use native Enums, you will have to perform a database migration every time you make changes. With Literals, you can get away with a varchar columns. In some cases, this can be a lot of overhead - in some teams/workflows this is actually desirable.[^3]

## The annoying things
There is something about the import performance of Python Enums[^4], however, if you are using python, does it really matter? (It sort of does.)

There are also a bunch of annoying things about enums, some of which are described in [this blog post](https://www.cosmicpython.com/blog/2020-10-27-i-hate-enums.html), but some of those issues are already fixed, or not real issues - as the comments point it out.

## Conclusion
I don't really want to draw any general conclusions on when and where to use Enums vs Literals. Hopefully, you have some more pointers on what to consider, before using one or the other.

---

## References
[^1]:[https://typing.python.org/en/latest/guides/unreachable.html](https://typing.python.org/en/latest/guides/unreachable.html)
[^2]:[https://typing.python.org/en/latest/spec/enums.html#enum-literal-expansion](https://typing.python.org/en/latest/spec/enums.html#enum-literal-expansion)
[^3]:[https://docs.sqlalchemy.org/en/21/orm/declarative_tables.html#using-python-enum-or-pep-586-literal-types-in-the-type-map](https://docs.sqlalchemy.org/en/21/orm/declarative_tables.html#using-python-enum-or-pep-586-literal-types-in-the-type-map)
[^4]:[https://snarky.ca/introducing-basicenum/](https://snarky.ca/introducing-basicenum/)
