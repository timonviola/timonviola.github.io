+++
title = "Debugging ssh"
date = 2025-02-27
description = "Some notes on debugging ssh connection."
draft = true

[taxonomies]
tags = []
categories = ["General"]

[extra]
lang = "en"
toc = true
+++

# Where do we start from?
So I never really thought about, how to *debug* `ssh`. It was always just working and if not, I could just quickly generate a new key-pair.

I also thought that ssh needs 2 files (keys):
- public (id_ed25519) and
- private key-pair (id_ed25519.pub)

And maybe a +1 (I have a pretty neat "config" file, with useful aliases, key-chain configuration etc.).

However, there is a `known_hosts` file, which is pretty important.
Here is the contents of `known_hosts`:
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

Yeah, this was the part where you just type in `y` . Quite an important piece of the protocol!

Here is a quick representation for the visualcortex:


# Useful commands
## ping the host (server)
ssh -Tv github.com -> just ping the server

## force ssh to use specific key:
ssh -o "IdentitiesOnly=yes" -i $HOME/.ssh/id_ed25519_gh git@github.com

## get the host public key
ssh-keyscan github.com > ./known_hosts



