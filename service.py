#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2014 KODeKarnage
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
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import xbmcgui
import os

DIALOG           = xbmcgui.Dialog()

if __name__ == "__main__":

    if os.path.isfile("/home/osmc/ttmessage.txt"):

        #open and read file, use line one, 80 character max
        with open("/home/osmc/ttmessage.txt") as ttm:
            message = ttm.readline()

        linecount = min(2,(len(message) / 40 ) + 1)
        final_message = ""

        for line in range(linecount):

            final_message = final_message + message[line*40:(1+line)*40] + "\n"

        DIALOG.ok("Message from your supplier",final_message)
        
        #burn after reading
        os.remove("/home/osmc/ttmessage.txt")
