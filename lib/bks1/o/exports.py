# -*- coding: utf-8 -*-
# exports.py, part for parse_video : a fork from parseVideo. 
# exports: exports and imports for lib/bks1/o. 

# import

# import out
from ... import flash
from ... import base

# import in
from .raw import key as key0
from .raw import uuid as uuid0
from .raw import remote_mixer
from . import get_video_url1 as get_video_url1_0

from .vv import p271v_conf as p271v0
from .vv import vauth_remote as vr0

# set in
uuid0.set_import(base)
get_video_url1_0.set_import(base, flash)

# functions
def getTimer():
    return flash.getTimer()

# exports
MixerRemote = remote_mixer.MixerRemote
UUIDManager = uuid0.UUIDManager

key = key0
get_video_url1 = get_video_url1_0

p271vc = p271v0
vr = vr0

# end exports.py


