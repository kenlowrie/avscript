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
[content]=We need at least one, but if we could get 2 or 3 options for the performance part, that would be great.

@html _id="_sect_div_" \
      _inherit="div" \
      class="section"
@html _id="_sect_p_" \
      _inherit="p" \
      class="divTitle"
@html _id="_sect_p_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="section" \
          _format="@@ {{html._sect_div_.<}}{{html._sect_p_.<}}{{self.t}}{{html._sect_p_.>}}{{html._sect_div_.>}}" \
          with_content="@@ {{html._sect_div_.<}}{{html._sect_p_.<}}{{self.t}}{{html._sect_p_.>}}{{html._sect_p_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your section title" \
          c=""

[var.section(t="Performance Video Notes")]
[var.section.with_content(t="Performance Video Notes", \
                          c="[content]" \
)]

// This is a hack until I can figure out how to allow a class override to be in a variable that expands after the markdown pass (and gets reparsed).
[comment]=<span class="italic bold">
[class]=:.note
[comment]={[{{class}}]}

- shot
[comment] this is a comment
@break
#

[header]
 
@import '[sys.imports]/film.md'
[var.fs]
[var.tags]
[var.notes]

