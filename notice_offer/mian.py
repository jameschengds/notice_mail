import urllib
import requests
def get_JSESSIONID():
    url = 'https://jlu.radiusbycampusmgmt.com/ssc/zx670w0zx670x6700txN.ssc'


    url = "https://jlu.radiusbycampusmgmt.com/ssc/zx670w0zx670x6700txN.ssc"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Accept-Language': 'zh,zh-CN;q=0.9',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    JSESSIONID = response.headers.get('set-cookie')[11:44]
    return JSESSIONID

def login(name,pwd,jsid):
    url = "https://jlu.radiusbycampusmgmt.com/ssc/j_spring_security_check"

    payload = 'j_username='+name+'%5E&j_password='+pwd+'%5E&spamProtection=false'
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://jlu.radiusbycampusmgmt.com',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Referer': 'https://jlu.radiusbycampusmgmt.com/ssc/zx670w0zx670x6700txN.ssc',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Cookie': 'JSESSIONID='+jsid,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

def step2(jsid):

    url = "https://jlu.radiusbycampusmgmt.com/ssc/zx670w0zx670x6700txN.ssc"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Referer': 'https://jlu.radiusbycampusmgmt.com/ssc/zx670w0zx670x6700txN.ssc',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Cookie': 'JSESSIONID='+jsid
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

def csrf1(jsid):
    import requests

    url = "https://jlu.radiusbycampusmgmt.com/ssc/CsrfJavaScriptServlet"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'script',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'DNT': '1',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'no-cors',
        'Referer': 'https://jlu.radiusbycampusmgmt.com/ssc/zx670w0zx670x6700txN.ssc',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Cookie': 'JSESSIONID='+jsid
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def scrf2(jsid):
    import requests

    url = "https://jlu.radiusbycampusmgmt.com/ssc/CsrfJavaScriptServlet"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'FETCH-CSRF-TOKEN': '1',
        'Sec-Fetch-Dest': 'empty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'DNT': '1',
        'Accept': '*/*',
        'Origin': 'https://jlu.radiusbycampusmgmt.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://jlu.radiusbycampusmgmt.com/ssc/zx670w0zx670x6700txN.ssc',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Cookie': 'JSESSIONID='+jsid
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
    return response.text.encode('utf8')


def get_status(jsid,t):
    url = "https://jlu.radiusbycampusmgmt.com/ssc/applications/load.ssc?page=1&start=0&limit=25"

    payload = {}
    headers = {
        'Cookie': 'JSESSIONID='+jsid,
        'stoken':t
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


if __name__ == '__main__':
    JSESSIONID = get_JSESSIONID()
    login('chengqianxiang','cqx0322.',JSESSIONID)
    step2(JSESSIONID)
    csrf1(JSESSIONID)
    token =str(scrf2(JSESSIONID), encoding = "utf8")[7:]
    get_status(JSESSIONID,token)


