If you try to reference attrs (self.) within a code macro, it overwrites params... ick.

@var _id="header" \
     _format="# [code.repeat.run(__t=\"-\", __c=\"42\")]"

[header]

# code.escape(t="<https://www.google.com>"))
[code.escape(t="<https://www.google.com>")]
[code.escape.last]

// -------------------------------------------------------------------
[header]


## right here dude

[code.get._help_]
[code.get]
[code.get(v="madeup")]
[code.get(v="sys.basepath")]

[code.get_default._help_]
d = [code.get_default]
[code.get_default(v="madeup", default="that didnt exist")]
[code.get_default(v="sys.basepath", default="that didnt exist")]
@dump code="get_default"
dd = [code.get_default]
@dump code="get_default"

[header]

@import '[sys.imports]/shot.md'

 Weird thing about how shot factory works. public attrs become sticky in the generated @var. 
 How is that happening? It's totally a side effect...
 
[shot_factory(nm="shot2", c="y", l="50mm", d="sticky desc")]
@dump var="shot2"
[var.shot2.d]
[var.shot2.l]
[var.shot2.c]
@dump var="shot2|shot"

[shot_factory(nm="shot31a", c="y", l="50mm", d="my desc")]
[shot_factory(nm="shot31b", c="y", l="85mm")]
[shot_factory(nm="shot31c", c="n")]
[shot_factory(nm="shot31d")]

[shot31a]
[shot31b]
[shot31c]
[shot31d]

## test1
[code.get_default(v="sys.basepath", default="No")]
[code.get_default(v="shot31ab", default="xxxx")]

@import '[sys.imports]/shot.md'

# 2-----

// Create the shot variables first
[code.shot_factory(nm="f1")]
[code.shot_factory(nm="f2")]
[code.shot_factory(nm="f3")]
[code.shot_factory(nm="f4")]

// Initialize each shot as needed
[f1(d="override", l="22mm")]
[f2(l="85mm")]
[f3(d="This is my fancy shot", l="50mm", c="Maybe")]
[f4(c="Yes")]

[code.get_default(v="$.x", default="nowayjose")]

## hi!

code.get is broken.
code.escape too
code.repeat too.

maybe if i could have both params and attrs. Is that possible?

# code.get(v="var.f3")
[code.get(v="var.f3")]


code.vn(local1="val")

when you define @code id="foo" var="x" ...




//@debug
@embed 'filename' - like @import, except just includes the code without processing. Could be useful for inserting raw html directly into the output, w/o processing at all. Would be especially cool if you could do this inline, like this:
&#91;myvar]=@embed 'foo.html'
Then, the embedded file would be marked down as normal, giving more flexibility. This wouldn't work, though, because it would have \n in the input, and that would fail, right?
@ @raw @embed 'foo.html'


Header define was here

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




