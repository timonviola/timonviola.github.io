+++
title = "Adding asciinema to Zola"
date = 2026-04-26
description = "Display terminal recordings in Zola"
draft = false

[taxonomies]
categories = ["General"]

[extra]
lang = "en"
toc = true
+++


I wanted to add some way to display terminal recordings here. I use wezterm so it was
an obvious choice to try [asciinema](https://asciinema.org/) and record with `wezterm
record`.

{{ asciinema(src="demo.cast", autoPlay=true, loop=true, controls=false) }}


It took a bit of work, but got it working. One of the quirks was actually getting the
recording to display with Serene (the theme I am using). 

In the end, I was able to add a short code as well, so after recording, I can simply
write 

```bash
{{/* asciinema(src="demo.cast", autoPlay=true, loop=true, controls=false)
*/}}
```
in markdown. 
