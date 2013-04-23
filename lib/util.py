def readConf():
	config = {}
	execfile("conf/config.conf", config)
	return config