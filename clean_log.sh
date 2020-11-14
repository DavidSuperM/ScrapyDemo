#!/bin/sh
for file in `find ./log/ -type f -name "*"`
    do
        local expired_time=$[30*24*60*60]        #此处定义文件的过期时间6天
        local currentDate=`date +%s`            #获取系统时间，所以时间格式为秒
        local modifyDate=$(stat -c %Y $file)    #获取文件修改时间
        local existTime=$[$currentDate-$modifyDate]     #对比时间，算出日志存在时间
        if [ $existTime -gt $expired_time ];
        then
            rm -rf $file    #删除文件
        fi
    done