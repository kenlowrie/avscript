[class]=:.section
[section0]={[{{class}}]}--- divTitle [{{SECTION}}]
//Variables///
// -------------------------------------------------------------------
{:.section}--- divTitle Performance Video Notes
    We need at least one, but if we could get 2 or 3 options for the performance part, that would be great.

[SECTION]=Performance Video Notes
[section0]
    We need at least one, but if we could get 2 or 3 options for the performance part, that would be great.

@embed 'filename' - like @import, except just includes the code without processing. Could be useful for inserting raw html directly into the output, w/o processing at all. Would be especially cool if you could do this inline, like this:
[myvar]=@embed 'foo.html'
Then, the embedded file would be marked down as normal, giving more flexibility.
@raw @embed 'foo.html'


//@link _id="bookmark_template" _tag="a" id="{{self._param}}"

@link _id="bm-section1" _inherit="bookmark_template"
@link _id="bm-section2" _inherit="bookmark_template"


[link.bm-section1(id="my bookmark" text="This is section 1")]
###This is a bookmark


// This is a hack until I can figure out how to allow a class override to be in a variable that expands after the markdown pass (and gets reparsed).
[comment]=<span class="italic bold">
[class]=:.note
[comment]={[{{class}}]}

- shot
[comment] this is a comment
@break

[link.bm-section1.link]
[link.bm-section1.link(text="Modified link text for section 1")]

@var _id="otf" _format="{:.bigandbold}{{self.text}}" text="usage: var.otf(text=\"text to format\")"

[foo]={:.bigandbold}me in big and bold text
[foo]

[otf]
[otf(text="are you kidding me?")]

@link _id="MYTEST" href="www.cloudylogic.com"
[link.MYTEST.<]hi there[link.MYTEST.>]

[code.esc_html.last]

And now for the attempted retry ...
[code.esc_html.run(url="<https://www.cloudylogic.com>")]

@link _id="cls42" _format="{{self.<}}{{code.esc_html.run(url=\"{{self._link}}\")}}"

[link.cls42(_link="<https://www.amazon.com>")]

@link _id="cloudylogic" _inherit="_template_" href="https://cloudylogic.com"
@link _id="cloudylogic2" _inherit="link._template_" href="https://cloudylogic.com"
@link _id="cloudylogic3" _inherit="_template_" href="https://cloudylogic.com"

[link.cloudylogic]
[link.cloudylogic2]
[link.cloudylogic3]

[link.cloudylogic(_text="Cloudy Logic Studios")]
[link.cloudylogic._asurl]

The current date and time is [code.datetime_stamp.last]

### Here is how to embed the cover page:

@set _id="defaults" title="Title of Work" author="Author of Work" logline="Logline of Work"

[var.cover]

### Here is how to embed revision information:

@set _id="defaults" revision="1a"

[var.revision]
[var.revision.plain]

@@ [var.revision]
@@ [var.revision.plain] 

### Here is how we embed contact information:

@set _id="defaults"\
     cn="Ken Lowrie"\
     ph="*512-710-7257*"\
     em="[ken@cloudylogic.com]"\
     c1="Copyright © 2018 Cloudy Logic Studios, LLC."\
     c2="All Rights Reserved."\
     c3="[www.cloudylogic.com]"

[var.contact]
@@ [var.contact]

//{:.review}--- divTitle Notes to Reviewer
//    Please send [me] any and all feedback, preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. Within different versions of this proposal, ++additions are marked like this++ and ~~deletions are marked like this~~


@link _="cls" _inherit="_template_" _text="{{self._}}" href="https://cloudylogic.com"  _qlink="{{self.<}}{{self._qtext}}{{self.>}}" _qtext="SETMETOLINKTEXT"

When I write: [link.cls._qlink(_qtext="My Production Website")] and [link.cls._qlink(_qtext="Cloudy Logic Studios, LLC")] and [link.cls] and [link.cls._qlink(_qtext="foo")] and [link.cls._qlink],

//@dump link="cls"

[link.ln_factory(nm="mytest42", hr="https://cloudylogic.com", t="cloudylogic.com")]
[link.mytest42]

@dump link="mytest42|generate"

[link.bm_factory(nm="inlinemd", t="Inline Markdown")]

[link.inlinemd.link] - **Formatting content inline**

// markdown tests
[link.inlinemd]

{:.toc}--- divTitle My Table of Contents
    [link.inlinemd.link] - **Formatting content inline**

Inline bookmarks too: [link.inlinemd._inline] This is the location where the links anchor has been dropped.


@dump link="[.lin]|bm_|ref|auto"

// TODO: MOVE THESE OVER TO THE BUILTINS FILE. THEY WILL BE USEFUL...

@code _id="repeat"\
      type="eval"\
      src="print('{}'.format('{{self.t}}'*{{self.c}}))"\
      t="Usage: code.repeat(t=\"text to repeat\", c=5)"\
      c="1"

// How the hell is echo useful? Seriously? It provides no value...
@code _id="echo"\
      type="eval"\
      src="print('{{self.t}}')"\
      t="Usage: code.echo(t=\"text to echo\")"

@dump code="echo|esc|repeat"

# [code.repeat.run(t="-", c="42")]
## Make factories for @cover

Things I learned while building these templates and factories.

A. You want to specify the _format="{{self._internal_}}" in the built-ins, so that
   we can easily reconstruct the functionality in the templates and macros.
B. You can rename the required variables by simply abstracting them away in the
   template.
C. In the factory, you GENERATE a new variable that is based on a TEMPLATE. By doing
   this, the attributes in the generated variable will be those of the template, not
   the factory. The factory is essentially a "make me a new variable of type X".

[var.cover_factory(nm="c1")]
[var.c1]
[var.c1.inline(t2="This is your t2 text")]
[var.c1.inline(t1="This is your t1 text" t3="This is your t3 text")]


# [code.repeat.run(t="-", c="42")]
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
@dump link="cls2"
[link.cls2._clsllc]
[link.cls2._clsllc0]

# [code.repeat.run(t="-", c="42")]

@code _id="escape"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html('{{self.t}}'))"\
      t="<http://www.google.com?h=1&w=0>"

[code.escape.last]

[globals.basepath]
[globals.import_path]

[var.contact]
[var.revision]
[var.revision.plain]
[var.revision._inline_]
[var.revision._inline_plain_]

### These are the old ways of embedding cover, revision and contact information:

@debug 
@cover author="**DISCLAIMER**: This document is strictly private, confidential and personal to its recipients and should not be copied, distributed or reproduced in whole or in part, nor passed to any third party without the expressed, written consent of [Cloudy Logic Studios], LLC."
@debug 
//@debug av="t" ns="f" 

@revision v="***[defaults.revision]***" timestamp="Yes"

//@dump all="*"