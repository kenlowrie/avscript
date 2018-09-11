@var _id="header" \
     _format="# [code.repeat.run(t=\"-\", c=\"42\")]"

[header]

//@debug
@embed 'filename' - like @import, except just includes the code without processing. Could be useful for inserting raw html directly into the output, w/o processing at all. Would be especially cool if you could do this inline, like this:
&#91;myvar]=@embed 'foo.html'
Then, the embedded file would be marked down as normal, giving more flexibility. This wouldn't work, though, because it would have \n in the input, and that would fail, right?
@ @raw @embed 'foo.html'

[header]

// -------------------------------------------------------------------




