# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pgeif', [dirname(__file__)])
        except ImportError:
            import _pgeif
            return _pgeif
        if fp is not None:
            try:
                _mod = imp.load_module('_pgeif', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pgeif = swig_import_helper()
    del swig_import_helper
else:
    import _pgeif
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def empty_cbuffer():
  return _pgeif.empty_cbuffer()
empty_cbuffer = _pgeif.empty_cbuffer

def empty_fbuffer():
  return _pgeif.empty_fbuffer()
empty_fbuffer = _pgeif.empty_fbuffer

def batch():
  return _pgeif.batch()
batch = _pgeif.batch

def use_buffer():
  return _pgeif.use_buffer()
use_buffer = _pgeif.use_buffer

def use_time_delay(*args):
  return _pgeif.use_time_delay(*args)
use_time_delay = _pgeif.use_time_delay

def draw_collision(*args):
  return _pgeif.draw_collision(*args)
draw_collision = _pgeif.draw_collision

def dump_world():
  return _pgeif.dump_world()
dump_world = _pgeif.dump_world

def check_objects():
  return _pgeif.check_objects()
check_objects = _pgeif.check_objects

def rm(*args):
  return _pgeif.rm(*args)
rm = _pgeif.rm

def get_time():
  return _pgeif.get_time()
get_time = _pgeif.get_time

def time_until():
  return _pgeif.time_until()
time_until = _pgeif.time_until

def is_frame():
  return _pgeif.is_frame()
is_frame = _pgeif.is_frame

def is_collision():
  return _pgeif.is_collision()
is_collision = _pgeif.is_collision

def process_event():
  return _pgeif.process_event()
process_event = _pgeif.process_event

def rotate(*args):
  return _pgeif.rotate(*args)
rotate = _pgeif.rotate

def accel(*args):
  return _pgeif.accel(*args)
accel = _pgeif.accel

def velocity(*args):
  return _pgeif.velocity(*args)
velocity = _pgeif.velocity

def circle(*args):
  return _pgeif.circle(*args)
circle = _pgeif.circle

def fix(*args):
  return _pgeif.fix(*args)
fix = _pgeif.fix

def mass(*args):
  return _pgeif.mass(*args)
mass = _pgeif.mass

def poly6(*args):
  return _pgeif.poly6(*args)
poly6 = _pgeif.poly6

def poly5(*args):
  return _pgeif.poly5(*args)
poly5 = _pgeif.poly5

def poly4(*args):
  return _pgeif.poly4(*args)
poly4 = _pgeif.poly4

def poly3(*args):
  return _pgeif.poly3(*args)
poly3 = _pgeif.poly3

def box(*args):
  return _pgeif.box(*args)
box = _pgeif.box

def get_xpos(*args):
  return _pgeif.get_xpos(*args)
get_xpos = _pgeif.get_xpos

def get_ypos(*args):
  return _pgeif.get_ypos(*args)
get_ypos = _pgeif.get_ypos

def get_xvel(*args):
  return _pgeif.get_xvel(*args)
get_xvel = _pgeif.get_xvel

def get_yvel(*args):
  return _pgeif.get_yvel(*args)
get_yvel = _pgeif.get_yvel

def get_xaccel(*args):
  return _pgeif.get_xaccel(*args)
get_xaccel = _pgeif.get_xaccel

def get_yaccel(*args):
  return _pgeif.get_yaccel(*args)
get_yaccel = _pgeif.get_yaccel

def gravity(*args):
  return _pgeif.gravity(*args)
gravity = _pgeif.gravity

def purple():
  return _pgeif.purple()
purple = _pgeif.purple

def blue():
  return _pgeif.blue()
blue = _pgeif.blue

def green():
  return _pgeif.green()
green = _pgeif.green

def red():
  return _pgeif.red()
red = _pgeif.red

def black():
  return _pgeif.black()
black = _pgeif.black

def white():
  return _pgeif.white()
white = _pgeif.white

def rgb(*args):
  return _pgeif.rgb(*args)
rgb = _pgeif.rgb

def l2h(*args):
  return _pgeif.l2h(*args)
l2h = _pgeif.l2h

def h2l(*args):
  return _pgeif.h2l(*args)
h2l = _pgeif.h2l

def skip_until(*args):
  return _pgeif.skip_until(*args)
skip_until = _pgeif.skip_until

def get_cbuf():
  return _pgeif.get_cbuf()
get_cbuf = _pgeif.get_cbuf

def get_ebuf():
  return _pgeif.get_ebuf()
get_ebuf = _pgeif.get_ebuf

def get_fbuf():
  return _pgeif.get_fbuf()
get_fbuf = _pgeif.get_fbuf
# This file is compatible with both classic and new-style classes.


