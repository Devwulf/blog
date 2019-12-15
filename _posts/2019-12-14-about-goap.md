---
title: "About GOAP"
date: 2019-12-14T10:50:24-05:00
categories:
 - Blog
tags:
 - ai
 - problem
 - solution
---

Ok, the GOAP tool I'm currently using is giving me only headaches instead of better AI. I have nothing against the concept of GOAP itself; in fact, that's the kind of thought process I want my AI to have. But its implementation through this tool is what I'd say as lacking and not enough for my needs.

I do understand why it's like this. It was made for a fast-paced brawler game, with probably only a "few" amount of actions per AI (when I say few, it can still be considered quite a lot, but it will still be few compared to how much I'm planning to do). Since it's fast-paced, it requires real-time decision making instead of per action. While my game will also require real-time decisions, that is needed only during fights and not during a normal AI day.

I still want to thank the developer that made this [GOAP tool](https://github.com/crashkonijn/GOAP) for creating a wonderful tool for its own use-case. This has also shown me the inner workings of GOAP for -- and this is the best part -- a total price of completely free! Thank you very much for this amazing tool!

With all that said, I'm planning to extend this GOAP tool with these requirements:

- Two options about the rate of update for actions: real-time and per action
  - **Real-time:** the rate of update for this will be once per second. This can be adjusted globally, but should not be different per goal/action. This can be used to intervene/stop a current action to do something else. For example, a farmer farming could run away anytime whenever there's an enemy around, instead of trying to finish the action first before running. This is also very useful during fights, so the AI can try to cancel its attacks when needed.
  - **Per Action:** each update will happen after an action is finished. Most actions will use this.
  - This option can be different per goal, but not per action. This means that a behavior can have both types of update rates at the same time.
- The addition of behaviors
  - A **behavior** is made up of multiple goals and actions.
  - It also has a list of dataset keys registered by its own actions. This is useful for resetting the dataset specific to this behavior.
  - It is also stored into a ScriptableObject. I was thinking of making this a GameObject prefab instantiated as a child of the AI, but there's no need since it doesn't really do anything by itself during runtime and is simply a holder of goals and actions.
  - However, it should be possible to disable behaviors by flagging its goals and actions as disabled. The behavior instance itself should be able to do this, since it will have the references to its instantiated goals and actions.
  - This makes AI behavior more modular and changeable during runtime, and makes managing AI way easier.
- Organize actions by their preconditions and effects during startup, for easy and faster access to them during runtime.
  - I'm thinking of simply making `Dict<string, List<Action>>`, one for preconditions and one for effects, where the strings are the dataset keys. This will be in expense of more memory used, but it's definitely worth it, especially with hundreds of AI at once.

Those should be all the features I need for my AI, but more may be needed the further I go with my game. Well, we'll just have to see.
