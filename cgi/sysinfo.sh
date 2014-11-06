#########################################################################
# File Name: sysinfo.sh
# Author: hao
# mail: haodu@hustunique.com
# Created Time: 2013年09月24日 星期二 12时13分22秒
#########################################################################
#!/bin/sh
echo "Content-type: text/html\r\n"
#echo "" 
echo "<html><head><title>主机监控页面"
echo "</title></head><body>"
#echo "<h1>主机$(hostname)–$(ifconfig eth0 | grep 'inet addr' | awk  -F ":" '{print $2}' | awk -F " " '{print $1}')</h1>"
#echo "" 
#echo "<h1><p><font color="#FF0000" size=5 face="微软雅黑">内存使用</font></h1>" 
#echo "<pre> $(free -m) </pre>"

#echo "<h1><font color="#FF0000" size=5 face="微软雅黑">磁盘使用</font></h1>"
#echo "<pre> $(df -h) </pre>"
#echo "<h1><font color="#FF0000" size=5 face="微软雅黑">端口使用</font></h1>"
#echo "<pre> $(netstat -tunlp) </pre>"
#echo "<center><font color="#FF0000" size=3 face="微软雅黑">当期系统时间$(date +"%Y-%m-%d %H:%M:%S")</font></center>" 
echo "</body></html>"
