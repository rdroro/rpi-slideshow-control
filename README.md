rpi-slideshow-control
=====================

Python application for the remote control of a slideshow on Raspberry Pi (or other computer) connected to a screen

## Start rpi-slideshow-control on boot

To start rpi-slideshow-control on boot please type this following line in crontab file for the current user

<pre>
	@reboot /home/sysalia/code/rpi-slideshow-control/start
</pre>

### On Debian-like

On Debian-like OS, you can follow these steps:

<pre>
	# launch crontab tool
	$ crontab -e
	# Add this line
	@reboot /home/sysalia/code/rpi-slideshow-control/start
	# Save & quit
</pre>
