# 2020 /r/CFB Tech Challenge

## Overview

/r/CFB has a suite of tools that's pretty neat. We're a volunteer team, and here are a few short challenges to give you a taste of what the tech side of /r/CFB is like! Most of our work is done in Python, SQL, and some PHP. Background in API design could be helpful, too. We also can always use help with art and design.

Here are some open-ended problems below that we'd love to see what you come up with. We'd be interested in what you can do with this data on a recurring basis, so feel free to attempt it any time!

### Web Development

### [Codepen Link](https://codepen.io/backonydraco/pen/XWPMagR)

The link above has a version of our https://banners.redditcfb.com site that showcases a historical archive of the banners that have been displayed on /r/CFB. We’d love for you to improve it!

* Modify the CSS to make it easier to read.
* Modify the HTML to add contextual info.
* Add JS for additional functionality.

**Desired Output:** A link to your saved fork of the codepen. Share the link with us by [sending us a modmail](https://old.reddit.com/message/compose?to=/r/CFB&subject=Tech%20Challenge - Web Development)!

## SQL

* Go to the [SQL Challenge](https://github.com/redditCFB/-r-CFB-Tech-Challenge/tree/main/SQL%20Challenge) folder in this repo.
* There are two tables that you can download as either *.csv files or *.sql files, and manipulate however you like.

### flairuserdata

This is a table that compiles everyone who had positive total comment karma on /r/CFB over a 3 month period (a few years ago) by the number of comments they made and their total karma. It's lightly anonymized by showing their primary flair rather than their username.

### teamsheet

This is a simplified version of the table we use to store all team data, just shown for D1 flair. It also includes a recent flair count.

Your task is to use information in either of these two tables to come to a conclusion that is useful! Feel free to write SQL queries or download the data as a CSV and analyze separately. Suggestions:

* What G5 teams had the most talkative users during this period?
* Which teams had the highest ratio of karma to comments?

**Desired Output:** A google doc or google spreadsheet that best articulates your finding. Share the link with us by [sending us a modmail](https://old.reddit.com/message/compose?to=/r/CFB&subject=Tech%20Challenge - SQL)!

### Python

### [Python Script](https://github.com/redditCFB/-r-CFB-Tech-Challenge/blob/main/gamethreadscraper.py)

Above is a Python script that takes the [Post Game Thread from this year's Peach Bowl Semifinal](https://old.reddit.com/r/CFB/comments/100cbyw/postgame_thread_georgia_defeats_ohio_state_4241/) and returns comments by users with Georgia or Ohio State flair that contain a certain keyword. Download this and save it under the name 'gamethreadscraper.py'. You'll need both Python and [PRAW]https://praw.readthedocs.io/en/v7.7.0/getting_started/quick_start.html).

To use it, simply run the script and put the keyword after it, for example you could run the command:

`python3 gamethreadscraper.py targeting`

and it will give you every comment in the top 1000 by a Georgia or TCU flaired users that contains the word ‘targeting' (case-insensitive). 

Your task is to build on this script to do something interesting. Suggestions:

* Which teams besides those playing were the chattiest?
* What did one team tend to say but not the other?

**Desired Output:** A link to your modified python code, explanation, and sample output. Share the link with us by [sending us a modmail](https://old.reddit.com/message/compose?to=/r/CFB&subject=Tech%20Challenge - Python)!

### Design

The biggest upset of the 2023 season has just happened! Unbelievably, [team of your choice] pulled off a massive victory over top 10-ranked [team of your choice]. As is our tradition on /r/CFB, the banner is updated to reflect this event. Here’s a big album of [“vandalisms” that never got used](https://imgur.com/a/q9oEUcu)​​ for inspiration. Your job is to make an image to include in the banner that celebrates the upset, is funny (but not *too* mean), and looks good at the size displayed on the banner (see https://banners.redditcfb.com). You can make your image at any size, but scale it down to 130x120 pixels because that’s what our banner uses.  Feel free to use any image editing software you like.

**Desired Output:** An imgur link or album with your creation(s). Share the link with us by [sending us a modmail](https://old.reddit.com/message/compose?to=/r/CFB&subject=Tech%20Challenge - Design)!
