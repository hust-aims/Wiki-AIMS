2018-12-06
  1. 修改Docker, Containerd在Checkpoint命令中加入prev-image-dir标志，Runc代码中实现容器restore代码，还未调试;
  1. 根据代码执行的路径以及自己添加修改的模块整理输出文档;
  
2018-12-13
  1. 在Docker中的checkpoint命令中加入pre-dump，prev-image-dir标志实现迭代快照，相应的在Containerd，Runc加入一些代码，
     将代码推到CntrLive，CntrLive_Containerd，CntrLive_Runc私有仓库中。其中走过一些挖路和解决一些bug，
     如docker checkpoint create --pre-dump的时候docker-runc进程无法退出，暂时的解决方案是设置进程运行2s后自动化杀掉该进程。
     **还未解决容器网络劫持的问题**。
  2. 修改论文背景和动机
  3. 看了两篇论文的PPT，觉得容器迁移这个点可能不够好，希望能从容器启动慢这部分直接做优化
  4. 看了open-lambda, openwhisk, openFaaS等无服务平台相关介绍
  
2018-12-20
  1. 找到docker-runc进程无法退出的原因并处理，注释掉一些没用的log日志，docker predump的时间少2/3的;
  2. 对比docker run和docker start --checkpoint启动时间，从快照启动时间少20%
  3. 搭建open-lambda平台，想将docker快照的方法引入到无服务器平台中，做好无服务器平台的QoS;
  
2018-12-27
  1. 将原先Docker in Docker的开发环境改成Docker in VM，重新配置虚拟机网络，存储，计算等环境，遇到的额外问题是cannot find -ldevmapper, 这在之前Docker in Docker是不存在的问题, 一直以为是动态链接库的问题，结果在Moby的Issue找到解决方案，要去掉静态链接。
  2. 在两个虚拟机之间迁移容器，虽然可以在功能上实现，但是发现了一个严重的问题就是迁移过来的容器要想启动，必须重启dockerd(因为dockerd需要读取容器的配置信息，这是容器在线迁移和应用程序在线迁移的关键区别)，缺点是1.性能损失;2.影响同VM的其他不相关容器。暂时没有想到解决方案;
  3. 阅读open-lambda代码，发现这方面有很多可以做的点，比如结合docker预拷贝优化容器启动时间，准备接下来这方面的尝试;
  4. 在论文的详细设计部分加入API接口设计部分;

2018-01-03
  1. 和童老师交流接下来的研究工作，确认一些时间点；阅读sock的related work<<Occupy the Cloud: Distributed Computing for the 99%>>和<<Pipsqueak: Lean Lambdas with Large Libraries>>

2018-01-10
  1. 阅读openwhisk相关[博客](https://medium.com/openwhisk/squeezing-the-milliseconds-how-to-make-serverless-platforms-blazing-fast-aea0e9951bd0)两篇，理解**冷启动**，**预热启动**和**热启动**的区别，搭建openwhisk环境并测试容器冷启动时间即：测试对比nodejs6action, python3action, java8action的Docker run与Docker start --checkpoint性能，发现两者差异不大，之前看过IBM的测试报告两者差十倍，写了封email过去问是否做优化，自己暂时还没有找到原因
  2. 容器化[parsec](https://github.com/Spirals-Team/benchmark-containers)负载镜像过大，试图利用[docker-slim](https://github.com/docker-slim/docker-slim)将容器镜像缩小，结果失败
  3. 阅读论文《Encoding, Fast and Slow:Low-Latency Video Processing Using Thousands of Tiny Threads》(NSDI '17),主要介绍如何利用无服务器平台优化视频处理延迟，阅读论文《SOCK: Rapid Task Provisioning with Serverless-Optimized Containers》(ATC '18)工作细节, 他用的NVMe SSD做的测试。
  
2018-01-17
  - 以上是上周的内容，Mike给我回信说用的是docker-17, criu-3.10版本，没有做优化，我根据他的提示做测试仍然发现两者性能相差不大，分析代码执行路径，从docker, docker-containerd, docker-runc一直跟到criu, 发现时间开销在criu, 其中三处关键的性能瓶颈（进程间通信开销70ms, mount挂载额外20ms开销，网络解锁额外20ms开销），在确定第一处瓶颈出现困难;
