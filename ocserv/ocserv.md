### ocserv vpn
```
官方地址
https://hub.docker.com/r/tommylau/ocserv
https://github.com/wppurking/ocserv-docker
```

基于该项目的docker进行修改
```
# 1.原项目docker-compose不可以使用 修复该BUG
2.支持通过环境变量设置域名 子网等参数
3.更改路由设置 删除翻墙相关的设置
4.优化Dockerfile 使用阿里云镜像下载,删除签名验证部分
5.更换ocserv为获取最新版本
6.增加dbug 日志 方便连接排错
```

更改后的镜像: docker pull younglinuxer/young-ocserv:latest


docker  run --rm  --name ocserv --privileged  -p 1443:443 -v `pwd`/server-cert.pem:/etc/ocserv/certs/server-cert.pem -v `pwd`/server-key.pem:/etc/ocserv/certs/server-key.pem  -e DOMAIN="harbor.youngblog.cc" -e EN_NETWORK="172.17.54.0"  younglinuxer/young-ocserv

新增环境变量解释:
```
DOMAIN:连接vpn的证书
EN_NETWORK: 设置当前路由 一般为当前主机的子网

```

问题记录
```
1.docker-compose 网络存在bug 无法正常使用
2.最新版本使用该镜像编译会有证书报错 gnutls 异常 使用上一个版本 ocserv-1.0.0.tar.xz 
3.运行还是使用docker 运行 将域名证书挂载到对应目录即可
```
