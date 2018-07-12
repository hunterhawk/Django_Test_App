# -*- coding:utf-8 -*-

import urllib.request
import json

req = urllib.request.urlopen(
    url="http://127.0.0.1:8000/getdata/"
)

result = json.loads(req.read())
with open("shijiahao.txt", "wb") as f:
   for ele in result:
       #f.write(bytes(json.dumps(ele), encoding="utf-8")+ '\n')
       test = json.dumps(ele) + '\n'
       test.encode(encoding="utf-8")
       test1 = (json.dumps(ele) + '\n').encode(encoding="utf-8")
       f.write(test1)
       #f.write(json.dumps(ele).encode(encoding="utf-8"))
