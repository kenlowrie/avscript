// This document contains the standard document heading for my scripts
// First let's declare some common links and aliases (variables)
// [workingtitle] and [storysummary] need to be defined *before* you include
// this template.
@link _id="cls" _inherit="_template_" _text="Cloudy Logic Studios" href="https://cloudylogic.com"
[cloudylogic.com]=[link.cls._qlink(_qtext="cloudylogic.com")]
@link _id="you" _inherit="_template_" _text="you@yourdomain.com" href="mailto:you@yourdomain.com"
@link _id="fbemailaddr" _inherit="_template_" _text="Your Name" href="mailto:you@yourdomain.com?subject=[workingtitle]%20Feedback"

@@ [var.cover(title="[workingtitle]" author="**Confidential**" logline="[storysummary].")]
@@ [var.cover(title="", logline="", author="**DISCLAIMER**: This document is strictly private, confidential and personal to its recipients and should not be copied, distributed or reproduced in whole or in part, nor passed to any third party without the expressed, written consent of [link.cls], LLC.")]
@@ [var.revision(revision="1d")]
@@ [var.contact(cn="Ken Lowrie" ph="*512-867-5309*" em="[link.you]" c1="Copyright (c) 2018 by [cls], LLC." c2="All Rights Reserved." c3="www.cloudylogic.com")]
{: .pba.review }--- divTitle Notes to Reviewer
    Please send [link.fbemailaddr] any and all feedback, preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. Within different versions of this proposal, ++additions are marked like this++ and ~~deletions are marked like this~~
