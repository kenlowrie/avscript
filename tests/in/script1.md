{:.red}# Script Series
@link _="domain" _inherit="_template_" _text="https://yourdomain.com" href="https://yourdomain.com"
@link _="me" _inherit="_template_" _text="me" href="email@yourdomain.com"
@link _="feedback" _inherit="me" _text="feedback" href="DELETE_ME_mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback"

[var.cover(title="Title of Script" author="Script Author" logline="Script summary goes here and can be as long as needed. Let is wrap around if you have softwrap, or just go on forever.")]
[var.revision.plain(v="1a")]
[var.contact(cn="Contact Name" ph="Phone" em="[me]" c1="Copyright (c) 2018 by YOURNAME." c2="All Rights Reserved." c3="Don't steal my script")]
{:.review}---    noteTitle       Notes to Reviewers
    Please send [me] any and all [feedback], preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. ++additions are marked like this++ ~~deletions are marked like this~~

{: .pbb.plain }--- divTitle Film Pitch for Potential Client
    ClientName:
    The overall purpose of this demo is to show the type of production value that we will bring to your project, focusing primarily on ...

@link _="article" _inherit="_template_" _text="Link to Article" href="https://domain.com/article_link/"

{:.section}@@@ divTitle
    AV Script

{: .red }- PART 1: Description for part 1
    PART 1A
    {:.blue}PART 1B
[link.article]

-       WS:Couple watching TV
- CU:Couple looking concerned
The narrative for the shots on the left would go here.
- MS:Paranoid guy looking thru blinds
    {:.ignore}Indent by itself to put a blank line between the shot and desc
    If you indent a line following a shot, then that text becomes part of the prior shot, allowing you to put a little more description if you need it.
- ECU:Perspective looking thru peephole.
- CU:Locking door
More narrative here that goes with the shot on the left...
@link _="article2" _inherit="_template_"

- PART 2: The middle section
This is a description for this section
[link.article2(_text="Link to Article" href="https://domain.com/another_article_link")] <-- That should have been turned into a link
{:.red}- MS/CU:Clips of people angry
    You can add more information about a shot by indenting the line that follows the definition. New shots are not started if you indent, however, so don't do that. :)
The narration for the Clips of people angry would be here...
- WS:violence
    This begins a new shot, because we used the shot delimiter at the beginning of the line.
    {:.green}You can, however, prefix each new indented line with a different class for formatting...
CGI Websites and blogs
{:.blue}CGI Use PIP to fill the screen
Words, words, words, blah, blah, blah
{:.section}--- divTitle section heading goes here...
- CGI:
CGI Text is here
{:.pba}### Random heading

{: .question .right}I wonder if we should maybe add that line from the unused section about "..."
* F2B:fin
{: .question .left}fin. credits.

{: .ignore}Anything with a .ignore class won't be displayed when the page is rendered by a browser, but is still part of the actual HTML document.
- WS:Stock clips of TV shows that ...
{:.blue}So many programs on television today ...
We should ***practice tolerance*** and ...
{:.green}It’s also crucial for people to *...* and **...**.
{:.red}We are past due for ...

- TS1

* TS2
- TS3 
footage

bar

## heading

##    heading with leading spaces

xyz

def

///Shotlist///
