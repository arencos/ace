import os, subprocess
from inspect import getframeinfo, stack
import aceconfig as conf
import xml.etree.ElementTree as xml
import getpass

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
		homedir = os.environ['HOME']
		Ace().ace_debug(os.getlogin())
		f = open("/home/" + os.getlogin() + "/.config/awesome/rc.lua", "a")
		try:
			f.write("\nawful.spawn.with_shell(\"%s\")\n" % cmd)
			Ace().ace_debug("Added %s to awesome autostart." % cmdS)
			f.close()
		except Exception as e:
			Ace().ace_debug(e)
			f.close()

	def add_to_xprofile(self, cmd):
		home = "/home/" + os.getlogin()
		f = open(home + "/.xprofile", "a")
		try:
		    f.write(cmd + "\n")
		    Ace().ace_debug("Found file, arg passed: " + cmd)
		    f.close()
		except Exception as e:
			Ace().ace_debug(e)
			f.close()




# ---- openbox ----

#Ace.openbox_add_to_autostart(Ace(), "nitrogen --restore")
#Ace.openbox_add_keybinding(Ace(), "C-W-a", "sudo shutdown now")

# ---- awesomewm ----

#Ace.awesome_add_to_autostart(Ace(), "xrandr -s 1440x900")

# ---- x11 ---- #

#Ace.add_to_xprofile(Ace(), "tilix")
#Ace.add_to_xprofile(Ace(), "feh --bg-scale --randomize ~/Pictures/Wallpaper-Stock/ &")
#Ace.add_to_xprofile(Ace(), "picom -f &")
#Ace.add_to_xprofile(Ace(), "# exec de_or_window_manager &")
