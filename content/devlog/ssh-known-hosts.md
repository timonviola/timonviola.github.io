+++
title = "ssh: know_hosts"
date = 2025-02-27
description = "Some notes on debugging ssh connection."
draft = false

[taxonomies]
tags = []
categories = ["General"]

[extra]
lang = "en"
toc = true
+++

# Where do we start from?
SSH has been around for quite a while - 30 years. It is one of those tools, which I rely on everyday, and never really looked into it after it was _working_. No I did not read the whole [RFC](https://www.openssh.com/txt/rfc4253.txt), but I picked one small part of it: `known_hosts`.

_(The RFC doesn't mention known hosts.)_

I also thought that ssh needs 2 files (keys):
- public (id_ed25519) and
- private key-pair (id_ed25519.pub)

And you can have a `+1` config file (with useful aliases, key-chain configuration etc.).

However, there is a `known_hosts` file, which is pretty important. From `man ssh`:
```
ssh  automatically  maintains  and  checks  a database containing
identification for all hosts it has ever been  used  with.   Host
keys  are  stored in ~/.ssh/known_hosts in the user's home direc‐
tory.  Additionally, the file /etc/ssh/ssh_known_hosts  is  auto‐
matically  checked  for known hosts.  Any new hosts are automati‐
cally added to the user's file.  If a host's identification  ever
changes,  ssh  warns about this and disables password authentica‐
tion to prevent server  spoofing  or  man-in-the-middle  attacks,
which  could otherwise be used to circumvent the encryption.  The
StrictHostKeyChecking option can be used to control logins to ma‐
chines whose host key is not known or has changed.
```

Yeah, this was the part where you just type in `y` . (hopefully, you pressed `y`)


