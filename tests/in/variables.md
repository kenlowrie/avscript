// variables

@+[aliases]
{:.plain}@@@ plainTitle Aliases
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

[abc]=123
[def]=456
[xyz]=?b=[abc]%20[def]
[jitlinkvar]:https://mydomain.com?a=[abc]%20[def]
[jitlinkvar2]:https://mydomain.com[xyz]
Here is my [jitlinkvar]
Here is my [jitlinkvar2]

{:.red.center}### avscript tester doc
@cover title="User Manual" author="Ken Lowrie" logline="This is a user manual for the AVScript utility."
// $$revision$$:<<*1b*>>
{:.blue.plain}--- plainTitle Variables
We can define variables using the syntax: ***[name]=value***. Here's an example. The next line will define the variable *whoami* and set it to *Ken Lowrie*.
[whoami]=Ken Lowrie
Now, whenever I write whoami inside square brackets **[ ]**, it will replace it with *Ken Lowrie*. Let's try that now. Hello, my name is *[whoami]*. That's pretty straightforward...
{:.plain}@@@ plainTitle Links
We can also define hyperlinks using a similar syntax: [linkID]:linkurl. Let's go ahead and define a few links now...
[cls]:https://cloudylogic.com
//[me]:mailto:myemail@cloudylogic.com
I've defined two new links, one called *cls* which is a standard HTTPS link for my website, and another called *me*, which is a mailto: link that will compose a new email to myself. I use these just like variables, just write the ID inside square brackets.

Visit my domain [cls] or send [me] an email. If you click on either *cls* or *me*, they should behave accordingly.

#### Aliases

So far so good. Typing [cls] is certainly better than typing out the entire URL, but it's not very descriptive... Sometimes, maybe I want to have more text, or even the URL as the hyperlink. In those cases, you can create variables whose value matches the name of a linkID, and when you use that variable, it will wrap the variable name with the link tag. Kind of like creating an alias for the link description.
So let's try that. The next line is ***defining the variable*** called "My Email Address" and setting its value to "me". 
[My Email Address]=me
By defining a variable's value such that the value is a valid linkID, when you use the variable's name in the document, it will be wrapped in the linkIDs hyperlink. So now when I write [My Email Address], it is more friendly than [me], even though they evaluate to the same link.

You can create more than one "alias" to the same underlying link. Here's an example of that:
[My Production Website]=cls
[Cloudy Logic Studios, LLC]=cls
In the previous 2 lines, I created two new variables and set both of their values to the linkID called *cls*. So now when I write [My Production Website] and [Cloudy Logic Studios, LLC], both of them are links to my website.

Most of the time, you'll just add normal links with the regular link syntax, but sometimes it's cool to have these other options.

#### Inline links

So far, both the reference link syntax and the variable definition syntaxes require that those elements be on lines by themselves. Not a big deal when you're using things over and over, but what if you just want to write a link inline in the document? You can do that using the inline syntax, which is similar to the reference link syntax, except that you need to wrap the URL with ()'s. For example, you would write: &#91;linkID]:(URL). Here's one for [Cloudy Logic]:(https://cloudylogic.com "title2abvg"), and one for [Google without a title]:(https://google.com).

{:.red}#### Shorthand link encoding - Will this be deprecated?

You can also just write a valid URL inside angle brackets, i.e. &lt; &gt;, for an even quicker way to write URLs inline. For example, <https://www.google.com> or <https://cloudylogic.com>. For now, these short hand methods require that the protocol be present on the URL. Not sure if I'm going to keep this support in though, because it's a bit complex to parse...

Here are a couple more examples:

//[feedback]:mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback
[Link to Article]:https://wordpress.org/news/2018/05/the-month-in-wordpress-april-2018/
[Link to Article2]:https://domain.com/another_article_link
[domain]=cls
[Link to Article] <-- That should have been turned into a link
[One with Title]:(https://www.cloudylogic.com "This is a link title...")

You can send [feedback]. Or you can just email [me]. Or go to my [domain]. But don't do that if [Cloudy Logic]:(cls) is not defined. Finally, [One with Title]

Remember, variable definitions and reference link definitions must be declared on a line by themself. If you put more stuff, it will just process the first one. If it isn't at the beginning of the line, it'll be ignored. For example:

[varName]=varValue is okay.
But [varName]=varValue is not...

///Variables///

///Links///
