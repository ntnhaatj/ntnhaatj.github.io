---
layout: post
title:  "[Head First Design Patterns] Adapter And Facade Pattern"
date:   2022-04-22
categories: work
author: ntnhaatj
tags: work designpattern
---

# Adapter Pattern
- class adapter (in language which allow to have multi-inheritance, Adapter inherite both Adaptee and Target)
![Class Adapter](/images/20220422/class_adapter.png)

- object adapter (compose `Adaptee` object in `Adapter` to implement `Target interface`)
![Object Adapter](/images/20220422/object_adapter.png)

## Implementation
(github)

----

# Facade Pattern
- to simplify interface (ie. the bundle of actions in smarthome when somebody back to home)

## Design principles
- `Principle of least knowledge` - talk only to your immediate friends: to prevent the design have a large number of class decouple together (which create a fragtile system) -> we should only invoke methods which belong to:
    + the object itself
    + objects passed in method as parameters
    + any object the method creates or instantiated
    + any component of the object
    
## Implementation
(github)
