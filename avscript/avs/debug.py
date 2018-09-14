#!/usr/bin/env python

def default_debug_register(obj, dups_okay):
    raise NotImplementedError("You need to define a default debug register first")

gb_debug_register_tag = default_debug_register

def set_default_debug_register(func):
    if not isinstance(func, DebugTracker):
        raise NameError("set_default_debug_register requires a DebugTracker object")

    global gb_debug_register_tag
    gb_debug_register_tag = func.debug_register_xface


class Debug(object):
    def __init__(self, classtag, initial_state=False, output=None):
        self._state = initial_state
        self._tag = '{}.{}'.format(classtag,id(self))
        self._out = output if output is not None else print
        global gb_debug_register_tag
        gb_debug_register_tag(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, newvalue):
        self._state = True if newvalue else False

    @property
    def output(self):
        self._out

    @output.setter
    def output(self, output):
        self._out = output

    @property
    def tag(self):
        return self._tag

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def toggle(self):
        self.state = not self.state

    def enabled(self):
        return self.state

    def print(self, msg, context=None):
        if not self.state:
            return

        s = '{:>20}: {}{}<br />\n'.format(self._tag, '{}'.format('' if context is None else '({})'.format(context)), msg)
        self._out('<span class="debug">{}</span>'.format(s))


class DebugTracker(object):
    def __init__(self, output=None):
        self._debug_tags = {}
        self._out = output if output is not None else print
        global gb_debug_register_tag
        gb_debug_register_tag = self.debug_register_xface

    @property
    def debug_tags(self):
        return self._debug_tags

    @debug_tags.setter
    def debug_tags(self, args):
        return self._debug_tags

    def _is_registered(self, tag):
        return True if tag in self.debug_tags else False

    def _check_valid(self, tag):
        if not self._is_registered(tag):
            raise NameError("tag {} is not registered".format(tag))

    def _get_tag(self, tag):
        if not self._is_registered(tag):
            raise NameError("tag {} is unknown".format(tag))

        return self.debug_tags[tag]

    def _get_state(self, tag):
        if not self._is_registered(tag):
            raise NameError("tag {} is unknown".format(tag))

        return self.debug_tags[tag].state

    def debug_register_xface(self, obj):
        if not isinstance(obj, Debug):
            raise NameError("obj must be instance of Debug class")

        if self._is_registered(obj.tag):
            raise NameError("tag {} already registered".format(obj.tag))

        self.debug_tags[obj._tag] = obj

    def call(self, which, method):
        from .regex import RegexSafe
        reObj = RegexSafe(which)
        
        for var in sorted(self.debug_tags):
            if reObj.is_match(var) is None:
                continue

            self._check_valid(var)
            eval('self._get_tag(var).{}()'.format(method))
            s = 'Process({1}): {0} is now {2}<br />'.format(var, method, 'enabled' if self._get_state(var) else "disabled")
            self._out('<span class="debug green">{}</span>'.format(s))

    def on(self, tag):
        self.call(tag, 'on')

    def off(self, tag):
        self.call(tag, 'off')

    def toggle(self, tag):
        self.call(tag, 'toggle')

    def enabled(self, tag):
        self.call(tag, 'enabled')

    #TODO: Should I have a print that takes a wildcard? print('avscript.header', 'msg'...)
    def dumpTags(self):
        for tag in self.debug_tags:
            self._out("{} is {}<br />".format(tag, 'on' if self.debug_tags[tag].state else 'off'))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
