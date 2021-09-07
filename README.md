# FuckOPPOAI

在models文件夹中下载各种模型。百度云盘链接：https://pan.baidu.com/s/1t4BBqNurCmm6nBNjP7HFeQ 密码：MODE

将比赛数据集放到images目录下，运行cal_likhood.ipynb可以得到一个json，每个键值记录相似度最高的三个图片

crop_image.py 用dlib检测人脸范围，扰动只在检测到的人脸范围内
target_iteration.py 用于构造对抗图片。将比赛图片放到images目录下，python target_iteration.py能得到对抗图片
image_resize.py 将图片调整为原大小