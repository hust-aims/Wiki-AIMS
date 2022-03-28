# NAS使用说明

## 访问NAS

QuickConnectID：`HUSTSSS-NAS`
网页端DSM, 内网使用https://10.17.21.102:5000, 外网使用http://quickconnect.cn/HUSTSSS-NAS

Windows：使用SMB服务，在资源管理器地址栏中输入：`\\10.17.21.102`，填写自己账号和密码即可

macOS：使用AFP/SMB服务，在访达菜单栏中选择`前往 -> 连接服务器`，点击加号新增`smb://10.17.21.102`或者`afp://10.17.21.102`，填写自己账号和密码即可	



## 文件同步

如果需要将本地文件与NAS进行同步，可使用Synology Drive进行同步，[下载链接](https://www.synology.cn/zh-cn/dsm/feature/drive)



## 共享文件夹说明

组内默认共享文件夹为`HUSTSSS共享文件夹`，用于组内文件共享，例如组内wiki、组会记录等，所有人都有读写权限进行访问。不同的研究小组可以设置自己的共享文件夹进行协同办公。小组自己的共享文件夹只限制总空间配额，不为每个人单独设置配额。



## 空间配额

- 学生默认每人500GB
- 老师默认每人1000GB
- HUSTSSS共享文件夹：总共500GB
- 其余小组共享空间需联系管理员



## 官方文档

1. [DSM文档](https://kb.synology.cn/zh-cn/DSM/help/DSM/MainMenu/get_started?version=7)
2. [使用教程](https://kb.synology.cn/zh-cn/search?sources%5B%5D=tutorial)
