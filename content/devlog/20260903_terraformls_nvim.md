+++
title = "My neovim is frozen - for the first time"
date = 2026-09-03
description = "A terraform-ls bug that freezes Neovim"
draft = false

[taxonomies]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++

I had the strangest problem in the past two weeks. The terraform repository I am working in became a mine field. Some files would completely freeze Neovim.

I thought it must be one of my plugins. Turns out, it is a [bug in terraform-ls](https://github.com/hashicorp/terraform-ls/issues/2094).

The solution? 

Well -- [a work-around](https://github.com/timonviola/config/commit/44dc86a7520bd5d68702f447ff244b0c3961b55b) -- disable semantic-token highlighting (which is already done by tree-sitter in my config, so no features are lost).

```diff
+      on_attach = function(client, _)
+        client.server_capabilities.semanticTokensProvider = nil
+      end,
```
