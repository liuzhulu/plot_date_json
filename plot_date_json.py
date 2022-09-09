import json
# 数据分析工具
import pandas as pd
#导入绘图module
import plotly.express as px
filename = "eq_data_30_day_m1.json"
with open(filename) as f:
	all_eq_data = json.load(f)

# 创建地震列表
all_eq_dicts = all_eq_data['features']
# 提取标题 震级 位置
mags,titles,lons,lats = [],[],[],[]
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	title = eq_dict['properties']['title']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	titles.append(title)
	lons.append(lon)
	lats.append(lat)

data = pd.DataFrame(
	data = zip(lons,lats,titles,mags),columns = ['longitude','attitude','position','magnitude']
	)
data.head()
figure = px.scatter(
	data,
	x = 'longitude',
	y = 'attitude',
	# labels = {'x':'longitude','y':'attitude'},
	range_x = [-200,200],
	range_y = [-90,90],
	width = 800,
	height = 800,
	title = 'Global Earthquake Scatter Plot',
	# 定制标记尺寸设为震级
	size = 'magnitude',
	size_max = 10,
	color = 'magnitude',
	hover_name = 'position',
	)
# 写入浏览器文件
figure.write_html('global_earthquakes.html')
figure.show()
# print(titles)

# 写到一个新的文件增强可读性
readable_file = "readable_eq_data.json"
with open(readable_file,'w')as f:
	json.dump(all_eq_data,f,indent = 4)