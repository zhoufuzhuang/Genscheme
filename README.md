# Genscheme
1.安装依赖库:
    
    pip install genson;
    pip install requests;
    pip install json;
    pip install yaml

2.在request.yaml中填写接口信息:
  
    #请求接口1
    -
        url : "/path?key1=value1&key2=value2"
        method : "GET"
        name: "生成文件名"
    
    #请求接口2
    -
        url : "/path?key1=value1&key2=value2"
        method : "GET"
        name: "生成文件名"
 3.在Genscheme.py修改常量HOST
 
 4.运行方法:
  
    python Genscheme.py
