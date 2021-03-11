### mysql

#### mysql单机版
```
注意执行 chmod 644 -R ./config 更改配置权限 否则可能无法挂载

1.数据目录挂载
2.配置文件基本调整

```

#### mysql一主一从
- [mysql-master-slave](./mysql-master-slave/master-slave.md) 

```
1.修改mysql主从配置文件
2.编写一键配置主从脚本 
3.主从数据验证sql
```

#### dynamic-datasource-spring-boot-starter 设置读写分离
参考官方: https://github.com/baomidou/dynamic-datasource-spring-boot-starter


#### mycat读写分离配置
参考: https://www.jianshu.com/p/cb7ec06dae05