import requests


def get_status():

    url = "https://jlu.radiusbycampusmgmt.com/ssc/applications/load.ssc?_dc=1612951226121&page=1&start=0&limit=25"

    payload = {}
    headers = {
        'Cookie': 'JSESSIONID=AEB604E882BF7E4E3580EE7C747F2099'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response



if __name__ == '__main__':
    print(get_status().text)