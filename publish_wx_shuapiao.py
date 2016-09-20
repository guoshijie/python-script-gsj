# coding: utf-8
import urllib.request,time,sys,hashlib
with urllib.request.urlopen('http://weika.mugeda.com/server/public_counter.php/incr?crid=57b6a58ca3664eb17c000d08&token=&t=1471688587959&counterid=b89gtj5nuu&type=jsonp&_mats=1471688587960&callback=like_callback') as f:
    print(f.read().decode('utf-8'))

def publish(counterid,num = 10):
    for i in range(num):
        now = time.time() * 1000
        now = int(now)
        t = str(now)
        crid = md5(t)
        crid = '57b6a58ca3664eb17c000d08'
        type = 'jsonp'
        _mats = t
        callback = 'like_callback'
        arr = ['crid='+crid,'token=','t='+t,'counterid='+counterid,'type='+type,'_mats='+_mats,'callback='+callback]
        url = 'http://weika.mugeda.com/server/public_counter.php/incr?' + '&'.join(arr)
        print(url)
        with urllib.request.urlopen(url) as f:
            print(f.read().decode('utf-8'))

def md5(data):
    m = hashlib.md5(data.encode(encoding='utf-8'))
    return m.hexdigest()[0:-8]

counter_id = sys.argv[1]

if counter_id == '2':
    counter_id = 'b89gtj5nuu'
if counter_id == '1':
    counter_id = 'babosnd4f9'
if counter_id == '3':
    counter_id = 'babowlz93m'
print(counter_id)
print(sys.argv[2])

publish(counter_id,int(sys.argv[2]))

