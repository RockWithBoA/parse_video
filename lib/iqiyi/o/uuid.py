# -*- coding: utf-8 -*-
# uuid.py, part for evparse : EisF Video Parse, evdh Video Parse. 
# uuid: iqiyi, com.qiyi.player.base.uuid 

# import

import random
import re
import json

# import from out
base = None
# NOTE should be set by exports
def set_import(base1):
    global base
    base = base1

# global static config
UUID_URL = 'http://data.video.qiyi.com/uid'

LOAD_UUID_RETRY = 5

# class

class UUIDManager(object):
    
    def __init__(self):
        self.uuid = ''
    
    def get_uuid(self):
        # check uuid
        if self.uuid != '':
            return self.uuid
        # load from server
        self.uuid = self._load_from_server()
        return self.uuid
    
    # auto retry load
    def _load_from_server(self):
        retry = 0
        while retry < LOAD_UUID_RETRY:
            try:
                uid = self._load_from_server0()
                return uid
            except Exception as err:
                if retry >= LOAD_UUID_RETRY:
                    raise Exception('DEBUG: load uuid retry' + str(retry) + ' failed', err)
        # done
    
    # load a user uuid from iqiyi server
    def _load_from_server0(self):
        # make a url to request
        url_to = UUID_URL + '?tn=' + str(random.random())
        try:
            # get uuid by http request
            info = base.get_html_content(url_to)
        except Exception as err:
            raise Exception('DEBUG: iqiyi, load uuid http error', err)
        # an example of info
        # 'var uid={"uid":"f21e1ae1c44f6c40f0674316ba7cf55b"};'
        # analyse received text
        uid_raw = re.findall('var uid=([^;]+);', info)
        json_text = uid_raw[0]
        uid_info = json.loads(json_text)
        uid = uid_info['uid']
        # done
        return uid

# end uuid.py


