{:.blue}#AVScript User Manual
[workingtitle]%AVScript Markdown Utility
[storysummary]%This manual describes the *AVScript Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create A/V Style scripts quickly, easily and most important, efficiently. ***Enjoy!***
//You will probably need to update this path to make this work
[path]%/Users/ken/Dropbox/shared/src/script/avscript/import
@import '[path]/userguideheading.md'
[SP]%&nbsp;
@@@ link noteTitle Table of Contents
    [SP]
    @:[inlinemd]<<Inline Markdown>> - **Formatting content inline**
    @:[links]<<Links>> - **Inline and Reference Link Styles**
    {:.indent}@:[inline+links]<<Inline Links>> - **Creating links inline**
    {:.indent}@:[ref+links]<<Reference Links>> - **Creating reference links**
    {:.indent}@:[auto+links]<<Automatic Links>> - **Creating automatic links**
    @:[aliases]<<Aliases>>  - **Text substitution aka Variables**
    @:[div]<<DIV>> - **Creating new DIV sections**
    @:[headers]<<Headers>> - **Adding Headers**
    @:[anchors]<<Anchors>> - **Using Anchors**
    @:[special+sections]<<Special Sections>> - **Covers, Revisions &amp; Contact sections**
    @:[imports]<<Imports>> - **Importing files**
    @:[shotlist]<<Shotlist>> - **Displaying the shotlist**
    @:[debug]<<Debug>> - **Dumping variables and links**

## What is AVScript?
AVScript is a Python utility that takes plain text files loosely based on Markdown as input and generates Audio/Video (A/V) Style scripts as output in HTML. A CSS file is used to style the output, making it super easy to customize the final render to your liking.
***TODO TODO TODO - Don't use valid email addresses in this document.***

In its simplest, Markdown list item tags (&#42;, -, +) are used to identify visuals (shots), and regular paragraphs are the audio/narration that go along with the visuals. Let's see a quick example now. The next line will begin with the * and then contain the text that describes the visual, and the line after that will contain the narration that goes with it.
*WS:Sunrise
There's just something about a sunrise that gets the blood flowing...
And here's some additional narration.
[null]%null
You can have as much narration as required, just keep writing, even starting new regular paragraphs. When you're done, start a new visual, or add any other block element, such as links, aliases, headers, divs, etc.
@+[inlinemd]
###Inline Markdown

A few of the standard markdown span elements are supported, as are a couple of specialized span elements. These include:

{:.indent}####&#42; - wrap text in a single asterisk for emphasis
{:.indent}####&#42;&#42; - wrap text in double asterisks for bold
{:.indent}####&#43;&#43; - wrap text in double plus signs for &ltins>
{:.indent}####&#126;&#126; - wrap text in double tilde for &ltdel>

Here are a few examples:

When I write **&#42;text&#42;**, it becomes *text*, and when I write **&#42;&#42;text&#42;&#42;**, it becomes **text**

You can stack them too, so that **&#42;&#42;&#42;text&#42;&#42;&#42;** becomes ***text***

When you want to wrap text with &ltins>, use the double plus signs like this: ++Stuff that's been added++. Similarly, when you want to wrap text with &ltdel> tags, do it like this: ~~Stuff that's been removed~~.

That's a brief look at using AVScript's built-in span element support. Now, let's take a look at support for links, the remaining span element.

@+[links]
###Links

Both inline and reference style links are supported. The syntax for each style is:
{:.indent}###Inline: &lt;***&#91;LinkID&#93;***&gt; &lt;*** :( ***&gt; &lt;***url***&gt; &#91;"optional title"&#93;*** )***

{:.indent}###Reference: &lt;***&#91;LinkID&#93;***&gt; &lt;*** : ***&gt; &lt;***url***&gt; &#91;"optional title"&#93;

@+[inline+links]
####Inline Style:

The following paragraph has the following inline links defined within it: This is **&#91;an example]:(http://example.com/ "Inline Link Sample")** of an inline link. **&#91;This inline link]:(http://example.net/)** has no title attribute.

This is [an example]:(http://example.com/ "Inline Link Sample") of an inline link. [This inline link]:(http://example.net/) has no title attribute.

Inline links can occur anywhere in the text. Once an inline link has been processed the first time, the link ID, i.e. the part between the [ ], can be used over and over. e.g.: [an example].

@+[ref+links]
####Reference Style:
Reference links use the format [linkID]:url "optional title". Essentially, just like inline links, but without the ( ) surrounding the URL and optional title.

The reference link style must be placed at the beginning of a line. Unlike true Markdown, reference links *must* be defined before they are referenced in the document. Let's create a reference link for the Google Home Page.

{:.indent}####[Google]:https://google.com "Google Search Page"
[Google]:https://google.com "Google Search Page"

Now, when I write &#91;Google], it is wrapped with a link tag like so: [Google].

####Inline links at the start of a new line
You can also use the inline link format at the start of a line, as in the following example for **[inline 1]**.
{:.indent}####&#91;inline 1]:(https://cloudylogic.com "inline link title") 
[inline 1]:(https://cloudylogic.com "inline link title")
Now, when we write &#91inline 1], it has been defined just like a normal reference link, like this: [inline 1]
When you use the inline link syntax at the start of a line, however, everything following the closing parenthesis is ignored. For example, if we write:
**&#91;inline 2]:(https://cloudylogic.com) - you won't see any of this text...**
Then the inline link isn't expanded inline as normal, and any text following the closing parenthesis is ignored.
{:.note.red}If you look at the source document immediately following this note,  you'll see the inline definition of **inline 2**, but it isn't displayed like normal inline links, it is only defined for use later.

[inline 2]:(https://cloudylogic.com)-you won't see any of this text...

Now, I can go ahead and write **&#91;inline 2]**, like this: [inline 2], and it's a valid link!
@+[auto+inks]
####Automatic links
Should I document automatic links? <http://www.cloudylogic.com>

@+[aliases]
## Aliases or Variables

Aliases (aka Variables), which is essentially text substitution, is supported using a similar syntax to reference links. **[variable]%value**. Take the following example:
{:.indent}###[my name]%Ken Lowrie
[my name]%Ken Lowrie
Now, anywhere I write &#91;my name], it will be replaced with "Ken Lowrie". Let's do that now: [my name] <-- Should be Ken Lowrie.

If I instead write: &#91;my name]%[&#42;Ken Lowrie*], then everywhere I write &#91;my name], it will be replaced with &lt;em>Ken Lowrie&lt;/em>. Okay, let's go ahead and do that now. 
[my name]%*Ken Lowrie*
And now, [my name] <-- should be Ken Lowrie wrapped with &lt;em> tags.
## Link aliases

Building on that, we can create aliases for inline links. Say I define a reference link like this: 
{:.indent}###&#91;cls]:https://cloudylogic.com
[cls]:https://cloudylogic.com
Now, when I write **&#91;cls]**, it is replaced with a link to https://cloudylogic.com. For example: [cls].
And that's all good. It's concise, I only have to write *cls* in [ ] and it is wrapped with an HTML link. Saves a lot of typing and potential mistakes. But what if I want to have other, more descriptive names for that URL? Good news, we can do that using a special form of aliases: [Descriptive Text]%[id], where *id* is the name of a previously described reference link. Let me go ahead and create an alias for the *cls* link so the descriptive name is Cloudy Logic.
{:.indent}###&#91;Cloudy Logic]%cls
[Cloudy Logic]%cls
Now, when I write [Cloudy Logic], it is wrapped with the link for *cls*. Cool!

@+[divs]
##Divs
You can create a new DIV using ***---*** or ***@@@*** at the start of a new line. The complete syntax is: 

###&lt;***---*** | ***@@@***&gt; &lt;***cssID***&gt; &lt;***className | .***&gt; &#91;optional title&#93;

For example, when I write ***@@@ section noteTitle This is my new DIV section*** at the start of a new line, I get this:
--- section noteTitle This is my new DIV section

There are a several built-in CSS ID's that are defined in the accompanying **avscript_md.css** file, and you can add your own to get new DIVs formatted to your liking.

@+[headers]
##Headers

@+[anchors]
##Anchors

@+[special+sections]
##Cover, Revision & Contact Sections

@+[imports]
##Importing documents

@@@ link noteTitle Syntax:
    {:.indent}**@import "filename"**
    {:.indent}**@import "/abs/path/to/filename"**
    {:.indent}**@import "../relative/path/to/filename"**
    {:.indent}**@import "$/relative/to/current/filename"**

The @import statement can be used to include documents that contain commonly used contents for your scripts, such as common aliases, links, headers, sections, etc. You can use fully qualified paths, relative paths, or paths based on the current file being processed. The latter uses the symbol '$' to designate that the path to this file should begin with the path the current file being processed. For example, assume the current file being processed is: /mydir/myfile.md. The statement:

#### @import "$/vars.md"

Would be the same as writing @import "/mydir/vars.md". This is useful because it doesn't require that you use absolute paths for everything.

{:.note}There is a gotcha when using this with BBEdit's Markup Preview. There is no context for the top level file, since it is passed to the Python script as sys.stdin. Because of that, you can't rely on avscript_md to determine the relative path of the top level file. It will work just fine when using mkavscript_md, but that won't be useful if you are using BBEdit's Markup Preview to write your documents...

@+[shotlist]
##Shotlist

@+[debug]
##Debugging

///Links///
///Variables///
