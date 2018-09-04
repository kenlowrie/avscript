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

@dump link="cls"