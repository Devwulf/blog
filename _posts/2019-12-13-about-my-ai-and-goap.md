---
title: "About my AI and GOAP"
date: 2019-12-13T19:33:39-05:00
categories:
 - Blog
tags:
 - ai
 - problem
 - solution
---

Holy wow, college and citizenship really takes away time, huh?

Anyways, I've just now realized... I've been doing my AI wrong.

Here are some things about it that I got wrong:

- The `MaxRuntime` shouldn't be messed with by adding a `PerformRuntime` to it.
  - Adding some value to `MaxRuntime` only makes updating an action much slower and doesn't actually make an action take time to do. I should be on the mindset that my actions are always going to "perform", therefore it's better to do checks to not repeat an action "performance".
  - I've also made a `CreateDelay` method in the `AIAction` to make it seem like doing an action takes time to do. Use that.
- Each **macro action** should have its own goal, instead of having one goal for an entire behavior.
  - **Macro actions** are actions that can be broken down into base actions.
  - **Base actions** are actions that are of the most basic form. These make up macro actions.
  - A good real-world model of this system is the atomic model. An atom is made up of protons, neutrons, and electrons. The particles are used by all atoms, but no compounds use all atoms, since some atoms just don't interact well together.
  - An example of a macro action is `ChopWood` action. That is made up of these base actions:
    - GetItem (axe)
    - BuyItem (axe)
    - EquipItem (axe)
    - CheckInventoryForItem (axe)
    - etc.
  - A goal called `ChopWoodGoal` can then be made for that action.
- Use the goal's multiplier to steer an AI into doing certain actions in a given time.
  - An example of this is this situation: An AI really, really needs to chop some wood. That will mean the multiplier for `ChopWood` will be low **(lower multiplier means higher priority)** but then that AI gets hungry. It won't immediately go for the nearest food. But the higher its hunger gets, the lower the multiplier for the `Eat` action gets, until its hunger gets to the point that eating is prioritized over chopping wood.
- I should really make a "Create Goal" wizard...
- The `GetTarget` method works well for basic AI, but I want it to use the AI's memory to get its target from.
  - The AI memory is basically a huge dictionary of strings and objects (like the `object` kind of object) that will store all kinds of things, things like its favorite store, where it should store its own stuff, what and where its house is, where its best friend lives, and so on.
  - There is no order or a specific type to the memory, they're all kinda just jumbled together, ints, floats, strings, GameObjects, Vector3s, etc.
  - It will work like JavaScript's variable array, and it's up to whatever needs that memory to cast it to a usable type.

With this, I'm finally gonna get started with AI! I know, I've been saying that lots before too, but getting this entire system's workings down is very important to making my AIs work properly. I'm very excited and happy, and it also helps that I just passed my Network class today! So... yay, me!
