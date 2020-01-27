# 残酷刷题

每天完成一道题，每天的截止时间20：00

## 如何加入

微信号添加：hjyyizi

## T人规则

连续三天不打卡，T人。准确来说是第三天过24点之后，仍然没有完成三天前的任何一道题。

举个例子：

```python
if 小黑22号没有刷 & 23号没有刷 & 24号20点过后仍然没有刷过22，23，24号的任何一道题：
	小黑被T
else:
  小黑侥幸活过来
```

T人的脚本你可以在github仓库中：https://github.com/JyiHUO/2020_qiuzhao。找到

## 代码提交

完成题目的代码需要提交到leetcode的同时也需要提交到github仓库上，方便统计。

github仓库：https://github.com/JyiHUO/2020_qiuzhao

**文件命名规范：leetcode id + leetcode题号。**

举个例子：

红色圈圈的是你的leetcode id

![image-20200121220805797](/Users/huojunyi/Library/Application Support/typora-user-images/image-20200121220805797.png)

红色圈圈是第一题，名字叫Two Sum

![image-20200121220951970](/Users/huojunyi/Library/Application Support/typora-user-images/image-20200121220951970.png)

那么你当天提交的文件名是：

* biss_1.py(如果你是用python写的话)
* biss_1.cpp(如果你是用cpp写的话)
* ...

**如何提交到github上**

假如你电脑上没有该github仓库：

```shell
git clone https://github.com/JyiHUO/2020_qiuzhao.git
```

加入有github仓库了，你需要更新该仓库：

```shell
git pull
```

接着，找到当天日期的文件夹（假如是2020_01_21）：

![image-20200121222212445](/Users/huojunyi/Library/Application Support/typora-user-images/image-20200121222212445.png)

将你的代码添加到该文件夹里面：

![image-20200121222322224](/Users/huojunyi/Library/Application Support/typora-user-images/image-20200121222322224.png)

返回到父目录中，使用以下代码更新仓库，并推送到服务器：

```shell
git add -A
git commit -m "your description"
git push origin master
```

