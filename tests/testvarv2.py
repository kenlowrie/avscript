#!/usr/bin/env python


from sys import path
from os.path import dirname, abspath, realpath, split, join
bin_path, whocares = split(dirname(realpath('__file__')))
lib_path = join(abspath(bin_path),'avscript')
path.insert(0, lib_path)

from avs.variable import *

"""
[foo]=bar
[foo.a]=1
[foo.b]=2
[foo.c.1]=x
[foo.c.2]=y
[foo.c] would print what?

[img] prints _format text
[img.x] prints image.x
@image addVar(ns='image', dict)
@html addVar(ns='html', dict)
addVar(name, value)

"""

mydict = {'_': 'v0', 'class': 'section0'}
md1=mydict.copy()
md2=mydict.copy()
md3=mydict.copy()
md1['class']='section1'
md2['class']='section2'
md3['class']='section3'

if 0:

    vs = VariableStore()
    vs.addVariable('foo', 'bar')
    vs.addVariable('dict', mydict)
    vs.addAttribute('foo', 'attr1', 'value1')
    vs.dup('foo', 'nu')
    vs.dumpVarsAsStrings()
    vs.setRVal('foo', 'new-rval')
    vs.setAttribute('foo', 'attr1', 'value1a')
    vs.addAttribute('nu', 'attr2', 'value2')

    print('single:{}'.format(vs.getValue('foo')))
    print('dict:{}'.format(vs.getValue('dict')))

    vs.dumpVarsAsStrings()

    print(vs.getPublicAttrs('foo'))
    print(vs.getPublicAttrs('nu'))
    print(vs.getPrivateAttrs('nu'))
    print(vs.getAllAttrs('nu'))

def markdown(s):
    #print('markdown:{}'.format(s))
    if s[0] == '[' and s[-1] == ']':
        #print("ns.getValue(s[1:-1])={}".format(s[1:-1]))
        return ns.getValue(s[1:-1])

    #print('NOT A VAR')

    return s

ns = Namespaces(markdown)

def _getValue(msg, expr=None):
    if msg is not None:
        msg = 'getting {}'.format(msg) if expr is not None else msg
    else:
        msg = 'getting {}'.format(expr)

    left = msg if msg is not None else expr if expr is not None else ''
    right = '={}'.format(ns.getValue(expr)) if expr is not None else ''
    print('{}{}'.format(left, right))

ns.addVariable('value', name='varname')
_getValue('simple variable varname', 'varname')

ns.addVariable('[{{value}}]', name='v1')
_getValue('adding to default name space')

ns.addVariable(mydict, name='v0')
_getValue('adding to var name space')
ns.addVariable(md1, ns='var')
_getValue('adding to html name space')
ns.addVariable(md2, ns='html')
_getValue('adding to image name space')
ns.addVariable(md3, ns='image')

_getValue(None, 'v0.class')

print("html.v0 exists ... {}".format(ns.exists('html.v0')))
ns.setAttribute('html.v0', 'class', 'section42')

_getValue(None,'html.v0.class')

var0= {'_': 'var0', '_format': '{{self._public_attrs_}}', 'style': '{{self.other}}', 'other': 'yes!'}

ns.addVariable(var0, ns="var")
def sep(size=60):
    print('{}'.format('-'*size))

sep()
_getValue(None,'var0')
_getValue(None,'var.var0._public_attrs_')
_getValue(None,'var0._private_attrs_')
_getValue(None,'var0._all_attrs_')
_getValue(None,'var0.style')


var0= {'_': 'var0', '_format': '{{self._public_attrs_}}', 'style': '{{self.other}}', 'other': 'yes!'}


anc0 = {'_id': 'anc0', '_tag':'a', '_link':'<a href="#{{self.id}}">{{self._linktext}}</a>', '_linktext':'The bookmark text used for link', 'id':'the_bookmark_id'}

ns.addVariable(anc0, ns="html")
_getValue(None,'html.anc0')
_getValue(None,'html.anc0._link')

anc1 = {'_id': 'anc1', '_format': '<a id="{{self.id}}"></a>', 'link':'<a href="#{{self.id}}">{{self.linktext}}</a>', 'linktext':'The bookmark text used for link', 'id':'the_bookmark_id'}

ns.addVariable(anc1, ns="html")
_getValue(None,'html.anc1')
_getValue(None,'html.anc1.link')

_getValue(None,'anc1.linktext')
ns.updateVariable({'_id': 'anc1', 'linktext': 'Change the link text'}, ns="html")
_getValue(None,'anc1.linktext')

sep(25)
anc2 = {'_id': 'anc2', '_tag': 'a', 'id':'text id'}
ns.updateVariable(anc2, ns="html")
_getValue(None,'anc2')

_getValue(None,'html.anc2._link')

del anc2['_tag']
del anc2['id']
anc2['_id'] = 'anc2'
anc2['_link'] = '<a href=\"#{{self.id}}\">the text to hyperlink</a>'
ns.updateVariable(anc2, ns="html")
_getValue(None,'html.anc2._link')

#_format will be automatically generated when the variable is defined to the default value.

#[anchor] - results in <a id=“the_bookmark_id”></a>
#[anchor._link] - results in <a id=“#the_bookmark_id”>The bookmark text used for link</a>

"""
"""

img0 = {'_id': 'imgTMPL', '_tag': 'img', '_format': '<{{self._tag}}{{self._public_attrs_}}/>', 'src': '[path]/XXX', 'class': 'myclass'}

ns.addVariable(img0, ns="html")
_getValue(None,'html.imgTMPL')

img1 = {'_id': 'img0', '_inherit': 'imgTMPL', 'src': '[path]/YYY'}
ns.addVariable(img1, ns="html")
_getValue(None,'html.img0')

lnk0 = {'_id': 'cls', 
        '_tag': 'a', 
        '_format': '{{self._all_attrs_}}', 
        'class': 'myclass'}

ns.addVariable(lnk0, ns="link")
_getValue(None,'link.cls')
_getValue(None,'link.cls.<')
_getValue(None,'link.cls.>')

my_jit_attrs = {'class': 'myclass2', 'style': 'my cool style', '_newfmt': '{{self.style}}'}

print('getting link.cls._newfmt={}'.format(ns.getValue('link.cls._newfmt', jit_attrs=my_jit_attrs)))

_getValue(None,'link.cls.style')


#[alt]=Google image
ns.addVariable('Google image', 'alt-text')
_getValue(None, 'alt-text')
img25 = {"_id": "img25", "src":"google.png", "alt":"[alt-text]"}
ns.addVariable(img25, ns='image')
_getValue(None, 'img25')
_getValue(None, 'img25.src')
_getValue(None, 'img25.alt')
link25 = {"_id":"link25", 
          "_text1":"{{self.<}}my link text{{self.>}}", 
          "_text2":"{{image.img25}}", 
          "_text3":"[image.img25]", 
          "_asurl":"&lt;{{self.href}}&gt;", 
          "href":"https://google.com"}
ns.addVariable(link25, ns="link")
_getValue(None, 'link.link25._public_attrs_')
_getValue(None, 'link.link25._private_attrs_')
_getValue(None, 'link.link25._all_attrs_')
_getValue(None, 'link.link25._text1')
_getValue(None, 'link.link25._text2')
_getValue(None, 'link.link25._text3')
# - would use _format
_getValue(None, 'link.link25')
# returns the href= string formatted as text...
_getValue(None, 'link.link25._asurl')

sep()

ns.dump()



if __name__ == '__main__':
    from sys import exit
    exit(0)
