# coding:utf-8
import requests
import re

def start_get_session():
    session_ = requests.session()
    return session_

def get_base_cookies(session_):
    session_.get('http://user.qunar.com/passport/login.jsp')
    get_image(session_)
    session_.get('https://user.qunar.com/passport/addICK.jsp?ssl')
    response = session_.get('https://rmcsdf.qunar.com/js/df.js?org_id=ucenter.login&js_type=0')
    #获取sessionID
    session_id = re.findall(r'sessionId=(.*?)&', response.text)
    session_id = session_id[0]

    # 获取fid
    session_.get('https://rmcsdf.qunar.com/api/device/challenge.json?callback=callback_1585481366826&sessionId={}'
                 '&domain=qunar.com&orgId=ucenter.login'.format(session_id))
    session_.cookies.update({'QN271': session_id})
    pass

def get_image(session_):
    response = session_.get('https://user.qunar.com/captcha/api/image?k={en7mni'
    '(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a&t=1584406205971')
    with open('code.png', 'wb') as f:
        f.write(response.content)

def login(session_, username_, password_, code_):
    data = {
        'loginType': 0,
        'username_': username,
        'password_': password,
        'remember': 1,
        'vcode_': code
    }

    url = 'https://user.qunar.com/passport/loginx.jsp'
    response = session_.post(url, data)
    print(response.text)
    session_.get('https://user.qunar.com/index/basic')
    print(response.text)

if __name__ == "__main__":
    session = start_get_session()
    get_base_cookies(session)
    username = input('请输入你的用户名：')
    password = input('请输入你的密码：')
    code = input('请输入你的验证码：')

    login(session, username, password, code)


