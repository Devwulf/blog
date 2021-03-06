---
title: "Attempting to Implement DHPA on Voxel Terrains"
date: 2019-12-08T21:03:53-05:00
last_modified_at: 2019-12-09T12:19:21-05:00
categories:
 - Blog
tags:
 - ai
 - pathfinding
---

Holy crap this is gonna give me lots of headaches! :cry:

Anyways, I've been looking around for a pathfinding that would work well on voxel terrains, and failing to find any good ones.

***cough*** Just found an implementation of HPA for Unity... forget what I said earlier (that was embarrassing! :persevere:)

Aaaaanyways, now that I've found a base implementation of it, I'll have to make it work on my game first. It won't be that easy, but at least some of the work is done for me already.

Since that implementation is on 2D tiles, I have to 3D-fy it using voxels. Then when it properly works, I'll have to convert it to DHPA and see if that is faster during runtime (initial load times matter less for now).

I also need to put some dynamic obstacles like doors, ladders, etc. After that, lots and lots of testing, very fun! /s

Then I'll have to package all these up for use on my project. This means I'll have to create a new project... but I swear I won't abandon my previous project! This new one is for the betterment of that one, after all.

Anyways, here are some useful sources I'd like to look through later:

- [**HPA implementation**](https://github.com/hugoscurti/hierarchical-pathfinding) (Thanks for lessening my work, hugo! Mad respect!)
- [**HPA paper**](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.479.4675&rep=rep1&type=pdf)
- [**DHPA paper**](https://www.aaai.org/ocs/index.php/AIIDE/AIIDE10/paper/viewFile/2131/2543)
- [**Hierarchical Dynamic Pathfinding for Large Voxel Worlds**](https://twvideo01.ubm-us.net/o1/vault/gdc2018/presentations/Alain_Benoit_HierarchicalDynamicPathfinding.pdf) - Useful for visuals. Now only if I could find the GDC video for that...
- [**Ultra-Fast Optimal Pathfinding without Runtime Search**](https://www.aaai.org/ocs/index.php/AIIDE/AIIDE11/paper/view/4050/4423)

**UPDATE**
Derp me, just realized Ultimate Terrains already have a good enough path finder. However it uses A*. However however, that's also good enough for me, since it's fast enough for now. If I truly find it too slow for my needs, I'll take a look into DHPA again and implement it.

The biggest problem for me is to convert HPA into 3D space from 2D. Most of the examples I've seen this used on are maps that are mostly flat. That is most often not the case with voxel terrains, where the heights per chunk can vary a lot. Or maybe I'm just not understanding this too well yet. I think it's the latter. (I really need access to that GDC video :persevere:)

Anyways, that means I'll have to shelf this idea for now, until I get to that point where I need it.
