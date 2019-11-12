#! python3
# netik.py - Launches a list of sites in the browser using an address 
# from the command line or clipboard.

import webbrowser, sys, pyperclip, shelve

op = webbrowser.get("C:/Program Files (x86)/Opera/launcher.exe %s")
webbrowser.register('opera', None,op)
netikShelf = shelve.open('netik')
if len(sys.argv) >= 3:
	if sys.argv[1] == 'add':
		for i in range(3, len(sys.argv)):
			if sys.argv[2] in netikShelf:
				netikShelf[sys.argv[2]] += [sys.argv[i]]
			else:
				netikShelf[sys.argv[2]] = [sys.argv[i]]
	elif sys.argv[1] == 'delk':
		if sys.argv[2] in netikShelf:
			netikShelf.pop(sys.argv[2])
	elif sys.argv[1] == 'delv':
		if sys.argv[3] in netikShelf[sys.argv[2]]:
			netikShelf[sys.argv[2]].pop(sys.argv[3])
			
elif len(sys.argv) == 2:
	# Get address from command line.
	if sys.argv[1] == 'list':
		for k, v in list(netikShelf.items()):
			print(str(k) + ": " + str(v))
	else:
		for value in netikShelf[sys.argv[1]]:
			op.open(value)
netikShelf.close()
