'''
Created on 2020/3/24

@author: qi
'''

import requests, json
import pyecharts
import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# get data from api
resp = requests.get("https://lab.isaaclin.cn/nCoV/api/area?latest=1")
data_json=resp.json()
data_global=data_json.get("results")
df_global = pd.read_json(json.dumps(data_global),orient='records')

# select columns
selected_cloumns = ['countryName','provinceShortName','provinceName','confirmedCount','currentConfirmedCount','deadCount','curedCount','updateTime']
# filter and sort data
df_selected_oversea=df_global[df_global.countryName!='中国'][selected_cloumns]
df_sorted_oversea=df_selected_oversea[df_selected_oversea.confirmedCount>1000].sort_values(by='confirmedCount', ascending=False)

# function to plot rose diagram
def plot_rose(item_list, data_list, title_string):
    ziped_item_data_list = [list(z) for z in zip(item_list, data_list)]

    rose_diagram = Pie(init_opts=opts.InitOpts(width='650px', height='650px'))
    rose_diagram.add("", ziped_item_data_list, radius=["40%", "130%"], center=["50%", "70%"], rosetype="area")
    rose_diagram.set_global_opts(title_opts=opts.TitleOpts(title=title_string),
                                 legend_opts=opts.LegendOpts(is_show=False),
                                 toolbox_opts=opts.ToolboxOpts()
                                )
    label_opts = opts.LabelOpts(is_show=True, position="inside", font_size=12, formatter="{b}:{c}人")
    rose_diagram.set_series_opts(label_opts=label_opts)
    rose_diagram.render('{}.html'.format(title_string))
    return rose_diagram

# prepare data to plot
item_oversea_list = df_sorted_oversea['countryName'].values.tolist()
data_oversea_list = df_sorted_oversea['confirmedCount'].values.tolist()
title_string = "rose-diagram"

# plot and save to <title_string>.html
rose2 = plot_rose(item_oversea_list, data_oversea_list, title_string)