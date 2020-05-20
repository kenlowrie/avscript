//This is the test file for @image (and maybe @raw)
//

@var _id="_path_" path="/Users/ken/Dropbox/shared/src/script/avscript/tests/in/import" _format="{{self.path}}"
[imports]=[var._path_(path="in/import")]

@import '[sys.imports]/image.md'

[IMG_SIZE_LARGE]
[ss]=[{{var.img_def.img_st_inline_border}}]
[trythis]={:.red.bold}Try to get this shot
[beforeshoot]={:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION

@import '[sys.imports]/shot.md'
@image _id="needshot" src="[imports]/needshot.png" style="[ss]"

[shot_factory(nm="shot1")]
[var.shot1._null_(d="*Short Description Here*" c="yes" l="85mm")]
[img_factory(nm="shot1" s="[imports]/shot1.jpg")]

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

[shot_factory(nm="shot0")]
[var.shot0._null_(d="*Short Description*" c="yes" l="85mm")]
[img_factory(nm="shot0" s="[imports]/shot1.jpg")]

//@image _id="shot0" src="[imports]/shot0.jpg" style="[ss]"
//@var _id="shot0" \
     desc="*Short Description*" \
     lens="**85mm**" \
     crane="yes" \
     _format="[_shotinfo_]"

[var.shotinfo2(shotid="shot0")]
And here is some info about shot0
@break

[shot_factory(nm="needshot")]
[var.needshot._null_(d="*Short Description*" c="yes" l="50mm")]
[var.needshot(shotid="shot0")]
[var.shotinfo2(shotid="needshot")]

@image _id="shot2a" src="[imports]/shot1.jpg" style="[var.img_def.img_st_inline]"
@image _id="shot2b" src="[imports]/shot1.jpg" style="[var.img_def.img_st_inline_border]"
@image _id="shot3a" src="[imports]/shot1.jpg" style="[var.img_def.img_st_block]"
@image _id="shot3b" src="[imports]/shot1.jpg" style="[var.img_def.img_st_block_border]"

[shot_factory(nm="shot2a")]
[var.shot2a._null_(d="shot1.jpg" c="yes" l="85mm")]
[shot_factory(nm="shot2b")]
[var.shot2b._null_(d="shot1.jpg" c="yes" l="50mm")]
[shot_factory(nm="shot3a")]
[var.shot3a._null_(d="shot1.jpg" c="yes" l="24mm")]
[shot_factory(nm="shot3b")]
[var.shot3b._null_(d="shot1.jpg" c="yes" l="70mm")]

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
[var.shotinfo2(shotid="shot2a")]
[var.shotinfo2(shotid="shot2b")]
[var.shotinfo2(shotid="shot3a")]
[var.shotinfo2(shotid="shot3b")]

## Testing namespaces

[shotinfo2]
shotinfo2._=[shotinfo2._]
shotinfo2._id=[shotinfo2._id]
shotinfo2.shotid=[shotinfo2.shotid]
### Namespace with prefix
[var.shotinfo2]
var.shotinfo2._=[var.shotinfo2._]
var.shotinfo2._id=[var.shotinfo2._id]
var.shotinfo2.shotid=[var.shotinfo2.shotid]

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

@dump var=".*shot" image="."