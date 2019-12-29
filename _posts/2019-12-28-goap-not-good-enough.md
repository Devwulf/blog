---
title: "GOAP is Not Good Enough"
date: 2019-12-28T12:22:41-05:00
categories:
 - Blog
tags:
 - ai
 - problem
 - solution
---

Wow, it's been quite a while since I posted here! I wish I did this more often, but holidays and college stuff got in the way...

Anyways, I've just recently figured out that GOAP is not good enough for my needs. Guess it took me almost half a month to figure that out, but I've learned a lot too, so I'd say it's a win overall. Better to change my mind about this early rather than later, right?

So, things I've learned:

- Out of my frustration trying to rework the GOAP tool I talked about earlier, I looked around for better ways to do AI, depending on my needs. GOAP seems to fit really well, but because it does a reverse search, it's much less performant compared to others (which I'll talk about later).
  - It also doesn't help that, before being able to do a goal, GOAP needs to do a reverse search among all the branches underneath that goal because it needs to find the least costly way of doing something, even if it may have already found it in an earlier branch.
  - However, an advantage to this is that the AI will always find the best solution (or rather, the cheapest solution) to do something.
- I've recently found out about HTNs (Hierarchical Task Networks) for doing AI.
  - To my understanding, an AI starts with the current state of the world that it knows about. Then, through conditions, it tries to find a way to get to a certain world state it wants. It plans for the future (forward search) which means it could stop searching once it gets to the world state it wants. This also means that, even if it finds a way quickly, it may not be the best solution for it. It's up to the AI designer to create conditions that would help, if not guarantee, to get to the best solution possible.
  - Because of time constraints, I'd rather look for a ready-to-use tools than having to make this by myself. Maybe after this game, I'll look into this some more.
  - There is one promising [tool](https://github.com/ptrefall/fluid-hierarchical-task-network) I found but working with it is frustrating since it's all code-based, meaning it's not easy to know what a behavior (domain) does at first glance, especially if it's huge and complex. A GUI for it will definitely help a lot with creation and iteration of behaviors.
    - Also, to be able to add behaviors during runtime, slots must first be created for those behaviors. But I'd have to hard-code the slots, so however many I hard-code, that's the limit on how many behaviors an AI can have.
    - Also also, it's really frustrating to code the "domains" (I think of them as behaviors) since I had to manually tab in each of the lines so it's easier to read.
    - Also also also, I've found an even better tool that uses a different AI system
- While looking around about HTNs to further understand it, I came across a [game dev forum post](https://www.gamedev.net/forums/topic/700989-fsm-bt-htn-goap-other/) talking about it and other AI systems. That was where I found out about IAUS (Infinite Axis Utility System), basically utility-based AI.
  - To my understanding, all decisions are made based on scores. If an action has a better score than another, then that action is done.
  - Those scores are determined by qualifiers and scorers.
    - Scorers give a score based on certain values. For example, there could be a scorer that is based on the current hunger value of the AI, and if hunger goes over a certain threshold, a high score is returned so the AI eats.
    - Qualifiers can contain multiple scorers and each qualifier type does a different thing depending on the scores returned by its scorers.
  - A [Unity asset](https://assetstore.unity.com/packages/tools/visual-scripting/apex-utility-ai-personal-edition-56306) has recently gone [open source](https://github.com/ApexGameTools/Apex-Game-Tools/tree/master/Apex%20Utility%20AI) and so far, it's really passing all the requirements I need for my AIs, so I think I'll be sticking to this unless I find some feature it doesn't have that I need and I can't work around it.

Anyways, that's all I've learned this past few days about different kinds of AI. I most likely got a lot of these explanations wrong too, but I'm honestly just looking for an AI tool that fits all my criteria, and if it does, I'll learn more about how it generally works. In the future, once I have different use-cases that need a different AI, I'll be looking through these 3 again in detail and see which one fits better.
