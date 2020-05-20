
@var _id="header" \
     _format="# [code.repeat.run(t=\"-\", c=\"42\")]"

[header]

@var _id="display0" \
    print="0"\
    test="1"\ 
    _format="{{code.equals(v1=\"self.print\", v2=\"self.test\", true=\"self.true\", false=\"self.false\")}}"\
    true="[code.replace(var=\"$.shotid\", val=\"var.display.shotid\", str=\"var.display.push\")]"\
    push="[code.pushlines(shotid=\"$.shotid\" t=\"[basic.shot_left]\")]"\
    false=""

//@debug on="ns.code"
@dump code="equals" var="display"
[code.equals(v1="display.print", v2="display.test", true="display.true", false="display.false")]

 
@import '[sys.imports]/shot.md' 
@import '[sys.imports]/../../avscript/import/shot.md' 

[header]
//@debug on="avscript.line"
[var.display(shotid="shot00", print="1")]
@dump var="display"
[header]
[var.display2(shotid="shot00", print="1")]
@dump var="display0"

@stop


//@debug toggle="." on="." off="." enabled="." foo="bar"  
@embed 'filename' - like @import, except just includes the code without processing. Could be useful for inserting raw html directly into the output, w/o processing at all. Would be especially cool if you could do this inline, like this:
&#91;myvar]=@embed 'foo.html'
Then, the embedded file would be marked down as normal, giving more flexibility. This wouldn't work, though, because it would have \n in the input, and that would fail, right?
@ @raw @embed 'foo.html'

[header]
// -------------------------------------------------------------------

@import '[sys.imports]/divs.md'
@import '[sys.imports]/shot.md'
@import '[sys.imports]/image.md'
[ss]=[{{var.img_def.img_st_inline_border}}]
[IMG_SIZE_LARGE]
[img_factory(nm="shot1", s="[sys.basepath]/../docs/import/shot1.jpg")]
[img_factory(nm="shot2a", s="[sys.basepath]/../docs/import/shot2.jpg")]
[code.shot_factory(nm="shot1", d="my desc")] 
[code.shot_factory(nm="shot2a", d="my really cool shot")] 
[shotinfo2(shotid="shot1")]

@break

# Example of code.pushline
[code.pushline(t="[var.shot1]")][code.pushline(t="@@ - [image.shot1]")]

//@debug on="ns.var" 
# Example of code.pushlines
//[code.pushlines(shotid="shot1", t="@@ [avwrapper.start][image.$.shotid][avwrapper.end]\n@@ <p>[var.$.shotid]</p>")] 
@break

//[storyboard]=@@ [{{avwrapper.start}}][image.$.shotid][{{avwrapper.end}}]
//[shotdetail]=@@ {{html.p.<}}[var.$.shotid]{{html.p.>}}
//[shot_split]=[{{storyboard}}]\n[{{shotdetail}}]

# Example of code.pushlines2
[code.pushlines(shotid="shot1", t="[storyboard]\n@@ <p>[var.$.shotid]</p>")] 
@break
[code.pushlines(shotid="shot2a", t="[storyboard]\n[shotdetail]")] 
[code.pushlines(shotid="shot1", t="[storyboard]\n[shotdetail]")] 
[code.pushlines(shotid="shot1", t="[shot_split]")] 
[IMG_SIZE_THUMB] 
[code.pushlines(shotid="shot1", t="[shot_split]")] 


// implement the quick and dirty "disable debug prints" while 
// executing code. See how that works

