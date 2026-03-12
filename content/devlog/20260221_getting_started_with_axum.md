+++
title = "Getting started with axum"
date = 2026-02-21
description = "Some useful resources and tips to get started with axum, a web framework for Rust."
draft = false

[taxonomies]
tags = ["rust"]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++
When it comes to picking a production ready, battle tested back-end framework for rust, it really comes down to Axum and Actix-web. Both are great frameworks.

# Why?
I have some beginner level experience with Actix-web, after following along the excellent book by Luca Palmieri, [Zero To Production](https://www.zero2prod.com/). (I highly recommend it to anyone looking to get started with web development in Rust.)

So why start learning another framework when I already learnt a fair amount about one framework? Well, the eco-system and my interests are more aligned with Axum.
- It is a lighter weight framework which prioritizes modularity and composability.
- It integrates well with tokio (where Actix-web has its own actor system).
- `WASM` fullstack frameworks like [`Dyoxus`](https://dioxuslabs.com/) or [`Leptos`](https://leptos.dev/) work with axum.


# How to get started?
- Axum's repo has a **lot** of examples, they are really good and cover a lot of common tasks, you would normally need for a production ready web server.
- A more advanced set up, that can help you to take off is the [`rust-web-app`](https://github.com/rust10x/rust-web-app/) project, Jeremy Chone also has a lot of awesome content on his [YouTube channel](https://www.youtube.com/@JeremyChone).

# My 2 cents
I think Axum is a great choice to build solid web servers. Even if you don't know Rust, I think it is a good place to start. It has a lot of good design choices, good learning materials that will help you along the way. The framework helps you quite a lot to write clean, well structured, well modularized code, that is also easy to run in production.
