import time
import os
import datetime
import shutil

filename = 'QuickSavegame.svx'
time_resoultion = 10#in seconds

extension = filename.split('.')[-1]
while True:
	change_mtime = os.path.getmtime(filename)

	change_datetime = datetime.datetime.fromtimestamp(change_mtime)
	now_ = datetime.datetime.now()
	diff = (now_-change_datetime)
	if diff.seconds < time_resoultion:
		s_timestamp = time.strftime("%I_%M_%S___%d_%m",time.localtime(change_mtime))
		shutil.copyfile(filename,s_timestamp+'.'+extension)
	time.sleep(time_resoultion)