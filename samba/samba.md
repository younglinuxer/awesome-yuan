### samba 文件共享服务
出处: https://github.com/dperson/samba

#### 运行

```
连接用户名密码及文件夹都为 younglinuxer
docker run -it -p 139:139 -p 445:445 --name samba -d --rm   -v /data/samba:/mount  dperson/samba  -u "younglinuxer;younglinuxer"  -s "younglinuxer;/mount/;yes;no;yes;all;all;all"  -w "WORKGROUP"  -g "force user= younglinuxer"  -g "guest account= younglinuxer"
```

#### 小米电视连接更改为smb1.0协议
```bash
#将协议支持范围缩小到支持 smb1.0 将配置文件中的所有值改为 NT1 windows连接则需要开启smb1客户端
   client max protocol = NT1
   client min protocol = NT1
   server max protocol = NT1
   server max protocol = NT1
   server min protocol = NT1

```