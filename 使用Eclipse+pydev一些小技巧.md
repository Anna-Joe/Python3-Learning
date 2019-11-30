### 目录
[执行python文件时候报错](#执行python文件时候报错)    
[修改新建python文件的时候自动生成的作者信息](#修改新建python文件的时候自动生成的作者信息)

-----
### 执行python文件时候报错
```Python
SyntaxError: Non-UTF-8 code starting with '\xb0' in file
```
在文件最前面添加一行
```
#coding=GBK
#注意不加空格
```


### 修改新建python文件的时候自动生成的作者信息
- Window >> Preferences >> PyDev >> editor >> tmplates
- ![image](https://github.com/Anna-Joe/Python3-Learning/blob/master/%E4%BF%AE%E6%94%B9%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E4%BD%9C%E8%80%85%E4%BF%A1%E6%81%AF.png)
