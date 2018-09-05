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

//@code _id="datetime_stamp" type="exec" src="from time import strftime;print(strftime(\"{{self.fmtstr}}\"))" _format="{{self.last}}" fmtstr="%Y%m%d @ %H:%M:%S"


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

### These are the old ways of embedding cover, revision and contact information:

@cover author="**DISCLAIMER**: This document is strictly private, confidential and personal to its recipients and should not be copied, distributed or reproduced in whole or in part, nor passed to any third party without the expressed, written consent of [Cloudy Logic Studios], LLC."

@revision v="***[defaults.revision]***" timestamp="Yes"

//{:.review}--- divTitle Notes to Reviewer
//    Please send [me] any and all feedback, preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. Within different versions of this proposal, ++additions are marked like this++ and ~~deletions are marked like this~~



///Variables///

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

@var _id="cover_template" \
     _inherit="cover" \
     title="{{self.t1}}" \
     author="{{self.t2}}" \
     logline="{{self.t3}}" \
     t1="Title" t2="author" t3="logline" \
     _format="@@ {{self._inline_}}" \
     inline="{{self._inline_}}"

@var _id="cover_factory" \
      _format="@var _id=\"{{self.nm}}\" \
      _inherit=\"cover_template\" \
      t1=\"\" \
      t2=\"{{self.usage}}\" \
      t3=\"\"" \
     usage="Usage: **{{self.nm}}(t2=&quot;text&quot;)** or **{{self.nm}}.gencover(t2=&quot;text&quot;**)"

[var.cover_factory(nm="c1")]
[var.c1]
[var.c1.inline(t2="This is your t2 text")]
[var.c1.inline(t1="This is your t1 text" t3="This is your t3 text")]


@xlink _id="bm_factory" \
      _format="@link _id=\"{{self.nm}}\" _inherit=\"bm_template\" text=\"{{self.t}}\""

@xlink _id="bm_template" \
      id="{{self._}}" \
      _format="@@ {{self._inline}}" \
      link="<a href=\"#{{self.id}}\">{{self.text}}</a>" \
      text="TEXT-TO-DISPLAY-FOR-LINK"   \
      _inline="<a id=\"{{self.id}}\"></a>"


# [code.repeat.run(t="-", c="42")]
## Create AddAlias factory for adding aliases to links...


 
[code.echo.run(t="@set _id=\"myvar25\" val=\"hello, world\"")]
[code.echo.run(t="@set _id=\"myvar25\" val2=\"hello, world!!\"")]
[code.echo.run(t="@set _id=\"link.mytest42\" _generic=\"{{self.<}}{{self._tt_}}{{self.>}}\"")]


@set _id="link.mytest42" _generic="{{self.<}}{{self._tt_}}{{self.>}}"

[link.mytest42._generic(_tt_="My link text")]

var.myvar25.val2=[var.myvar25.val2]
link.mytest42.val=[link.mytest42.val]
@dump var="myvar25|mytest42" link="mytest42|link.my"

# [code.repeat.run(t="-", c="42")]

[link.ln_factory(nm="jjj", hr="https://cloudylogic.com", t="cls")]
[link.jjj]

//@set _id="link.jjj" _NEWATTR="{{link.jjj.<}}{{self.NEWTEXT}}{{link.jjj.>}}" _NEWTEXT="MYNEWTEXT" _open="{{self.<}}" _close="{{self.>}}"
//@dump link="jjj"


//@debug 
# [code.repeat.run(t="-", c="42")]
//@code _id="format_attr"\
      type="eval"\
      src="print('{{self._fmtstr_}}'.format('{{', '}}', '{{self.ns}}', '{{self.nm}}', '{{self.attr}}', '{{self.text}}', '\\"'))"\
      ns="?" nm="?" attr="?" text="?" _fmtstr_="set _id={6}{2}.{3}{6} {4}={6}{0}{2}.{3}.<{1}{6}{5}{0}{2}.{3}.>{1}\""


@code _id="add_attr"\
      type="eval"\
      src="print('@set _id=\"{0}\" {1}=\"{3}{3}{0}.<{4}{4}{2}{3}{3}{0}.>{4}{4}\"'.format('{{self.nm}}', '{{self.attr}}', '{{self.text}}', '{', '}'))"\
      nm="?" attr="?" text="?"

[code.add_attr.run(nm="link.jjj", attr="_altname2", text="Cloudy Logic Studios, LLC")]
@dump link="jjj"

# WTF
//[code.format_attr.run(ns="link", nm="jjj", attr="_altname", text="This is my new cool text to link")]

//@dump link="jjj"
[link.jjj._altname2]

# [code.repeat.run(t="-", c="42")]
# [code.repeat.run(t="-", c="42")]

@ [code.repeat.run(t="-", c="100")]
@link _id="AddAlias" \
     _format="{{code.echo.run(t="@set _id=\\"{{self.nm}}\\" _x{{self.an}}=\\"{{link.{{self.nm}}.<}}{{self.at}}{{link.{{self.nm}}.>}}\\")}}"
echo [link.AddAlias(nm="cls", an="coolness", at="Cloudy Logic Studios, LLC")]
@dump link="AddAlias" code="echo"

ECHO [link.AddAlias(nm="cls", an="coolness", at="Cloudy Logic Studios, LLC")]
//@debug
[link.AddAlias(nm="cls", an="coolness", at="Cloudy Logic Studios, LLC")]
@dump link="AddAlias" code="echo"

[cls._coolness]

@dump link="AddAlias|cls"
