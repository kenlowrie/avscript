//@debug
@embed 'filename' - like @import, except just includes the code without processing. Could be useful for inserting raw html directly into the output, w/o processing at all. Would be especially cool if you could do this inline, like this:
&#91;myvar]=@embed 'foo.html'
Then, the embedded file would be marked down as normal, giving more flexibility. This wouldn't work, though, because it would have \n in the input, and that would fail, right?
@ @raw @embed 'foo.html'

@var _id="header" \
     _format="# [code.repeat.run(t=\"-\", c=\"42\")]"

[header]
## Create AddAlias factory for adding aliases to links...

[link.ln_factory(nm="cls2", hr="https://cloudylogic.com", t="Cloudy Logic")]
[link.cls2]


@code _id="AddAliasToLink2"\
      type="exec"\
      src="from .utility import CodeHelpers;print('@set _id=\"{0}\" {1}=\"{3}{0}.<{4}{2}{3}{0}.>{4}\"'.format('{{self.nm}}', '{{self.attr}}', '{{self.lt}}', CodeHelpers.b(0), CodeHelpers.b(1)))"\
      nm="link.?" attr="_attr_name" lt="New Link Text goes here"

@code _id="AddAliasToLink"\
      type="eval"\
      src="print('@set _id=\"{0}\" {1}=\"{3}{3}{0}.<{4}{4}{2}{3}{3}{0}.>{4}{4}\"'.format('{{self.nm}}', '{{self.attr}}', '{{self.lt}}', '{', '}'))"\
      nm="link.?" attr="_attr_name" lt="New Link Text goes here"

[code.AddAliasToLink.run(nm="link.cls2", attr="_clsllc", lt="Cloudy Logic Studios, LLC")]
[code.AddAliasToLink2.run(nm="link.cls2", attr="_clsllc0", lt="Cloudy Logic Studios")]
[link.cls2._null_(_clsllc1="{{link.cls2.<}}CLS1{{link.cls2.>}}" )]
@dump link="cls2"
[link.cls2._clsllc]
[link.cls2._clsllc0]
[link.cls2._clsllc1]

[header]

[code.escape(t="<https://www.google.com>")]
[code.escape.last]

[sys.basepath]
[sys.import_path]

// -------------------------------------------------------------------

[header]
 
//@import '[sys.imports]/film.md'
//[var.fs]
//[var.tags]
//[var.notes]

// This is a hack until I can figure out how to allow a class override to be in a variable that expands after the markdown pass (and gets reparsed).
[class2]=:.note
[comment2]={[{{class2}}]}

@import '[sys.imports]/film.md'
@import '[sys.imports]/shortcuts.md'

[content]=We need at least one, but if we could get 2 or 3 options for the performance part, that would be great.

@break
@dump html=".*ol" var="ol1|li1"

[var.section(t="Performance Video Notes")]
[var.section.with_content(t="Performance Video Notes", \
                          c="[content]" \
)]


[ol1_open]
[li1(t="my list item 1")]
[li1(t="my list item 2")]
[ol1_close]

- shot
[var.comment(t="this is a comment that is long enough to span 2 lines actually it has to be quite a bit longer for that to happen and then if i go even longer")] 
@break
[var.comment]
[var.ul1] 

- shot 2
here is some other text
[comment2]this is a note

@break


//[which]=Song Lyrics
//[lyric]=
//@raw [verse]
[var.lyrics(lyric="I'm sorry momma[b]that you're reading this[b]I never wanted to make you cry[b]but I can't go on like this")]

[header]

[scene]
[var.scene(t="Scene 4 - [var.tags.narr] Mom at Son's Room")]
[var.scene.with_content(t="Scene 4 - [var.tags.narr] Mom at Son's Room" \
       c="[bb][var.tags.wardrobe][bb][var.tags.props][bb][var.tags.makeup][bb][var.tags.cast]" \
)]

[header]

[var.plain]
[var.plain.with_content]

[var.plain(t="Your title")]
[var.plain.with_content(t="Your other title" c="Your content")]

[header]

@dump basic="."

[var.tags]

[header]

@import '[sys.imports]/image.md'
@import '[sys.imports]/shot.md'

[ss]=[{{var.img_def.img_st_inline_border}}]
[ws]=[var.fs.ws]


[header]
## RIGHT HERE
[var.shot_factory(nm="shot38" d="My shot 38" c="" l="")]
// Can be used by itself and it goes full screen. This is the shot table
[var.shot38]

[var.img_factory(nm="shot38" s="{{sys.basepath}}/../tests/in/import/shot1.jpg")]

[header]

[var.shot38]
[image.shot38]
[var.shotinfo2(shotid="shot38")]


