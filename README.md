***Requiement***

- [aliyun-python-sdk-core](https://github.com/aliyun/aliyun-openapi-python-sdk/tree/master/aliyun-python-sdk-core)
- [aliyun-python-sdk-alidns](https://github.com/aliyun/aliyun-openapi-python-sdk/tree/master/aliyun-python-sdk-alidns)

***Need to be complete***

aliyunDNSS.py

```
# 请填写你的Access Key ID
access_key_id = ""

# 请填写你的Access Key Secret
access_Key_secret = ""

# 请填写你的账号ID
account_id = ""

# 请填写你的一级域名
rc_domain = ''
```

publicIP.py

```
# Modify ip address location and service provider
# Copy below link to browser look what ip information is
# http://cn.bing.com/search?q=ip&go=%E6%8F%90%E4%BA%A4&qs=n&form=QBLH&pq=ip&sc=8-2&sp=-1&sk=&cvid=14b93b305cdc4183875411c3d9edf938
self.html_re = re.compile(r'ip: (.+?) 广东省深圳市 天威视讯',re.DOTALL)
```
***Set schedule task***
```
1.Edit cron schedule task 
crontab -e

2.Add new schedule task below 
* * * * * /usr/bin/python /{path to the source}/aliyunDNSS.py

3.Save and exit

4.Check cron task 
crontab -l

5.check log.txt
cat log.txt
```
