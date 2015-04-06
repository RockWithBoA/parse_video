#!/usr/bin/env python
# -*- coding: utf-8 -*-
# parse-video, part for parse_video
# parse-video: main bin file. 
# author sceext <sceext@foxmail.com> 2015.04 
# copyright 2015 sceext 
#
# This is FREE SOFTWARE, released under GNU GPLv3+ 
# please see README.md and LICENSE for more information. 
#
#    parse_video : parse videos from many websites. 
#    Copyright (C) 2015 sceext <sceext@foxmail.com> 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# import modules

# python3 modules
import sys
import json

# parse_video modules

# functions
def json_output(info_obj, fix_unicode=False):
    text = json.dumps(info_obj, sort_keys=True, indent=4, ensure_ascii=fix_unicode)
    # just print it
    print(text)

# main funciton
def main(lib):
    
    # get command line input url
    url = sys.argv[1]
    
    # import parse_video modules
    from lib import parser
    
    # parse
    info = parser.entry(url)
    
    # just print it
    json_output(info)
    
    # done

# start from main
if __name__ == '__main__':
    main()


# end parse-video

