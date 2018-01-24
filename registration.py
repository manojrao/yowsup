from yowsup.registration import WACodeRequest
method='sms'
config={'cc': '00', 'mcc': '000', 'sim_mcc': '000', 'phone': 'xxxxxxxxxxxx', 'sim_mnc': '000', 'mnc': '00'}
codeReq = WACodeRequest(config["cc"],
                        config["phone"],
                        config["mcc"],
                        config["mnc"],
                        config["mcc"],
                        config["mnc"],
                        method
)
result = codeReq.send()
print result
