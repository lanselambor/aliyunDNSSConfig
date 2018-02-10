***Requiement***

- [aliyun-python-sdk-core](https://github.com/aliyun/aliyun-openapi-python-sdk/tree/master/aliyun-python-sdk-core)
- [aliyun-python-sdk-alidns](https://github.com/aliyun/aliyun-openapi-python-sdk/tree/master/aliyun-python-sdk-alidns)

***Need to be complete***

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
