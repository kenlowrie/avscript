###Table of Contents
@link _id="inlinemd" _inherit="bookmark_template"
@link _id="links" _inherit="bookmark_template"
@link _id="inline_links" _inherit="bookmark_template"
@link _id="ref_links" _inherit="bookmark_template"
@link _id="auto_links" _inherit="bookmark_template"

[link.inlinemd.link(text="Inline Markdown")] - **Formatting content inline**
[link.links.link(text="Links")] - **Inline and Reference Link Styles**
[link.inline_links.link(text="Inline Links")] - **Creating links inline**
[link.ref_links.link(text="Reference Links")] - **Creating reference links**
[link.auto_links.link(text="Automatic Links")] - **Creating automatic links**

// markdown tests
@@ [link.inlinemd]
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
@@ [link.links]
##Links
This is a section about links
@@ [link.inline_links]
###Inline Style:

The next paragraph has inline links defined: This is **&#91;an example]:(http://example.com/ "Inline Link Sample")** of an inline link. **&#91;This inline link]:(http://example.net/)** has no title attribute.

@link _="sample1" _inherit="_template_" title="Inline Link Sample" href="http://example.com"
@link _="sample2" _inherit="_template_" href="http://example.net"

This is [link.sample1(_text="an example")] of an inline link. [link.sample2(_text="This inline link")] has no title attribute.

Inline links can occur anywhere in the text. Once an inline link has been processed the first time, the link ID, i.e. the part between the [ ], can be used over and over. e.g.: [link.sample1].

@@ [link.ref_links]
###Reference Style:
Reference links use the format [linkID]:url "optional title". Essentially, just like inline links, but without the ( ) surrounding the URL and optional title.

The reference link style **must** be placed at the beginning of a line. Unlike true Markdown, reference links *must* be defined before they are referenced in the document. Let's create a reference link for the Google Home Page.

{:.indent}####@link _="Google" _inherit="_template_" title="Google Search Page" href="https://google.com"
@link _="Google" _inherit="_template_" title="Google Search Page" href="https://google.com" _text="{{self._}}"

If I write &#91;Google], it is wrapped like so: [Google].

Now, I can go ahead and write **&#91;inline 2]**, like this: [inline 2], and it's a valid link!
@@ [link.auto_links]
###Automatic links
The final type of link format is automatic links. Automatic links are created by simply wrapping a URL with ***&lt; &gt;*** like this: <http://www.cloudylogic.com>. When you do that, the URL (everything between the angle brackets) is wrapped with an **A** tag whose **HREF** attribute is the URL. Unfortunately, this is no longer supported. However, the default template for links includes an attribute *_asurl*, which returns the href styled appropriately. For example: [link.Google._asurl]

&nbsp;

@dump var="." link="."