# Sleep Process and Policies

Regularly getting good sleep is the single most important physiological factor for maintaining my energy, intentionality, and focus. 

Almost everyone has felt for themselves much of a drag it is on their effectiveness to be tried or sleep deprived during the day and it's common wisdom that it's important and healthy to "get enough sleep" is good for you. But I've found that there's a level *beyond* merely getting enough sleep. 

When I get 9 hours of very high quality sleep (resting heart rate below 51, HRV above 50), what I wimsically call "mega sleep", my focus and alertness is palpably better than baseline. It's like being on a stimulant, except it's the best stimulant I've ever tried, without the attendant contraction of my awareness (or other side effects). It feels amazing, and I have some much energetic capacity for doing stuff and making progress.

Additionally, while focusing hard for many days in a row is draining, I find that I get most of the benefits of a rest day from high quality sleep. Sleeping deeply for 9 hours every day gives me the physiological capacity to lock in on a project and work for weeks at a time.[^1] 

For theses reasons, the *foundation* of my systems for maintaining high momentum and energy is to prioritize getting very high quality sleep, on a daily basis.

Sleep is not the end all be all. Even when I'm getting megasleep, I need to make sure not to mess up the energy benefits by eating at the wrong times. And having that expanded capacity, I need to additional make sure to spend it well, instead of frittering my focus away on low value distractions. But I'm so much more effective when I'm extremely well rested, that sleep (and exercise, which supports my sleep) is the single highest priority of my self-support systems.

<TOC>

## Meta

The main sleep metric that I optimize is my average HRV over the period that I'm asleep, measured by my oura ring. I keep an eye on a few other metrics (also measured by oura) as well, including lowest resting heart rate, total sleep time, sleep efficiency, and sleep latency. 

Also, before I look at any oura data, every morning, I log my subjective feeling of restedness and alertness. That, along with my focus data <link after I've documented my focus tracking system> and tracking when I ship something,  can serve as an outer loop verifying that nighttime HRV actually translates into the outcomes I care about.

I used to test interventions by doing occasional randomized controlled trials. For about the length of a month, I would flip a (digital) coin every night to randomize whether I took a particular supplement or did a particular sleep intervention, and then I would compare to my oura data after the fact.

These days, I use my [sleep bandit app](https://github.com/Etyre/sleep-bandit) instead, which more elegantly addresses the explore exploit tradeoff. Every night, the app randomly assigns an intervention (and in some cases a dosage) with the measured probability that that intervention improves my nighttime HRV, based on past data.[^2] Now, I'm continually testing interventions, and I'm not giving up the benefit of an intervention that works, 50% of the time, while testing it.

Interventions in this doc are recorded along with their current measured effect on my nighttime HRV compared to the baseline nights, when I don't use that intervention. (My nighttime HRV has been improving over the past year, and in recent months, and this does introduce a bias that might be inflating these estimates in the short term, but they should converge eventually.)

## Schedule

I’ve lived on a number of different sleep schedules, depending on the circumstances, and the people that I’m working with, including waking up at 4 or 5 in the morning, waking up at 10 or 11 in the morning, and waking up at 4:00 in the afternoon and mostly being awake during the night, and even a [26 hour schedule](https://xkcd.com/320/) in which my sleep periods are not synced up with the days of the week.

Since 2021, I’ve kept to a mostly biphasic sleep schedule: Sleeping for 6 to 9 hours at night, and about an hour in the mid to late afternoon. 

Historically, on days when I don't nap, I've felt notably more tired by the evening, and am a lot less motivated to get stuff done. By napping in the middle of my day, I effectively get two, stacked, high focus work days for each calendar day. But, as my sleep quality has improved and I get mega-sleep more often, I find that an afternoon nap is less important.

At the time of this writing, I wake up at 9:30 AM, and go to sleep at about 12:30 AM, with a nap from about 4:30 to 5:30 or 5:00 to 6:00 in the late afternoon. When I’m on an earlier or a later schedule, all the times in this document are adjusted up or down accordingly.

## Sleep-supporting practices

### Support for sleep during the day

#### Exercise

One of the clearest impacts on my nighttime HRV is doing [intense exercise](elityre.com/exercise-policy.html), and [Cardio Interval Training](https://elityre.com/exercise-policy.html#cardio-interval-training) in particular, during the day. 

Analysis of my sleep data shows that very roughly, every day of intense cardio interval training *depresses* my nighttime HRV by about 1-1.5ms, that night. But after that short term effect, each interval session *raises* subsequent nighttime HRV by about 1 ms, and that effect decays with a half-life of roughly two to six weeks. 

If that model is trustworthy, one day of cardio interval training tends to have an effect of about +0.7 ms on every night over the next month. Further, doing cardio interval training every 3 days for 90 days has a total accumulated effect of +11.5 ms on the night of the ninetieth day, and training every other day has an accumulated effect of +17.5 ms on the ninetieth day (though this is going out on a bit of a limb, since it's ignoring likely saturation effects, and I don't have enough measured data to verify yet). 

In practice I typically do cardio interval training between every other and every third day. 

### Pre-sleep routine

#### Pre-sleep fast

I don’t eat anything for at least four hours before bed. The cutoff for the last time that I'll eat anything is 7:00 pm.

However, I will sometimes drink liquid meal replacement (Soylent or huel) in the hours before, or even immediately before bed. I haven't observed this to have an impact on my sleep metrics.

#### Supplements

Every night, around a half hour before I go to sleep (usually just before I leave the office), I take...

* 0.3 mg of melatonin[^3] [+3.1 ms] 
* 150-200 mg of apigenin [+5.7 ms]
* 1000-4000 mg of Glycine [+4.5]

I’ve set an alarm that rings at (currently) 11:40pm as a signal to wind down work, brush my teeth, and take my sleep supplements. 

I used to take...

* 200 mg of L-Theanine
* 144 mg of Magnesium L-theronate

...but both of these had a negaitve effect on my sleep metrics, -1.6 ms, and -5.2 ms, respectively. The 

Magnesium in partcular passes through the blood brain barrier, and is supposed to have recuperative benefits (eg it helps replenish depleted neurotransmitters). Perhaps thes benefits outweigh the measured cost on my recovery? Maybe I should only take Magnesium on particular days (days where I took an anphatmine?) Maybe if I took it earlier in the day it would have less of an impact on my sleep? All of this is currently unclear.

### Pre-sleep behavioral interventions

#### Big six lymph reset

After I take my sleep supplements, I'll do a big six lymph reset as described [here](https://www.youtube.com/watch?v=lT_wW5pNHa4). [+3.3 ms]

#### Acupressure mat

[Data is still coming in for this one]

### Sleep systems and setup

- I use mouthtape while I sleep, to induce me to breath through my nose instead of my mouth. I don’t know if this improves my sleep, but I buy that it is good for my overall health, and possibly improves my allergies.[^4][^5]
- I sleep with an air conditioner, set to 61 degrees, in my personal room pointed directly at my face. Being in a cold room, or having cool air blown over me, helps me fall asleep. [+5.4 ms]
  - The air conditioner is on an outlet timer, so it turns off automatically about an hour before my wakeup time. There's more resistance to waking up and getting out of bed immediately if it's cold, so having the air conditioner turned off helps.
  - In the office sleep-space where I nap, I use a fan pointed at my face. And I use a mini-fan when I travel.

- I additonally use a chili pad, set to somewhere between 13 and 25 degreees celcius. [+2.8 ms]
- I have two sets of lights in my room: red lights that I turn on when I enter my room after coming back from work in the evening, and a set of two [36 watt 3300 lumen corn bulbs](https://store.yujiintl.com/products/cri-max-cri-95-e27-36w-led-corn-bulb-3200k?_pos=1&_sid=6d2a1c3c6&_ss=r), that I use in the morning. 
  - The switch to the corn bulbs is attached to the air conditioner next to my bed. The first thing that I do as soon as I wake up, in the second or two before I get out of bed, is reach over and turn on those lights, to fill my (blacked out) room with light.

- In my personal room, I sleep with a weighted blanket.
- I block out all the light in my room, covering the windows with cardboard panels, and filling the gaps with aluminum foil secured with painters tape. I additionally hang blackout curtains over the windows. I crack the window to allow for circulation, but have attach a strip tinfoil or blackout cloth to the top of the window, covering the gap.
  - Just using blackout curtains is insufficient if I'm on a late or nocturnal schedule in which my sleep period overlaps with the sun. I find that if I sleep in a room that has some light leakage, I feel subtly *off* all day long. If I’m asleep during a period that overlaps substantially with when the sun is up, I need to sleep in a very dark space, or I’ll feel groggy all day/night long. I want my room to be dark enough that I can't see the objects and furniture in it, even in the middle of the day. This is seem to be adequate enough for me to be sharp on a late schedule.
    - If blocking all the light in a room isn't easy, I've  sometimes slept in a closet, or with a four-panel shelter of balsa wood long enough to enclose the top half of my body, in a merely-normally dark room, instead of a pitch black room. This seems to work adequately as well.
- I make it easy to get up to pee in the middle of the night.
  - This sounds kind of silly, but I have sometimes find that I sleep badly because I’ll wake up in the middle of the night with a full bladder. I should get up and pee, but because there are a number of steps between me and the bathroom (maybe I need to put on a robe, or navigate around a desk that I can’t see well in the dark), I have an aversion to getting up, and I just stay there in bed and then fall back into an uncomfortable, restless sleep.
  - I can circumvent this via future-pacing and rehearsal. I’ll practice, when I’m awake, the steps that I need to take to go pee. Then when I wake up in the middle of the night, that’s the default action.
  - When I have been on a schedule where my sleep window overlaps with the sun substantially and I've gone to lengths to block out all the light entering my room, but the nearest bathroom is not similarly shielded, I've kept a two gallon jug partially filled with water in my bedroom. If I get up in the middle of my sleep period to pee, I can pee in the jug and then dump it out the toilet after I get up for the day.

### If I’m restless

Mostly, I don’t have any difficulty falling asleep these days. In the past, I would sometimes lie down to go to sleep and my mind would be churning or my physiology activated, or otherwise not be able to fall asleep. That doesn’t really happen any more. I’m not sure why. Presumably one or several of the interventions above resolved it.

That said, if I've been lying in bed for 40 minutes or more, and haven't fallen asleep yet, I'll get out of bed and do something else (as is the standard recommendation). However, when I get up like this, there are only three activities that I allow myself, so that I don't get hooked by something stimulating and stay up for an extra hour when I could have been asleep.

##### Journal

I have a chromebook that is set up just for journaling. I've blocked that everything except roam, google docs (for my tracking spreadsheets and forms), and toggl.

This way, when I'm restless, I can get up and journal in Roam, typically outlining and thinking through whatever churning thoughts were keeping me awake, without the temptation of browsing the internet more generally (which is motivationally-sticky, and doesn’t help me get to sleep).

##### Meditation/HRV breathing

Alternatively, I might get up and either meditate or do a few minutes of HRV breathing (probably with biofeedback) to increase my parasympathetic activation.

##### Drink Soylent/Huel

Eating actives the parasympathetic and enteric nervous system, and is one way to calm sympathetic activation. That's why stress eating is a thing.

However, eating in the hours before bed harms sleep quality. So it isn't a good idea to eat just before bed.

However-however, my initial experiments suggest that liquid food doesn't worsen my sleep, so I'll sometimes have a bottle of soylent or huel non-dairy milk if I'm restless.

### Waking up

One of the most important inputs to good sleep is waking up consistently at the same time every day. If I focus on making my morning wakeup good, falling asleep will follow, not automatically, than more easily than otherwise.

#### External Systems

- ~~In my personal room, I have a 12000lux light panel, attached to the wall near my bed, set on a timer so that it turns on (gradually) just before my wakeup time.~~ [Edit: this hasn't been set up for a while]
- My air conditioner is on a timer so that it turns off about an hour earlier than when I wake up. If it’s cold outside my bed at the time when I wake up, that creates a microhedonic gradient that incentivizes me to stay in bed, but I can circumvent that in a couple of ways:
  - During the winter, I’ll leave sweatpants and warm socks, right near or on my bed, to make it as easy and quick as possible to get up and get warm, instead of being tempted to stay in my cozy bed.
  - A possibly even better idea to try: set up a heating pad on a timer right at the side of my bed, so that I can wake up and step onto that.
- The main lights in my room are on a bluetooth controlled circuit. There's a switch for that circuit on my wall next to the door, for turning on the lights when I enter my room. My bed is right next to the door, such that I can reach this switch from my bed. But, I need to sit up to reach it, which is an additional bit of friction to going from asleep to awake. So I've also attached an identical switch to my air conditioner unit, that I can reach out to turn on without needing sit up.
- In the past I've put my morning checklist in a h x w picture frame, and I check off items with a whiteboard marker, without needing to look at my phone or laptop. (This is less relevant now, since I don't use the checklist any more.)

#### Behavioral practices

- I train myself to wake up, at the time I want, without an alarm.

  - As I do it, this involves setting intention to wake up at my chosen time, when I lay down to go to sleep. I'll relax my body and then verbally (out loud) affirm that I'm going to wake up at my chosen time.

    It has at least sometimes taken a few days to calibrate, but after that I will wake up automatically, within about a minute of my chosen time.

    Calibrating: I wear a watch in bed so that when I wake up in the night / morning, I can check what time it is. Crucially, if I wake up and see that it is within an hour of my chosen time, I'll get up, even if that is a bit early or a bit late. Over the course of a few days my mind and body will narrow the interval until I am waking up at my chosen time.

- I’ve further trained myself so that **when I wake up, I get up, and spring out of bed, immediately**, and then do 25 to 30 jumping jacks. This allows to start the day with momentum, which can carry through for hours.

  - I built this habit with offline habit training: practicing, (during the day, when I'm fully awake), laying down in bed with my eyes closed, and then opening my eyes and jumping out of bed. I do 10 reps of this, being careful to reset after each one, so that I'm not practicing _getting back into bed_, each time.
  - I've sometimes used a mantra in this moment as well, to remind me of my intention or why I care about getting up. When I was a teenager, I used to wake up at 5:00 AM to get up and meditate and do "energetic exercises" (as part of astral projection training). I used to say, as I got out of bed "this is what it means to be a wizard", particularly in the months when it was cold.

- One of the first things that I do in the morning is brush my teeth, outside. This means that I get sunlight exposure to my eyes, first thing in the morning, which reinforces / resets my circadian rhythm, to make it easier to fall asleep at the time I want.

**See also:**

- [Napping protocol](https://docs.google.com/document/d/1ctnO9pwF7Ti7AjyYGoSiiTzAHidUZn-mZ4EvwHqPl9M/edit#heading=h.i24l245gvr44)
- [Sleep deficit compensation procedures](https://www.notion.so/Sleep-deficit-compensation-procedures-5ecebd076d7446fd99e2d2f62961ae5b?pvs=21)
- Morning routine

[^1]: The physiological component is only half of the equation, however. The other half is psychological—a matter of meaning and value to me rather than just biological capacity. The work has to be worth for me to dedicate myself to it like that.

[^2]: Actually, it's not quite that simple, because there are some built in adjustments that compensate for small sample sizes, which nudges the system toward correcting possible self-reinforcing errors faster.

[^3]: For more on the impact of melatonin, [Gwern’s page](https://gwern.net/melatonin) says it all.

[^4]: When I first decided that I wanted to start mouthtaping, it wasn’t feasible for me. I just couldn’t breath through my nose well enough, while lying down, to fall asleep. (For a while I had a [bounty](https://elityre.com/bounties.html) up, requesting a way to learn to breath through my nose.) I eventually solved this by taking a nasal decongestant that cleared up my nose enough that I could fall asleep with mouthtape on, and after a few nights of that, my sinuses opened up enough that I was able to breath through my nose normally. I think that for the first 27 years of my life, my sinuses were chronically inflamed, but practice breathing through my nose started a positive feedback cycle.

[^5]: I used to get conjunctivitis, in the springtime, reliably, just about every year. I think this is because I would have seasonal allergies, which would cause me to rub my eyes, and then rubbing my eyes would cause them to get infected. I haven't had conjunctivitis since 2021, which is the year that I started mouth taping.
