// This document contains the standard document heading for a user guide.
// First let's declare some common links and aliases (variables)
// [workingtitle] and [storysummary] need to be defined *before* you include
// this template.
@link _="company" _inherit="_template_" _text="Your Company Name" href="https://yourcompanydomain.com"
@link _="domain" _inherit="_template_" _text="yourcompanydomain.com" href="https://yourcompanydomain.com"
[me]=John Smith
[phone]=210-555-1212
[email]=johnsmith@yourcompanydomain.com
[var.cover(title="[workingtitle]" author="**This guide is NOT Confidential**" logline="[storysummary].")]
@set _id="defaults" revision="***0.38a***" 
[var.revision.plain]
[var.contact(cn="[me]" ph="*[phone]*" em="[email]" c1="Copyright (c) 2018 by [link.company], LLC." c2="All Rights Reserved." c3="[link.domain]")]
{: .pba.review }--- divTitle Notes to Reviewer
    Please send [me] any and all feedback, preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. Within different versions of this proposal, ++additions are marked like this++ and ~~deletions are marked like this~~
