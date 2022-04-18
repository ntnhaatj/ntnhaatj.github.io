---
layout: post
title:  "[Head First Design Patterns] Singleton Pattern"
date:   2022-04-17 08:00:00 +0700
categories: work
author: ntnhaatj
tags: work designpattern
---

# Singleton Pattern
- one of a kind object, there is only one instance
- no public constructor, only provide an global point to access an instance

## Implementation
- is aware about dealing with multithreading, synchronize `getInstance()` method if needed
- [source code](https://github.com/ntnhaatj/head-first-design-patterns/tree/master/singletonpattern)
