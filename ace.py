import os, subprocess
from inspect import getframeinfo, stack
import aceconfig as conf
import xml.etree.ElementTree as xml

class Ace:
	def __init__(self):
		if os.geteuid() != 0:
			exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

	def ace_debug(self, message):
		if conf.showDebugMsgs == True:
			caller = getframeinfo(stack()[1][0])
			print("%s:%d - %s" % (caller.filename, caller.lineno, message))
		else:
			print("Disabled debug messages.")

	def openbox_add_to_autostart(self, cmd):
		f = open("/etc/xdg/openbox/autostart", "a")
		try:
			f.write(cmd + "\n")
			Ace().ace_debug("Found file, arg passed: " + cmd)
			f.close()
		except IOError as e:
			Ace().ace_debug(e)
			f.close()


	def openbox_add_keybinding(self, keys, whatToExec):
		
		keybinding = "<keybind key=\"%s\"><action name=\"Execute\"><command>%s</command><action></keybind>" % (keys, whatToExec)
		Ace().ace_debug("not finished yet")


	def awesome_add_to_autostart(self, cmd):
		f = open("/home/aren/.config/awesome/rc.lua", "a")
		try:
			f.write("\nawful.spawn.with_shell(\"%s\")\n" % cmd)
			Ace().ace_debug("Added %s to awesome autostart." % cmdS)
			f.close()
		except Exception as e:
			Ace().ace_debug(e)
			f.close()



#Ace.openbox_add_to_autostart(Ace(), "nitrogen --restore")
#Ace.openbox_add_keybinding(Ace(), "C-W-a", "sudo shutdown now")
#Ace.awesome_add_to_autostart(Ace(), "nitrogen --restore")
