// LiveFlash : LiveSocket
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

class LiveSocket 
{
	private var socket:XMLSocket;
	
	private static var HOST:String = "localhost";
	private static var PORT:Number = 3000;
	
	private var commandBuffer:Array;
	
	private var waiting:Boolean;
	
	private var console:Console;
	
	private var currentCommand:Object;
	
	public function LiveSocket()
	{
		socket = new XMLSocket();
		socket.onConnect = Delegate.create(this,onConnect);
		socket.onClose = Delegate.create(this,onClose);
		socket.onData = Delegate.create(this,onData);
		
		commandBuffer = [];
	}

	public function connect()
	{
		socket.connect(HOST,PORT);
	}
	
	public function setConsole(c:Console)
	{
		console = c;
	}
	
	public function sendCommand(cmd:String, handler:Function)
	{
		var cObj:Object = {command:cmd,handler:handler};
		
		if(waiting)
		{
			commandBuffer.push(cObj);
		}
		else
		{
			process(cObj);
		}
	}
	
	public function isWaiting():Boolean
	{
		return waiting;
	}

	private function process(cmd:Object)
	{
		currentCommand = cmd;
		socket.send(cmd.command);
		waiting = true;
	}
	
	private function onConnect(success:Boolean)
	{
		if(success)
		{
			console.display("Connected");	
		}
		else
		{
			console.display("Connect failed");
		}
	}
	
	private function onClose()
	{
		console.display("Connection closed");
	}
	
	private function onData(data:Object)
	{
		if(currentCommand.handler != null)
		{
			currentCommand.handler(data.toString());
		}
		
		if(commandBuffer.length > 0)
		{
			process(commandBuffer.shift());
		}
		else
		{
			currentCommand = null;
			waiting = false;
		}
	}
}