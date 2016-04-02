import requests

def search(argument):

    http_proxy = 'http://HITN042:69183421@172.31.1.3:8080/'
    
    proxyDict = { 
              "http"  : http_proxy, 
              "https" : http_proxy
            }

    url = "https://en.wikipedia.org/wiki/%s" %(argument)

    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
        'referer': "https//en.wikipedia.org/wiki/Main_Page",
        'accept-encoding': "gzip, deflate, sdch",
        'accept-language': "en-US,en;q=0.8",
        'cookie': "GeoIP=INDelhi28.666777.2167v4; mediaWiki.user.sessionId=7bb12a0d4efecd24; enwikimwuser-sessionId=58822f8a835a8aa0; GeoIP=IN%3A07%3ADelhi%3A28.666700%3A77.216698%3Av4; CP=H2; CN=Wikimania_registration!57455260!4605480!1*wm2016reg_anon!58106200!3866400!0; WMF-Last-Access=02-Apr-2016",
        'cache-control': "no-cache",
        'postman-token': "0876ff8e-1e8b-5375-8e6d-63df5ddb7094"
        }

    response = requests.request("GET", url, headers=headers, proxies=proxyDict)

    return response.text