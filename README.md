# avscript_md

### A/V Script Markdown Processor

Welcome to the A/V Script Markdown Processor. This document should help you get the project up and running. If you have questions, or would like to provide feedback and/or to report a bug, feel free to contact the author, Ken Lowrie, at [www.kenlowrie.com](http://www.kenlowrie.com/).

### Attributions

This project was inspired by John Gruber's [Markdown](https://daringfireball.net/projects/markdown/), the [Python Markdown](https://github.com/Python-Markdown/markdown) Project, and Mark Boszko's [AVScriptFormat](https://github.com/bobtiki/AVScriptFormat) BBEdit plug-in.

#### Installing this app on your system

To install this on your system, do the following from a terminal window:

TODO: This isn't done yet. Hang tight...

cp avscript_md ~/Library/Application\sSupport\BBEdit\Preview\sFilters
cp avscript_md.css ~/Library/Application\sSupport\BBEdit\Preview\sCSS

TODO: Rethink these instructions so the system can be used stand alone too.

That's it! If you run into any problems, feel free to contact me for assistance.

#### Why A/V Script Markdown Processor?

As I wrote more and more scripts that relied partially on Python Markdown, along with the AVScriptFormat CSS mentioned above, I found myself wanting features, mostly to help avoid duplication amongst AV scripts, that were too difficult (for me) to implement within the existing framework. Someday when I have some time, I'd love to learn the ins and outs of Python Markdown, so I could write proper extensions to implement the features I need, while being able to rely on a proper Markdown implementation.

Enter AVScript_md, mkavscript_md and avscript_md.css. These two Python scripts and the corresponding CSS file make up a BBEdit compliant Markdown-syntax-like system for creating Audio/Visual scripts from text documents. Although BBEdit isn't required to use the scripts, it is quite convenient to use their built-in markdown preview support when writing.

#### Getting Started with the App

I don't think this app requires much documentation. But again, I will write up some additional basic information after I finish fixing a few more bugs and testing it out on different devices and browsers.

An example AV Script is included with the source. It's called "example.md", and it relies on an import file import/header.md.

User documentation is available via the "userdocs.md" file, which relies on the import file import/userguideheading.md.


#### Summary

This concludes the documentation on the A/V Script Markdown (avscript_md) Processor.
