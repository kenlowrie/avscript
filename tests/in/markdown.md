###Table of Contents
@:[inlinemd]<<Inline Markdown>> - **Formatting content inline**
@:[links]<<Links>> - **Inline and Reference Link Styles**
@:[inline+links]<<Inline Links>> - **Creating links inline**
@:[ref+links]<<Reference Links>> - **Creating reference links**
@:[auto+links]<<Automatic Links>> - **Creating automatic links**

// markdown tests
@+[inlinemd]
*emphasis*
**strong**
***emphasis and strong***
++this is added++
~~this is deleted~~
// blank lines

    
    
// multiple markdowns
*emphasis* and regular and **strong** and regular and ***both***
not at start *emphasis* and regular and **strong** and regular and ***both***
not or start *emphasis* and regular and **strong** and regular and ***both*** or end
++this is added++ and ~~this is deleted~~
n o s ++this is added++ and ~~this is deleted~~
nos ++this is added++ and ~~this is deleted~~ or end

// nested
*emphasis and **strong** and ++new stuff++ and ~~old stuff~~*
*emphasis and **strong** and ~~old ++new stuff inside++ stuff~~ and ~~old stuff~~*

// headers
# h1
## h2
### h3
#### h4
##### h5
###### h6

#h1
words
##h2
words
###h3
words
####h4
words
#####h5
words
######h6
words

// links
@+[links]
##Links
This is a section about links
@+[inline+links]
###Inline Style:

The next paragraph has inline links defined: This is **&#91;an example]:(http://example.com/ "Inline Link Sample")** of an inline link. **&#91;This inline link]:(http://example.net/)** has no title attribute.

This is [an example]:(http://example.com/ "Inline Link Sample") of an inline link. [This inline link]:(http://example.net/) has no title attribute.

Inline links can occur anywhere in the text. Once an inline link has been processed the first time, the link ID, i.e. the part between the [ ], can be used over and over. e.g.: [an example].

@+[ref+links]
###Reference Style:
Reference links use the format [linkID]:url "optional title". Essentially, just like inline links, but without the ( ) surrounding the URL and optional title.

The reference link style **must** be placed at the beginning of a line. Unlike true Markdown, reference links *must* be defined before they are referenced in the document. Let's create a reference link for the Google Home Page.

{:.indent}###[Google]:https://google.com "Google Search Page"
[Google]:https://google.com "Google Search Page"

If I write &#91;Google], it is wrapped like so: [Google].

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
@+[auto+links]
###Automatic links
The final type of link format is automatic links. Automatic links are created by simply wrapping a URL with ***&lt; &gt;*** like this: <http://www.cloudylogic.com>. When you do that, the URL (everything between the angle brackets) is wrapped with an **A** tag whose **HREF** attribute is the URL.

&nbsp;
