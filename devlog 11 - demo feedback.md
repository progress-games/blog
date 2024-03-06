# demo feedback

I didn't end up adding anything else to the feedback compilation devlog. A lot of the time the issues were things I could address and begin working on right away so it felt useless to write what I was just about to do when I was just about to do it. Now the demo has settled down we can consider what needs to be done to maximise the full potential of this game.

## numbers

Before we do so, let's take a brief detour and have a look at the numbers. Unfortunately, Retromation never ended up playing the demo. It is hard to tell if this is a good or bad thing at this point in development. Of course, more eyes on the game would've been fantastic but the amount of feedback I recieved implies that the game is far from feature complete. Naively, I presumed the only big issue with the game would be its lack of content and different towers and while that is certainly something that needs to be addressed, it is not the biggest concern.

Without the boost from any large YouTube channels (thanks FaintlySaintly for covering it!) the game saw incredibly minimal reception. Considering it wasn't part of the Next Fest, this was realistically to be expected.

[![Demo Players](https://i.postimg.cc/tgYJ3LQh/Screenshot-2024-02-26-145854.png)](https://postimg.cc/TyvTGNPw)

Here's a look at the numbers. Perhaps to the uninitiated, this seems alright. Over 8,000 free licenses sounds pretty impressive. However I have gathered that on Steam, there are a lot of accounts, some bots some not, that add every free game to the library regardless of the game itself. To get a better sense of the userbase, look at the lifetime unique users. 53 people played the game, certainly better than 0, but far from an ideal amount. Unfortunately, the game wasn't able to gain any traction because of the Next Fest. With too much competition, there was simply no reason for people to play fishTDX, and it got no downloads because of that. That means I didn't get as much feedback as I'd hoped, and I saw a negligible uptick in wishlists. 

[![Lifetime Play Time](https://i.postimg.cc/7YwLsCrP/Screenshot-2024-02-26-at-15-06-08-Lifetime-play-time-stats-fish-TDX-Demo.png)](https://postimg.cc/ThNGh3PB)

Having a look at the lifetime play time stats, we're also relatively underwhelmed. The amount of content in this demo was more than bugTDX, however that didn't translate to a larger median play time. We're currently at 14 minutes with an average play time for an hour and a half - I would guess this is from people leaving it on for long times accidentally, not trying to grind out all the difficulties.

[![Wishlists](https://i.postimg.cc/MK9z9dYt/Screenshot-2024-02-26-151029.png)](https://postimg.cc/LnZdXkwZ)

And finally, the wishlists. Before the demo it was at around 60, now it is at 95. Almost at 100 which will be a neat little milestone but ultimately pretty pathetic. The wishlist conversion rate is notoriously low and I'd be suprised to see any more than 20% of these wishlists result in week 1 sales. Now there's an idea of where the game currently sits, let's deduce why this went so poorly, the issues with the game, and my plans going forward.

## creating a good demo

The first thing I'd like to briefly touch on is the idea of creating a good demo. A good demo should give players a taste of the game and leave them wanting more. It should be refined in what it does, but leave plenty of content hidden behind 'not available in the demo!'. Sure, this might annoy certain players, but it will mean that people have more anticipation to the full game's release, because they know how much more there will be. 

There's another way to look at it, where creating such a polished and content-heavy demo will have even better results (consider Balatro or Brotato) but I'd say doing it this way is not the best use of one's time. Balatro felt like a finished product when I played the first demo and I think most devs could get away with something with a bit less content and polish. The better the demo, the better the reaction, but it's important to finetune the balance between having a great product, but releasing it early enough to get the ball moving in terms of marketing.

Having too good of a product might mean that you had a viable demo ages ago that people could've played, reviewed, and wishlisted. But, having a poor product will permanently taint the reception of your game. This links back to why I am unsure whether Retro not covering it was good or bad. It could've pushed marketing forward but it also could've turned a bunch of potential players off the game too soon.

But it's tricky to create a good demo because creating a good demo doesn't link in to creating a good full game. Having a great demo means certain parts are incredibly polished, and other features are omitted. It means developing unevenly and this can challenge your conceptual thinking of the gameplay loop as you're yet to test major features being implemented. What I mean by this is in my demo, there was one type of fish. But in the full game there will be multiple. But right now, since I put creating multiple types of fish on the backburner in favour for the demo, I don't actually know whether that's feasible, or it will provide the additional enjoyment I think it will. Additionally, I don't know whether or not it should have been included in the demo because I haven't implemented it yet.

This is all a round about way of saying creating a good demo is incredibly difficult and it requires a much more finished product that what I had. In rushing to get something out, I made something lacking major features - it didn't even have a settings menu until a few days into the demo.

So, lesson learnt here, as important as getting a demo out ASAP is, making sure it's good is ultimately more important. I would say a good metric of where you should be once you publish your first Steam demo is at least halfway into development. Major systems should be in place and feel good to interact with, menus should be intuitive and not placeholder, and there should be enough content to get to at least 30 minutes to an hour of median playtime. Less is too little and more is unnecessary. 

## the issues with the game

Now the juicy stuff. What are the issues with the game? Let's rapidfire!

- Too easy/too hard
- No incentive to branch (towers or otherwise)
- No variation from enemies
- Towers feel same-y
- Not enough strategies
- Not enough synergies
- Not enough versatility for plots
- Gaining interest isn't apparent enough
- Unlock system isn't intuitive
- Every run feels similar
- Affixes don't have enough impact
- Menus have weird layouts
- Tutorial is just a slab of text
- The speed up button is in a bad spot
- No indicator where the enemies spawn
- Only one spawn location
- Doesn't look that good
- Don't like killing cute fish
- Only one enemy type
- No way to tell which enemies are coming up
- Sfx get annoying
- No way to get back lives
- Checking tower upgrades is unintuitive
- No post-run break down

And the list goes on. Some of these can be fixed easily, but all of them will take time to do. I think the most challenging and scary issues are the ones that link to people finding the game boring. Buggy stuff and UI fixes are easy enough to add in theory, although they do take a bit of time to code, but game balancing and game design require large changes to core structures that I didn't think I'd have to do.

There's two ways to approach tackling this feedback. The first is to say: 'fuck it. it's my game, my design, and if I find it fun then others must find it fun too. I will keep designing the game the way I'd like to and if it doesn't get as much success then so be it. I want to create a game for me, not for everyone else.' But the other approach that's harder to take but ultimately more rewarding is, 'I don't know everything. I have a biased perception of the game and I always will and as much as I'd like to enjoy playing it, I want everyone else to enjoy it too.'

These issues are massive and will challenge me. I spent the better half of today trying to draw some decorations for different plot types and I just kept trying to avoid making huge changes because they're frightening. It was only until I sat down and wrote this devlog that I realised that I might have to break the game in order to fix it into a better product. I'll fuck up the tutorial, the save system, the plot creation system, the entire fucking game loop with these changes, but I have to push through and come out the other side because I just don't yet know if these changes are worth it. It could be a huge waste of time, but if it's not, I'll come out with a better game.

Taking on such belittling feedback is really hard. I think about localthunk taking on feedback for Balatro and I think about how much praise he got for his game, even when there were only a few people playing it. All the feedback seemed overwhelmingly positive from the get-go. But it's important to remember that every game is different, and all feedback is valuable. What I will earn most from the completion of fishTDX (however daunting and impossible that may seem) is valuable experience for my next game, then my next, then my next.

## addressing these issues

So what am I going to do about it? Well, unlike most of development thus far, this will be difficult to manage without an ordered plan. The changes will be drastic and it'll be important to constantly have a task at hand otherwise I'll spend every day like I spent today - adding minor changes and watching major Seinfeld. 

### plot variety

1. Create a function `add_decor` that takes in a plot and returns that plot with decorations based off its type
2. Create a system where I can define different draw methods for different plot types
3. Add a new info panel for information about the current selected plot
4. Define a bunch of plot types in concept
5. Create a system where they can be implemented
6. Create a graphic for each plot type

### branch system

1. Add a system where rewards/cost can be added to splits
2. Create graphics for rewards

### new enemies

1. Deduce what different enemies will do
2. Create systems for each enemy type
3. Draw new enemies and implement them in game

### ui

1. Rework each UI menu focusing on:
- Minimal information
- Intuitive flow
- Simple aesthetic
- Unimpeding (no longer require new rooms)

### unlocks

1. Rework the game over screen
2. Add a pack system
3. Implement a pack creator

I would predict this all to take me quite a long time but we will see where we land with it. Side note, it is the next day and Olexa has just released a video on the demo so that's pretty cool. Will update on how it impacts the stats.

## update on 5/03 (day after deactivation)

So Olexa ended up making a video on fishTDX. Not really something I expected considering I had minimal interaction with him during my promotion for the demo. My only guess would be he saw something on Twitter or might've been browsing the demo list in full. The video performed slightly worse than his average 'new roguelike' video, currently sitting at 22k views. This is alright considering I wasn't expecting it to be covered at all, and it still outperformed some of his running series like Balatro, as well as a few other demos.

His experience with the game seemed relatively positive, but he had a lot of difficulty parsing all the information during the tutorial and remembering it for the actual gameplay. He was quite bad at the game because he didn't look at the different stats of the towers and focused on leveling up his tier one towers. I've found this to be a common issue with the game - the discrepancy between people finding the game way too easy, and people really struggling. I think this comes down to teaching the basics more thoroughly as well as giving a few hints about good strategies during the tutorial. 

It's fortunate I made this devlog when I did because now we can easily have a direct comparison between the before and after of a single moderately successful YouTube video. The Discord has gained 5 members in this time in relatively quick succession. I know that doesn't seem like a lot but I think Discord members are far more valuable than player metrics as they tend to provide more feedback and be more invested in the game's development.

Speaking of players, the demo has now had 475 lifetime unique users. That's not an ideal number had this demo been closer to release but considering that I still have 2 more demos to go, hopefully it's a sign of good things to come. Having this many players was really fantastic and fortunately only a couple of major bugs arose during this time which is a testament to how helpful the initial group of playtesters were in ironing out the game and dealing with lots of crashes. For future demos I will consider doing a limited release within the Discord server before re-activating them to the public as I feel this is a good way to get some immediate feedback as well as squash any major bugs.

[![image.png](https://i.postimg.cc/kXpk9QMC/image.png)](https://postimg.cc/qz2mxCCD)

The most valuable number in terms of financial success is certainly the wishlists. According to sources online, week one sales typically ends up being 10%-20% of your launch day wishlist numbers. My goal is to reach 1000 wishlists before launch, which would hopefully correlate to about 100 sales. After the video, we're now at 284 wishlists, almost triple what we had beforehand! That's still only a quarter of my personal goal, and a tiny fraction of the praised number 7000, but it's certainly a considerable uptick.

[![image.png](https://i.postimg.cc/02PBst1h/image.png)](https://postimg.cc/grtDyHJK)

And with an increase in wishlists, there's also been an increase in the rate of wishlisting. Hopefully this doesn't crash back down to zero too soon!

[![image.png](https://i.postimg.cc/gkj38RVn/image.png)](https://postimg.cc/XpMZ0rDb)

And finally we can have a look at the store page traffic. We can see the biggest spike is when I released the demo which resulted in 603 visits that day. That's then followed by Olexa's video, which climbed to 531 visits. It's kind of hard to judge where the ideal impressions to visits ratio is, but in my own opinion, 2 in 7 seems like a pretty good ratio. Hopefully this can convert to a lot more visibility during the Steam Next Fest where Steam will encourage further promotion if the ratio is good.

And there's my learnings. As was hinted, I have a bunch of these devlogs that I'll publish when the game releases which I think will be really interesting to reflect on.