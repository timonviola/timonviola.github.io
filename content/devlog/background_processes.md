+++
title = "Background processes in Shell"
date = 2025-02-12
description = "A short use case for background processes."
draft = false

[taxonomies]
tags = ["general", "blog", "bash"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++

# What are shell background processes?
Looking at the man page of [`gnu bash section 3.2.4`](https://www.gnu.org/software/bash/manual/bash.html#Lists), a command executed in *background* is essentially *asynchronous* execution of multiple commands.

One way to run a command in background is to terminate the command with the `&` operator:

```bash
> (sleep 5 && echo 5 )& (sleep 2 && echo 2)&

```
The output of *background* commands are redirected to `/dev/null`, so to see the `echo` output:
```bash
(sleep 5 && echo 5 >&1 )& (sleep 2 && echo 2 >&1)&
```

# Why use this?
The two main use-cases are running things in parallel and not wanting to wait for the output of a command. One example is starting multiple processes in a container.

[Docker documentation](https://docs.docker.com/engine/containers/multi-service_container/) recommends creating a wrapper script.

This is a great way of running set-up tasks if `initContainers` or multi-stage builds cannot solve your problem.

## Example
As an example, let's run Airflow and create a user via airflow CLI. For development this is acceptable, for production, I would prefer to use initContainers over this approach.

```Dockerfile
FROM  apache/airflow:slim-2.9.1-python3.12 AS base

ARG AIRFLOW_USER_HOME=/opt/airflow

VOLUME /opt/airflow
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
COPY start-airflow-bg .

ENTRYPOINT ["./start-airflow-bg"]
```

```bash
#!/bin/bash

set -exv
# Start the first process
sleep 5 && airflow users create -e aoeu@aoeu.cc -f aoeu -l aeou -r Admin -u airflow -p airflow && echo "manual airflow-admin created" &
CREATE_PID=$!

airflow standalone
```

