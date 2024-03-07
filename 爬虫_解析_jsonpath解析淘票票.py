import urllib.request

import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1706274203789_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ',
    'Cookie':'cna=h4qJGRl1OhACAXWuDnGcqtSy; miid=2791376811224400971; enc=9IPsniN5H1eS5jxtVsPCxtzWZE621kejF8yg5h4%2B%2B%2B%2FpCXZE3la5bW9jUBPdjpiib5CKoIf2jBdaJVNfT2UJRw%3D%3D; tracknick=%5Cu7092%5Cu83DC111; thw=cn; sgcookie=E100e7vPyyVfYPWh0s4uApAEuCnE1x0nAjUSqfmkDYDvcO2cTQnNYSxkhHlNW7yHEWQpbJ%2FJL%2B4soavJ9%2BIk7buDib1%2BnuxVkfxYBmzNtpxGZXg%3D; _cc_=W5iHLLyFfA%3D%3D; l=fBPKmOlRgOKz6721BO5aourza779gCRfcsPzaNbMiIEGa1YhjgKADNCOG1XHKdtjgT5AsLKyQgQsVd3w7J4T5jkDBeYBRs5mpC968eM3N7AN.; t=23d92cb03397d2acef88abdbff1c15e8; xlly_s=1; cookie2=159f7043c25ca4b6f558558a93cfcf99; v=0; _tb_token_=503e553fe8a85; tb_city=510100; tb_cityName="s8m2vA=="; tfstk=ePck3cgmNYyW90fsk0FWMfvfsiJYFgNQ3DCLvWEe3orj94pSJBRnmcwF9LN8KWm4DbE-y77Shc3Nwbp796V7OW-9XCdty4NQTDAh1R3W_i5MNhd964JzPW32XUZqsHIUi6BtYnGerRqGS0yDZNIDkl3zm10jizoVF4rD8elmn8qNMofFTj4l4d6VQE4ROr8Kg96QUra0X8nZrG01Mm-MoEXwR8zbPlLDo96QUra0XEYcQewzlzZO.; isg=BBYWvscLb1Jx8FpzJkTN-143Z8wYt1rxC4UYR4B_dPmUQ7bd6EcGATc929-va1IJ',
    'Referer':'https://dianying.taobao.com/?spm=a1z21.3046609.city.52.32c0112adhnKyM&city=510100'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# split()方法以指定分隔符将字符串分割为序列
content = content.split('(')[1].split(')')[0]

with open('淘票票.json','w',encoding='utf-8') as f:
    f.write(content)

import json
obj = json.load(open('淘票票.json','r',encoding='utf-8'))
city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)