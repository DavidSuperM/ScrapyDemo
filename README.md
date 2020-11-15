# ScrapyDemo

1. 安装python3 (建议安装anaconda3)
2. 安装scrapy及其他代码中需要的包
```
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
// 如果安装的是python2，则可能需要指定scrapy版本，如 pip install scrapy==1.8.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install fake-useragent -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Faker -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install twisted -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install datetime -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install scrapy-fake-useragent -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install scrapy-user-agents -i https://pypi.tuna.tsinghua.edu.cn/simple
```

3. 运行爬虫
```
// 进入项目根目录
cd SpiderDemo
scrapy crawl book_spider
```

3.1 main函数运行爬虫
idea运行main.py

4. 其他说明
4.1 monitor.sh是守护脚本，用以检测脚本是否在后台运行，如果不在，则启动脚本
脚本的内容可以是循环执行爬虫
然后在linux的crontab设置定时一分钟执行一次脚本

4.2 clean_log.sh是情理日志
项目中settings.py定义了日志以天为单位分割日志，所以需要一个脚本定时情理过久的日志文件


#### 如果需要phantomjs来实现截图  
mac安装phantomjs 
```
brew update && brew install phantomjs
phantomjs -v
```
linux安装phantomJs
```
// 找官网下载 
https://bitbucket.org/ariya/phantomjs/downloads/ 
// 设置环境变量
sudo ln -sf /usr/local/app/.local/lib/python2.7/site-packages/phantomjs /usr/local/bin/phantomjs
// linux下phantomjs截图会有字体乱码情况，需要安装下面的字体
yum install bitmap-fonts bitmap-fonts-cjk
```

