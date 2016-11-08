import QL as embed
import sys
import time

try:
	time.sleep(0.05)
	embed.openrun(sys.argv[1])
except:
	time.sleep(0.05)
	embed.ql('out <Press CTRL-C to quit>')
	embed.ql('out <Quick Language 1.2 by Yovel Key-Cohen>')
	while True:
		try:
			cmd = input(':: ')
			embed.ql(cmd+'<>') 
			# I put the extra angle brackets at the end
			# Because nothing works without brackets at the end
			# But everything works with extra brackets!
			# So why not!?
		except KeyboardInterrupt:
			embed.ql('out<>')
			embed.ql('exit<>')