from yowsup.demos import echoclient
credentials =('xxxxxxxxxxxx', 'xxxxxxxxxxxxxxx')
if not credentials:
	print("Error: You must specify a configuration method")
stack = echoclient.YowsupEchoStack(credentials, True)
stack.start()
