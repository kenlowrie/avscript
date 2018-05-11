AVScript User Manual



Inline references

*text* will place text in <em>text</em> tags.
**text** will place text in <strong>text</strong> tags.

You can stack them, so that ***text*** becomes <em><strong>text</strong></em>

Links

Both inline and reference style links are supported.

Inline Style:

This is [an example](http://example.com/ "Title") of an inline link.

[This inline link](http://example.net/) has no title attribute.

Inline links can occur anywhere in the text. Once an inline link 

## Variables

Variables, or essentially, text substitution is supported using the reference link style.

[Ken Lowrie][id]

Now, anywhere I write [id], it will be replaced with "Ken Lowrie". Of course it won't be surrounded by quotes, however, if I instead write: [*Ken Lowrie*][id], then everywhere I write [id], it will be replaced with <em>Ken Lowrie</em>.

Building on that, if I then "define" *id* like this:

[id]: http://www.cloudylogic.com

Now, whenever I write [Ken Lowrie], it will instead be wrapped with <a href="http://www.cloudylogic.com">Ken Lowrie</a>.

So, using [anytext][id] is an easy way to perform text substitution, and if we assign a link to the substitution identifier, then if the substitution text is used inside square brackets on its own, it'll be wrapped with an HTTP hyperlink.

[id] used here then works?

 