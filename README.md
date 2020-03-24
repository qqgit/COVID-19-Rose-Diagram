# COVID-19-Rose-Diagram
Nightingale rose diagram plot for COVID-19，绘制新型冠状病毒肺炎疫情的南丁格尔玫瑰图。

可以参考[用PYTHON绘制海外新冠肺炎疫情的南丁格尔玫瑰图](https://qcloud.fun/2020/03/23/covid-19-rose-diagram-with-python/)。

本项目的代码运行后会生成海外确认人数过千诸国的确诊病例数疫情玫瑰图。
![海外诸国确诊人数玫瑰图](https://github.com/qqgit/COVID-19-Rose-Diagram/blob/master/rose-diagram.PNG)

如果想要生成其他数据（例如显存确诊病例数、治愈人数、死亡人数等）的玫瑰图，只需要稍作修改，选择对应的数据列即可。

# Data Source 数据源
使用BlankerL童鞋提供的[DXY-COVID-19-Data](https://github.com/BlankerL/DXY-COVID-19-Data)作为数据源。
具体来说，是通过其在[isaaclin.cn](https://lab.isaaclin.cn/nCoV/)提供的API接口来获取最新的疫情数据。
![使用的数据示例](https://github.com/qqgit/COVID-19-Rose-Diagram/blob/master/selected-data.PNG)

# Usage 使用
需要安装Python 3、pandas、pyecharts以及jupyter notebook（可选，使用qplot.ipynb时才需要）。
建议直接安装Anaconda，这样Python、pandas和jupyter notebook就全有了，只需要通过pip安装pyecharts：
```
pip install pyecharts
```
两种使用方式，一种是直接下载rose_diagram.py文件，在命令行运行
```
python qplot.py
```
运行之后会在与qplot.py同目录下生成一个html文件，用浏览器打开文件即可看到玫瑰图。

另一种是通过jupyter notebook打开rose_diagram.ipynb，然后逐行运行即可。
![在jupyter notebook中渲染玫瑰图](https://github.com/qqgit/COVID-19-Rose-Diagram/blob/master/rose-diagram-render-notebook.PNG)

推荐使用juypter notebook方式，便于自己发挥。