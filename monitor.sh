#!/bin/sh
source /etc/profile
ps -fe|grep spider_start_script |grep -v grep
if [ $? -ne 0 ]
then
  echo "start process....."
  nohup python -u spider_start_script.py > run.out 2>&1 &
else
  echo "runing....."
fi



