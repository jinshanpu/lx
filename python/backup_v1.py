import os
import time

source = ["/home/sssl/Downloads/", "/home/sssl/opt/bin/"]
target_dir = '/home/sssl/workspace/backupTMP/'
today = time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

comment = raw_input('Enter a comment --> ')
if len(comment) != 0:
	comment = '_' + comment.replace(' ', '_')

target_dir = target_dir + today 
if not os.path.exists(target_dir):
	os.mkdir(target_dir)
	print 'Successfully created directory', target_dir


target = target_dir + '/' + now + comment + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
