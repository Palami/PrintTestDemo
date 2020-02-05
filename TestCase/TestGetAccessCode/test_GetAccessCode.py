import requests
from TestCase.TestGetToken.test_gettoken import Basic_One
import pytest
import json
import allure

class Basic_Two():
    def get_code(self,token):
        method = 'GetAccessCode'
        data = {'accessToken': token}
        headers = {'Content-type': 'application/json',
                   'Host': 'api.teemo.silkage.net',
                   'Accept': '*/*',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        url = 'http://api.teemo.silkage.net/ReportService.gspx?method=' + method + '&accessToken='+token
        response = requests.post(url,data=json.dumps(data),headers=headers)
        return response.json()

# @pytest.fixture(autouse=True)
# def myfixture():
#'''前置函数，但这个case暂时不用'''
#   access_token = Basic_One().get_token('pytest')['accessToken']

@allure.feature('Test_GetAccessCode接口')
class Test_GetAccessCode(Basic_Two):

    access_token = Basic_One().get_token('pytest')['accessToken']

    @allure.story('获取code')
    @allure.issue('case id：020402')
    @pytest.mark.parametrize(
        'token,result', [
            (access_token, True),
            ('wrong',False)
        ],
        ids=[
            '正确的accesstoken返回成功',
            '错误的accesstoken返回失败'
        ]
    )
    def test_get_access_code(self,token,result):
        response = Basic_Two().get_code(token)
        success = response['success']
        assert success == result


