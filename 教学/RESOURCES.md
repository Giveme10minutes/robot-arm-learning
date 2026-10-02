# RESOURCES

所有链接均已实际访问验证（2026-09-21）。标注 **[中文]** 为中文内容，**[视频]** 为视频教程。

## 一、环境与 Python 基础（统一用 uv）

| 资源 | 类型 | 说明 |
|---|---|---|
| https://docs.astral.sh/uv/getting-started/installation/ | 官方文档 | uv 安装（macOS/Linux/Windows 各平台命令），**首选** |
| https://docs.astral.sh/uv/guides/projects/ | 官方文档 | uv 项目工作流：`uv init` / `uv add` / `uv run` / `uv sync` |
| https://uv.doczh.com/guides/projects/ | 中文文档 | 上一条的中文版，读起来更快 |
| https://www.cnblogs.com/ymtianyu/p/19361370 | 文章 [中文] | 国内镜像配置（`UV_DEFAULT_INDEX`）、离线安装与加速实践 |
| https://mirrors.tuna.tsinghua.edu.cn/help/pypi/ | 镜像站 | 清华 PyPI 镜像说明，uv 与 pip 都用它加速 |

> 课程统一约定：**用 uv 管理环境**（`uv init` → `uv add` → `uv run`）。工控机上的厂商环境不要用 uv 覆盖。

## 二、OpenCV 与图像处理

| 资源 | 类型 | 说明 |
|---|---|---|
| https://woshicver.com/ | 官方中文文档 | OpenCV-Python 中文官方文档镜像，**首选**。重点看"视频入门""图像阈值""形态学操作""轮廓" |
| https://www.bilibili.com/video/BV1Fo4y1d7JL/ | 视频 [中文] | 黑马程序员《10 小时学会图像处理 OpenCV 入门教程》 |
| https://www.bilibili.com/video/BV1hM4y1M7vQ/ | 视频 [中文] | 《OpenCV-Python 快速入门 30 讲》，单集短，适合碎片时间 |
| https://www.bilibili.com/video/BV1YnELzfEFZ/ | 视频 [中文] | 2025 版 OpenCV 零基础入门到实战（含环境安装配置） |
| https://numpy.net/doc/stable/user/quickstart.html | 官方文档 [中文] | NumPy 快速入门：ndarray、shape、切片、广播 |

> 图像在 NumPy 里就是一个三维数组（高 × 宽 × 通道），OpenCV 读取后通道顺序是 **BGR**（不是 RGB）——这是新手最常见的坑。

## 三、目标检测：YOLO11 推理

| 资源 | 类型 | 说明 |
|---|---|---|
| https://docs.ultralytics.com/zh/ | 官方文档 [中文] | Ultralytics 官方中文文档，**首选**，含快速开始 |
| https://docs.ultralytics.com/zh/modes/predict/ | 官方文档 [中文] | 预测模式：参数、结果解析、画框 |
| https://www.bilibili.com/video/BV1eDy3YCEia/ | 视频 [中文] | 《一小时掌握：YOLOv8 环境安装+推理+自定义数据集+训练》 |
| https://www.bilibili.com/video/BV1zKRYBfE9p/ | 视频 [中文] | YOLOv8 小白入门（内容较新，思路与 YOLO11 一致） |

## 四、数据标注与数据集

| 资源 | 类型 | 说明 |
|---|---|---|
| https://github.com/HumanSignal/labelImg | 代码库 | labelImg 官方仓库（厂商手册指定工具；注意项目已归档，Windows 安装见其 README） |
| https://docs.ultralytics.com/zh/datasets/detect/ | 官方文档 [中文] | **必读**：YOLO 检测数据集目录结构与标签格式（`class cx cy w h` 归一化） |
| https://docs.ultralytics.com/zh/usage/simple-utilities/ | 官方文档 [中文] | 数据集划分、格式转换的小工具 |
| https://roboflow.com/ | 在线平台 | 在线标注 + 自动划分数据集，可作为 labelImg 的替代/补充 |

## 五、模型训练

| 资源 | 类型 | 说明 |
|---|---|---|
| https://docs.ultralytics.com/zh/modes/train/ | 官方文档 [中文] | 训练模式：参数含义、结果目录、指标解读 |
| https://docs.ultralytics.com/zh/guides/model-training-tips/ | 官方文档 [中文] | 训练调参技巧（轮次、批量、增强、小目标） |
| https://docs.ultralytics.com/zh/modes/val/ | 官方文档 [中文] | 验证与指标：mAP、Precision、Recall 怎么读 |

## 六、Jetson Xavier NX 部署（现场主控）

| 资源 | 类型 | 说明 |
|---|---|---|
| https://docs.ultralytics.com/guides/nvidia-jetson/ | 官方文档 | Ultralytics 的 NVIDIA Jetson 完整部署指南（含 PyTorch/TensorRT 安装），**首选** |
| https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html | 官方文档 | NVIDIA 官方 PyTorch for Jetson 说明；国内访问可能较慢，可用上面那条替代 |
| https://forums.developer.nvidia.com/ | 官方论坛 | Jetson 环境问题的搜索入口（多数报错都有人问过） |

> JetPack 6（Ubuntu 22.04）上务必用 **Jetson 专用 PyTorch wheel**，`pip install torch` 装不上可用的 aarch64 版本。

## 七、手眼标定与坐标转换

| 资源 | 类型 | 说明 |
|---|---|---|
| https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html | 官方文档 | `findHomography` 单应矩阵原理与代码（浏览器打开正常，curl 会被拒） |
| https://developer.aliyun.com/article/1461992 | 文章 [中文] | 《详解机械手相机 9 点标定与 5 点圆心标定》，与厂商 `xsl` 标定流程对应 |
| https://www.bilibili.com/video/BV1zg4y1m7By/ | 视频 [中文] | Eye-to-hand 手动标定（标定板多随机位姿） |
| https://www.bilibili.com/video/BV1Rw411d7ch/ | 视频 [中文] | 3D 视觉机器人的手眼标定流程记录 |
| https://develop.realman-robotics.com/AI/developerGuide/hand/ | 厂商文档 [中文] | 睿尔曼 SDK 手眼标定章节，工程实现参考 |

## 八、机械臂控制

| 资源 | 类型 | 说明 |
|---|---|---|
| https://github.com/Dobot-Arm/TCP-IP-Python-V4 | 代码库 | Dobot 官方 Python SDK（TCP/IP），示例含回零、移动、夹爪 |
| https://www.dobot.cn/service/download-center | 官方下载 | Dobot 越疆官方下载中心：SDK、DobotStudio、文档（按实际型号选） |
| https://www.dobot-robots.com/service/faq/455.html | 官方 FAQ | Dobot 二次开发说明 |
| https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p20_communicating_with_serial_ports.html | 文档 [中文] | pyserial 串口通信（若走串口而非 TCP/IP） |
| https://developer.aliyun.com/article/761647 | 文章 [中文] | pyserial 串口通信实践 |

## 九、语音播报与识别

| 资源 | 类型 | 说明 |
|---|---|---|
| https://www.cnblogs.com/sj-max/p/17294332.html | 文章 [中文] | `edge-tts` 文字转语音（免费、中文音色好） |
| https://developer.cloud.tencent.com/article/2419978 | 文章 [中文] | edge-tts 使用说明 |
| https://github.com/openai/whisper | 代码库 | 语音识别（若需识别语音指令） |

## 十、工业相机

| 资源 | 类型 | 说明 |
|---|---|---|
| https://zhaoxuhui.top/blog/2022/05/25/hikcamera-use-and-sdk-notes.html | 文章 [中文] | 海康威视工业相机 SDK 数据获取笔记（与厂商手册中的海康相机对应） |
| https://www.cnblogs.com/gooutlook/p/15240265.html | 文章 [中文] | Ubuntu 下海康 USB 相机图像转 OpenCV |
| https://github.com/xg590/Learn_MV-CS200-10GC | 代码库 | 海康 MV 系列相机采图示例代码 |

## 十一、社区（遇到问题去哪问）

- **赛事技术交流 QQ 群：636734846**（赛项 7、8 共用；组委会与厂商都在）— 器材与赛制问题首选
- https://github.com/ultralytics/ultralytics/issues — YOLO 报错、训练异常的搜索入口
- https://forums.developer.nvidia.com/c/agx-autonomous-machines/jetson-embedded-systems/ — Jetson 环境问题
