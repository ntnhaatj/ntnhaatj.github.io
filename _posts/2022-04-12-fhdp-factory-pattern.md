---
layout: post
title:  "[Head First Design Patterns] Factory Pattern"
date:   2022-04-12 08:00:00 +0700
categories: work
author: ntnhaatj
tags: work designpattern
---

# Factory Pattern
- to solve the problem about complexity by using `conditional if/else` method
- to encapsulate the object creation to another component, to make it easy for changing, understanding and modifying
- to follow the `single responsibilty principle` - every object/function only handles one thing and always only has one reason to change

## Def
- Factory pattern defines an interface for creating an object, but lets subclass decides which class to initiate. It lets a class defer instantiation to subclass
- Decoupling `Products class` and `Creators class`
- 3 types of factory patterns 
    1) Simple Factory
    2) Factory Method
    3) Abstract Factory

## Design principles
- `Dependency Inversion Principle`: depend upon abstraction, do not depend upon concrete classes (high level modules should not depend on low level modules; both should depend on abstractions)

## Implementation
- The idea is just letting to other classes implement object creation against on provided parameters 
- [source code](https://github.com/ntnhaatj/head-first-design-patterns/tree/master/factorypattern)

