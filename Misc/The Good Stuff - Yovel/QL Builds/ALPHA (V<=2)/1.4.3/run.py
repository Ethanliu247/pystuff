import ql as embed
import sys
import time

try:
	time.sleep(0.05)
	embed.openrun(sys.argv[1])
except:
	time.sleep(0.05)
	embed.ql('out <Press CTRL-C to quit> <n>')
	embed.ql('out <Quick Language 1.4.3 by Yovel Key-Cohen> <n>')
	while True:
		try:
			cmd = input(':: ')
			try: embed.ql(cmd+'<>') 
			except: embed.ql('out <An unknown error occurred in the code> <n>')
			# I put the extra angle brackets at the end
			# Because nothing works without brackets at the end
			# But everything works with extra brackets!
			# So why not!?
		except KeyboardInterrupt:
			embed.ql('out <> <n>')
			embed.ql('exit<>')