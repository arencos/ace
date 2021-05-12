import os, subprocess
from inspect import getframeinfo, stack
import aceconfig as conf
import xml.etree.ElementTree as ET
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

	def openbox_add_to_autostart(self, cmd, remove = False):
		f = open("/etc/xdg/openbox/autostart", "a")
		try:
			f.write(cmd + "\n")
			Ace().ace_debug("Found file, arg passed: " + cmd)
			f.close()
		except IOError as e:
			Ace().ace_debug(e)
			f.close()


	def openbox_add_keybinding(self, keys, whatToExec, remove = False):
		
		Ace().ace_debug("Not implemented yet!")

		# keybind = ET.Element('keybind')
		# keybind.set("key", keys)

		# action = ET.SubElement(keybind, 'action')
		# action.set("name", "Execute")
	    
		# command = ET.SubElement(action, 'command')
		# command.text = whatToExec
		
		# tree = ET.parse("/etc/xdg/openbox/rc.xml")
		# tree.find("keyboard").append(keybind)
		#tree.write("/etc/xdg/openbox/rc.xml")


	def awesome_add_to_autostart(self, cmd, remove = False):
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

	def add_to_xprofile(self, cmd, remove = False):
		if remove:
			home = "/home/" + os.getlogin()
			f = open(home + "/.xprofile", "r")

			lines = f.readlines()
			f.close()

			new_file = open(home + "/.xprofile", "w")
			for line in lines:
			    if line.strip("\n") != "%s" % cmd:
			        new_file.write(line)

			new_file.close()
		else:
			home = "/home/" + os.getlogin()
			f = open(home + "/.xprofile", "a")
			try:
			    f.write(cmd + "\n")
			    Ace().ace_debug("Found file, arg passed: " + cmd)
			    f.close()
			except Exception as e:
				Ace().ace_debug(e)
				f.close()

	def i3wm_add_keybinding(self, keys, type, exec, remove = False):


		if remove:
			home = "/home/" + os.getlogin()
			f = open(home + "/.config/i3/config", "r")

			lines = f.readlines()
			f.close()

			new_file = open(home + "/.config/i3/config", "w")
			for line in lines:
			    if line.strip("\n") != "bindsym %s %s %s" % (keys, type, exec):
			        new_file.write(line)

			new_file.close()
		else:


			# bindsym $mod+Shift+r restart
			home = "/home/" + os.getlogin()
			f = open(home + "/.config/i3/config", "a")
			try:
				f.write("\nbindsym %s %s %s" % (keys, type, exec))
				Ace().ace_debug("bindsym %s %s %s" % (keys, type, exec))
				f.close()
			except Exception as e:
				Ace().ace_debug(e)
				f.close()

	def i3wm_add_to_autostart(self, exec, remove = False):

		if remove:
			home = "/home/" + os.getlogin()
			f = open(home + "/.config/i3/config", "r")

			lines = f.readlines()
			f.close()

			new_file = open(home + "/.config/i3/config", "w")
			for line in lines:
			    if line.strip("\n") != "exec %s" % (exec):
			        new_file.write(line)

			new_file.close()
		else:
			home = "/home/" + os.getlogin()
			f = open(home + "/.config/i3/config", "a")
			try:
				f.write("\nexec %s" % exec)
				Ace().ace_debug("\nexec %s" % exec)
				f.close()
			except Exception as e:
				Ace().ace_debug(e)
				f.close()



#Ace.i3wm_add_keybinding(Ace(), "Mod1+Control+Shift+p", "exec", "tilix &", False)
#Ace.i3wm_add_to_autostart(Ace(), "firefox", True)
# ---- openbox ----

#Ace.openbox_add_to_autostart(Ace(), "nitrogen --restore")
#Ace.openbox_add_keybinding(Ace(), "C-W-a", "sudo shutdown now")

# ---- awesomewm ----

#Ace.awesome_add_to_autostart(Ace(), "xrandr -s 1440x900")

# ---- x11 ---- #

#Ace.add_to_xprofile(Ace(), "tilix", True)
#Ace.add_to_xprofile(Ace(), "feh --bg-scale --randomize ~/Pictures/Wallpaper-Stock/ &")
#Ace.add_to_xprofile(Ace(), "picom -f &")
#Ace.add_to_xprofile(Ace(), "# exec de_or_window_manager &")
