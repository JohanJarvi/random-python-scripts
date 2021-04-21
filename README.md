# Random Python Scripts
Just a collection of random python scripts that I have written as fun little things I think of and/or to help my normal 9-5 workday be more productive.

## Scripts

### POMO

This is currently a console app that is pretty crudely written but it works. It is to show the pomodoro technique in action and tells you through Linux 
desktop notifications that it is time for a break and also when it is time to jump back into the action. I find that using the pomodoro technique can 
sometimes jumpstart my productivity if I am struggling with some really difficult problem as thinking super hard for 25 minutes knowing that you will 
be rewarded with a 3-5 minute break afterwards and easy. Once I force myself to then do a couple of these pomoodoros I find that I very often lose track
of both time and the breaks and all of a sudden I have worked for 4 hours straight without blinking and that difficult problem is almost solved. 

Whether the pomodoro technique is for you or not it is very easy to use - especially on Linux right now. I haven't tested the desktop notifications on any
other system.

### Time Left

This one is just a basic little fun experiment I did to play with some File IO. But it does help me from time to time because working remotely and having
very flexible hours I sometimes wonder come Friday how much time I have left to work to fill my 38 hour quota. It's not for everyone - many people enjoy
working more than 38 hour weeks and many people probably are more task orientated then time orientated but even though I am working remotely and have no
one watching over me I like to create the illusion that I am in an office from 9-5 every day. Clock in, clock out. Even if I do those hours much more 
sporadically.

Of course this console application only works if you are very diligently tracking your hours by some other means. For example, I run a stopwatch when I am
working and I pause the stopwatch when I am not. Then when I decide that I have had enough of a day I write it down. This then works well with the `how-much-time-left-this-week.py`
script as it takes a comma seperated list of hours in the format of "H.mm" and then spits out a "you have worked X amount, you have Y amount left".
