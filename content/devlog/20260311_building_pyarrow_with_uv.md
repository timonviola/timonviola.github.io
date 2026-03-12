+++
title = "Building Pyarrow with uv"
date = 2026-03-11
description = "Python platform compatibility flags and building with uv"
draft = false

[taxonomies]
tags = ["python"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++
Sometimes it can be tricky to figure out the right flags for a tool, I have seen that
many people ran into issues, trying to use `uv` and `pyarrow` together ([e.g. this
commenter most
likely](https://github.com/astral-sh/uv/issues/7516#issuecomment-3311977405)). The error
looks like this:

```text
check.warn(importable)
  CMake Error at CMakeLists.txt:289 (find_package):
    By not providing "FindArrow.cmake" in CMAKE_MODULE_PATH this project has
    asked CMake to find a package configuration file provided by "Arrow", but
    CMake did not find one.

    Could not find a package configuration file provided by "Arrow" with any of
    the following names:

      ArrowConfig.cmake
      arrow-config.cmake

    Add the installation prefix of "Arrow" to CMAKE_PREFIX_PATH or set
    "Arrow_DIR" to a directory containing one of the above files.  If "Arrow"
    provides a separate development package or SDK, be sure it has been
    installed.


  error: command '/Users/timon/.nix-profile/bin/cmake' failed with exit code 1
```


A common use case is to build a Zip archive of your package, [uv has a dedicated repo
for that](https://github.com/astral-sh/uv-aws-lambda-example?tab=readme-ov-file#zip-archive).

Here is how you can build pyarrow for a `linux_x86_64` platform with `uv`.

```bash
uv pip install \
  --no-installer-metadata \
  --no-compile-bytecode \
  --python-platform x86_64-manylinux_2_28 \
  --python python3.14 \
  --target build \
  -r requirements.txt
```

The key here is to use `x86_64-manylinux_2_28`[^1] and check the packages site on `pypi`
to see for which platforms the package has pre-built wheels:
[pyarrow](https://pypi.org/project/pyarrow/23.0.1/#files).

If you use a platform, which has no pre-built wheels, you will have to build the package from source. The error message above is about missing CMake (and a bunch of other things in my environment), but the reason for it, is that a wrong platform was used, which has no pre-built wheel e.g.: `x16-linux-gnu`.


[^1]: [binary-distribution-format](https://packaging.python.org/en/latest/specifications/binary-distribution-format/)
