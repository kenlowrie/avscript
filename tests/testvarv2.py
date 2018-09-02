#!/usr/bin/env python


from sys import path
from os.path import dirname, abspath, realpath, split, join
bin_path, whocares = split(dirname(realpath('__file__')))
lib_path = join(abspath(bin_path),'avscript')
path.insert(0, lib_path)
from sys import exit

from avs.variable import *

from markdown import Markdown

def assertEqual(a, b):
    assert a == b

def assertNotEqual(a, b):
    assert a != b

md = Markdown()
ns = Namespaces(md.markdown, md.setNSxface)

def msg(msg):
    print(msg)

def sep(size=60):
    print('{}'.format('-'*size))

def gvExpr(expr):
    print('GV:{}={}'.format(expr, ns.getValue(expr)))

def gvMsgExpr(msg, expr):
    print('GV:{}={}'.format(msg, ns.getValue(expr)))

def gvAE(a, b):
    assertEqual(a, ns.getValue(b))
    
def mdExpr(expr):
    print('MD:{}={}'.format(expr, md.markdown(expr)))

def mdMsgExpr(msg, expr):
    print('MD:{}={}'.format(msg, md.markdown(expr)))
    
def mdAE(a, b):
    #print(">>>>>>>>>>>>>>>{}---{}".format(a,b))
    assertEqual(a, md.markdown(b))
    
def gvTest(varname, value, mdValue=None):
    gvExpr(varname)
    gvAE(value, varname)
    mdVarName = '[{}]'.format(varname)
    mdExpr(mdVarName)
    mdAE(value if mdValue is None else mdValue, mdVarName)

def gvTestGV(varname, value, mdValue=None):
    gvExpr(varname)
    gvAE(value, varname)

def gvTestMD(varname, value):
    mdExpr(varname)
    mdAE(value, varname)

msg('Adding to default name space')
sep(28)
ns.addVariable('value', name='varname')

gvTest('varname', 'value')
gvTest('basic.varname', 'value')

gvTestMD('[basic.varname(foo="bar")]', 'value')

ns.addVariable('[{{value}}]', name='v1v')
ns.addVariable('[{{varname}}]', name='v1n')
gvTest('v1v', '[value]')

gvTest('v1n', '[varname]', 'value')

sep()
msg("Adding variable by same name to each namespace")

mydict = {'_': 'v0', 'name': 'INVALID dict 0 - should not be in basic. namespace'}
md1=mydict.copy()
md2=mydict.copy()
md3=mydict.copy()
md4=mydict.copy()
md5=mydict.copy()
md1['name']='var dict 1'
md2['name']='html dict 1'
md3['name']='image dict 1'
md3['_tag']='image'
md4['name']='link dict 1'
md4['_tag']='a'
md5['name']='code dict 1'

try:
    ns.addVariable(mydict, name='v0')
except TypeError as te:
    msg("ERROR: {}".format(te))

msg('adding "v0.class" to basic name space')
ns.addVariable("basic attr", name="v0.class")

msg('adding "v0" to var name space')
ns.addVariable(md1, ns='var')
msg('adding "v0" to html name space')
ns.addVariable(md2, ns='html')
msg('adding "v0" to image name space')
ns.addVariable(md3, ns='image')
msg('adding "v0" to link name space')
ns.addVariable(md4, ns='link')
msg('adding "v0" to code name space')
ns.addVariable(md5, ns='code')

gvTest('v0.class', 'basic attr')
gvTest('basic.v0.class', 'basic attr')

gvTest('v0.name', 'var dict 1')
gvTest('html.v0.name', 'html dict 1')
all_d_ns = ['var', 'html', 'image', 'link', 'code']
for item in all_d_ns:
    msg('Checking namespace {}'.format(item))
    gvTest('{}.v0.name'.format(item), '{} dict 1'.format(item))

gvTest('v0', ' name="var dict 1"<br />\n')
gvTest('var.v0', ' name="var dict 1"<br />\n')
gvTest('html.v0', '<[html.v0._tag] name="html dict 1"></[html.v0._tag]>')
gvTest('image.v0', '<image name="image dict 1"/>')
gvTest('link.v0', '<a name="link dict 1"></a>')
gvExpr('code.v0')
gvTest('code.v0', ' name="code dict 1"<br />\n')

ns.setAttribute('html.v0', 'class', 'class42')
gvTest('html.v0.class', 'class42')

sep()

var0= {'_': 'var0', 
       '_format': '{{self._public_attrs_}}', 
       'style': '{{self.other}}', 
       'other': 'yes!'}

ns.addVariable(var0, ns="var")

gvTest('var0', ' style="{{self.other}}" other="yes!"')
gvTest('var0._public_attrs_', ' style="{{self.other}}" other="yes!"')
gvTest('var0._private_attrs_', ' _format="{{self._public_attrs_}}"')
gvTest('var0._all_attrs_', ' _format="{{self._public_attrs_}}" style="{{self.other}}" other="yes!"')
gvTest('var0.style', 'yes!')
gvTest('var0.other', 'yes!')

gvTest('var.var0', ' style="{{self.other}}" other="yes!"')
gvTest('var.var0._public_attrs_', ' style="{{self.other}}" other="yes!"')
gvTest('var.var0._private_attrs_', ' _format="{{self._public_attrs_}}"')
gvTest('var.var0._all_attrs_', ' _format="{{self._public_attrs_}}" style="{{self.other}}" other="yes!"')
gvTest('var.var0.style', 'yes!')
gvTest('var.var0.other', 'yes!')

anc0 = {'_id': 'anc0', 
        '_tag':'a', 
        '_link':'<a href="#{{self.id}}">{{self._linktext}}</a>', 
        '_linktext':'The bookmark text used for link', 
        'id':'the_bookmark_id'}

ns.addVariable(anc0, ns="html")

gvTest('anc0', '<a id="the_bookmark_id"></a>')
gvTest('anc0._tag', 'a')
gvTest('anc0._link', '<a href="#the_bookmark_id">The bookmark text used for link</a>')
gvTest('anc0._linktext', 'The bookmark text used for link')
gvTest('anc0.id', 'the_bookmark_id')
gvTest('html.anc0', '<a id="the_bookmark_id"></a>')
gvTest('html.anc0._tag', 'a')
gvTest('html.anc0._link', '<a href="#the_bookmark_id">The bookmark text used for link</a>')
gvTest('html.anc0._linktext', 'The bookmark text used for link')
gvTest('html.anc0.id', 'the_bookmark_id')

anc1 = {'_id': 'anc1', 
        '_format': '<a id="{{self.id}}"></a>', 
        'link':'<a href="#{{self.id}}">{{self.linktext}}</a>', 
        'linktext':'The bookmark text used for link', 
        'id':'the_bookmark_id'}

ns.addVariable(anc1, ns="html")

gvTest('anc1', '<a id="the_bookmark_id"></a>')
gvTest('anc1.link', '<a href="#the_bookmark_id">The bookmark text used for link</a>')
gvTest('anc1.linktext', 'The bookmark text used for link')
gvTest('anc1.id', 'the_bookmark_id')
gvTest('html.anc1', '<a id="the_bookmark_id"></a>')
gvTest('html.anc1.link', '<a href="#the_bookmark_id">The bookmark text used for link</a>')
gvTest('html.anc1.linktext', 'The bookmark text used for link')
gvTest('html.anc1.id', 'the_bookmark_id')

ns.updateVariable({'_id': 'anc1', 'linktext': 'Change the link text'}, ns="html")
gvTest('anc1', '<a id="the_bookmark_id"></a>')
gvTest('anc1.link', '<a href="#the_bookmark_id">Change the link text</a>')
gvTest('anc1.linktext', 'Change the link text')
gvTest('anc1.id', 'the_bookmark_id')
gvTest('html.anc1', '<a id="the_bookmark_id"></a>')
gvTest('html.anc1.link', '<a href="#the_bookmark_id">Change the link text</a>')
gvTest('html.anc1.linktext', 'Change the link text')
gvTest('html.anc1.id', 'the_bookmark_id')

sep(25)
msg('Testing adding a new variable via the updateVariable method')
anc2 = {'_id': 'anc2', 
        '_tag': 'a', 
        'id':'text id'}
ns.updateVariable(anc2, ns="html")

gvTest('anc2', '<a id="text id"></a>')
gvTest('anc2.id', 'text id')
gvTest('html.anc2', '<a id="text id"></a>')
gvTest('html.anc2.id', 'text id')

del anc2['_tag']
del anc2['id']
anc2['_id'] = 'anc2'
anc2['_link'] = '<a href=\"#{{self.id}}\">the text to hyperlink</a>'
ns.updateVariable(anc2, ns="html")
gvTest('anc2._link','<a href="#[html.anc2.id]">the text to hyperlink</a>')
gvTest('html.anc2._link','<a href="#[html.anc2.id]">the text to hyperlink</a>')

"""
"""
sep()
msg('Implementing images using the HTML tag and TEMPLATES')

img0 = {'_id': 'imgTMPL', 
        '_tag': 'img', 
        '_format': '<{{self._tag}}{{self._public_attrs_}}/>', 
        'src': '[path]/XXX', 
        'class': 'myclass'}

ns.addVariable(img0, ns="html")
gvTest('imgTMPL', '<img src="[path]/XXX" class="myclass"/>')
gvTest('imgTMPL._tag', 'img')
gvTest('imgTMPL._format', '<img src="[path]/XXX" class="myclass"/>')
gvTest('imgTMPL.src', '[path]/XXX')
gvTest('imgTMPL.class', 'myclass')
gvTest('html.imgTMPL', '<img src="[path]/XXX" class="myclass"/>')
gvTest('html.imgTMPL._tag', 'img')
gvTest('html.imgTMPL._format', '<img src="[path]/XXX" class="myclass"/>')
gvTest('html.imgTMPL.src', '[path]/XXX')
gvTest('html.imgTMPL.class', 'myclass')

img1 = {'_id': 'img0', 
        '_inherit': 'imgTMPL', 
        'src': '[path]/YYY'}
ns.addVariable(img1, ns="html")

gvTest('img0', '<img src="[path]/YYY" class="myclass"/>')
gvTest('img0.src', '[path]/YYY')
gvTest('img0._tag', 'img')
gvTest('img0.class', 'myclass')
gvTest('img0._format', '<img src="[path]/YYY" class="myclass"/>')
gvTest('html.img0', '<img src="[path]/YYY" class="myclass"/>')
gvTest('html.img0.src', '[path]/YYY')
gvTest('html.img0._tag', 'img')
gvTest('html.img0.class', 'myclass')
gvTest('html.img0._format', '<img src="[path]/YYY" class="myclass"/>')

lnk0 = {'_id': 'cls', 
        '_tag': 'a', 
        '_format': '{{self._all_attrs_}}', 
        'class': 'myclass'}

ns.addVariable(lnk0, ns="link")

gvTest('cls',' _tag="a" _format="{{self._all_attrs_}}" class="myclass"')
gvTest('cls.<','<a class="myclass">')
gvTest('cls.>','</a>')
gvTest('cls.class','myclass')
gvTest('cls._tag', 'a')

gvTest('link.cls',' _tag="a" _format="{{self._all_attrs_}}" class="myclass"')
gvTest('link.cls.<','<a class="myclass">')
gvTest('link.cls.>','</a>')
gvTest('link.cls.class','myclass')
gvTest('link.cls._tag', 'a')

my_jit_attrs = {'class': 'myclass2', 
                'style': 'my cool style', 
                '_newfmt': '{{self.style}}'}

msg("Adding new attributes to link.cls variable...")
ns.getValue('link.cls._newfmt', jit_attrs=my_jit_attrs)

gvTest('cls.class', 'myclass2')
gvTest('cls.style', 'my cool style')
gvTest('cls._newfmt', 'my cool style')
gvTest('link.cls.class', 'myclass2')
gvTest('link.cls.style', 'my cool style')
gvTest('link.cls._newfmt', 'my cool style')

#[alt]=Google image
ns.addVariable('Google image', 'alt-text')
gvTest('alt-text', 'Google image')
img25 = {"_id": "img25", 
         "src":"google.png", 
         "alt":"[alt-text]", 
         "_tag": "img"}
ns.addVariable(img25, ns='image')

gvTest('img25', '<img src="google.png" alt="Google image"/>')
gvTest('img25.src', 'google.png')
gvTest('img25.alt', 'Google image')
gvTest('img25._tag', 'img')
gvTest('image.img25', '<img src="google.png" alt="Google image"/>')
gvTest('image.img25.src', 'google.png')
gvTest('image.img25.alt', 'Google image')
gvTest('image.img25._tag', 'img')

link25 = {"_id":"link25", 
          "_tag": "a", 
          "_text1":"{{self.<}}my link text{{self.>}}",
          "_text2":"{{image.img25}}", 
          "_text3":"[image.img25]", 
          "_text4":"{{self.<}}{{image.img25}}{{self.>}}",
          "_text5":"{{self._text6}}",
          "_text6":"{{self._text4}}",
          "_[":"[",
          "_]":"]",
          "_var":"self.",
          "_t5":"_text5",
          "_t6":"{{self._var}}{{self._t5}}",
          "_wow":"{{{{self._t6}}}}",
          "_asurl":"&lt;{{self.href}}&gt;", 
          "href":"https://google.com"}
ns.addVariable(link25, ns="link")

gvTest('link25', '<a href="https://google.com"></a>')
gvTest('link.link25', '<a href="https://google.com"></a>')

gvTest('link.link25._public_attrs_', ' href="https://google.com"')
gvTest('link.link25._private_attrs_', ' _tag="a" _text1="{{self.<}}my link text{{self.>}}" _text2="{{image.img25}}" _text3="<img src="google.png" alt="Google image"/>" _text4="{{self.<}}{{image.img25}}{{self.>}}" _text5="{{self._text6}}" _text6="{{self._text4}}" _[="[" _]="]" _var="self." _t5="_text5" _t6="{{self._var}}{{self._t5}}" _wow="{{{{self._t6}}}}" _asurl="&lt;{{self.href}}&gt;" _format="<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>"')
gvTest('link.link25._all_attrs_', ' _tag="a" _text1="{{self.<}}my link text{{self.>}}" _text2="{{image.img25}}" _text3="<img src="google.png" alt="Google image"/>" _text4="{{self.<}}{{image.img25}}{{self.>}}" _text5="{{self._text6}}" _text6="{{self._text4}}" _[="[" _]="]" _var="self." _t5="_text5" _t6="{{self._var}}{{self._t5}}" _wow="{{{{self._t6}}}}" _asurl="&lt;{{self.href}}&gt;" href="https://google.com" _format="<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>"')
gvTest('link.link25._text1', '<a href="https://google.com">my link text</a>')
gvTest('link.link25._text2', '<img src="google.png" alt="Google image"/>')
gvTest('link.link25._text3', '<img src="google.png" alt="Google image"/>')
gvTest('link.link25._asurl', '&lt;https://google.com&gt;')

sep()

gvTestMD('*[link.link25]*', '<em><a href="https://google.com"></a></em>')
gvTestMD('*[link.link25._text4]*', '<em><a href="https://google.com"><img src="google.png" alt="Google image"/></a></em>')
gvTestMD('*[link.link25._text5]*', '<em><a href="https://google.com"><img src="google.png" alt="Google image"/></a></em>')
gvTestMD('***[link.link25._wow]***', '<em><strong><a href="https://google.com"><img src="google.png" alt="Google image"/></a></strong></em>')

gvTestMD('[link.link25._text4(_text4="{{self.<}}My Image{{image.img25}}{{self.>}}" b="bar")]', '<a href="https://google.com" b="bar">My Image<img src="google.png" alt="Google image"/></a>')



ns.dump()


ref0 = {
       '_id':"ref0",
       'type':"exec", 
       'src':'from time import strftime',
       '_format':'{{self.exec||self.eval||self.last}}',
       'fmtstr':'%Y%m%d - ()'
}

msg('Adding ref0...')
ns.addVariable(ref0, ns="code")

msg('Referencing [code.ref0.last]')
mdExpr('[code.ref0.last]')

from time import strftime
ref1 = {
       '_id':"ref1",
       'type':"eval", 
       'src':'print("hello, world")',
       '_format':'{{self.exec||self.eval||self.last}}',
       'fmtstr':'%Y%m%d - ()'
}
sep()

msg('Adding ref1...')
ns.addVariable(ref1, ns="code")

msg('Referencing [code.ref1.last]')
mdExpr('[code.ref1.last]')

sep()

ref5 = {
       '_id':"ref5",
       'type':"exec", 
       'src':'from time import strftime\nprint(strftime("{{self.fmtstr}}"))',
       '_format':'{{self.last}}',
       'fmtstr':'%Y%m%d - ()'
}

msg('Adding ref5...')
ns.addVariable(ref5, ns="code")

msg('Referencing [code.ref5.last]')
mdExpr('[code.ref5.last]')


if __name__ == '__main__':
    from sys import exit
    exit(0)
