---
layout: post
title:  "[Head First Design Patterns] Strategy Pattern"
date:   2022-04-07 08:00:00 +0700
categories: work
author: ntnhaatj
tags: work designpattern
---

# Design pattern pros
- give you a shared volcabulary with other developers -> easily communicate with other devs and inspire who dont know start learning them.
- elevate your thinking about architecture by letting you think at `pattern level`, not a nitty gritty `object level`

# Common design principles
## Interface, Abtract class and Mixin
- `Interface`: including abtract methods, no concrete method and internal state
- `Abtract class`: including abtract methods, concrete methods and internal state
- `Mixins`: including abtract methods, concrete methods but no internal state

# SimUDuck app
## Design principles
- Identify the aspects of your application that vary and seperate them from what stays the same (encapsulate what varies)
- Program to an interface, not an implementation
    + for some languages like Python which supports `multi-inheritance`, program an abstract class is acceptable
    + but always keep in mind that program an interface always fexible to create your own implementation
- Favor composition over inheritance
## Pattern
- `Strategy pattern` defines a family of algorithms, encapsulates each one and makes them interchangeable
