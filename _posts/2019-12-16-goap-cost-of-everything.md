---
title: "GOAP AI: Cost of Everything"
date: 2019-12-16T23:46:52-05:00
categories:
 - Blog
tags:
 - ai
 - ideas
---

Now that I've finally finished implementing the first requirement in my last post (easier said than done, but it only took a while because of how inefficient my changes were :persevere:), I should now be focusing on how to calculate the action costs and goal multipliers to make realistic-looking AI.

Also, it seems I didn't need the third requirement, since those look-ups, if implemented, will be used only during the game initialization and adding/removing actions during runtime, the latter of which shouldn't really be happening much anyways. But if I ever somehow need to add/remove actions many times during runtime, I'll be revisiting that requirement and implementing it. One example I can think of is making separate actions for visiting different places when the AI learns about those said places. I may just make a manager that maintains all these though, instead of creating an action for each and every one of those places.

Anyways, here are some types of costs I can think of right now:

- **Cost based on distance:** I believe this kind of cost should be implemented as a procedural condition instead of a global modifier to cost. An example of a need for this is going to the closest store instead of the favored one, which may end up being in another town miles away.
- **Cost based on favorability:** Kinda like looking up reviews of a restaurant online, favorability will have some effect on action cost. May be used with distance.
- **Cost based on values:** For example, the hungrier the AI gets, the least costly eating gets, and the more likely it'll be done next. The value in this case is the hunger value. Some other values I can think of:
  - Other need values
  - Health/Mana
  - Money
  - Personality
  - Like/dislike
- **Cost during battles:** I think this will be the hardest one to implement. I need this to be accurate enough that the next action made by the AI won't kill it, but make it still have some flaws to not make the player feel like they're fighting a "cheater" AI with aimbots and wall hacks and knowing what the player is about to do next.

Tomorrow though, I'm just planning to get a basic woodcutter AI to work. And maybe even implement shops to buy and sell stuff.
