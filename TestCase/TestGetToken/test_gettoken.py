import configparser as conf
import pytest
import time
import json
import hashlib
import requests
import allure

# @pytest.fixture(autouse='true')
# def myfixture():
#     '''前置函数'''
class Basic_One():
    def get_token(self,visitor):
        '''gettoken函数，因为每个接口的url都不一样，所以请求单独写在每个用例组中了'''
        method = 'GetAppToken'
        productName = "Default"
        productVersion = '1.0.0'
        callBackUrl = 'http://127.0.0.1'
        AppSecret = '46458A604792946B56A6546C3374D9AA'
        appkey = '38669EB53BFDF2A8A0FDCCBDB2538500'
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
        data = {
            "visitor": visitor,
            "callBackUrl": callBackUrl,
            "productName": productName,
            "productVersion": productVersion
        }
        string = AppSecret + 'appKey' + appkey + 'method' + method + 'timestamp' + timestamp + json.dumps(
            data, separators=(",", ":")) + AppSecret

        sign = hashlib.md5(string.encode('utf-8')).hexdigest()
        headers = {'Content-type': 'application/json',
                   'Host': 'api.teemo.silkage.net',
                   'Accept': '*/*',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        url = 'http://api.teemo.silkage.net/ReportService.gspx?method=' + method + '&appKey=' + appkey + '&timestamp=' + timestamp + '&sign=' + sign

        data = json.dumps(data).encode('utf-8')
        response = requests.post(url, data, headers=headers)
        return response.json()

@allure.feature('Test_GetAppToken接口')
class Test_GetAppToken(Basic_One):    #继承Basic_One()类

    @allure.story('获取授权')
    @allure.issue('case id：020401')
    @pytest.mark.parametrize(
        'visitor,result',[
            ('不存在',False),
            ('pytester',True)
        ],
        ids=[
            'visitor不存在，返回success状态为False',
            'visitor存在，返回success状态为True'
        ]
    )
    def test_getapptoken(self,visitor,result):
        '''用例————visitor不存在和visitor存在来断言'''

        response=Basic_One().get_token(visitor)
        success = response['success']
        assert success==result









