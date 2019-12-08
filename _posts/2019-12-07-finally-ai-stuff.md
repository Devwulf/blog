---
title: "Finally, AI Stuff!"
date: 2019-12-07T12:07:41-05:00
categories:
 - Blog
tags:
 - problem
 - solution
 - ideas
 - ai
---

Finally done with UI stuff for now! Well, I still have to implement it, but it shouldn't take too long.

Anyways, let's forget about UI and talk about AI instead!

I already have the AI system implemented, I just need to make the behaviors and actions and make sure they all work.

The actions I already made are:

- Buy Item
- Get Item
- Check Inventory
- Check Wallet
- Check Storage

I've made some other ones, but I've forgotten. I've also made some behavior-specific ones.

I still need to make these, and some more later:

- Check Shop
- Sell Item

I also need to make some more behavior-specific actions, like woodcutter, miner, farmer, etc.

Oh, I've also already made the tool that makes it easier to add actions to behaviors, so that's useful.

Anyways, my plan is to separate the world into regions. Each AI will have its own home region, and usually, only traders and adventurers need to leave their own home region because of the quest system.

That means, if a blacksmith needs a specific metal found outside the region, it only needs to make a quest about it on its own region, and the adventurers there, either passing by or staying there, can take it up if they're strong enough.

Usually, all materials any AI could ever need should be doable by all AI adventurers. But if there are some too hard ones, that quest will be marked as "prefers players". However, if an adventurer gets strong enough to do it, an adventurer could still take this up. It's just that these quests will also show up in the "Player Specific" section of the quest board.

My goal for now is to make the proper Interactables that AI can use and make a basic farmer.

Hmm... maybe the creation of houses can also be given to the AI?

AIs can have skills, each with a value (1-10) signifying how good they are with that skill. House blueprints can also have a minimum skill requirement attached to them too. So if an AI is good enough to make its own house, it can, but if not, it'll just put up a quest for it. Magic can also be used to make parts of the house, with good enough magic level.

Blueprints shouldn't be that hard to make, we can derive it from the house prefabs. The only difficulty I can see about this is making the assets for the modular house parts that would make up a house. It's not hard to make them into ScriptableObjects either.

Oh! Before I forget. I should really make a way so that the AI changes behavior based on the time it takes to do something and the money spent if a quest is put up for it instead. So for example, if a house builder is rushing to build a house, it would instead put up quests about cutting wood instead of cutting the wood by itself.

Hmm... isn't that just the cost for each action? I should really use the goal multipliers too...

Anyways, that's it for me for today. Can't say anything bad about church because of the people behind me...

P.S. Church sucks!
