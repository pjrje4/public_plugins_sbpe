import logging
import math
import time

from _remote import ffi, lib
from manager import PluginBase
import util


class Plugin(PluginBase):
    def onInit(self):
   
        self.config.option('show_room_seed', True, 'bool')

        self.roomseed = util.PlainText(size=90)
        self.oldseed = 0

    def onPresent(self):

        cw = self.refs.ClientWorld
        wv = self.refs.WorldView
        if cw == ffi.NULL or wv == ffi.NULL:
            return

        # show the world seed bottom right
        if self.config.show_room_seed:
            cwprops = cw.asWorld.props
            seedVal = cwprops.seed
            seedStr = '{} {}'.format('seed:', seedVal)
            self.roomseed.text = seedStr
            self.roomseed.draw( # not in the correct spot, will
                 # test when I have access to dev pc
                 self.refs.windowW, self.refs.windowH,
                 anchorX=1, anchorY=1)
            if not self.oldseed == seedVal:
                logging.info(seedVal)
                self.oldseed = seedVal

   