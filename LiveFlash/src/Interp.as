// LiveFlash : Interp
// Copyright (C) 2007 Martin Wood-Mitrovski (martin@relivethefuture.com)
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//
// For questions regarding this code
// Martin Wood-Mitrovski 
// martin@relivethefuture.com

import com.dynamicflash.utils.Delegate;

class Interp 
{
	private var handle:MovieClip;
	private var socket:LiveSocket;
	
	public function Interp(mc:MovieClip,server:LiveSocket)
	{
		handle = mc.handle;
		socket = server;
		handle.onPress = Delegate.create(this,startDrag);
		handle.onRelease = handle.onReleaseOutside = Delegate.create(this,endDrag);
	}	
	
	private function startDrag()
	{
		handle.startDrag(true,0,0,200,0);
		handle.onEnterFrame = Delegate.create(this,updatePos);
	}
	
	private function updatePos()
	{
		var pos:Number = (handle._x / 200);
		
		if(!socket.isWaiting())
		{
			socket.sendCommand("interp 0 0 1 " + pos);
		}
	}
	
	private function endDrag()
	{
		handle.stopDrag();
		delete handle.onEnterFrame;
	}
}