---
title: "Problems with the Shop Menu!"
categories:
  - Blog
tags:
  - problem
  - solution
---

Gah! Why is UI work too bothersome?!

Basically, I made a UI system for inventories where I can just drag and drop between inventories. It works well so far because all this time, each of the inventory displays don't need to know **WHO** is involved when swapping items.

Is it between a chest and a player? Is it between players? Or maybe even a player with itself, like its own hotbar?

It works very well when we're not concerned with those questions. The problem arises when we start being concerned about those. Like for example, with shops!

When a shop and a player trades items, those items (slots in my case) not only needed to know about the inventories they were in and they're going to, but also **WHO** they're from and going to. They need to know if the other person has enough money to buy them, and they also need to somehow be able to subtract or add money to their wallets. And that's already giving them way too much responsibility.

Wow, I actually thought of the solution while I was typing these. Huh, didn't expect this to work this well...

Anyways, the solution I'm thinking about is this:

- I already have the interaction system working, so we can simply make the two entities involved (ex. shop and player) start a "transaction" when the player interacts with the entity (in this case, the shop). This will also be the case for chests.
- This transaction will be its own object, and both entities will have a reference to it. Naturally, this transaction will also have a reference to both the entities involved.
- The slots already have access to the entity that owns the inventory that owns the slot, but it won't have access to the entities involved. It can only ask the transaction to try to make the swapping happen. If it can't, then the slot won't continue with the swapping.
- The type of transaction is determined by the type of interaction, and it will do different things. For example, a trading transaction will be different to a swapping transaction since it will have to check if either entities can afford to make the trade happen.

A problem arises when we simply want to drag an item onto the hotbar. When should the transaction be started? It can't really start when we begin dragging and dropping our item, since the slots don't have any clue who the entities are.

I'll have to think about this some more...
