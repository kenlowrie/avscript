#!/usr/bin/env python

class _DebugTag(object):
    def __init__(self, tag, initial_state=False):
        self._state = initial_state
        self._tag = tag

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, newvalue):
        self._state = True if newvalue else False

    def on(self):
        return self.state is True

    def off(self):
        return self.state is False

    def toggle(self):
        self.state = not self.state

    def print(msg):
        s = '{}: {}'.format(self._tag, msg)
        if self.on:
            print(s)

class Debug(object):
    def __init__(self):
        self._debug_tags = {}

    @property
    def debug_tags(self):
        return self._debug_tags

    @debug_tags.setter
    def debug_tags(self, args):
        return self._debug_tags

    def debug_register_xface(self, xface):
        # Does this make sense? Is it the right way to do this?
        xface(self)     # pass this object reference to the client

    def _has_tag(self, obj):
        return True if hasattr(obj, 'DBG') else False

    def _is_registered(self, obj):
        return True if self._has_tag(obj) and obj.DBG in self.debug_tags else False

    def at3(self, obj, initial_state=False):
        if self._is_registered(obj):
            raise NameError("tag {} already registered".format(obj.DBG))

        self.debug_tags[obj.DBG] = _DebugTag(initial_state)

    def me(self, obj):
        return obj.DBG if self._has_tag(obj) else "UNKNOWN"

    def on3(self, obj):
        if not self._is_registered(obj):
            self.at3(obj, True)
            return

        self.debug_tags[obj.DBG].state = True

    def off3(self, obj):
        if not self._is_registered(obj):
            self.at3(obj, False)
            return

        self.debug_tags[obj.DBG].state = False

    def toggle3(self, obj):
        if not self._is_registered(obj):
            self.at3(obj, True)
            return

        self.debug_tags[obj.DBG].toggle()

    def enabled3(self, obj):
        if not self._is_registered(obj):
            return False

        return self.debug_tags[obj.DBG].state

    def addTag(self, tag, initial_state=False):
        if tag in self.debug_tags:
            raise NameError("Debug tag [{}] already registered.".format(tag))
    
        self.debug_tags[tag] = _DebugTag(initial_state)

    def on(self, tag):
        if tag in self.debug_tags:
            self.debug_tags[tag].state = True
    
    def off(self, tag):
        if tag in self.debug_tags:
            self.debug_tags[tag].state = False
    
    def toggle(self, tag):
        if tag in self.debug_tags:
            self.debug_tags[tag].toggle()

    def enabled(self, tag):
        if tag in self.debug_tags:
            return self.debug_tags[tag].state

    def dumpTags(self):
        for tag in self.debug_tags:
            print("{} is {}".format(tag, 'on' if self.debug_tags[tag].state else 'off'))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
