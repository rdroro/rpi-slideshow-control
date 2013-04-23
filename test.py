import subprocess

c = subprocess.Popen(["eog", "/home/sysalia/Pictures"])

if type(c) is subprocess.Popen:
	print("hh")
else:
	print("bad")
