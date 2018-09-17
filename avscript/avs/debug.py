#!/usr/bin/env python

def default_debug_register(obj):
    # A default register in case someone tries to instantiate a Debug() object
    # before a DebugTracker() is up and running and the registration API exposed
    raise NotImplementedError("You need to define a default debug register first")

# When a Debug() object is instantiated, it registers itself with the DebugTracker
# via this interface.
gb_debug_register_tag = default_debug_register
# The suspend interface is initialized when the debug_register is done. This API
# provides a way for any Debug() instance to suspend/resume output.
gb_debug_suspend_xface = None

def set_default_debug_register(func):
    if not isinstance(func, DebugTracker):
        raise NameError("set_default_debug_register requires a DebugTracker object")

    global gb_debug_register_tag, gb_debug_suspend_xface
    gb_debug_register_tag = func.debug_register_xface
    gb_debug_suspend_xface = func.debug_suspend_xface

def default_debug_print(s):
    # We have a default handler for printing in case we are called too early...
    raise NotImplementedError("You need to define a default debug print handler")

# This is the API that prints debug messages. Debug() objects call their print() method
# Which uses this entry point to serialize the messages through a common output function,
# enabling us to control output globally.

gb_debug_print = default_debug_print


class Debug(object):
    def __init__(self, classtag, initial_state=False):
        self._state = initial_state
        self._tag = '{}.{}'.format(classtag,id(self))
        global gb_debug_register_tag
        gb_debug_register_tag(self)

    def global_suspend(self, suspend):
        # used to globally suspend debug messages
        global gb_debug_suspend_xface
        gb_debug_suspend_xface(suspend)


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

    def print_msg(self, msg, context=None):
        s = '{:>20}: {}{}<br />\n'.format(self._tag, '{}'.format('' if context is None else '({})'.format(context)), msg)
        global gb_debug_print
        gb_debug_print('<span class="debug">{}</span>'.format(s))

    def print(self, msg, context=None):
        if not self.state:
            return

        self.print_msg(msg, context)

class DebugTracker(object):
    def __init__(self, output=None):
        self.suspendCounter=0
        self._debug_tags = {}
        self._msg_cache = []
        global gb_debug_register_tag
        gb_debug_register_tag = self.debug_register_xface

        global gb_debug_print
        gb_debug_print = self.print

        # This is the output method. print() by default, unless passed in
        self._out = output
        
        self.sys_debug = Debug('_SYSTEM')    # Define our own tracker to format...

    def print(self, s):
        if self.suspendCounter == 0:
            self._out(s)
        else:
            self._msg_cache.append(s)

    def output(self, s):
        # We only want to print if at least one debug tag is on
        # This prevents spurious messages from being output when
        # debug tracking is not currently enabled.
        if self.debug_active():
            self.sys_debug.print_msg(s)

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

    def dump_cache(self):
        msgs = self._msg_cache[::-1]
        self._msg_cache = []
        if len(msgs):
            self.output("Dumping debug cache.")
            while len(msgs):
                self._out(msgs.pop())

    def debug_suspend_xface(self, suspend):
        if suspend == True:
            self.output("Debug output has been suspended.")
            self.suspendCounter += 1
        else:
            self.suspendCounter -= 1
            if self.suspendCounter < 0:
                raise ValueError("Debug suspend counter went below zero.")
            elif self.suspendCounter == 0:
                # Dump any cached messages
                self.dump_cache()
                self.output("Debug output will be resumed.")
            else:
                # cache a debug output decrement counter message
                self.output("Debug output suspendCounter--")

    def debug_register_xface(self, obj):
        if not isinstance(obj, Debug):
            raise NameError("obj must be instance of Debug class")

        if self._is_registered(obj.tag):
            raise NameError("tag {} already registered".format(obj.tag))

        self.debug_tags[obj._tag] = obj

    def debug_active(self):
        # Check to see if any debug trackers are enabled
        for var in self.debug_tags:
            if self.debug_tags[var].enabled():
                return True

        return False

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

    def dumpTags(self):
        for tag in self.debug_tags:
            self._out("{} is {}<br />".format(tag, 'on' if self.debug_tags[tag].state else 'off'))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
