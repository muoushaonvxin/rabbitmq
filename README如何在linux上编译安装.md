#### 在CentOS 6.4上安装python
```shell
[root@zhangyz ~]# yum install zlib zlib-devel
```

#### 安装simplejson

如果机器上python 版本为2.6以下版本会提示You don't appear to havesimplejson.py installed 安装。

下载链接：http://pypi.python.org/packages/source/s/simplejson/simplejson-2.6.1.tar.gz

```shell
[root@zhangyz ~]# tar xvzf simplejson-2.6.1.tar.gz
[root@zhangyz ~]# cd simplejson-2.6.1
[root@zhangyz ~]# python setup.py install
[root@zhangyz ~]# python -V
Python 2.7.5
```
在CentOS 6.4上安装Erlang在安装之前，需要先要安装一些其他的软件，否则在安装中间会出现一些由于没有其依赖的软件模块而失败, 首先要先安装GCC GCC-C++ Openssl等以来模块

```shell
[root@zhangyz ~]# yum -y install make gcc gcc-c++ kernel-devel m4 ncurses-devel openssl-devel  
```

#### 下载Erang源代码文件文件，并对其付权限和解压文件：
```shell
[root@zhangyz ~]# wget http://www.erlang.org/download/otp_src_R16B02.tar.gz
[root@zhangyz ~]# tar -xzvf otp_src_R16B02.tar.gz  /
[root@zhangyz ~]# cd /
[root@zhangyz /]# mv otp_src_R16B02 erlang_R16B   #重命名解压后的文件 
[root@zhangyz /]# mv otp_src erlang_R16B
[root@zhangyz /]# cd erlang_R16B/ 
[root@zhangyz erlang_R16B]# ./configure --prefix=/usr/local/erlang \
--with-ssl \
--enable-threads \
--enable-smp-support \
--enable-kernel-poll \
--enable-hipe
[root@zhangyz erlang_R16B]# make && make install
```
#### 配置erlang环境

```shell
vim /etc/profile 
export PATH=$PATH:/usr/local/erlang/bin
source /etc/profile 
```

测试一下是否安装成功在控制台输入命令 erl

```shell
[root@zhangyz ~]# erl
Erlang/OTP 20 [erts-9.1.2] [source] [64-bit] [smp:1:1] [ds:1:1:10] [async-threads:10] [hipe] [kernel-poll:false]
Eshell V9.1.2  (abort with ^G)
1> 
```

