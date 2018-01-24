from yowsup.registration import WARegRequest
config={'cc': 'xx', 'phone': 'xxxxxxxxxx'}
opt='xxxxxx'
opt = opt.replace('-', '')
req = WARegRequest(config["cc"], config["phone"], opt)
result = req.send()
print result
#before run file is /yowsup/registration.py
