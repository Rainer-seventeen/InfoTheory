# 实验二：平均互信息量
import numpy as np


def average_mutual_information(source_probs, channel_probs):
    """平均交互信息量"""
    source_probs = np.array(source_probs)
    channel_probs = np.array(channel_probs)

    # 联合分布概率 P(XY)
    joint_probs = np.zeros_like(channel_probs, dtype=float)
    for i in range(len(source_probs)):
        for j in range(channel_probs.shape[1]):
            joint_probs[i, j] = source_probs[i] * channel_probs[i, j]

    # 边缘分布概率 P(Y)
    marginal_probs_y = joint_probs.sum(axis=0)

    # 存储交互信息量的二维表格
    mi_values = np.zeros(joint_probs.shape)

    # 计算平均交互信息量 I(X;Y)
    ami = 0
    for x in range(joint_probs.shape[0]):
        for y in range(joint_probs.shape[1]):
            if joint_probs[x, y] > 0:  # 避免 log(0)
                # 计算单个交互信息量，存储于mi列表
                mi_values[x, y] = mutual_information(
                    joint_probs[x, y], source_probs[x], marginal_probs_y[y]
                )
                ami += np.log2(joint_probs[x, y]) * mi_values[x, y]
    # mi_values = np.round(mi_values, 5)
    return ami, mi_values


def mutual_information(joint_probs, source_probs, marginal_probs_y):
    """交互信息量"""
    # P(X|Y) / P(X) = P(XY) / (P(X) * P(Y))
    mi = np.log2(joint_probs / (source_probs * marginal_probs_y))
    return mi


# 信源概率分布 P(X)
source_probs = [0.1, 0.2, 0.3, 0.25, 0.15]
# 信道转移概率 P(Y|X)
channel_probs = [
    [0.15, 0.05, 0.25, 0.1, 0.3, 0.15],
    [0.2, 0.1, 0.05, 0.25, 0.15, 0.15],
    [0.1, 0.2, 0.1, 0.1, 0.3, 0.2],
    [0.25, 0.15, 0.1, 0.15, 0.2, 0.15],
    [0.2, 0.1, 0.2, 0.1, 0.1, 0.3],
]

# 计算
ami, mi_values = average_mutual_information(source_probs, channel_probs)
print(f"平均交互信息量：{ami:.4f} bits")
print(f"交互信息量表格：\n{mi_values}")
