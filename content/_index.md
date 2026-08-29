+++
template = 'home.html'

[extra]
lang = 'en'

footer = false

name = "tmon"
id = "timonviola"
bio = "I write here things. Sometimes."
avatar = "img/avatar.webp"
links = [
  { name = "GitHub", icon = "github", url = "https://github.com/timonviola" },
]

recent = false
recent_max = 15
recent_more_text = "more »"
date_format = "%Y-%m-%d"
+++


This is my devlog 📃.

<div id="demo"></div>
<script src="/asciinema-player.min.js"></script>
<script>
  AsciinemaPlayer.create('/demo.cast', document.getElementById('demo'), {
    autoPlay: true,
    loop: true,
    controls: false,
    fit: 'width',
  });
</script>
