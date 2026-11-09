# Custom Software

<TOC>

### Tracking and logging
* **[Focus and distraction monitor](https://github.com/Etyre/focus-and-distraction-monitor)** - Watches the active window on your Mac, uses an ensemble of models to evaluate periods of focused vs unfocused attention and when the object of attention changes, and records aggregate focus data
* **[Sleep bandit](https://github.com/Etyre/sleep-bandit)** - Nightly Bayesian bandit for sleep interventions (HRV/resting HR), scored against Oura
* [**Meditation timer/logger iphone app**](https://github.com/Etyre/meditation-app) - A meditation timer for iPhone with a gong, overtime stopwatch, heartrate monitor integration, and session logging
* **[Ecological Momentary Assessment iphone app](https://github.com/Etyre/EMA-app)** - Random-interval experience sampling (EMA) app for iOS/Android, syncing to Google Sheets
* **[Randomized presence checker](https://github.com/Etyre/randomized-activity-based-google-form-activater)** - Opens a Google Form survey in the browser at random intervals, for experience sampling from a Mac
* **[Exercise tracker iphone app](https://github.com/Etyre/exercise-tracker)** - A phone app for logging workouts, with the data mirrored to a Google Sheet as the long-term record
* **[Phone unlock logger](https://github.com/Etyre/phone-unlock-logger)** - Logs every iPhone unlock, whether a notification seems to have caused it, and every stretch an app was on screen, to measure how strongly stimuli pull attention in the hours after meditation
* **[Claude usage dashboard](https://github.com/Etyre/claude-usage-dashboard)** - A local, auto-updating dashboard of what I spend on Claude: tokens and dollars per day, per app, per model, and per billing source

### Software devlopement and AI agent management tools
* **[Agent Coding UI](https://github.com/Etyre/agent-coding-UI)** - A Typora-style wrapper around terminal sessions for running several Claude Code sessions side by side, each labelled with the project it is in and showing which one is waiting for input, and none of which die when the app relaunches or the Mac reboots
* **[LLM inbox](https://github.com/Etyre/llm-inbox)** - A local web page for reading the messages that the models inside my apps send me, and talking back to the same model
* **[iOS auto deploy](https://github.com/Etyre/ios-auto-deploy)** - Keeps the iPhone's copy of each of my Flutter apps current with the latest commit, over Wi-Fi, with nothing to tap on the phone

### Composition tools 
* **[Literal](https://github.com/Etyre/literal-markdown)** - A WYSIWYG Markdown editor for macOS that never hides or rewrites a line: every blank line and every indent on screen is exactly what is on disk. (I was previously using Typora, but that was doing weird stuff where it would hide some of the line breaks.)
* **[History mapper](https://github.com/Etyre/history-mapper)** - Software for outlining the great web of historical cause and effect

### Personal espistemics augmentation
* **[Nosey fact checker](https://github.com/Etyre/nosey-fact-checker)** - A macOS menu bar app that watches my screen and flags statements that are false or misleading, using Claude

### Anki and roam integrations
* **[Claude in Roam / Claude in Logseq](https://github.com/Etyre/logseq-and-roam/tree/main/claude-chat)** - Ask Claude from a block and get the reply streamed into nested blocks, then keep the thread going by typing in the next block
* **[Auto-anki](https://github.com/Etyre/logseq-and-roam/tree/main/auto-anki)** - Claude writes and maintains Anki flashcards under a tagged block in Roam or Logseq, reading the surrounding blocks as source material
* **[ankify_logseq](https://github.com/Etyre/logseq-and-roam/tree/main/ankify_logseq)** - A port of ankify_roam that syncs blocks tagged #ankify from a Logseq graph to Anki
* **[Roam to Logseq converter](https://github.com/Etyre/logseq-and-roam/tree/main/switching-from-roam-to-logseq)** - A one-shot, reversible converter for moving a 300k-block Roam graph to Logseq, plus the hourly backup that protects the result
* **[Logseq plugins and Roam add-ons](https://github.com/Etyre/logseq-and-roam/tree/main/logseq-plugins)** - Ten small plugins that recreate what I relied on in Roam: Roam-style inline checkboxes, random page, auto-collapse, expand buttons, template commands, page tag inheritance, backwards embeds, and persistent block ids
* **[Otter import](https://github.com/Etyre/logseq-and-roam/tree/main/otter-import)** - Pulls my Otter.ai transcripts into Roam or Logseq, one block tree per recording
* **[LLM inbox for Roam and Logseq](https://github.com/Etyre/logseq-and-roam/tree/main/llm-contact)** - Lets the models running inside my graph send me messages, which land in the shared LLM inbox below
* **[Folk to Anki](https://github.com/Etyre/folk-to-anki)** - Finds the people I've met or am about to meet (from my calendar) in a folk CRM and builds Anki cards for them from my networking templates

### Executive function support
* **Executive assistant agent](https://github.com/Etyre/executive-assistant-agent)** - A personal executive-assistant agent that watches my metrics (Toggl, the focus monitor, Oura, my exercise log), keeps my project tracker current, keeps a dated searchable memory, and talks with me through its own iPhone and Mac apps, a web page, and live phone calls
* **[Project tracker](https://github.com/Etyre/project-tracker)** - A personal GTD system with a project hierarchy, a Claude-powered quick-add, and a feed that serves one card at a time from a schedule rebuilt from my calendar, daily checklist, exercise sheet, open tasks and my own rules document, filing time into Toggl and mirroring Linear
* **[Nighttime internet blocker](https://github.com/Etyre/nighttime-internet-blocker)** - Blocks the internet on my Mac from midnight to 6am, with a short allowlist and a 60-minute override that you have to type out by hand
* **[Meeting alerts](https://github.com/Etyre/meeting-alerts)** - A tiny native macOS app that posts a notification 10 minutes before every meeting, with a title that counts down until it starts

### Feeds and Information filtering
* [**Personal recommender feed app**](https://github.com/Etyre/recommender-feed-app) - A personal reading feed, ranked by LLM agents according to marginal value, that learns user taste from ratings
* **[Filtered Twitter](https://github.com/Etyre/filtered-twitter)** - A calm desktop client for X: one finite edition of about 100 posts a day, chosen for me, plus the replies and mentions that need an answer, and nothing that scrolls forever

### Personal training and deliberate practice environments
* [**Arithmetic training desktop app**](https://github.com/Etyre/arithmetic-training-app) - A simple adaptive flashcard app for learning arthmetic
* **[Deliberatetyping.app](https://deliberatetyping.app/)** - A web app for practicing typing and  spelling, focusing specifically on words that the user has misstyped historically.

### Automations
* **[Bayesian Tinder Swiper](https://github.com/Etyre/bayesian-tinder-swiper)** - A webapp that swipes tinder, prompting claude to do a Bayesian analysis of the probability that a given person is vegan or vegetarian, and swiping right if the probability is greater than some threshold.
* **[Feeld Swiper](https://github.com/Etyre/feeld-swiper)** - A local web app that swipes Feeld for me, driving the app on an Android emulator. Claude gives each profile a Bayesian estimate of the probability that they're vegan or vegetarian and a separate score for fit, likes or pings above the thresholds I set, and drafts openers for the best matches





See also: [my personal computer setup](Computer setup.md)



