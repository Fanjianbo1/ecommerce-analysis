import pandas as pd
import matplotlib.pyplot as plt

# 读取前10万行数据（避免卡顿）
df = pd.read_csv('UserBehavior.csv', nrows=100000, header=None)
df.columns = ['user_id', 'item_id', 'category_id', 'behavior_type', 'timestamp']

# 统计行为类型
counts = df['behavior_type'].value_counts()
print(counts)

# 画柱状图
counts.plot(kind='bar')
plt.title('用户行为类型分布')
plt.xlabel('行为类型')
plt.ylabel('次数')
plt.show()