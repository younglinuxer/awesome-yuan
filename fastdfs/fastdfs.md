### fastdfs

```
FastDFS是一个开源的轻量级分布式文件系统，它对文件进行管理，功能包括：文件存储、文件同步、文件访问（文件上传、文件下载）等，
解决了大容量存储和负载均衡的问题。特别适合以文件为载体的在线服务，如相册网站、视频网站等等。

```
因为独立安装fastdfs 需要重新编译nginx 操作比较繁琐 本篇使用docker安装 会简单很多

文中nginx的端口设置为9999 直接使用ip:9999即可获取资源 可以使用nginx代理9999端口 或者使用cdn配置都可

#### 安装说明
1.修改docker-compose中对应的IP
```
  # docker所在主机的IP地址，默认使用eth0网卡的地址
  - IP=10.1.34.15  #此处修改为主机对应的IP
```

2. 执行docker-compose命令  
```
docker-compose up -d
```
3. 测试fastdfs是否搭建成功
```
docker exec -it fastdfs /bin/bash 
```
```
echo "Hello FastDFS!">index.html
```
```
fdfs_test /etc/fdfs/client.conf upload index.html
```     

#### nginx反向代理fastdfs配置
```
	location ~/group([0-9])/M([0-9])([0-9]) {
	          proxy_http_version 1.1; 
	          proxy_set_header Host $host; 
        	  proxy_set_header X-Real-IP $remote_addr; 
                  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	          proxy_pass http://10.1.34.15:9999;

	}

```