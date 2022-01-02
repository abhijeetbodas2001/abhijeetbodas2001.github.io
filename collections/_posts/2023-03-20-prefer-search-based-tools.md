---
layout: post
---

Recently, I've taken to classify software into broadly 2 categories:

1. One where you tell the software what to do, and it does that
2. Another where the software shows you what you might want to do, and you do
   that

Today, most software seems to fall into the second type, because of overuse (and
abuse) of recommendation systems and algorithms. Such software is usually
"in-your-face" -- the moment you open the app/website, it will throw a bunch of
stuff at you, with the hope that you find something interesting in it. The
obvious examples of this are social media feeds, news sites, the YouTube
homepage, and the like.

The not so obvious ones are things like instant chat applications and app
launchers on smartphones. When you open your chat app to message someone, if the
app shows you "unread" chats at the very top, its a sign the app falls into the
second category. App launchers on smartphones which show recently used apps at
the top, or, even if not, bunch together all the apps in a single list/grid for
the user to search through, fall into this category as well.

If one has _any_ intention to be productive, it is obvious that the second
category apps are not helping. Software is a tool for knowledge workers, just
like the hammer is a tool for the blacksmith. The difference is, it is pretty
much impossible for a blacksmith to get distracted (_because of the hammer_)
while using a hammer. With software, that is not the case.

Even in leisure time (when not "working") it is easy to get overwhelmed with the
information and content thrown at you by type 2 apps, and forget what you really
wanted to do. Most people would remember the time when they opened YouTube to
search for/get to a specific video they know exists, but ended up clicking on a
shiny homescreen recommendation, only to suddenly remember an hour later why
they had come to https://www.youtube.com/ in the first place. Or, when they
opened WhatsApp to send a message to someone, and forget "that" someone (as well
as the message they had meant to send) when they see the pile of green unreads
waiting to be opened.

The solution to this? Search-based tools, I propose. This method is more about
_how to make your tools search-oriented_ than about _how to switch to
search-oriented tools_, since the tools themselves often can't be replaced for
various reasons. I'll explain this method with some examples:

1. **YouTube**: Install [uBlock Origin](https://ublockorigin.com/), and remove
   the recommendation elements one by one, using the
   ["element picker"](https://github.com/gorhill/uBlock/wiki/Element-picker).
   Or,
   [directly use the filters which I use](https://gist.github.com/abhijeetbodas2001/e0c330c83e5b7929d41abb163b046e11).
   Here's what my YouTube homescreen looks like:

   <img src="/assets/posts/2023-03-20-prefer-search-based-tools/YouTube.png" width="100%"/>

   Even the video player page is much cleaner than th default one.

   Another solution is to use the
   [YouTube search engine](https://addons.mozilla.org/en-US/firefox/addon/youtube-search-engine/)
   add-on on Firefox.

   On mobile, [NewPipe](https://newpipe.net/) allows hiding all recommendations
   and comments. (But its a fantastic client even if you don't want those
   features!)

2. **WhatsApp**: "Permanently Archive" _all_ your chats. Yes, all of them.
   Here's what my WhatsApp landing screen looks like:

   <img src="/assets/posts/2023-03-20-prefer-search-based-tools/WhatsApp.jpg" width="100%"/>

   When I open the app to text someone, I simply click on the search icon, and
   go to the chat window with that person directly.

   A few times a day, I will intentionally open the archived pane to read other
   stuff people have sent. Emphasis on the word _intentionally_.

3. **Smartphone Homescreen**: Just use
   [KISS Launcher](https://kisslauncher.com/).
4. **Browsers**: This is easy. Turn off all News/Recently opened/Recommendation
   elements on the browser. Or just set the "New Tab" page to be a search
   engine. Most browsers allow doing this even today, thankfully.

I hope you get the idea. I've implemented things like these for quiet some time
now to make visually cluttered and bloated software more usable. It's debatable
whether the Search Box is the only UI element which most apps ever need (apart
from the main content in the app itself). But it can't be denied that easy to
access search elements make software a lot more efficient to use.
