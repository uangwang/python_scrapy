import urllib.request

url = 'https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_module?g_iframeUser=1&i_uin=2743335179&i_login_uin=2743335179&mode=4&previewV8=1&style=35&version=8&needDelOpr=true&transparence=true&hideExtend=false&showcount=5&MORE_FEEDS_CGI=http%3A%2F%2Fic2.s8.qzone.qq.com%2Fcgi-bin%2Ffeeds%2Ffeeds_html_act_all&refer=2&paramstring=os-winxp|100'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ',
    'Cookie':'RK=9RrMJ5Suxn; ptcz=79acbe41e9e03b8d4b99268c5e9b6f0179f989375a682faf50412217bef22095; tvfe_boss_uuid=6a14cedb507fcb8a; pgv_pvid=8362423684; fqm_pvqid=54cd68e1-4d72-4200-841c-22345596c9df; pac_uid=0_728798c1d018d; iip=0; _clck=1974iy0|1|fdx|0; eas_sid=s1G6F9L6j5j8K8s310a1D8N0f8; zzpaneluin=; zzpanelkey=; _qpsvr_localtk=0.8273347929130106; pgv_info=ssid=s389976966; uin=o2743335179; skey=@I0LCnJCcx; p_uin=o2743335179; pt4_token=5ivx2FLaXtGYbKc0XZ1UTfoTI2p4Yw6JBuqz9INBDrA_; p_skey=K14uHFpsKE0sIHQRzyMhDXbFHA7LmR-LDz4vq7YDVOc_; Loading=Yes',
    'Referer':'https://user.qzone.qq.com/2743335179'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

with open('qq.html','w',encoding='utf-8') as fp:
    fp.write(content)