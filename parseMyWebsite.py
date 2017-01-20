import urllib.request
import urllib.parse
import re

#site = urllib.request.urlopen("https://kalekem.github.io");
#print(site.read());


url = "https://kalekem.github.io";
req = urllib.request.Request(url);
resp = urllib.request.urlopen(req);
respData =  resp.read();

#print(respData);

#print everything between paragraph tags
#.*?--look for everthing within paragrapgh texts
paragraph= re.findall(r'<p>(.*?)</p>', str(respData));

for eachP in paragraph:
    print (eachP);






     
