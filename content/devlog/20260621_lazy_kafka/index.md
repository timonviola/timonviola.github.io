+++
title = "Lazy Kafka"
date = 2026-06-21
description = "Making lazy-kafka repo public"
draft = false

[taxonomies]
tags = ["python"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++

[Lazy-kafka](https://github.com/timonviola/lazy-kafka) is celebrating soon it's second birthday, so I thought, I would just publish the repo instead of letting it sitting on my gh account.


{{ asciinema(src="cast.txt", autoPlay=true, loop=true, controls=true) }}

# the ambition

The goal of this project was to create a minimalistic (also linecount wise minimalistic) kafka tui. The primary paint was actually checking the status of *kafka connectors*. But this project is a lot more ambitious:
- Kafka topic:
    - list topics
    - follow topic messages
- Kafka Connectors:
    - list connectors
    - live follow status
- Schema registry:
    - list schemas
    - describe schemas

There is more to these operations, e.g.: deleting, creating entities. Some of the features are there, some are not. The code is in a limbo state, just between being split up into *uv workspaces* to support a plugin architecture. There is also some dead-code. All in all, there is a lot of work left before this could be used.

Maybe one day I will work more on it.
