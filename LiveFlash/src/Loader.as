// LiveFlash : Loader
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

class Loader 
{
	private var ui:MovieClip;
	private var app:Application;
	private var loader:MovieClipLoader;
	
	public function Loader(mc:MovieClip)
	{
		ui = mc.createEmptyMovieClip("ui",1);
		loader = new MovieClipLoader();
		loader.addListener(this);
		loader.loadClip("UI.swf",ui);
	}

	private function onLoadInit()
	{
		trace("UI Loaded");
		app = new Application(ui);	
	}
		
	public static function main()
	{
		var l:Loader = new Loader(_root);
	}	
}