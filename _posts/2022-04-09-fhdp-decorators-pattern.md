---
layout: post
title:  "[Head First Design Patterns] Decorators Pattern"
date:   2022-04-07 08:00:00 +0700
categories: work
author: ntnhaatj
tags: work designpattern
---

# The decorator pattern
## Design principles
- `Classes should be open for extension, but closed for modification`

## Def

- decorating objects
- Figure shows decorators objects `Mocha, Whip` wrap and decorate `concrete Beverage (DarkRoast)` component

![Wrapped Objects In Decorator Pattern](/images/20220407/decorator_pattern.png)
- it has a `same supertype` as the object they decorate
- `the decorators adds its own behavior` before/after delegating to the object it decorates to do the rest of the job
- objects can be decorated at any time, so we can `decorate object dynamically at runtime` with as many decorators as we like

## Implementation

- Brief implementation flow:
    1) Implement concrete classes for `Beverage` abtract class / interface, ie. `DarkRoast, Juice`
    2) Define decorators which will be able to wrap and extend new behaviors to concrete `Beverage` classes
        + `By inheriting Beverage`, create abstract class for beverage condiments `BeverageCondiment` which  to follow the same type which the superclass `Beverage`
        + By `composing Beverage` in condiments abtract class, it will allow us to add any new behaviors to the condiment decorators at runtime
    3) Implement condiment decorators (`Mocha, Ship, Soy`) which extended from abtract class `BeverageCondiment`
    4) Now the decorators ready to wrap any Beverage objects to extend new behaviors

- Notes: (confusion over `Inheritance` versus `Composition`)
    + using inheritance -> `type matching` (not to `get behaviors`)
    + acquiring new behavior by composing objects together
    + why we need `type matching`? We need the `same interface` as the component because they need to stand in place of the component

- if we rely on `inheritance`, our behaviour can only be determined statically `at compile time`. `With composition`, we can mix and match decorators any way we like `at runtime`

## Java I/O decorators

