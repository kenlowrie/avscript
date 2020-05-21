#!/usr/bin/env python

import avscript.avs.debug as debug

"""
tags = {'ns': ns(), 'fs': fs(), 'md': md(), 'ns.code': nscode()}
x = dbg.Debug()
for key, val in tags.items():
    x.at3(tags[key])

print("enabled: {}".format(x.enabled3(tags['ns'])))
x.on3(tags['ns'])
print("enabled: {}".format(x.enabled3(tags['ns'])))

x.off3(tags['ns'])
print("enabled: {}".format(x.enabled3(tags['ns'])))

x.toggle3(tags['fs'])
print("enabled: {}".format(x.enabled3(tags['ns'])))

x.toggle3(tags['fs'])
print("enabled: {}".format(x.enabled3(tags['ns'])))

x.dumpTags()
"""
"""
What if I instead declare a _DebugTag() object, that registers itself with an outer controller? Then, the other
can do the toggling, but within the local methods of an object, I can use a local. I'd have to use unique names,
otherwise, inheritance would hook the super class method, resulting in the same issue I have right now...

codeDebug.on()
mdDebug.on()
mainDebugger.register(mdDebug)

I think this would work. 
"""

class var(object):
    def __init__(self):
        #print("var constructor".format(id(self)))
        self.dbg = debug.Debug('var27')
        #if not hasattr(self, 'dbg'): self.dbg = debug.Debug(var.DBG)
    def test(self):
        self.dbgPr("test message", 'customtag')
    def dbgPr(self, msg, ctx=None):
        self.dbg.print(msg, ctx)

class vstor(var):
    DBG='vstor'
    def __init__(self):
        #print("vstor constructor".format(id(self)))
        self.dbg = debug.Debug(vstor.DBG)
        #super(vstor, self).__init__()
    def test2(self):
        self.dbgPr("this is my test message", 'TEST2')

class vbasic(var):
    DBG='vbasic'
    def __init__(self):
        #print("vbasic constructor".format(id(self)))
        self.dbg = debug.Debug(vbasic.DBG)
        #super(vbasic, self).__init__()
    def test2(self):
        self.dbgPr("this is my test message")


myDT = debug.DebugTracker()
debug.set_default_debug_register(myDT)

t = var()
t.test()
t.dbg.on()
t.test()
myDT.on('v')

x = vstor()
x.test()
x.test2()
x.dbg.on()
x.test()
x.test2()

y = vbasic()
y.test()
y.test2()
y.dbg.on()
y.test()
y.test2()
z = vbasic()
z.dbg.toggle()
z.test2()

myDT.dumpTags()

"""
class ns(var):
    DBG='ns'
    def __init__(self):
        self.dbg = _DebugTag(ns.DBG)

class fs(object):
    DBG='fs'

class md(object):
    DBG='md'

class nscode(object):
    DBG='ns.code'

class foo(object):
    DBG='ft'
    CLS=''
    def __init__(self):
        #foo.CLS='{}.DBG'.format(self.__class__.__name__)
        x.off3(self)
        print("+++{}".format(eval('foo.DBG')))
        print(">>>{}".format(foo.DBG))
        print("---{}".format(eval(foo.CLS)))

class bar(foo):
    DBG='fs.sub'
    def __init__(self):
        super(bar, self).__init__()
        x.on3(self)

class fu(bar):
    def __init__(self):
        super(fu, self).__init__()
        x.toggle3(self)
        pass

b = bar()
c= fu()

x.dumpTags()

"""
