import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体（解决警告和乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 读取数据（前10万行，可根据需要调整）
df = pd.read_csv('UserBehavior.csv', nrows=100000, header=None)
df.columns = ['user_id', 'item_id', 'category_id', 'behavior_type', 'timestamp']

# 1. 基础统计
behavior_counts = df['behavior_type'].value_counts()
print("用户行为分布：")
print(behavior_counts)

# 画柱状图
plt.figure(figsize=(8,5))
behavior_counts.plot(kind='bar', color=['skyblue', 'orange', 'green', 'red'])
plt.title('用户行为类型分布')
plt.xlabel('行为类型')
plt.ylabel('次数')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('images/behavior_dist.png')  # 保存到images文件夹
plt.show()

# 2. 漏斗分析
pv = df[df['behavior_type'] == 'pv']['user_id'].count()
fav = df[df['behavior_type'] == 'fav']['user_id'].count()
cart = df[df['behavior_type'] == 'cart']['user_id'].count()
buy = df[df['behavior_type'] == 'buy']['user_id'].count()

print("\n漏斗分析：")
print(f"点击（pv）: {pv}")
print(f"收藏（fav）: {fav}")
print(f"加购（cart）: {cart}")
print(f"购买（buy）: {buy}")
if pv > 0:
    print(f"浏览→购买转化率: {buy/pv:.2%}")
    print(f"浏览→收藏转化率: {fav/pv:.2%}")
    print(f"浏览→加购转化率: {cart/pv:.2%}")

# 3. 时间趋势分析（按天）
# 将时间戳转换为日期
df['date'] = pd.to_datetime(df['timestamp'], unit='s')
daily_behavior = df.groupby([df['date'].dt.date, 'behavior_type']).size().unstack(fill_value=0)

# 画每日趋势图
plt.figure(figsize=(12,6))
for behavior in ['pv', 'fav', 'cart', 'buy']:
    if behavior in daily_behavior.columns:
        plt.plot(daily_behavior.index, daily_behavior[behavior], label=behavior)
plt.title('每日用户行为趋势')
plt.xlabel('日期')
plt.ylabel('次数')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/daily_trend.png')
plt.show()