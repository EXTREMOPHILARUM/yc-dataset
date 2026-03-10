# Launches

## Galaxy 🕹️ - Social multiplayer for games

**The Problem:** Mobile games are fun for a while, but players get bored quickly (especially when it’s singleplayer)

**The Solution:** Competing with friends makes games way more interesting

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70127&key=user_uploads/263116/31b26d16-89c8-4088-80a4-8d47611a6919)

Galaxy is a free SDK that adds **community** to any single or multiplayer game (in less than an hour). 

* _Clans_: Players can create, join, and recruit teams. They compete against other teams and can chat with the group.
* _Real Friends_: Players can sync their contacts and easily see/interact with their friends on leaderboards.
* _Avatars_: Demonstrating the authenticity of opponents amplifies the feeling of winning. It also provides an optional revenue stream to games who want to sell cosmetics.
* _Powerful Leaderboards:_ Configure & manage leaderboards from a dashboard. Set up automatic prizes, repeating tournaments, ban users, customize UI, and more.

Players love it. Session length increases by \~1m55s and D7 retention rises by as much as 37%. Additionally, teams encourage players to invite their friends who don’t already play the game - leading to free user growth as well. Here’s a graph from one of our customers after they added Clan leaderboards:  

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70127&key=user_uploads/263116/a21e9395-7c8f-4bdd-b6bf-48c1949b33a9)

But what about implementation? We’ve worked hard to make it as simple as possible to implement. Here’s the steps:

1. Call ReportScore()
2. Call ShowLeaderboard()

That’s it! The UI is customizable, localized and works on mobile or web.

We’re already working with 115 games and serving over 250,000 end users. You can [sign up](https://galaxysdk.com) for free or [book a call](https://calendly.com/adambn/galaxy-sdk) if you’re interested.
