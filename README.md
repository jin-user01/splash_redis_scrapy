##### 1.安装工具库：

```
  pip install scrapy_splash
  pip install scrapy
  pip install scrapy_redis
```

##### 2.在pipelines.py中修改保存的路径

##### 3.启动自己的splash服务，将配置文件中的SPLASH_URL修改为自己的路径

##### 4.启动自己的redis服务，将配置文件中的REDIS_URL修改为自己的路径

##### 5.将bailu.py文件中第25行路径作为value添加至redis中，key为py21

##### 6.运行startcmd.py即可

