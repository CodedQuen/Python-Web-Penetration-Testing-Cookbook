import screenshot
import requests

portList = [80,443,2082,2083,2086,2087,2095,2096,8080,8880,8443,9998,4643,9001,4489]

IP = '127.0.0.1'

http = 'http://'
https = 'https://'

def testAndSave(protocol, portNumber):
    url = protocol + IP + ':' + str(portNumber)
    try:
        r = requests.get(url,timeout=1)
        
        if r.status_code == 200:
            print 'Found site on ' + url 
            s = screenshot.Screenshot()
            image = s.get_image(url)
            image.save(str(portNumber) + '.png')
    except:
        pass

for port in portList:
    testAndSave(http, port)
    testAndSave(https, port)
