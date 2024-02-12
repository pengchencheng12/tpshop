
from utils.RequestsUtils import requests_get, requests_post


def cart_api():
    url = "http://demo6.tp-shop.cn/Home/Cart/index.html"
    header={"cookie":"CNZZDATA009=30037667-1536735; province_id=1; city_id=72; district_id=2819; town_id=0; PHPSESSID=ghl9cnk5ompdqni5euv2nfqae4; cn=0; user_id=313; is_distribut=1; uname=13290063078; head_pic=%252Fpublic%252Fimages%252Ficon_goods_thumb_empty_300.png"}
    r = requests_get(url, header)
    print(r)
def login_api():
    url="http://demo6.tp-shop.cn/index.php?m=Home&c=User&a=do_login&t=0.8170359809223715"
    body={"username":"13290063078","password":"12345","referurl":"%2FHome%2FUser%2Findex.html","verify_code":"SNRA"}
    header={"Content-Type":"application/x-www-form-urlencoded"}
    r=requests_post(url,body,header)
    print(r)

if __name__ == '__main__':
    #cart_api()
    login_api()
