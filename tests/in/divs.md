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

