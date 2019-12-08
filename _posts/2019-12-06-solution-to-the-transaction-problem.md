---
title: "Solution to the Transaction Problem and Awakening Stuff"
date: 2019-12-06T14:36:15-05:00
categories:
 - Blog
tags:
 - problem
 - solution
 - ideas
 - ui
---

Basically, transactions should only occur between two entities. Whenever an entity wants to change its own items, no transaction needs to be created; that entity has total control over its own items.

A transaction cannot be made with only one entity anyways, since slots are not supposed to know anything beyond the inventories they're in and the slots they interact with. I also need to make sure that transactions can never be made with only one entity.

This also has the benefit of being able to record all the transactions happening in the game/server, since admins will probably want records of that anyways, even if it's just putting or grabbing stuff from chests.

Also, the infrastructure to make it happen is already in place because entities need to interact first before swapping items. For example, if a player wants to grab an item from a chest, that player will first need to "interact" with that chest, or else no UI will show up. That "point of interaction" can be used to create that transaction and make the UI pop up.

As for the "awakening" and leveling idea, here are my thoughts:

- Awakening can only happen after defeating a boss and absorbing its soul. Bosses become harder the more people in a party, but it's also easier than soloing it. Each person in a party has their own chance (dice roll) of getting the soul.
- Awakening also puts players into the next class. The classes are (these are subject to change):
  - God/Godhood
  - Demigod
  - Seraph
  - Guardian
  - Arch Magus
  - High Magus
  - Magus
  - Apprentice
  - Acolyte
  - Initiate
- When awakening, only the maxed out spells will have their level limit increased.
- The more spells are used, the more powerful they get by getting more levels
  - Incentivizes players to use their spells instead of just adding points to them and only using them once they're powerful enough

However, I have to be careful about how spells should increase their levels.

- Increasing them through simply counting their usage can be cheesed by using these spells on very low level enemies. This will also lead to **spell spamming**, but this is not a priority problem since there will exist people that just spams spells anyways. All I can do is incentivize against that.
- Increasing them by counting their usage against same or higher level enemies will simply lead to players looking for an easy to dodge but hardy enemy to farm spell usage. This will also force players to fight the same type of enemies again and again while using the same kind of spells, which will lead to their boredom.

What if we use an xp system for spells then?

- The amount xp their spells get is determined by the level of their enemies and they get it only after killing an enemy
  - The problem with this is powerleveling, which isn't that bad of a problem and if done right, it even leads to socializing players.
  - The problem with the second part is that it will force people to play only dps roles, leading to unfun tanking and support roles. Why tank or support anywhere else besides bosses, when 4 dps will kill enemies faster than 2 dps, 1 tank, and 1 support? Maybe have 1 support and 3 dps, but anyone can use any spells anyways, making everyone a hybrid role which isn't that bad, unless it completely removes the other roles.
- What if we still use an xp system, let them gain xp while using the spell instead of after killing, but make it so that comboing spells will give way more xp, similar to Devil May Cry?
  - This could definitely work! Using the same spell again and again will give less and less xp for that spell.
  - Also, the fewer different spells between each same spell instance, the less combo bonus given.
  - This behavior can be further incentivized by having different combo bonuses for each of the spells, like extra damage, making cooldowns go faster, etc.
  - This will also let players explore possible combos, even with the weaker spells, making them use much more varied kinds of spells.

The only problem I can think of right now is for the playstyle where some players don't wanna think too much to combo their spells and just wanna use one spell again and again (heck, even I'm guilty of this in Smash Ult, spamming Isabella's fishing rod is just too hilarious!)

- This is still viable, but definitely weaker than those who combo. If they wanna compete against those players, they better combo!
- I'll also have to balance enemy AI and stats so that it's a bit harder for no-combo players and a bit easier for combo players, but it should still be doable for no-combo players.
  - The bosses should be an exception, since they'll need to take the players everything they got to kill them.

As for the tanks and supports, I'll definitely try to make them fun, but they're not meant to solo stuff. They're meant to party up with others. I also need to make sure that they get some bonuses that will make their roles easier to do, unlike the Reinhardts during cc meta.
