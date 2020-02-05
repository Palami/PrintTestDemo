import os
import shutil

os.chdir('C:/Users\Administrator\PycharmProject\PrintTestDemo\TestCase')   #cd到case目录
os.system('pytest --alluredir C:/Users\Administrator\PycharmProject\PrintTestDemo/report/result')  #运行用例保存用例执行数据
shutil.rmtree('C:/Users\Administrator\PycharmProject\PrintTestDemo/report/report')   # 递归删除report文件夹为下次生成清理数据
os.system('allure generate C:/Users\Administrator\PycharmProject\PrintTestDemo/report/result -o C:/Users\Administrator\PycharmProject\PrintTestDemo/report/report')   #生成HTML报告

