{:.blue.center}#AVScript User Manual
[workingtitle]=AVScript Markdown Utility
[storysummary]=This manual describes the *AVScript Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create A/V Style scripts quickly, easily and most important, efficiently. ***Enjoy!***[bb]**NOTE:**[bb]This manual was originally written in the first version of avscript, and as such, there are likely things that may not be as efficient as they could/should be. Be sure to take a look at the test code (../tests/in/*.md) to see examples of the latest syntax.

//You will probably need to update this path to make this work
[path]=/Users/ken/Dropbox/shared/src/script/avscript/docs/import
@import '[path]/userguideheading.md'

[link.bm_factory(nm="inlinemd" t="Inline Markdown")]
[link.bm_factory(nm="links" t="Links")]
[link.bm_factory(nm="inline_links" t="Inline Links")]
[link.bm_factory(nm="ref_links" t="Reference Links")]
[link.bm_factory(nm="auto_links" t="Automatic Links")]
[link.bm_factory(nm="mailto_links" t="mailto Links")]
[link.bm_factory(nm="aliases" t="Aliases")]
[link.bm_factory(nm="div" t="DIV")]
[link.bm_factory(nm="headers" t="Headers")]
[link.bm_factory(nm="anchors" t="Anchors")]
[link.bm_factory(nm="special_sections" t="Special Sections")]
[link.bm_factory(nm="imports" t="Importing files")]
[link.bm_factory(nm="advanced" t="Advanced Topics")]
[link.bm_factory(nm="predefined_classes" t="Predefined Classes")]
[link.bm_factory(nm="shotlist" t="Shotlist")]
[link.bm_factory(nm="debug" t="Debug")]
[link.bm_factory(nm="summary" t="Summary")]

{:.toc}@@@ divTitle Table of Contents
    [link.inlinemd.link] - **Formatting content inline**
    [link.links.link] - **Inline and Reference Link Styles**
    {:.indent}[link.inline_links.link] - **Creating links inline**
    {:.indent}[link.ref_links.link] - **Creating reference links**
    {:.indent}[link.mailto_links.link] - **Creating mailto links**
    {:.indent}[link.auto_links.link] - **Creating automatic links**
    [link.aliases.link] - **Text substitution aka Variables**
    [link.div.link] - **Creating new DIV sections**
    [link.headers.link] - **Adding Headers**
    [link.anchors.link] - **Using Bookmarks**
    [link.special_sections.link] - **Covers, Revisions &amp; Contact sections**
    [link.imports.link] - **Importing files**
    [link.advanced.link] - **Introducing @raw, @image & @var**
    [link.predefined_classes.link] - **Using predefined CSS classes**
    [link.shotlist.link] - **Displaying the shotlist**
    [link.debug.link] - **Dumping variables and links**
    [link.summary.link] - **Summary of the User Guide**

## What is AVScript?
AVScript is a Python utility that takes plain text files loosely (oh, so loosely) based on Markdown as input, and generates Audio/Video (A/V) Style scripts in HTML format. A CSS file is used to style the output, making it super easy to customize the final render to your liking.

At least that's how it started out. It's grown quite a bit since the early days, and this document will attempt to provide an in-depth overview of most of the capabilities of the package.

In its simplest terms:

[ast]=&#42;
[obr]=&#91;
[lt]=&lt;
[gt]=&gt;
[at]=&#64;

{:.note}**Markdown** list item tags ***([ast], -, +)*** are used to identify ***visuals*** (shots), and regular paragraphs are the ***audio/narration*** that go along with the visuals.

Let's see a quick example now. The next line will begin with an ***&#42;*** and then contain the text that describes the visual, and the line after that will contain the narration that goes with it.
*WS:Sunrise
There's just something about a sunrise that gets the blood flowing...
And here's some additional narration.
@break
{:.note.red.indent}When you want to force the document out of shot mode, use ***@break*** or ***@exit*** on an empty line. That will reset the floats which are controlling the AV formatting, and start a new section. See how the document leaves the narration mode of the prior shot, and starts this new block paragraph?
**[at]break** [lt]--Use @break or @exit to close a shot DIV.
You can have as much narration as required, just keep writing, even starting new regular paragraphs. When you're done, start a new visual, or add any other block element, such as links, aliases, headers, divs, etc. To add another shot, just repeat the steps above, like this:
*CU:Coffee pot heating on wire rack of fire pit
There's nothing like waking up to the smell of coffee percolating in the outdoors.
@exit
If you have text you want included in the HTML document, but do not want it rendered by the browser, use the **{:.ignore}** class prefix. For example, on the next line, we'll write {:.ignore}You won't see this.
{:.ignore}You won't see this.
When you examine the HTML, you'll see the prior text wrapped in **[lt]p[gt]** tags, inside **[lt]div class="extras"[gt]** markup. However, it will not be rendered by the browser, unless you modify the CSS rule for the ignore class.
Lines that begin with a double forward slash [***//***] are treated as comments, and are discarded by AVScript. They will not appear in the HTML at all. As another example, we'll write *//This will not appear in the HTML* on the next line.
//This will not appear in the HTML
If you examine the HTML output, you will not see the previous line in the output.

[link.inlinemd]
###Inline Markdown

A few of the standard markdown span elements are supported, as are a couple of specialized span elements. These include:

{:.indent}###[ast]; - wrap text in a single asterisk for *emphasis*
{:.indent}###[ast][ast] - wrap text in double asterisks for bold
{:.indent}###&#43;&#43; - wrap text in double plus signs for ++&lt;ins>++
{:.indent}###&#126;&#126; - wrap text in double tilde for ~~&lt;del>~~

Here are a few examples:

When I write **[ast]text[ast]**, it becomes *text*, and when I write **[ast][ast]text[ast][ast]**, it becomes **text**

You can stack them too, so that **[ast][ast][ast]text[ast][ast][ast]** becomes ***text***

When you want to wrap text with [lt]ins[gt], use the double plus signs like this: ++Stuff that's been added++. Similarly, when you want to wrap text with [lt]del[gt] tags, do it like this: ~~Stuff that's been removed~~.

That's a brief look at using AVScript's built-in span element support. Now, let's take a look at support for links, the remaining span element.

[link.links]
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

[link.inline_links]
###Inline Style:

The next paragraph has the following inline links defined within it: This is **&#91;an example]:(http://example.com/ "Inline Link Sample")** of an inline link. **&#91;This inline link]:(http://example.net/)** has no title attribute.

This is [an example]:(http://example.com/ "Inline Link Sample") of an inline link. [This inline link]:(http://example.net/) has no title attribute.

Inline links can occur anywhere in the text. Once an inline link has been processed the first time, the link ID, i.e. the part between the [ ], can be used over and over. e.g.: [an example].

[link.ref_links]
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
[link.mailto_links]
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

[link.auto_links]
###Automatic links
The final type of link format is automatic links. Automatic links are created by simply wrapping a URL with ***&lt; &gt;*** like this: <http://www.cloudylogic.com>. When you do that, the URL (everything between the angle brackets) is wrapped with an **A** tag whose **HREF** attribute is the URL.
{:.note}**NOTE: **I'm still on the fence as to whether support for automatic links will remain in AVScript, so don't get too comfortable with them just yet...

[link.aliases]
{:.plain}@@@ plainTitle
## Aliases or Variables

Aliases (aka Variables), which is essentially text substitution, is supported using a similar syntax to reference links. **[variable]=value**. Take the following example:
{:.indent}###[my name]=Ken Lowrie
[my name]=Ken Lowrie
Now, anywhere I write &#91;my name], it will be replaced with "Ken Lowrie". Let's do that now: [my name] &lt;-- Should be Ken Lowrie.

If I instead write: &#91;my name]=[&#42;Ken Lowrie*], then everywhere I write &#91;my name], it will be replaced with &lt;em>Ken Lowrie&lt;/em>. Okay, let's go ahead and do that now. 
[my name]=*Ken Lowrie*
And now, [my name] &lt;-- should be Ken Lowrie wrapped with &lt;em> tags.

You can also specify a class prefix when defining a variable, using the following syntax:

{:.syntax}--- divTitle Variable Decorators
    [SP]
    {:.bigandbold.indent}&#91;variable]={:.class}value

So, if you declared this: &#91;mynewvar]={:.bigandbold.red}My new big bold value, and then put &#91;mynewvar], you'd get this:
[mynewvar]={:.bigandbold.red}My new big bold value
[mynewvar]

### Delayed Expansion

Sometimes, it's useful to delay the expansion of a variable until right before it's used. Take the following example:

&#91;first]=Ken<br />&#91;last]=Lowrie[b]&#91;full]=&#91;first]&#91;last]

When you look at this, the expectation might be that the variable **&#91;full]** would be different if I changed &#91;first]=Brenda. But let's see what happens when we do that. Here's the code:

&#91;first]=Ken<br />&#91;last]=Lowrie[b]&#91;full]={:.red}&#91;first]&#91;last] \
[b]&#91;full][b]&#91;first]=Brenda[b]&#91;full]

And when we run that code:

[first]=Ken
[last]=Lowrie
[full]={:.red}[first] [last]
[full]
[first]=Brenda
[full]

This happens because any variable used in an assignment is expanded at the time that the variable is defined, and not when it's actually used. However, it's possible to force that behavior using **{{}}** when defining a variable. In this example, we'll change the line **&#91;full]={:.red}[{{first}}] [{{last}}]**, but everything else remains the same. Let's see what happens.

[first]=Ken
[last]=Lowrie
[full]={:.red}[{{first}}] [{{last}}]
[full]
[first]=Brenda
[full]

Sweet! Just what we wanted. By using the {{}} around a variable name used in an assignment of another variable, expansion is delayed until the variable is used. This feature is used quite a bit in the film, shot and image support later on. Check the examples in the tests directory to see it in action.

## Link aliases

Building on that, we can create aliases for inline links. Say I define a reference link like this: 
{:.indent}###&#91;cls]:https://cloudylogic.com
[cls]:https://cloudylogic.com
Now, when I write **&#91;cls]**, it is replaced with a link to https://cloudylogic.com. For example: [cls].
And that's all good. It's concise, I only have to write *cls* in [ ] and it is wrapped with an HTML link. Saves a lot of typing and potential mistakes. But what if I want to have other, more descriptive names for that URL? Good news, we can do that using a special form of aliases: [Descriptive Text]=[id], where *id* is the name of a previously described reference link. Let me go ahead and create an alias for the *cls* link so the descriptive name is Cloudy Logic.
{:.indent}###&#91;Cloudy Logic]=cls
[Cloudy Logic]=cls
Now, when I write [Cloudy Logic], it is wrapped with the link for *cls*. Cool!

[link.divs]
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

[link.headers]
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

[link.anchors]
##Bookmarks
You can also define bookmarks in your document, and then reference them with links using the following syntax:

{:.indent}###@&#43;&#91;bookmark name&#93; - Define local bookmark
{:.indent}###@&#58;&#91;bookmark name&#93; - Create hyperlink to bookmark

This is useful for creating things like a table of contents (TOC) for your document, or anywhere that you want to provide a hyperlink to a different part of your doc. These do not have to be defined in any particular order. That is, you can create the hyperlink before the bookmark has been defined.

For an example of bookmarks, just take a look at how this user guide defined and uses its own TOC.

[link.special_sections]
##Cover, Revision & Contact Sections

There are three (3) specialized sections that can be defined within your document to add commonly used information in script files. They are:

{:.syntax.width60}--- divTitle Specialized Sections
    [SP]
    {:.indent.bigandbold}@cover - To add a cover section
    {:.indent.bigandbold}@revision - To add a revision section
    {:.indent.bigandbold}@contact - To add a contact section

The details for each specialized section follows.

{:.plain}@@@ plainTitle
### Cover Title

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@cover title="title of script" author="written by" logline="logline or short description"

Each element is optional, and they can appear in any order. Also note that the value of any parameter can be whatever you want. Just because it says "author", doesn't mean you have to put the author name there. You could instead write *"Roses are Red"*, and that would be just fine...

{:.plain}@@@ plainTitle
### Revision

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@revision v="revision" timestamp="yes"
Specify the revision number of your document within the angle brackets. If timestamp is either not specified or has any value other than "No", "Off", "False" or "0", the current date and time of the document at the time of processing will also be inserted immediately following the revision number. This provides additional clarification of the version, in case you forget to bump the version number.

If you specify timestamp="No" | "Off" | "False" | "0", then the timestamp will not be added to the revision string.

{:.plain}@@@ plainTitle
### Contact

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@contact cn="name" ph="phone" em="email" c1="copyright 1" c2="copyright 2" c3="copyright 3"

The contact section allows you to specify several key elements about the script project. They include the following elements:

{:.syntax.width60}@@@ divTitle Contact Elements
    [SP]
    {:.indent.bigandbold}cn="Contact Name"
    {:.indent.bigandbold}ph="Contact Phone"
    {:.indent.bigandbold}em="Contact Email"
    {:.indent.bigandbold}c1="Copyright Line 1"
    {:.indent.bigandbold}c2="Copyright Line 2"
    {:.indent.bigandbold}c3="Copyright Line 3"

Each contact element is optional, and the elements can appear in any order. To see these tags in action, take a look at the **userguideheading.md** document in the import folder of this user guide.

[link.imports]
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

{:.note.blue.indent4}There is a gotcha when using this with BBEdit's Markup Preview. There is no context for the top level file, since it is passed to the Python script as sys.stdin. Because of that, you can't rely on avscript_md to determine the relative path of the top level file. It will work just fine when using mkavscript_md, but that won't be useful if you are using BBEdit's Markup Preview to write your documents...

The path can be specified as either **'$/path/filename'** or **'$path/filename'**. In other words, you can specify the '/' after '$' or leave it off, whatever your preference is.


[link.advanced]
{:.plain}@@@ plainTitle
##Advanced Topics: @raw, @image, @var &amp; @set

{:.syntax}@@@ divTitle Syntax:
    {:.indent}**@raw raw HTML**
    {:.indent}**@image _id="name" src="/path/to/image" ...**
    {:.indent}**@var _id="name" attr1="value1" _format="fmt string"**

These keywords, @raw, @image and @var, can be used to incorporate more control over the output of your document. I'll provide a high level look at each of them, but probably the best way to see what type of flexibility they offer would be to review some of the samples in the "tests" directory.

First things first, because these describing content dynamically using these keywords can get a bit long, you'll want to get familiar with the line continuation character '\'. The line continuation character can actually be used anywhere, but I document it here because it was this support that caused me to introduce it. Anyway, you can continue a line by ending it with the '\' character (spaces or tabs can follow, but it must be the last non-white space character on the line). When you do that, the internal file handler sees the continuation character, and reads the next line, concatenating it onto the current line. For example:

{:.syntax}--- .
    {:.indent}@var _id="myvar"  &#92;
    {:.indent4}attr1="value1" &#92;
    {:.indent4}attr2="value2"

Causes that line to be interpreted as **@var _id="myvar" attr1="value1" attr2="value2"**, as if it were all typed on the same line. You'll see this convention used quite a bit in the samples and the tests.

### The @image keyword

The @image statement can be used to include images in your document. Basically, @image is a convenient way to abstract the &lt;IMG&gt; HTML tag. The full syntax is:

{:.syntax}--- divTitle @image keyword
    {:.indent}@image _id="imagename" src="pathtoimage" alt="" _private="val"

Here's how it works. _id="imagename" is going to be how you cause the &lt;img&gt; tag to be generated in your document. Any variable that begins with an underscore (_) is considered private, and will not be included in the generated IMG HTML code. So, if you were to write:

{:.indent}#### @image _id="img1" src="path/foo.jpg" alt="my text for alt" class="myclass" _private="My private note"

and then I wrote:
{:.indent}#### [img1]

The code that would be inserted in the an "extras" DIV would be:

{:.indent}#### &ltimg src="path/foo.jpg" alt="my text for alt" class="myclass" /&gt;

Note that _id wasn't included, nor was _private. However, I can reference them both using the syntax:

{:.indent}#### &#91;img1._id] and &#91;img1._private].

This also works to reference the normal attributes. e.g. &#91;img1.class] would print **myclass**.

Note that if there's ambiguity in the names used for regular variables, image variables and *as you'll see next*, varv2 variables, you can add a prefix to clarify. For example, ***image.*** in front of the name to force the correct namespace to resolve. For example:

{:.indent.bigandbold}&#91;img1]=image1[b]@image _id="img1" \
    src="foo.png"[b]&#91;img1] would expand as ***image1***, and \
    &#91;image.img1] would expand as the ***&ltimg ...&gt*** html code.

### The @var keyword

The @var keyword is used to construct a more flexible type of variable for your documents. It uses a syntax similar to the @image keyword.


{:.syntax}--- divTitle @image keyword
    {:.indent}@var _id="varname" attr1="value1" _format="format string"

Here's how it works. _id="varname" is going to be how you reference any of the attributes of the variable. You can specify up to 20 attributes per variable, including the name, so really only 19. Accessing the variable attributes is similar to what we say with the @image attributes, using the dot syntax. Given the prior example:

{:.indent.bigandbold}&#91;varname.attr1] would be ***value1***[b] \
            &#91;varname._id] would be ***varname***, and [b]\
            &#91;varname._format] would be ***format string***.

So that's pretty cool, but there's a bit more to the _format attribute. You can reference the attributes contained within the variable by using **{{self.}}.attrname**. Given that, if we rewrote the prior example as:

{:.indent.bigandbold} @var _id="varname" first="ken" last="lowrie" _format="{{self.first}} {{self.last}}" 

and then we wrote:

{:.indent.bigandbold}&#91;varname]

@var _id="varname" first="ken" last="lowrie" _format="{{self.first}} {{self.last}}"

The result would be: **[varname]**

Using that, you can build some pretty powerful tools for automating frequently used tasks in your documents. Take a look at the film.md, image.md and varv2.md tests to get an idea of what you can do.

Before we leave this, take note of the difference between {{first}} and {{self.first}}. Both syntaxes are valid, but the first one references the normal variable first, while the second one (self.first) references the first attribute defined within the *varname* variable. Also take note that you can reference the attributes of other @var variables as long as you qualify them. Let me show you a quick example of that. Take this:

{:.indent.bigandbold} @var _id="var1" first="ken" last="lowrie"[b] \
@var _id="var2" prefix="mr." _format="{{self.prefix}} {{var1.first}} {{var1.last}}"[b] \
&#91;var2]

When you run it, you get:

@var _id="var1" first="ken" last="lowrie"
@var _id="var2" prefix="mr." _format="{{self.prefix}} {{var1.first}} {{var1.last}}"
{:.indent}**[var2]**

One last thing, remember how we discussed that sometimes you need a way to resolve ambiguities of variables across the different variable types? **image.** can be used to resolve a variable inside the @image namespace, and **varv2.** can be used to resolve a variable inside the @var namespace. Given that:

{:indent.bigandbold} &#91;var2] and &#91;***varv2.***var2] resolve to the same variable.

This can let you build some really cool automation in your documents. But you need one more thing before you get started. A way to change one or more attributes of an existing @image or @var variable. Enter @set.

### @set keyword

Once you build some cool abstractions to assist with the automation of common tasks in your documents, you'll need to have a method for changing a value for an attribute in order to affect the generation of the output. Take the following example.

Say we want to display a storyboard in our shot AV file along with some common camera and setup information. So we create the following set of expansions to assist:

{:.indent.bigandbold}// provide default values[b]\
&#91;_i_width]=90%[b]\
[_b_size]=1px[b]\
[_b_type]=solid[b]\
[img-border-style]=border:[{{_b_size}}] [{{_b_type}}];padding:1em;[b]\
[img-inline-style]=margin-left:auto;margin-right:auto;width:[{{_i_width}}];[b]\
[img-st-inline]=[{{img-inline-style}}][b]\
[img-st-inline-border]=[{{img-inline-style}}][{{img-border-style}}][b]\
[ss]=[{{img-st-inline-border}}][b]\
// Some useful defaults for _i_width[b]\
[IMG_SIZE_THUMB]=20%[b]\
[IMG_SIZE_SMALL]=40%[b]\
[IMG_SIZE_MEDIUM]=70%[b]\
[IMG_SIZE_LARGE]=90%[b]\
[_shotinfo_]=&lt;table class="shotinfo"&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="center" colspan="2"&gt;***Shot Information***&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;th class="item"&gt;Item&lt;/th&gt;&lt;th class="desc"&gt;Description&lt;/th&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Shot&lt;/td&gt;&lt;td class="desc"&gt;{{self.name}}&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Desc&lt;/td&gt;&lt;td&gt;*{{self.desc}}*&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Lens&lt;/td&gt;&lt;td&gt;**{{self.lens}}**&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Crane&lt;/td&gt;&lt;td&gt;{{self.crane}}&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
&lt;/table&gt;[b]\
@var _id="shotinfo" _format="- [varv2.{{self.shotid}}.desc]&lt;br /&gt;[image.{{self.shotid}}]&lt;br /&gt;[varv2.{{self.shotid}}]" shotid="NOTSET"

And now we agree to use the convention of defining an **@image** and an **@var** variable using the same ***_id*** value, which would result in us doing something like this in our document:

{:.indent.bigandbold} @var _id="shot1" desc="*Short Description shot 1*" lens="**85mm**" crane="yes" _format="[_shotinfo_]"[b]\
@image _id="shot1" src="[imgpath]/shot1.jpg" style="[ss]"[b][b]\
@var _id="shot2" desc="*Short Description shot 2*" lens="**50mm**" crane="yes" _format="[_shotinfo_]"[b]\
@image _id="shot2" src="[imgpath]/shot2.jpg" style="[ss]"
And now, we can auto generate the shot and info using syntax like this:

{:.indent.bigandbold} @set _id="shotinfo" shotid="shot1"[b]\
[varv2.shotinfo][b]\
And some random shot comments here.[b]\
[b]\
@set _id="shotinfo" shotid="shot2"[b]\
[varv2.shotinfo][b]\
Some random shot 2 comments here.

And then, when we run the prior code, we'd get this:

// provide default values
[_i_width]=90%
[_b_size]=1px
[_b_type]=solid
[img-border-style]=border:[{{_b_size}}] [{{_b_type}}];padding:1em;
[img-inline-style]=margin-left:auto;margin-right:auto;width:[{{_i_width}}];
[img-st-inline]=[{{img-inline-style}}]
[img-st-inline-border]=[{{img-inline-style}}][{{img-border-style}}]
[img-st-block]=display:block;[{{img-inline-style}}]
[img-st-block-border]=display:block;[img-inline-style][img-border-style]
[ss]=[{{img-st-inline-border}}]
// Some useful defaults for _i_width
[IMG_SIZE_THUMB]=20%
[IMG_SIZE_SMALL]=40%
[IMG_SIZE_MEDIUM]=70%
[IMG_SIZE_LARGE]=90%

[_shotinfo_]=<table class="shotinfo">\
    <tr><td class="center" colspan="2">***Shot Information***</td></tr>\
    <tr><th class="item">Item</th><th class="desc">Description</th></tr>\
    <tr><td class="item">Shot</td><td class="desc">{{self.name}}</td></tr>\
    <tr><td class="item">Desc</td><td>*{{self.desc}}*</td></tr>\
    <tr><td class="item">Lens</td><td>**{{self.lens}}**</td></tr>\
    <tr><td class="item">Crane</td><td>{{self.crane}}</td></tr>\
</table>

@var _id="shotinfo" _format="- [varv2.{{self.shotid}}.desc]<br />[image.{{self.shotid}}]<br />[varv2.{{self.shotid}}]" shotid="NOTSET"

@var _id="shot1" desc="*Short Description*" lens="**85mm**" crane="yes" _format="[_shotinfo_]"
@image _id="shot1" src="[path]/shot1.jpg" style="[ss]"

@var _id="shot2" desc="*Short Description*" lens="**50mm**" crane="yes" _format="[_shotinfo_]"
@image _id="shot2" src="[path]/shot2.jpg" style="[ss]"


@set _id="shotinfo" shotid="shot1"
[varv2.shotinfo]
And some random shot comments here.[b]\

@set _id="shotinfo" shotid="shot2"
[varv2.shotinfo]
Some random shot 2 comments here.

@break
What the ...? Sweeeeet! So basically, by simply changing the value of the attribute **shotid** in the **shotinfo** variable, we can cause **shotinfo** to display different shots (both images and shot information)!

Okay, that should give you an idea of how you can use these advanced keywords to build some cool automation for your AV documents. There's quite a bit of these already built and included in the various tests that I've created to assist with the development, so take a look at them, and build from there! And when you come up with some new and improved versions of them, please share!

Keep in mind that once you have this stuff defined, it's easy to change. For example, if I write &#91;_i_width]=80%, and then write &#91;varv2.shotinfo], look what happens:

[_i_width]=80%
[varv2.shotinfo]

@break
And look what happens if we generate the image outside of a shot. I'll do that by just writing the image reference, like so: &#91;image.shot1], and you'll get this:

@break
[image.shot1]

I can make it small by setting the width to one of those predefined sizes. For example, &#91;_i_width]=&#91;IMG_SIZE_SMALL]. And then I'll get this:

[_i_width]=[IMG_SIZE_SMALL]
[image.shot1]

Awww. And if I don't want the border, I could choose a different style. So if I write this:

{:.indent.bigandbold} &#91;ss]=&#91;{{img-st-inline}}[b]\
    &#91;image.shot1]

I'll get this instead:

[ss]=[{{img-st-inline}}]
[image.shot1]

Same image, but without a border.

So that pretty much sums up the advanced section. Hopefully it was helpful, if not, ask questions, and I'll clarify. Or better yet, improve the docs, and submit a pull request. :)

[link.predefined_classes]
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

[link.shotlist]
{:.plain}@@@ plainTitle
##Shotlist

For convenience, you can list all of the defined shots in a list at the end of your script by using the ***///Shotlist///*** tag. This tag must begin on a line of its own, and it is replaced on the fly with all the shots that have been defined up to that point. The following shows what it would do for this document:

///Shotlist///

[link.debug]
{:.plain}@@@ plainTitle
{:.plainTitle}##Debugging

There are two debugging tags that can be used in your document, and like ***///Shotlist///***, they must be on a line of their own.

{:.indent}###///Links/// - dumps all the links defined so far
{:.indent}###///Variables/// - dumps all the variables (aliases) defined

Here are those two tags in action for this document.

///Links///
///Variables///

[link.summary]
{:.plain}@@@ plainTitle
## Summary

Well that's it! Hope you've enjoyed reading the docs for the avscript_md utility. More importantly, I hope that you can use this app to streamline your audio/visual script development!
