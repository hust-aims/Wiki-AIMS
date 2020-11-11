### [TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems](http://download.tensorflow.org/paper/whitepaper2015.pdf)(OSDI '16)   
异构平台的移植性，方便client，master，worker在异构平台上的部署。训练模型通常需要很长时间，无法保证资源的持续可用性，此时需要Borg进行资源的调度与管理。进行资源的调度与管理   
### [PGA: Using Graphs to Express and Automatically Reconcile Network Policies](http://pages.cs.wisc.edu/~akella/papers/pga-sigcomm15.pdf)(SIGCOMM '15)   
网络label的使用，可以基于label value进行访问控制。   
### [Profiling a warehouse-scale computer](http://www.eecs.harvard.edu/~skanev/papers/isca15wsc.pdf)(ISCA '15)   
分析仓库级计算机，对比kernel和Borg的调度器作为应用的的调度，发现Borg 的调度器只占用5%的cycle。感觉是想说明kernel只适合单机，集群计算更需要专用的调度器。   
### [Hawk: Hybrid Datacenter Scheduling](https://www.usenix.org/system/files/conference/atc15/atc15-paper-delgado.pdf)(ATC '15)   
Borg的调度器使用副本机制保证可用性以及扩展性，调度策略类似于Omega的优化并发控制。Hawk提出混合架构(中心化/分布式调度)策略，主要解决高负载的短任务(感觉有点像存储里的小文件写。)   
第一代调度器着重考虑扩展性；第二代包含两层架构，分离应用逻辑和资源分配策略，而中心化的资源分配会成为瓶颈。
