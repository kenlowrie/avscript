//This is the test file for @image (and maybe @raw)
//

@var _id="_path_" path="/Users/ken/Dropbox/shared/src/script/avscript/tests/in/import" _format="{{self.path}}"
[imports]=[var._path_(path="in/import")]

@import '[imports]/image.md'

[_i_width]=[IMG_SIZE_LARGE]
[ss]=[{{img-st-inline-border}}]
[trythis]={:.red.bold}Try to get this shot
[beforeshoot]={:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION

@import '[imports]/shot.md'
@image _id="needshot" src="[imports]/needshot.png" style="[ss]"

//Use _shotinfo_ as _format string
@image _id="shot1" src="[imports]/shot1.jpg" style="[ss]"
@var _id="shot1" \ 
     desc="*Short Description Here*" \ 
     lens="**85mm**" \   
     crane="yes" \
     _format="[_shotinfo_]"
//Can be used inside a shot like this
- WS:a shot
    [image.shot1]
[var.shot1]
//Or can be used outside a shot like this
@break
[image.shot1]
[var.shot1]
//Use it @raw, except it smashes against the sides...
@raw [image.shot1]
@raw [var.shot1]

@image _id="shot0" src="[imports]/shot0.jpg" style="[ss]"
@var _id="shot0" \
     desc="*Short Description*" \
     lens="**85mm**" \
     crane="yes" \
     _format="[_shotinfo_]"

@set _="shotinfo" shotid="shot0"
[var.shotinfo]
And here is some info about shot0

@set _="needshot" shotid="shot0"
@set _="needshot"
[var.needshot]

@image _id="shot2a" src="[imports]/shot1.jpg" style="[img-st-inline]"
@image _id="shot2b" src="[imports]/shot1.jpg" style="[img-st-inline-border]"
@image _id="shot3a" src="[imports]/shot1.jpg" style="[img-st-block]"
@image _id="shot3b" src="[imports]/shot1.jpg" style="[img-st-block-border]"

@var _id="shot2a" desc="shot1.jpg" lens="85mm" _format="[_shotinfo_]"
@var _id="shot2b" desc="shot1.jpg" lens="50mm" _format="[_shotinfo_]"
@var _id="shot3a" desc="shot1.jpg" lens="24mm" _format="[_shotinfo_]"
@var _id="shot3b" desc="shot1.jpg" lens="70mm" _format="[_shotinfo_]"

- Single Shot Sequence
    [image.shot2a]
    [image.shot2b]
    [image.shot3a]
    [image.shot3b]

@break
## Inline SHOTS
[image.shot2a]
[image.shot2b]
[image.shot3a]
[image.shot3b]

## @raw inline SHOTS

@raw [image.shot2a]
@raw [image.shot2b]
@raw [image.shot3a]
@raw [image.shot3b]

## Splitting smart shots
@set _="shotinfo" shotid="shot2a"
[var.shotinfo]
@set _="shotinfo" shotid="shot2b"
[var.shotinfo]
@set _="shotinfo" shotid="shot3a"
[var.shotinfo]
@set _="shotinfo" shotid="shot3b"
[var.shotinfo]

## Testing namespaces

[shotinfo]
shotinfo._=[shotinfo._]
shotinfo._id=[shotinfo._id]
shotinfo.shotid=[shotinfo.shotid]
### Namespace with prefix
[var.shotinfo]
var.shotinfo._=[var.shotinfo._]
var.shotinfo._id=[var.shotinfo._id]
var.shotinfo.shotid=[var.shotinfo.shotid]

## Now just 'shot2a' in the brackets with attributes
@break
[image.shot2a]
shot2a=[shot2a.desc]
shot2a.lens=[shot2a.lens]
shot2a._format=[shot2a._format]
### with image. prefix on shot2a
[image.shot2a]
[image.shot2a.src]
[image.shot2a.style]
### with varv2. prefix on shot2a
[var.shot2a]
[var.shot2a.desc]
[var.shot2a.lens]
[var.shot2a._format]

//Variables///