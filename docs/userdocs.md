{:.blue.center}#AVScript User Manual
[workingtitle]=AVScript Markdown Utility
[storysummary]=This manual describes the *AVScript Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create A/V Style scripts quickly, easily and most important, efficiently. ***Enjoy!***
//You will probably need to update this path to make this work
[path]=/Users/ken/Dropbox/shared/src/script/avscript/docs/import
@import '[path]/userguideheading.md'
[SP]=&nbsp;
{:.toc}@@@ divTitle Table of Contents
    [SP]
    @:[inlinemd]<<Inline Markdown>> - **Formatting content inline**
    @:[links]<<Links>> - **Inline and Reference Link Styles**
    {:.indent}@:[inline+links]<<Inline Links>> - **Creating links inline**
    {:.indent}@:[ref+links]<<Reference Links>> - **Creating reference links**
    {:.indent}@:[mailto+links]<<mailto Links>> - **Creating mailto links**
    {:.indent}@:[auto+links]<<Automatic Links>> - **Creating automatic links**
    @:[aliases]<<Aliases>>  - **Text substitution aka Variables**
    @:[div]<<DIV>> - **Creating new DIV sections**
    @:[headers]<<Headers>> - **Adding Headers**
    @:[anchors]<<Anchors>> - **Using Bookmarks**
    @:[special+sections]<<Special Sections>> - **Covers, Revisions &amp; Contact sections**
    @:[imports]<<Imports>> - **Importing files**
    @:[predefined classes]<<Predefined Classes>> - **Using predefined CSS classes**
    @:[shotlist]<<Shotlist>> - **Displaying the shotlist**
    @:[debug]<<Debug>> - **Dumping variables and links**
    @:[summary]<<Summary>> - **Summary of the User Guide**

## What is AVScript?
AVScript is a Python utility that takes plain text files loosely based on Markdown as input and generates Audio/Video (A/V) Style scripts in HTML format. A CSS file is used to style the output, making it super easy to customize the final render to your liking.

In its simplest terms:

{:.note}**Markdown** list item tags ***(&#42;, -, +)*** are used to identify ***visuals*** (shots), and regular paragraphs are the ***audio/narration*** that go along with the visuals.

Let's see a quick example now. The next line will begin with an ***&#42;*** and then contain the text that describes the visual, and the line after that will contain the narration that goes with it.
*WS:Sunrise
There's just something about a sunrise that gets the blood flowing...
And here's some additional narration.
@break
{:.note.red.indent}When you want to force the document out of shot mode, use ***@break*** or ***@exit*** on an empty line. That will reset the floats which are controlling the AV formatting, and start a new section. See how the document leaves the narration mode of the prior shot, and starts this new block paragraph?
**&#64;break** &lt;--Use @break or @exit to close a shot DIV.
You can have as much narration as required, just keep writing, even starting new regular paragraphs. When you're done, start a new visual, or add any other block element, such as links, aliases, headers, divs, etc. To add another shot, just repeat the steps above, like this:
*CU:Coffee pot heating on wire rack of fire pit
There's nothing like waking up to the smell of coffee percolating in the outdoors.
@exit
If you have text you want included in the HTML document, but do not want it rendered by the browser, use the **{:.ignore}** class prefix. For example, on the next line, we'll write {:.ignore}You won't see this.
{:.ignore}You won't see this.
When you examine the HTML, you'll see the prior text wrapped in **&lt;p&gt;** tags, inside **&lt;div class="extras"&gt;** markup. However, it will not be rendered by the browser, unless you modify the CSS rule for the ignore class.
Lines that begin with a double forward slash [***//***] are treated as comments, and are discarded by AVScript. They will not appear in the HTML at all. As another example, we'll write *//This will not appear in the HTML* on the next line.
//This will not appear in the HTML
If you examine the HTML output, you will not see the previous line in the output.

@+[inlinemd]
###Inline Markdown

A few of the standard markdown span elements are supported, as are a couple of specialized span elements. These include:

{:.indent}###&#42; - wrap text in a single asterisk for *emphasis*
{:.indent}###&#42;&#42; - wrap text in double asterisks for bold
{:.indent}###&#43;&#43; - wrap text in double plus signs for ++&lt;ins>++
{:.indent}###&#126;&#126; - wrap text in double tilde for ~~&lt;del>~~

Here are a few examples:

When I write **&#42;text&#42;**, it becomes *text*, and when I write **&#42;&#42;text&#42;&#42;**, it becomes **text**

You can stack them too, so that **&#42;&#42;&#42;text&#42;&#42;&#42;** becomes ***text***

When you want to wrap text with &lt;ins>, use the double plus signs like this: ++Stuff that's been added++. Similarly, when you want to wrap text with &lt;del> tags, do it like this: ~~Stuff that's been removed~~.

That's a brief look at using AVScript's built-in span element support. Now, let's take a look at support for links, the remaining span element.

@+[links]
###Links

Both inline and reference style links are supported. The syntax for each style is:

{:.syntax}@@@ divTitle Link Syntax
    {:.indent2.bigandbold}Inline: &lt;&#91;*LinkID*&#93;&gt; &lt; :( &gt; &lt;***url***&gt; &#91;"*optional title*"&#93; &lt; ) &gt;
    {:.indent2.bigandbold}Reference: &lt;&#91;***LinkID***&#93;&gt; &lt; : &gt; &lt;*url*&gt; &#91;"*optional title*"&#93;
    [SP]
    {:.indent2.bigandbold}Examples:
    [SP]
    {:.indent3.bigandbold}&#91;MyLinkID&#93;:(http://url.com "title") *&lt;-- Inline Link Example - Parenthesis around URL &amp; Title*
    {:.indent3.bigandbold}&#91;MyLinkID&#93;:http://url.com "title" *&lt;-- Reference Link Example - Must be at beginning of line*

@+[inline+links]
###Inline Style:

The next paragraph has the following inline links defined within it: This is **&#91;an example]:(http://example.com/ "Inline Link Sample")** of an inline link. **&#91;This inline link]:(http://example.net/)** has no title attribute.

This is [an example]:(http://example.com/ "Inline Link Sample") of an inline link. [This inline link]:(http://example.net/) has no title attribute.

Inline links can occur anywhere in the text. Once an inline link has been processed the first time, the link ID, i.e. the part between the [ ], can be used over and over. e.g.: [an example].

@+[ref+links]
###Reference Style:
Reference links use the format [linkID]:url "optional title". Essentially, just like inline links, but without the ( ) surrounding the URL and optional title.

The reference link style must be placed at the beginning of a line. Unlike true Markdown, reference links *must* be defined before they are referenced in the document. Let's create a reference link for the Google Home Page.

{:.indent}###[Google]:https://google.com "Google Search Page"
[Google]:https://google.com "Google Search Page"

Now, when I write &#91;Google], it is wrapped with a link tag like so: [Google].

###Inline links at the start of a new line
You can also use the inline link format at the start of a line, as in the following example for **[inline 1]**.
{:.indent}###&#91;inline 1]:(https://cloudylogic.com "inline link title") 
[inline 1]:(https://cloudylogic.com "inline link title")
Now, when we write &#91;inline 1], it has been defined just like a normal reference link, like this: [inline 1]
When you use the inline link syntax at the start of a line, however, everything following the closing parenthesis is ignored. For example, if we write:
{:.indent}###**&#91;inline 2]:(https://cloudylogic.com) - you won't see any of this text...**
Then the inline link isn't expanded inline as normal, and any text following the closing parenthesis is ignored.

{:.note.red.width90}If you look at the source document immediately following this note,  you'll see the inline definition of **inline 2**, but it isn't displayed like normal inline links, it is only defined for use later.

[inline 2]:(https://cloudylogic.com)-you won't see any of this text...

Now, I can go ahead and write **&#91;inline 2]**, like this: [inline 2], and it's a valid link!
@+[mailto+links]
###mailto links
You can create mailto: links in your document too, which enables users to click on a link to automatically compose an email addressed to the specified email address. AVScript will encode the entire mailto: link URL using a mix of decimal and hexadecimal HTML entities as a deterrent to spam bots that mine email addresses from HTML documents. Here's the syntax for a *mailto:* link:
 
{:.syntax}@@@ divTitle mailto Link Syntax
    {:.indent2.bigandbold}&lt;&#91;*LinkID*&#93;&gt; &lt; : &gt; &lt;***mailto:you@yourdomain.com***&gt;
    [SP]
    {:.indent2.bigandbold}Examples:
    [SP]
    {:.indent3.bigandbold}&#91;email_me&#93;:mailto:user@mydomain.com *&lt;-- mailto Link Example*
    {:.indent3.bigandbold}&#91;feedback&#93;:mailto:user@mydomain.com?subject=feature%20feedback*&lt;-- mailto link with subject*
[email_me]:mailto:user@mydomain.com
[feedback]:mailto:user@mydomain.com?subject=feature%20feedback

I've defined the previous examples inline in the user docs, so now we can use them by embedding the link id within square brackets, like so: [email_me]. Or using the second form, send me [feedback].

@+[auto+links]
###Automatic links
The final type of link format is automatic links. Automatic links are created by simply wrapping a URL with ***&lt; &gt;*** like this: <http://www.cloudylogic.com>. When you do that, the URL (everything between the angle brackets) is wrapped with an **A** tag whose **HREF** attribute is the URL.
{:.note}**NOTE: **I'm still on the fence as to whether support for automatic links will remain in AVScript, so don't get too comfortable with them just yet...

@+[aliases]
{:.plain}@@@ plainTitle
## Aliases or Variables

Aliases (aka Variables), which is essentially text substitution, is supported using a similar syntax to reference links. **[variable]=value**. Take the following example:
{:.indent}###[my name]=Ken Lowrie
[my name]=Ken Lowrie
Now, anywhere I write &#91;my name], it will be replaced with "Ken Lowrie". Let's do that now: [my name] &lt;-- Should be Ken Lowrie.

If I instead write: &#91;my name]=[&#42;Ken Lowrie*], then everywhere I write &#91;my name], it will be replaced with &lt;em>Ken Lowrie&lt;/em>. Okay, let's go ahead and do that now. 
[my name]=*Ken Lowrie*
And now, [my name] &lt;-- should be Ken Lowrie wrapped with &lt;em> tags.
## Link aliases

Building on that, we can create aliases for inline links. Say I define a reference link like this: 
{:.indent}###&#91;cls]:https://cloudylogic.com
[cls]:https://cloudylogic.com
Now, when I write **&#91;cls]**, it is replaced with a link to https://cloudylogic.com. For example: [cls].
And that's all good. It's concise, I only have to write *cls* in [ ] and it is wrapped with an HTML link. Saves a lot of typing and potential mistakes. But what if I want to have other, more descriptive names for that URL? Good news, we can do that using a special form of aliases: [Descriptive Text]=[id], where *id* is the name of a previously described reference link. Let me go ahead and create an alias for the *cls* link so the descriptive name is Cloudy Logic.
{:.indent}###&#91;Cloudy Logic]=cls
[Cloudy Logic]=cls
Now, when I write [Cloudy Logic], it is wrapped with the link for *cls*. Cool!

@+[divs]
{:.plain}@@@ plainTitle
##Divs
You can create a new DIV using ***---*** or ***@@@*** at the start of a new line. The complete syntax is: 

###&#91;{:.class}&lt;***---*** | ***@@@***&gt; &lt;***title_className | .***&gt; &#91;optional title&#93;

The class prefix is optional, but handy if you want your DIV to be styled in a unique way. You can list one or more classes in dotted notation. E.g.: **{:.myclass}** or **{:.myclass1.myclass2}**. Then an optional class for the title, or '.' to indicate no title class, and finally, the optional title. Let's take a look at an example:

When I write ***{:.section}@@@ divTitle This is my new DIV section*** at the start of a new line, I get this:
{:.section}--- divTitle This is my new DIV section

If I indent subsequent lines immediately following the DIV declaration, they become part of the DIV as a regular paragraph. For example, I'll add four (4) indented lines immediately after the previous DIV declaration and I get this:

{:.section}--- divTitle This is my new DIV section
    This is line 1
    This is line 2
    This is line 3
    This is line 4

There are a several built-in CSS classes that are defined in the accompanying **avscript_md.css** file, and you can add your own to get new DIVs formatted to your liking.

{:.syntax}@@@ divTitle Predefined DIVs
    [SP]
    {:.indent.bigandbold}&#123;:.toc} -- For Table of Contents sections.
    {:.indent.bigandbold}&#123;:.section} -- Generic section.
    {:.indent.bigandbold}&#123;:.unused} -- Unused section.
    {:.indent.bigandbold}&#123;:.syntax} -- Syntax section.
    {:.indent.bigandbold}&#123;:.review} -- Review section.
    {:.indent.bigandbold}&#123;:.plain} -- Plain section.

Remember, you can add your own classes in a CSS file, and then reference them using the built-in formatting of **avscript_md**.

@+[headers]
{:.plain}@@@ plainTitle
##Headers

Just like in standard Markdown, you can use the # symbol at the beginning of a line to designate an HTML &lt;H1&gt; element. ## symbols designate an &lt;H2&gt; element, and so on, up to ###### for &lt;H6&gt;. Here are examples of each.
{:.indent}### # H1
{:.indent}### ## H2
{:.indent}### ### H3
{:.indent}### #### H4
{:.indent}### ##### H5
{:.indent}### ###### H6
And this is how they will look in the document when it's formatted:
# H1
## H2
### H3
#### H4
##### H5
######H6

You may want to style the headers to your liking in the avscript_md.css file.

@+[anchors]
##Bookmarks
You can also define bookmarks in your document, and then reference them with links using the following syntax:

{:.indent}###@&#43;&#91;bookmark name&#93; - Define local bookmark
{:.indent}###@&#58;&#91;bookmark name&#93; - Create hyperlink to bookmark

This is useful for creating things like a table of contents (TOC) for your document, or anywhere that you want to provide a hyperlink to a different part of your doc. These do not have to be defined in any particular order. That is, you can create the hyperlink before the bookmark has been defined.

For an example of bookmarks, just take a look at how this user guide defined and uses its own TOC.

@+[special+sections]
##Cover, Revision & Contact Sections

There are three (3) specialized sections that can be defined within your document to add commonly used information in script files. They are:

{:.syntax}--- divTitle Specialized Sections
    [SP]
    {:.indent.bigandbold}@cover - To add a cover section
    {:.indent.bigandbold}@revision - To add a revision section
    {:.indent.bigandbold}@contact - To add a contact section

### The details for each specialized section follows.

{:.plain}@@@ plainTitle
## Cover Title

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@cover title="title of script" author="written by" logline="logline or short description"

Each element is optional, and they can appear in any order. Also note that the value of any parameter can be whatever you want. Just because it says "author", doesn't mean you have to put the author name there. You could instead write *"Roses are Red"*, and that would be just fine...

{:.plain}@@@ plainTitle
## Revision

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@revision v="revision" timestamp="yes"
Specify the revision number of your document within the angle brackets. If timestamp is either not specified or has any value other than "No", "Off", "False" or "0", the current date and time of the document at the time of processing will also be inserted immediately following the revision number. This provides additional clarification of the version, in case you forget to bump the version number.

If you specify timestamp="No" | "Off" | "False" | "0", then the timestamp will not be added to the revision string.

{:.plain}@@@ plainTitle
## Contact

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@contact cn="name" ph="phone" em="email" c1="copyright line 1" c2="copyright line 2" c3="copyright line 3"

The contact section allows you to specify several key elements about the script project. They include the following elements:

{:.syntax}@@@ divTitle Contact Elements
    [SP]
    {:.indent.bigandbold}cn="Contact Name"
    {:.indent.bigandbold}ph="Contact Phone"
    {:.indent.bigandbold}em="Contact Email"
    {:.indent.bigandbold}c1="Copyright Line 1"
    {:.indent.bigandbold}c2="Copyright Line 2"
    {:.indent.bigandbold}c3="Copyright Line 3"

Each contact element is optional, and the elements can appear in any order. To see these tags in action, take a look at the **userguideheading.md** document in the import folder of this user guide.

@+[imports]
{:.plain}@@@ plainTitle
##Importing documents

{:.syntax}@@@ divTitle Syntax:
    {:.indent}**@import "filename"**
    {:.indent}**@import "/abs/path/to/filename"**
    {:.indent}**@import "../relative/path/to/filename"**
    {:.indent}**@import "$/relative/to/current/filename"**

The @import statement can be used to include documents that contain commonly used contents for your scripts, such as common aliases, links, headers, sections, etc. You can use fully qualified paths, relative paths, or paths based on the current file being processed. The latter uses the symbol '$' to designate that the path to this file should begin with the path the current file being processed. For example, assume the current file being processed is: /mydir/myfile.md. The statement:

### @import "$/vars.md"

Would be the same as writing **@import "/mydir/vars.md"**. This is useful because it doesn't require that you use absolute paths for everything.

{:.note.blue}There is a gotcha when using this with BBEdit's Markup Preview. There is no context for the top level file, since it is passed to the Python script as sys.stdin. Because of that, you can't rely on avscript_md to determine the relative path of the top level file. It will work just fine when using mkavscript_md, but that won't be useful if you are using BBEdit's Markup Preview to write your documents...

@+[predefined classes]
{:.plain}@@@ plainTitle
##Predefined classes
There are a number of predefined classes in the primary CSS file that can be used to quickly style your AV scripts. You can add others as required, and decorate your elements as needed. Here are a few of them, used outside the AV DIV, and then again inside an AV DIV.

{:.syntax}@@@ divTitle Predefined classes
    [SP]
    {:.indent.bigandbold}&#123;:.note} -- This is a note.
    {:.indent.bigandbold}&#123;:.question} -- This is a question.
    {:.indent.bigandbold}&#123;:.vo} -- This is a VO note
    {:.indent.bigandbold}&#123;:.important} -- This is important.
    {:.indent.bigandbold}&#123;:.greyout} -- This is grey text on grey background.

Here they are used outside an AV DIV Section.

{:.note}This is a note.
{:.question}This is a question.
{:.vo}This is a VO note
{:.important}This is important.
{:.greyout}This is grey text on grey background.

*CU: Predefined Classes used inside AV section
Here they are again, used inside an AV DIV section

{:.note}This is a note.
{:.question}This is a question.
{:.vo}This is a VO note
{:.important}This is important.
{:.greyout}This is grey text on grey background.

@exit
Here are a few more of the predefined classes available, and remember, you can tailor these or add more as required for your particular purpose.

{:.syntax.width70}@@@ divTitle More predefined classes
    [SP]
    {:.indent}**&#123;:.pbb}** -- Page Break Before (when printing).
    {:.indent}**&#123;:.pba}** -- Page Break After (when printing).
    {:.indent}**&#123;:.red}** -- To color text red.
    {:.indent}**&#123;:.green}** -- To color text green.
    {:.indent}**&#123;:.blue}** -- To color text blue.
    {:.indent}**&#123;:.center}** -- To center text.
    {:.indent}**&#123;:.left}** -- To left align text.
    {:.indent}**&#123;:.right}** -- To right align text.
    {:.indent}**&#123;:.bigandbold}** -- To increase text size and make it bold.
    {:.indent}**&#123;:.box}** -- To put a box around it.
    {:.indent}**&#123;:.dashed}** -- To put a dashed line around it.
    {:.indent}**&#123;:.greybg}** -- To make the background grey.
    {:.indent}**&#123;:.ignore}** -- So it won't display in the output.

You can stack multiple classes by simply stringing them together. For example, on the next line, I'll write **{:.greybg.bigandbold.blue}This is a big and bold blue note on a grey background.**

{:.greybg.bigandbold.blue}This is a big and bold blue note on a grey background.

@+[shotlist]
{:.plain}@@@ plainTitle
##Shotlist

For convenience, you can list all of the defined shots in a list at the end of your script by using the ***///Shotlist///*** tag. This tag must begin on a line of its own, and it is replaced on the fly with all the shots that have been defined up to that point. The following shows what it would do for this document:

///Shotlist///

@+[debug]
{:.plain}@@@ plainTitle
{:.plainTitle}##Debugging

There are two debugging tags that can be used in your document, and like ***///Shotlist///***, they must be on a line of their own.

{:.indent}###///Links/// - dumps all the links defined so far
{:.indent}###///Variables/// - dumps all the variables (aliases) defined

Here are those two tags in action for this document.

///Links///
///Variables///

@+[summary]
{:.plain}@@@ plainTitle
## Summary

Well that's it! Hope you've enjoyed reading the docs for the avscript_md utility. More importantly, I hope that you can use this app to streamline your audio/visual script development!
