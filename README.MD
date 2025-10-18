# 使用 Selenium 自动从谷歌学术引用文献
如果你写论文需要引用大量文献，并需要使用谷歌学术获取统一的引用格式 (GB/T 7714)，此程序可帮你自动从谷歌学术上获取文献引用
## Python 开发环境
anaconda3  
conda-25.5.1  
python-3.14

## 安装
爬虫依赖于 Selenium 和 chrome 浏览器，需要安装最新浏览器和对应版本的 Selenium 驱动程序以及 Python 的 Selenium 库

1. Selenium 驱动下载

Chrome：
```
https://googlechromelabs.github.io/chrome-for-testing/
```

2. 克隆存储库
```
git clone https://github.com/CaiWenDa/SearchRefOnGoogleScholar.git
```

3. 将 Selenium 驱动复制到 SearchRefOnGoogleScholar 目录下

4. 安装 Selenium
```
conda create -n scratch
conda activate scratch
conda install conda-forge::selenium
```

## 运行
将需要在谷歌学术上搜索的论文题目保存到 ref_titles.txt 中，每一行一个论文标题
```
python ./SearchGoogleSchoolar.py
```
运行完毕后引用结果输出到 saved_cites.txt 中

## 扩展
如果你需要其他引用格式，请手动修改 SearchGoogleSchoolar.py

## 参阅
[Selenium 文档](https://www.selenium.dev/documentation/)  
[Selenium Python 开发文档](https://selenium-python.readthedocs.io/index.html)