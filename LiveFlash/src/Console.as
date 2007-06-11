// LiveFlash : Console
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

class Console
{
	private var inputText:TextField;
	private var outputText:TextField;
	
	private var socket:LiveSocket;
	
	private var history:Array;
	private var historyIndex:Number;
	
	private var commandHandler:Function;
	
	public function Console(mc:MovieClip, liveSocket:LiveSocket)
	{
		trace("New Console : " + mc);
		inputText = mc.inputText;
		outputText = mc.outputText;
		socket = liveSocket;
		
		socket.setConsole(this);
		
		history = [];
		historyIndex = 0;
			
		Key.addListener(this);
		
		commandHandler = Delegate.create(this,display);
	}

	public function display(msg:String)
	{
		outputText.text += msg + "\n";
		outputText.scroll = outputText.maxscroll + 1;
	}
	
	private function sendCommand()
	{
		socket.sendCommand(inputText.text,commandHandler);
		history.splice(historyIndex);
		history.push(inputText.text);
		historyIndex = history.length - 1;
		inputText.text = "";
	}
	
	private function showHistory(dir:Number)
	{
		if(dir > 0 && (historyIndex + dir) < history.length)
		{
			historyIndex += dir;
		}
		else if(dir < 0 && (historyIndex + dir) > 0)
		{
			historyIndex += dir;
		}
		
		inputText.text = history[historyIndex];
	}
	
	private function onKeyDown()
	{
		if(Key.isDown(Key.ENTER))
		{
			sendCommand();
		}
		else if(Key.isDown(Key.PGUP))
		{
			showHistory(-1);
		}
		else if(Key.isDown(Key.PGDN))
		{
			showHistory(1);
		}
	}
}