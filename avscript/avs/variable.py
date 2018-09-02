#!/usr/bin/env python

from __future__ import print_function

"""
I want to be able to attach attributes to 
"""

class Variable(object):
    private = '_private_attrs_'
    public = '_public_attrs_'
    all = '_all_attrs_'
    rvalue = '_rval'
    prefix = '_'

    """Abstracts variable. Keeps track of the name and the value."""
    def __init__(self, name, value):
        self.name = name
        if type(value) is dict:
            self.rval = value
        else:
            self.rval = {Variable.rvalue: value}

    def getValue(self, attribute=None):
        # This doesn't really make sense, because if someone puts _rval in the dict, it won't
        # return the dict. Probably need to check also that len() is 1...
        if attribute is None:
            return self.rval[Variable.rvalue] if Variable.rvalue in self.rval else self.rval
            
        return self.rval[attribute] if attribute in self.rval else ''

    def getAttrsAsDict(self, which):
        if which == Variable.private:
            return {key: value for (key,value) in self.rval.items() if key[0] == Variable.prefix}
        elif which == Variable.public:
            return {key: value for (key,value) in self.rval.items() if key[0] != Variable.prefix}

        return self.rval.copy()

    def getAttrsAsString(self, which):
        attrsDict = self.getAttrsAsDict(which)
        attrs = ''
        for item in attrsDict:
            attrs += ' {}="{}"'.format(item, attrsDict[item])

        return attrs

    def addAttribute(self, attrName, attrValue):
        self.rval[attrName] = attrValue

    def dup(self, name):
        v = Variable(name,None)
        v.rval=self.rval.copy()
        return v

    def dump(self, output):
        if len(self.rval) == 1 and Variable.rvalue in self.rval:
            output("{0}={1}".format(self.name, self.rval[Variable.rvalue]))
            return

        output("{}".format(self.name))
        for item in self.rval:            
            output("\t{0}={1}".format(item, self.rval[item]))


class VariableStore(object):
    _special_attributes = [Variable.public, Variable.private, Variable.all]

    """Class to abstract a dictionary of variables"""
    def __init__(self, markdown, oprint):
        self.vars = {}
        self._md_ptr = markdown
        self.oprint = oprint

    def _markdown(self, s):
        markdown = self._md_ptr
        return markdown(s)

    def addVariable(self, value, name):
        """Add a variable called 'name' to the list and set its value to 'value'."""

        self.vars[name] = Variable(name, value)

    def exists(self, name):
        """Returns true if the variable 'name' exists."""
        return name in self.vars

    def getValue(self, name, attribute=None):
        """Gets the value of the variable 'name'
        
        If it doesn't exist, it returns ''."""

        return self.vars[name].getValue(attribute) if self.exists(name) else ""

    def dup(self, current, new):
        if self.exists(current):
            if self.exists(new):
                # TODO: raise exception
                self.oprint('{} already exists'.format(new))
                return

            self.vars[new] = self.vars[current].dup(new)
        else:
            # TODO: raise exception
            self.oprint('{} doesn\'t exist'.format(current))

    def addAttribute(self, name, attrName, attrValue):
        if self.exists(name):
            self.vars[name].addAttribute(attrName, attrValue)

    def getRVal(self, name):
        if self.exists(name):
            return self.vars[name].rval

    def setRVal(self, name, rval):
        if self.exists(name):
            # TODO: This must account for type of incoming
            # del existing, then call underlying method so
            # it handles _rval vs. dictionary...
            self.vars[name].rval['_rval'] = rval

    def setAttribute(self, name, attr, value):
        if self.exists(name):
            self.vars[name].rval[attr] = value

    def getPublicAttrs(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsString(Variable.public)

    def getPrivateAttrs(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsString(Variable.private)

    def getAllAttrs(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsString(Variable.all)

    def getSpecialAttr(self, which, variable):
        if which == Variable.public:
            return self.getPublicAttrs(variable)
        elif which == Variable.private:
            return self.getPrivateAttrs(variable)
        elif which == Variable.all:
            return self.getAllAttrs(variable)

        raise

    def escape_html(self, s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def unescapeString(self,s):
        return s.replace('\\"', '"')

    def unescapeStringQuotes(self,d):
        for item in d:
            d[item] = self.unescapeString(d[item])

        return d     

    def dumpVars(self, indent=''):
        """Dumps the variable list, names and values."""
        def escape_html(s):
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        for var in sorted(self.vars):
            self.oprint("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].name, self.escape_html(self.vars[var].rval['_rval']), indent))

    def dumpVarsAsStrings(self, indent='', output=print):
        """Dumps the variable list, names and values."""
        def escape_html(s):
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        for var in sorted(self.vars):
            self.vars[var].dump(output)


class Namespace(VariableStore):
    def __init__(self, markdown, namespace_name, oprint):
        super(Namespace, self).__init__(markdown, oprint)  # Initialize the base class(es)
        self._namespace = '{}.'.format(namespace_name)

    @property
    def namespace(self):
        return self._namespace


class BasicNamespace(Namespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(BasicNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        #print("BASIC: My NS is: {}".format(self.namespace))
        from .regex import Regex
        self.delayedExpansion = Regex(r'(\[{{([^}]+)}}\])')

    def addVariable(self, value, name):
        """Add a variable called 'name' to the list and set its value to 'value'."""
        if type(value) is not str:
            raise TypeError("BasicNamespace only supports string data type")

        # If they used the delayed expansion syntax, remove it before storing value
        from re import findall
        matches = findall(self.delayedExpansion.regex, value)
        for m in matches:
            # for each delayed expansion variable, strip the {{}} from the name
            value = value.replace(m[0],'[{}]'.format(m[1]))

        super(BasicNamespace, self).addVariable(value, name)

    """
    """
    def _stripNamespace(self, id):
        if id.startswith(self.namespace):
            return id[len(self.namespace):]

        return id

    def exists(self, name):
        #print("basic: {}".format(name))
        #if name == 'class':
        #    raise NameError("WTF, How did I get here?")
        return super(BasicNamespace, self).exists(self._stripNamespace(name))

    def getValue(self, name):
        return super(BasicNamespace, self).getValue(self._stripNamespace(name))


class AdvancedNamespace(Namespace):
    _variable_name_str = ["_id", "_"]
    _default_format_attr = '_format'
    _inherit_attr = '_inherit'

    def __init__(self, markdown, namespace_name, oprint):
        super(AdvancedNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)

    def _missingID(self, dict, which="ADD"):
        self.oprint("{}: Dictionary is missing {}<br />{}<br />".format(which, AdvancedNamespace._variable_name_str, dict))

    def getIDstring(self, dict):
        for id in AdvancedNamespace._variable_name_str:
            if id in dict:
                return id
        return None

    def inheritsFrom(self, dict):
        return True if AdvancedNamespace._inherit_attr in dict else False

    def addVariable(self, dict, name=None):
        myID = self.getIDstring(dict)
        if myID is None:
            self._missingID(dict)
            return

        varID = dict[myID]
        del dict[myID]
        
        if self.inheritsFrom(dict):
            tempDict = self.getRVal(dict[AdvancedNamespace._inherit_attr]).copy()
            for item in dict:
                if item != AdvancedNamespace._inherit_attr:
                    tempDict[item] = dict[item]
            dict = tempDict

        super(AdvancedNamespace, self).addVariable(self.unescapeStringQuotes(dict), varID)
        return varID

    def updateVariable(self, dict, name=None):
        myID = self.getIDstring(dict)
        if myID is None:
            self._missingID(dict, "UPDATE")
            return

        varID = dict[myID]
        if varID not in self.vars:
            return self.addVariable(dict)

        del dict[myID]
        for item in dict:
            self.vars[varID].rval[item] = self.unescapeString(dict[item])

    def _isSpecial(self, attr):
        return True if attr in AdvancedNamespace._variable_name_str + VariableStore._special_attributes else False

    def _parseVariable(self, id, do_not_test_attr=False):
        #if id.startswith(self.namespace):
        #    id = id[len(self.namespace):]

        compoundVar = id.split('.', 1)     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            id0, el0 = compoundVar
            if id0 in self.vars and (do_not_test_attr or el0 in self.vars[id0].rval or self._isSpecial(el0)):
                return compoundVar

        return id, None

    def exists(self, id):
        id0, el0 = self._parseVariable(id)
        if el0 is not None:
            # _parseVar() only returns both elements if the attribute exists
            return True

        return id0 in self.vars

    def getVarID(self, id):
        id0, el0 = self._parseVariable(id, True)
        return id0 if el0 is not None else id

    def getValue(self, id):
        id0, el0 = self._parseVariable(id)
        if el0 is not None:
            # If they are asking for the special name (_, _id)
            if el0 in AdvancedNamespace._variable_name_str:
                # return the variable name itself, no markdown.
                return id0

            if el0 in VariableStore._special_attributes:
                # should this be marked down? Probably.
                return self._markdown(self.getSpecialAttr(el0, id0))

            # TODO: When test code in place, I need to remove this and see what happens.
            #       Feels a bit like a side affect...
            # First, apply standard markdown in case _format has regular variables in it.
            fmt_str = self._markdown(self.vars[id0].rval[el0]).replace('{{','[').replace('}}',']')
            # And now, markdown again, to expand the self. namespace variables
            #print("SETTING SELF to: {}{}".format(self.namespace,id0))
            #if self.namespace == 'image.' and id0 == 'v0':
                #raise NameError("WTF")
            return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))

        if self.exists(id0):
            # if the special _format element exists, return it with markdown applied
            fmt = AdvancedNamespace._default_format_attr
            if fmt in self.vars[id0].rval:
                #print("RETURNING _format()")
                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = self._markdown(self.vars[id0].rval[fmt]).replace('{{','[').replace('}}',']')
                # And now, markdown again, to expand the self. namespace variables
                return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))

            compoundVar = ''
            for item in sorted(self.vars[id0].rval):
                attrText = self._markdown(self.vars[id0].rval[item])
                compoundVar += ' {}="{}"<br />\n'.format(item, attrText)
            return compoundVar

        # logically, you won't ever get here, because everyone always
        # calls exists() first, and if false, it just echos out what you
        # passed in. But just in case...
        return '(undefined variable) {}"'.format(id)

    def dumpVars(self, indent='', output=print):
        """Dumps the image variable list, names and values."""
        for var in sorted(self.vars):
            dict_str = '<br />'
            for d_item in self.vars[var].rval:
                dict_str += '&nbsp;&nbsp;{}:{}<br />\n'.format(d_item, self.escape_html(self.vars[var].rval[d_item]))
            output("{2}<strong>{0}=</strong>{1}<br />".format(var, dict_str, indent))

class VarNamespace(AdvancedNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(VarNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)

        #print("VAR: My NS is: {}".format(self.namespace))



class ImageNamespace(AdvancedNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(ImageNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        #print("IMAGE: My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None):
        var_name = super(ImageNamespace, self).addVariable(dict)

        if not super(ImageNamespace, self).exists('{}.{}'.format(var_name, AdvancedNamespace._default_format_attr)):
            super(ImageNamespace, self).addAttribute(var_name,AdvancedNamespace._default_format_attr,'<{{self._tag}}{{self._public_attrs_}}/>')


class HtmlNamespace(AdvancedNamespace):
    _start = '<'
    _end = '>'
    _element_partials = [_start, _end]

    def __init__(self, markdown, namespace_name, oprint):
        super(HtmlNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        #print("HTML: My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None):
        var_name = super(HtmlNamespace, self).addVariable(dict)

        if not super(HtmlNamespace, self).exists('{}.{}'.format(var_name, AdvancedNamespace._default_format_attr)):
            super(HtmlNamespace, self).addAttribute(var_name,AdvancedNamespace._default_format_attr,'<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>')

    def _isSpecial(self, attr):
        if attr in HtmlNamespace._element_partials:
            return True

        return super(HtmlNamespace, self)._isSpecial(attr)

    def getElementPartial(self, which):
        if which == HtmlNamespace._start:
            # TODO: should do error checking here (make sure _tag is defined?)
            return '<{0}self._tag{1}{0}self.{2}{1}>'.format('{{', '}}', Variable.public)
        elif which == HtmlNamespace._end:
            # TODO: should do error checking here (make sure _tag is defined?)
            return '</{{self._tag}}>'

        raise

    def getValue(self, id):
        id0, el0 = self._parseVariable(id)
        #print("HTML.getValue({},{},{})".format(id,id0,el0))
        if el0 is not None:
            if el0 in HtmlNamespace._element_partials:

                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = self._markdown(self.getElementPartial(el0).replace('{{','[').replace('}}',']'))
                # And now, markdown again, to expand the self. namespace variables
                #print("LINK: {}".format(self.namespace))
                return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace,id0)))

        return super(HtmlNamespace, self).getValue(id)


class LinkNamespace(HtmlNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(LinkNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)

        #print("LINK: My NS is: {}".format(self.namespace))

class CodeNamespace(AdvancedNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(CodeNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)

    def executePython(self, dict):
        import sys
        from io import StringIO
        import contextlib

        @contextlib.contextmanager
        def stdoutIO(so=None):
            old = sys.stdout
            if so is None:
                so = StringIO()
            sys.stdout = so
            yield so
            sys.stdout = old

        with stdoutIO() as s:
            exec(dict['_code']) if dict['type'] == 'exec' else eval(dict['_code'])

        #print('>>>>>>>>>>>{}{}'.format(type(s.getvalue()),s.getvalue()))
        return s.getvalue()

    def addVariable(self, dict, name=None):
        var_name = super(CodeNamespace, self).addVariable(dict)

        #if not super(CodeNamespace, self).exists('{}.{}'.format(var_name, AdvancedNamespace._default_format_attr)):
        #    super(CodeNamespace, self).addAttribute(var_name,AdvancedNamespace._default_format_attr,'<{{self._tag}}{{self._public_attrs_}}/>')
        """
        Compiles src and stores in _code attribute.
        ref._code = compile(ref.src,’<string>’, ref.type)

        [code.ref] 
            if ref.type == ‘exec’
                # capture stdout, and return that value formatted as _format
                exec(_code)
                ref.last = stdout
                return ref.last
            elif ref.type == ‘eval’
                ref.last = eval(_code)
                return ref.last

        [code.ref.last] - returns the result of the last call
        [code.ref.exec] - returns exec(_code)
        [code.ref.eval] - returns eval(_code)
        """
        dict = super(CodeNamespace, self).getRVal(var_name)
        if 'src' not in dict or 'type' not in dict:
            print('CODE namespace requires src= and type= attributes')
            return

        if dict['type'] not in ['exec', 'eval']:
            print('CODE namespace type= must be either "exec" or "eval"')
            return

        # Need to expand any variables inside src...
        src = super(CodeNamespace, self).getValue('{}.src'.format(var_name))
        dict['_code'] = compile(src, '<string>', dict['type'])
        #dict['last'] = eval(dict['_code']) if dict['type'] == 'eval' else self.executePython(dict)
        dict['last'] = self.executePython(dict)
        
        #print("<<<<<<<<<<<<{}{}".format(type(dict['last']), dict['last']))

        #type = 
        #print("CODE: My NS is: {}".format(self.namespace))


class Namespaces(object):
    _default = 'basic'
    _html = 'html'
    _var = 'var'
    _link = 'link'
    _image = 'image'
    _code = 'code'
    _search_order = [_default, _var, _image, _link, _html, _code]

    def __init__(self, markdown, setNSxface, oprint=print):
        self._namespaces = {
            Namespaces._default: BasicNamespace(markdown, Namespaces._default, oprint),
            Namespaces._html: HtmlNamespace(markdown, Namespaces._html, oprint),
            Namespaces._var: VarNamespace(markdown, Namespaces._var, oprint),
            Namespaces._image: ImageNamespace(markdown, Namespaces._image, oprint),
            Namespaces._link: LinkNamespace(markdown, Namespaces._link, oprint),
            Namespaces._code: CodeNamespace(markdown, Namespaces._code, oprint),
        }
        #for ns in self._namespaces:
        #    print("Namespace for {} is set to {}".format(ns, self._namespaces[ns].namespace))

        setNSxface(self)

    def addVariable(self, value, name=None, ns=None):
        if ns is None:
            ns = Namespaces._default

        if ns not in self._namespaces:
            #TODO: Raise exception
            raise

        self._namespaces[ns].addVariable(value, name)

    def updateVariable(self, value, name=None, ns=None):
        if ns is None:
            ns = Namespaces._default

        if ns not in self._namespaces:
            #TODO: Raise exception
            raise

        self._namespaces[ns].updateVariable(value, name)

    def _splitNamespace(self, variable_name):
        compoundVar = variable_name.split('.',1)     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            return (compoundVar[0], compoundVar[1])

        return (None, variable_name)

    def removeVariable(self, name):
        # TODO: Add this
        # name [[ns].name]
        pass

    def removeAttribute(self, name):
        # TODO: Add this
        # name [[ns].name.attr]
        pass

    def dupVariable(self, curname, newname):
        # TODO: Add this
        # curname [[ns].name]
        # newname [[ns].name]
        pass

    def exists(self, variable_name):
        ns, name = self._splitNamespace(variable_name)
        if ns is not None:
            if ns in Namespaces._search_order:
                return self._namespaces[ns].exists(name)

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(variable_name):
                return True

        return False

    def getValue(self, variable_name, jit_attrs=None):
        #print("INSIDE GV: {}".format(variable_name))

        def addJITattrs(jit_attrs, ns, var):
            if ns == Namespaces._default:
                # TODO: Should I print a message or something?
                return  # For now, just return. Basic namespace doesn't support attrs...

            if jit_attrs is not None:   # and self._namespaces[ns].exists(variable_name):
                #print('inside addJITattrs({})'.format(var))
                jit_attrs['_'] = self._namespaces[ns].getVarID(var)
                self._namespaces[ns].updateVariable(jit_attrs)
        
        ns, name = self._splitNamespace(variable_name)
        #if jit_attrs is not None:
        #    print('{}'.format(jit_attrs))
        #print('ns,name={},{}'.format(ns,name))
        if ns is not None:
            if ns in Namespaces._search_order:
                # TODO: add jit_attrs right here (like below)?
                addJITattrs(jit_attrs, ns, name)

                #print("FALLING THRU")
                # TODO: Shouldn't we check to see that it's there?
                return self._namespaces[ns].getValue(name)

        #print("NO NAMESPACE OR UNKNOWN NAMESPACE")
        # Since the NS wasn't valid, we need to fall back to the full name again
        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(variable_name):
                # TODO: add jit_attrs right here
                # except right here, we need just the root part of the name
                # TODO: this is confusing, and will lead to errors. REFACTOR.
                addJITattrs(jit_attrs, ns, name)
                return self._namespaces[ns].getValue(variable_name)

        # TODO: We may want to just return variable_name instead... like before...
        return "Variable {} is (undefined)".format(variable_name)    # I don't think this will ever happen

    def setAttribute(self, variable_name, attr_name, attr_value):
        ns, name = self._splitNamespace(variable_name)
        if ns is not None:
            if ns in Namespaces._search_order:
                if self._namespaces[ns].exists(name):
                    return self._namespaces[ns].setAttribute(name, attr_name, attr_value)
                
                return "Variable {} is (undefined)".format(variable_name)    # I don't think this will ever happen

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(variable_name):
                #print("attribute exists")
                return self._namespaces[ns].setAttribute(variable_name, attr_name, attr_value)

        return "Variable {} is (undefined)".format(variable_name)    # I don't think this will ever happen

    def dump(self):
        for ns in Namespaces._search_order:
            print("{1}\nNAMESPACE: {0}\n{1}".format(ns,'-'*40))
            self._namespaces[ns].dumpVarsAsStrings()

    def dumpVars(self):
        for ns in Namespaces._search_order:
            print("{1}\nNAMESPACE: {0}\n{1}<br />".format(ns,'-'*40))
            self._namespaces[ns].dumpVars()



# =================================================================================================


class _Variable(object):
    """Class to abstract a variable (alias). Keep track of the ID (name) and
    the value (text)."""
    def __init__(self, id, text):
        self.id = id
        self.text = text


class VariableDict(object):
    """Class to abstract a dictionary of variables (aliases)"""
    def __init__(self):
        self.vars = {}
        from .regex import Regex
        self.delayedExpansion = Regex(r'(\[{{([^}]+)}}\])')

    def addVar(self, id, text):
        """Add a variable called 'id' to the list and set its value to 'text'."""
        if type(text) is str:
            from re import findall
            matches = findall(self.delayedExpansion.regex, text)
            for m in matches:
                # for each delayed expansion variable, strip the {{}} from the name
                text = text.replace(m[0],'[{}]'.format(m[1]))

        self.vars[id] = _Variable(id, text)

    def exists(self, id):
        """Returns true if the variable 'id' exists."""
        return id in self.vars

    def getText(self, id):
        """Gets the value of the variable 'id', unless it doesn't exist, in
        which case it returns (undefined).
        TODO: Should this just return an empty string if undefined?"""
        return "(undefined)" if not self.exists(id) else self.vars[id].text

    def escape_html(self, s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def dumpVars(self, indent='', output=print):
        """Dumps the variable list, names and values."""
        def escape_html(s):
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        for var in sorted(self.vars):
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, self.escape_html(self.vars[var].text), indent))


class VariableV2Dict(VariableDict):
    """Class to abstract a dictionary of images"""
    _var_prefix = 'varv2.'
    _idstr = ["_id", "__", "_"]

    def __init__(self):
        super(VariableV2Dict, self).__init__()  # Initialize the base class(es)

    def _missingID(self, dict, oprint, which="ADD"):
        #from sys import stderr
        oprint("{}: Dictionary is missing {}<br />{}<br />".format(which, VariableV2Dict._idstr, dict))

    def getIDstr(self, dict):
        for id in VariableV2Dict._idstr:
            if id in dict:
                return id
        return None

    def unescapeString(self,s):
        return s.replace('\\"', '"')

    def unescapeStringQuotes(self,d):
        for item in d:
            d[item] = self.unescapeString(d[item])

        return d     

    def addVarV2(self, dict, oprint):
        myID = self.getIDstr(dict)
        if myID is None:
            self._missingID(dict, oprint)
            return

        varID = dict[myID]
        del dict[myID]
        if 'name' not in dict:
            dict['name'] = varID

        self.addVar(varID, self.unescapeStringQuotes(dict))

    def updateVarV2(self, dict, oprint):
        myID = self.getIDstr(dict)
        if myID is None:
            self._missingID(dict, oprint, "UPDATE")
            return

        varID = dict[myID]
        if varID not in self.vars:
            return self.addVarV2(dict, oprint)

        del dict[myID]
        for item in dict:
            self.vars[varID].text[item] = self.unescapeString(dict[item])

    def _parseVar(self, id):
        if id.startswith(VariableV2Dict._var_prefix):
            id = id[len(VariableV2Dict._var_prefix):]

        compoundVar = id.split('.')     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            id0, el0 = compoundVar
            if id0 in self.vars and (el0 in self.vars[id0].text or el0 in VariableV2Dict._idstr):
                return compoundVar

        return id, None

    def exists(self, id):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            # _parseVar() only returns both elements if the attribute exists
            return True

        return id0 in self.vars

    # TODO: what if we could specify the HTML tag that should be formed with one of these
    # Maybe have an _element=HTMLTAG, and form it like the one for IMAGE if you ask for all

    def getVarV2(self, id, _markdown):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            # If they are asking for the special name (_, __, _id)
            if el0 in VariableV2Dict._idstr:
                # return the variable name itself, no markdown.
                return id0

            return _markdown(self.vars[id0].text[el0])

        if self.exists(id0):
            # if the special _format element exists, return it with markdown applied
            fmt = '_format'
            if fmt in self.vars[id0].text:
                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = _markdown(self.vars[id0].text[fmt]).replace('{{','[').replace('}}',']')
                # And now, markdown again, to expand the self. namespace variables
                return _markdown(fmt_str.replace('self.','{}.'.format(id)))

            compoundVar = ''
            for item in sorted(self.vars[id0].text):
                attrText = _markdown(self.vars[id0].text[item])
                compoundVar += ' {}="{}"<br />\n'.format(item, attrText)
            return compoundVar

        # logically, you won't ever get here, because everyone always
        # calls exists() first, and if false, it just echos out what you
        # passed in. But just in case...
        return '(undefined variable) {}"'.format(id)

    def dumpVars(self, indent='', output=print):
        """Dumps the image variable list, names and values."""
        for var in sorted(self.vars):
            dict_str = '<br />'
            for d_item in self.vars[var].text:
                dict_str += '&nbsp;&nbsp;{}:{}<br />\n'.format(d_item, self.escape_html(self.vars[var].text[d_item]))
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, dict_str, indent))


class ImageDict(VariableDict):
    """Class to abstract a dictionary of images"""
    _var_prefix = 'image.'
    _idstr = "_id"

    def __init__(self):
        super(ImageDict, self).__init__()  # Initialize the base class(es)

    def _missingID(self, dict, oprint, which="ADDIMAGE"):
        oprint("{}: Dictionary is missing {}<br />{}<br />".format(which, VariableV2Dict._idstr, dict))

    def addImage(self, dict, oprint):
        if ImageDict._idstr not in dict:
            self._missingID(dict, oprint)
            return

        imageID = dict[ImageDict._idstr]
        del dict[ImageDict._idstr]
        self.addVar(imageID, dict)

    def _parseVar(self, id):
        if id.startswith(ImageDict._var_prefix):
            id = id[len(ImageDict._var_prefix):]

        compoundVar = id.split('.')     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            id0, el0 = compoundVar
            if id0 in self.vars and el0 in self.vars[id0].text:
                return compoundVar

        return id, None

    def exists(self, id):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            return id0 in self.vars and el0 in self.vars[id0].text

        return id0 in self.vars

    def getImage(self, id, _markdown):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            return _markdown(self.vars[id0].text[el0])

        if self.exists(id0):
            imageTag = '<img'
            for item in sorted(self.vars[id0].text):
                if item[0] == '_':
                    continue    # don't add any attributes that start with _
                attrText = _markdown(self.vars[id0].text[item])
                imageTag += ' {}="{}"'.format(item, attrText)
            imageTag += '/>'
            return imageTag

        return '<img src="undefined image {}"/>'.format(id)

    def dumpVars(self, indent='', output=print):
        """Dumps the image variable list, names and values."""
        for var in sorted(self.vars):
            dict_str = '<br />'
            for d_item in self.vars[var].text:
                dict_str += '&nbsp;&nbsp;{}:{}<br />\n'.format(d_item, self.escape_html(self.vars[var].text[d_item]))
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, dict_str, indent))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
