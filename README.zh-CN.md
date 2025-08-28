[**English Version**](README.md)
# Android应用自动化测试与网络流量捕获工具

一个基于Python的Android应用自动化测试工具，能够自动执行应用操作并捕获相应的网络流量。

## 项目概述

本项目旨在自动化测试Android应用程序并同时捕获其网络流量数据。通过结合uiautomator2、adb和mitmdump工具，项目能够自动执行应用操作（如打开应用、搜索内容等），并同时记录应用的网络通信数据，用于后续分析。

## 主要功能

- Android应用自动化操作（基于uiautomator2）
- 网络流量捕获（使用adb tcpdump）
- HTTPS流量解密（使用mitmdump和SSLKEYLOGFILE）
- 多进程管理与控制
- 支持YouTube和Reddit等应用的自动化测试

## 项目结构

- `main.py` - 主入口文件，用于启动不同应用的测试
- `beans/` - 应用特定的自动化操作实现
  - `youtube.py` - YouTube应用的自动化操作
  - `reddit.py` - Reddit应用的自动化操作
- `utils/` - 工具类
  - `process.py` - 进程管理和流量捕获功能
  - `random_string.py` - 随机字符串生成工具

## 工作原理

1. 启动mitmdump代理服务器并设置SSL密钥日志文件
2. 在Android设备上启动tcpdump进行流量捕获
3. 通过uiautomator2连接设备并执行应用操作
4. 操作完成后终止所有相关进程
5. 生成包含应用操作和对应网络流量的配对数据

### 流量捕获配置
- 确保Android设备已启用开发者选项和USB调试
- 在Android设备上创建pcap目录: `adb shell mkdir -p /data/local/tmp/pcap/`
- 确保设备已安装tcpdump工具并具有执行权限

### process.py中的配置
- `process.py` 中的mitmdump使用了上游代理模式 (`--mode upstream:http://127.0.0.1:7897`)，可以按需求修改代理服务
- SSL密钥日志文件将保存在 `C:/Users/nstl/Downloads/extract/key/` 目录下，可以按照需求更改
- 流量捕获文件(.pcap)将保存在Android设备的 `/data/local/tmp/pcap/` 目录下

## 使用方法
1. 安装mitmproxy中间人环境，并在测试机上安装中间人证书。详细参考：https://docs.mitmproxy.org/stable/
2. 安装uiaotomator2。详细参考：https://github.com/openatx/uiautomator2
3. 编写需要采集的应用的脚本，可以参考beans/youtube.py
4. 运行main.py