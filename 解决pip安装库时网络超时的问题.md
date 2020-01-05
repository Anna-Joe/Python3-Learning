1.使用镜像网站下载python库，可用的镜像网站：
```
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
豆瓣(douban) http://pypi.douban.com/simple/ 
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```

2.使用方法：
```
1 pip install web.py -i http://pypi.douban.com/simple

2 pip install web.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

3.如果觉得上面i两种使用方法麻烦，还修改pip.ini文件的配置：
```
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
``` 
