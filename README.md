# Genscheme
1.安装依赖库
    
    pip install genson;
    pip install requests;

2.填写接口信息:
  
    #请求接口的host
    HOST = "http://xxx.xxx.xxx"
  
    #请求接口的path和参数
    PATH = "/path?key1=value1&key2=value2"
  
    #请求的方法
    METHOD = "GET"
  
    #生成json文件名字
    NAME = "xxx.json"
 
 3.运行方法
  
    python Genscheme.py
