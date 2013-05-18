#!/usr/bin/env python

import sys
import gtk
import appindicator

import imaplib
import re
import os

class SshServersIndicator:
	def __init__(self):
		self.ind = appindicator.Indicator("ssh-servers-indicator", "icon", appindicator.CATEGORY_APPLICATION_STATUS)
		self.ind.set_status(appindicator.STATUS_ACTIVE)

		path = os.path.dirname( os.path.realpath(__file__) )
		self.ind.set_icon_theme_path(path)
		self.ind.set_attention_icon("icon")

		self.makeMenu()
		self.ind.set_menu(self.menu)

	def makeMenu(self):
		self.menu = gtk.Menu()

		import glob
		import SimpleConfigParser
		cp = SimpleConfigParser.SimpleConfigParser()

		path = os.path.dirname( os.path.realpath(__file__) )
		os.chdir( path + "/servers" )

		for files in glob.glob("*"):

			cp.read(path + "/servers/" + files)

			item = gtk.MenuItem( cp.getoption("title") )
			item.file = path + "/servers/" + files

			item.connect("activate", self.run)
			item.show()
			self.menu.append(item)


		os.chdir( path )

		sep = gtk.SeparatorMenuItem()
		sep.show()
		self.menu.append(sep)

		self.quitItem = gtk.MenuItem("Quit")
		self.quitItem.connect("activate", self.quit)
		self.quitItem.show()
		self.menu.append(self.quitItem)

	def main(self):		
		gtk.main();

	def quit(self, widget):
		sys.exit(0)

	def run(self, widget):
		
		label = widget.get_label()

		path = os.path.dirname( os.path.realpath(__file__) )

		#os.system("xterm -e " + label)
		os.system("gnome-terminal -e '" + path + "/login.bash " + widget.file + "'" )

		#import pprint
		#pprint.pprint(widget)
		#pprint.pprint( "gnome-terminal -e '" + path + "/login.bash " + widget.file + "'" )
		

if __name__ == "__main__":
	indicator = SshServersIndicator()
	indicator.main()
