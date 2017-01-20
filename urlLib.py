import urllib.request
import urllib.parse

#site = urllib.request.urlopen("https://kalekem.github.io");
#print(site.read());


url = "https://pythonprogramming.net";
values = {"s": "basic", "submit":"search"};
data = urllib.parse.urlencode(values);
data = data.encode("utf-8");
req = urllib.request.Request(url, data);
resp = urllib.request.urlopen(req);
respData =  resp.read();

print(respData);

try:
    x = urllib.request.urlopen("https://www.google.com/search?q=test");
    print(x.read());

except Exception as e:
    print(str(e));




     
