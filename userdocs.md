{:.blue}#AVScript User Manual
[workingtitle]%AVScript Markdown Utility
[storysummary]%This manual describes the *AVScript Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create A/V Style scripts quickly, easily and most important, efficiently. ***Enjoy!***
[path]%/Users/ken/Dropbox/shared/src/script/avscript/include
@import '[path]/userguideheading.md'
## What is AVScript?
AVScript is a Python utility that takes plain text files loosely based on Markdown as input and generates Audio/Video (A/V) Style scripts as output in HTML. A CSS file is used to style the output, making it super easy to customize the final render to your liking.

In its simplest use, Markdown list item tags (&#42;, -, +) are used to identify visuals (shots), and regular paragraphs are the audio/narration that go along with the visuals. Let's see a quick example now. The next line will begin with the * and then contain the text that describes the visual, and the line after that will contain the narration that goes with it.
*WS:Sunrise
There's just something about a sunrise that gets the blood flowing...
And here's some additional narration.
[null]%null
You can have as much narration as required, just keep writing, even starting new regular paragraphs. When you're done, start a new visual, or add any other block element, such as links, aliases, headers, divs, etc.
###Inline Markdown

&#42;text&#42; will place text in &lt;em>text&lt;/em> tags. e.g.: *text*
&#42;&#42;text&#42;&#42; will place text in &lt;strong>text&lt;/strong> tags. e.g.: **text**

You can stack them, so that &#42;&#42;&#42;text&#42;&#42;&#42; becomes &lt;em>&lt;strong>text&lt;/strong>&lt;/em>. e.g.: ***text***

++Stuff that's been added++

~~Stuff that's been removed~~

###Links

Both inline and reference style links are supported.

####Inline Style:

This is [an example]:(http://example.com/ "Inline Link Sample") of an inline link. [This inline link]:(http://example.net/) has no title attribute.

Inline links can occur anywhere in the text. Once an inline link has been processed the first time, the link ID, i.e. the part between the [ ], can be used over and over. e.g.: [an example].

####Reference Style:
Reference links use the format [linkID]:url "optional title". Essentially, just like inline links, but without the ( ) surrounding the URL and optional title.

The reference link style must be placed at the beginning of a line. Unlike true Markdown, reference links *must* be defined before they are referenced in the document. Let's create a reference link for the Google Home Page.

[Google]:https://google.com "Google Search Page"

Now, when I write &#91;Google], it is wrapped with a link tag like so: [Google].

####Inline links at the start of a new line
You can also use the inline link format at the start of a line, as in the following example for [inline 1].
[inline 1]:(https://cloudylogic.com "inline link title") 
When you do that, however, everything following the closing parenthesis is ignored. 
{:.note.red}Look at the source document for an example, immediately following this note!

[inline 2]:(https://cloudylogic.com) - you won't see any of this text...

####Automatic links
Should I document automatic links? <http://www.cloudylogic.com>

## Aliases or Variables

Aliases (aka Variables), which is essentially text substitution, is supported using a similar syntax to reference links. **[variable]%value**. In the following example, I will write [my name]%Ken Lowrie:
[my name]%Ken Lowrie
Now, anywhere I write &#91;my name], it will be replaced with "Ken Lowrie". Let's do that now: [my name] <-- Should be Ken Lowrie.

If I instead write: &#91;my name]%[&#42;Ken Lowrie*], then everywhere I write &#91;my name], it will be replaced with &lt;em>Ken Lowrie&lt;/em>. Okay, let's go ahead and do that now. 
[my name]%*Ken Lowrie*
And now, [my name] <-- should be Ken Lowrie wrapped with &lt;em> tags.
## Link aliases

Building on that, we can create aliases for inline links. Say I define a link like this: &#91;cls]:https://cloudylogic.com, which I'm going to do now...
[cls]:https://cloudylogic.com
So when I write &#91;cls], it is replaced with a link to https://cloudylogic.com. For example: [cls].
And that's all good. It's concise, I only have to write *cls* in [ ] and it is wrapped with an HTML link. Saves a lot of typing and potential mistakes. But what if I want to have other, more descriptive names for that URL? Good news, we can do that using a special form of aliases: [Descriptive Text]%[id], where *id* is the name of a previously described reference link. Let me go ahead and create an alias for the *cls* link so the descriptive name is Cloudy Logic.
[Cloudy Logic]%cls
Now, when I write [Cloudy Logic], it is wrapped with the link for *cls*. Cool!

##Divs

##Headers

##Cover, Revision & Contact Sections

##Importing documents

##Shotlist

##Debugging

///Links///
///Variables///
