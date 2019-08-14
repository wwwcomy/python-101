import uuid
import redis

#0001
arr=[]
for i in range(0,100):
    # notice there's a comma at the end
    arr.append(str(uuid.uuid1()))
print(arr)

#pip install redis

#0003
r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
for i in range (0,len(arr)):
    r.sadd("coupon", arr[i])

print(r.smembers("coupon"))
print("****")
print(r.scard("coupon"))
print("****")

