# SteamTopSellerSpider
  Steam销量榜的爬虫,基于**Python 3**
## 如何使用
   1.从 [这里下载Code](https://github.com/ReeChee7355608/SteamTopSellerSpider) (需安装Python 3)或从[这里下载Release](https://github.com/ReeChee7355608/SteamTopSellerSpider/releases) (Release限Win)
  
   2.从 [这里下载wget](https://ftp.gnu.org/gnu/wget)

   3.将下载的.py(源码)或.exe(Release里)和wget放在同一目录(或把wget放在PATH中)

   4.运行程序
   
   Tips:如果使用源码,请先安装lxml (python -m pip install lxml==3.4.0)

## 常见错误
  ### 1.程序假死

  首先确认wget是否在同一目录或PATH中

  然后确认当前目录能否写入文件

  最后确认[这个XML](https://store.steampowered.com/feeds/weeklytopsellers.xml)能否访问

  如果都不行请提交issues或[发邮件](mailto:reechee7355608@gmail.com)

  ### 2.代码报错

  在确认没有对源码作任何改动的情况下提交issues或[发邮件](mailto:reechee7355608@gmail.com)

  ### 其它错误

  如果上面都没有你的问题

  #### 1.将wget的静默参数(-q)删除,查看报错情况

  #### 2.如果显示结果出错或其它情况,请提交issues或[发邮件](mailto:reechee7355608@gmail.com)

## 已知BUG
  UNKNOWN(欢迎提交BUG!)

## 更新日志
  ### 1.1 2020.10.14
  修复了 UBS-1 显示"™"等特殊字符时会出现乱码
  
  精简了代码
  
  添加了Linux版源码
  
  ### 1.0 2020.10.8
  
  最基础的版本
  
## 开源协议
  [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)  
