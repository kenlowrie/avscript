[title]=*Title of Project*
[artist]=Artist Name
[thisproject]=Music Video Treatment
{:.blue.center}# [thisproject]
[revision]=1f
[proj_desc]=This is the proposed music video treatment for the upcoming **[artist]** single titled [title].

@var _id="_path_" path="/Users/ken/Dropbox/shared/src/script/avscript/tests/in/import" _format="{{self.path}}"
[imports]=[var._path_(path="in/import")]
@import '[imports]/cls-noreviewer.md'
@import '[imports]/shortcuts.md'
@import '[imports]/film.md'

[mom]={:.cast}MOM
[daughter]={:.cast}DAUGHTER
[son]={:.cast}SON
[grocerybags]={:.props}Grocery Bags
[keys]={:.props}KEYS
[note]={:.props}The Note
[food]={:.props}Food items
[cap]={:.props}Baseball Cap
[picture]={:.props}Framed Family Picture

//-------------------------------------------------------------------
[prodnotes]={:.indent}We want to shoot between August 13th - August 17th, based on schedules. Prefer if cast can be available to shoot any day/time (weekdays, evenings or weekends), but we will work around schedules. Primary location will be NE San Antonio. 
[section-pbb] [title] Music Video Casting Call and Character Breakdown
**Production Title:** [title][b]**Independent/Student/Studio:** Independent[b]**Production Type:** Music Video[dblbrk]**Production Location:** NE San Antonio[dblbrk]**Production Start Date:** 08/05/2018[b]**Production Wrap Date:** 08/20/2018[b]**Production Schedule:** August 13 - 17 (*Preferred*)[dblbrk][prodnotes]

**Producer(s):/Director(s):** [Cloudy Logic Studios]

**Synopsis:** “[title]” will be a combination narrative and performance video. The song is about ...

[plain] Character Breakdowns:

***All parts are non-speaking, and we are in search of actors that are able to emote well, especially for the role of [mom].***

Ethnicities aren't important, however, we will try to cast the [mom], [son] and [daughter] roles with actors that *could be* related.

[familypix]=*Must be available to take family pictures before production begins.*
[mom] (Female, 35-45) This is the lead role in the video. Mother arrives home and discovers... In the various scenes, we follow her through ... This character will be a very emotional role throughout the video. [familypix] 

//several She goes from panic and alarm to anger and depression, and then to acceptance. 

@import '[imports]/image.md'
[_i_width]=[IMG_SIZE_LARGE]
[framegrab]=*NEED FRAME GRAB FROM VIDEO HERE*
[ss]=[{{img-st-inline-border}}]
[trythis]={:.red.bold}Try to get this shot
[beforeshoot]={:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION

@import '[imports]/shot.md'
@image _id="needshot" src="[imports]/needshot.png" style="[ss]"

// -------------------------------------------------------------------
[scene] Scene 1 - [narr] Location S:0 (Instrumental)
    [wardrobe]
    [props] [grocerybags]
    [makeup]
    [cast] [mom], [daughter]

@image _id="shot0" src="[imports]/shot0.jpg" style="[ss]"
@var _id="shot0" \
     desc="[ws]Crane high shooting over car" \
     lens="24mm" \
     crane="yes" \
     _format="[_shotinfo_]"
@set _id="shotinfo" shotid="shot0"
[var.shotinfo]
[slate]
Probably just use the [title] and [artist] titles on this shot.
[comment]This needs to start high enough up that you can't see the trunk, and make sure the sky is NOT blown out! It comes down to reveal [mom] opening trunk and reaching in to grab groceries.

@image _id="shot1" src="[imports]/shot1.jpg" style="[ss]"
@var _id="shot1" \
     desc="[ws]Crane Down to Mom removing groceries" \
     lens="24mm" \
     crane="yes" \
     _format="[_shotinfo_]"
@set _id="shotinfo" shotid="shot1"
[var.shotinfo]
[comment]Make sure [mom] is already moving when she comes into frame.
@break

// -------------------------------------------------------------------
@break
[section] [narr] continues - Location S:15 L:~14s-

[which]=Song Lyrics
[lyric]=I'm sorry momma[b]that you're reading this[b]I always wanted to make you smile[b]so I must go on with this 
@raw [verse]

@break
// -------------------------------------------------------------------
[plain] Scene 99 - (Random Stuff)

[stockshot]=- [{{stock}}]

[stockshot] Clips of moments from his life
Various shots implying flashbacks to memories or moments of his life. *If needed*

[stockshot] Possibly one w/[mom] comforting son
Show his smile. Return to stock image. *If needed*

//
@break
[section] Cast Headshots
[headshots]=[imports]
[sTAW]=Source: TAW

@image _id="actress1" src="[headshots]/actress1.jpg" style="[ss]" _name="Actor1 Name" _source="[sTAW]"
@image _id="actress2" src="[headshots]/actress2.jpg" style="[ss]" _name="Actor2 Name" _source="[sTAW]"


[_i_width]=[IMG_SIZE_SMALL]
[backup]=**BACKUP CAST MEMBER**
[tnted]=**TNT SENT**

## For the part of [daughter]
[image.actress1] [actress1._name] - [actress1._source]
[image.actress2] [actress2._name] - [actress2._source]

{:.pbb} ## Proposed shooting schedule
Originally, production was planned for August 2018, but it has been delayed until September due to scheduling conflicts of both cast and crew. We are anticipating two to three (1/2) days for production as follows:

[scene] Scene 3 EXT
    Cast: [mom], [daughter], [son]
    Info: One (1) production day, evening shoot, *call time **5pm**, wrap time **8pm***.

[scene] Scene 1 EXT & Scene 2 INT
    Cast: [mom], [daughter]
    Info: 1/2 Production day, *call time **8a**, wrap time **12pm** (noon)*

[scene] Scene 4 INT & Scene 5 EXT
    Cast: [mom]
    Info: 1/2 Production day, *call time **3p**, wrap time **8p***. This could be scheduled the same day as Scenes 1 and 2 if the actor is available and prefers this option (longer day)

**NOTE:** Actual shoot days will be scheduled according to cast availability

@dump basic="." images="." var="." link="."
///Shotlist///
