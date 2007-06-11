# LiveFlash, a flash socket interface for controlling Ableton Live
# Based on the LiveOSC code from liveapi.org
#
# Copyright (C) 2007 Martin Wood-Mitrovski (martin@relivethefuture.com)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For questions regarding this module contact
# Martin Wood-Mitrovski 
# martin@relivethefuture.com

import Live
import sys, StringIO, socket, code
from LiveUtils import *
import Command

class LiveFlash:
    __module__ = __name__
    __doc__ = "Main class that establishes the Live Flash Socket Handler\n"

    def __init__(self, c_instance):
        self._LiveFlash__c_instance = c_instance

        self.flashSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.flashSocket.bind( ('', 3000) )
        self.flashSocket.setblocking(False)
        self.flashSocket.listen(1)
        self.clientConnection = None
        self.commandHandler = Command.FlashCommands()
        self.bufsize = 4096
        
        self.command = ""
        
    def disconnect(self):

        self.flashSocket.close()

    def connect_script_instances(self, instanciated_scripts):
        """
        Called by the Application as soon as all scripts are initialized.
        You can connect yourself to other running scripts here, as we do it
        connect the extension modules
        """
        return

    def application(self):
        """returns a reference to the application that we are running in"""
        return Live.Application.get_application()

    def song(self):
        """returns a reference to the Live Song that we do interact with"""
        return self._LiveFlash__c_instance.song()

    def handle(self):
        """returns a handle to the c_interface that is needed when forwarding MIDI events via the MIDI map"""
        return self._LiveFlash__c_instance.handle()

    def refresh_state(self):
        """I'm sure this does something useful.."""
        return

    def is_extension(self):
        return False

    def request_rebuild_midi_map(self):
        """
        To be called from any components, as soon as their internal state changed in a 
        way, that we do need to remap the mappings that are processed directly by the 
        Live engine.
        Dont assume that the request will immediately result in a call to
        your build_midi_map function. For performance reasons this is only
        called once per GUI frame.
        """
        return

    def build_midi_map(self, midi_map_handle):
        """
        New MIDI mappings can only be set when the scripts 'build_midi_map' function 
        is invoked by our C instance sibling. Its either invoked when we have requested it 
        (see 'request_rebuild_midi_map' above) or when due to a change in Lives internal state,
        a rebuild is needed.
        """
        return
    
    def update_display(self):
        #Updates every 100ms

        #Keep trying to accept a connection until someone actually connects
        if not self.clientConnection:
            try:
                #Does anyone want to connect?
                self.clientConnection, self.addr = self.flashSocket.accept()
            except:
                #No one connected in this iteration
                pass
            else:
                #Yay! Someone connected! Send them the banner and first prompt.
                self.clientConnection.send("Welcome to the Ableton Live Flash Interface" + "\x00")
                
        else:
            #Someone's connected, so lets interact with them.
            try:
                #If the client has typed anything, get it
                self.buffer += self.clientConnection.recv(self.bufsize)
            except:
                #Nope they haven't typed anything yet
                self.buffer = "" #

            self.processBuffer()
            
    def processBuffer(self):
        while(self.buffer.find("\x00") > -1):
            eom = self.buffer.find("\x00")
            message = self.buffer[:eom]
            self.buffer = self.buffer[eom+1:]
            
            res = self.commandHandler.handleCommand(message)
            if res != None:
                self.clientConnection.send(str(res) + "\x00")
            else:
                self.clientConnection.send("No Response " + "\x00")
        
    def send_midi(self, midi_event_bytes):
        """
        Use this function to send MIDI events through Live to the _real_ MIDI devices 
        that this script is assigned to.
        """
        pass
    
    def receive_midi(self, midi_bytes):
        return
    
    def can_lock_to_devices(self):
        return False

    def suggest_input_port(self):
        return ''

    def suggest_output_port(self):
        return ''

    def suggest_map_mode(self, cc_no):
        result = Live.MidiMap.MapMode.absolute
        if (cc_no in range(FID_PANNING_BASE, (FID_PANNING_BASE + NUM_CHANNEL_STRIPS))):
            result = Live.MidiMap.MapMode.relative_signed_bit
        return result

    def __handle_display_switch_ids(self, switch_id, value):
        pass
