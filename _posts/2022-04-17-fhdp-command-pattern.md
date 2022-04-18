---
layout: post
title:  "[Head First Design Patterns] Command Pattern"
date:   2022-04-17 08:00:00 +0700
categories: work
author: ntnhaatj
tags: work designpattern
---

# Command Pattern
- all commands will implement the interface `Command` which including `execute()` method
- requester invokes `Command.execute()` without having any knowledge about detailed behavior in `execute` func

![Command Pattern](/images/20220417/command_pattern.png)

## Design principles
- decoupling requester and receiver actions

## Implementation
- [source code](https://github.com/ntnhaatj/head-first-design-patterns/tree/master/commandpatttern)
