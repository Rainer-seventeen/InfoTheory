# 实验一：信息度量与信源编码

import random
from math import log2, ceil
import heapq

# 信源
messages = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
probabilities = [0.1, 0.2, 0.15, 0.05, 0.2, 0.1, 0.1, 0.05, 0.05]


def generate_message(messages, probabilities, length=10):
    """生成消息序列"""
    return random.choices(messages, probabilities, k=length)


def print_info(probabilities):
    """信源信息"""

    # 自信息量
    self_informations = [-log2(p) for p in probabilities]

    # 保留四位小数
    print("自信息量:", end="")
    print([f"{info:.4f}" for info in self_informations])

    # 信源熵
    source_entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    print("信息熵：%f" % source_entropy)

    # 冗余度
    n = len(probabilities)  # 信源长度
    H_max = log2(n)  # 最大信息
    redundancy = H_max - source_entropy
    print("冗余度：%f" % redundancy)


def fano_encoding(messages, probabilities):
    """费诺编码"""

    def fano_recursive(codes, probs, prefix=""):
        if len(codes) == 1:
            return {codes[0]: prefix}
        total = sum(probs)
        accum = 0
        for i in range(len(probs)):
            accum += probs[i]
            if accum >= total / 2:
                break
        left = codes[: i + 1]
        right = codes[i + 1:]
        left_probs = probs[: i + 1]
        right_probs = probs[i + 1:]
        return {
            **fano_recursive(left, left_probs, prefix + "0"),
            **fano_recursive(right, right_probs, prefix + "1"),
        }

    sorted_pairs = sorted(
        zip(messages, probabilities), key=lambda x: x[1], reverse=True
    )
    sorted_messages, sorted_probabilities = zip(*sorted_pairs)
    return fano_recursive(sorted_messages, sorted_probabilities)


def huffman_encoding(messages, probabilities):
    """哈夫曼编码"""

    heap = [[weight, [symbol, ""]]
            for symbol, weight in zip(messages, probabilities)]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huffman_code = sorted(heapq.heappop(
        heap)[1:], key=lambda p: (len(p[-1]), p))
    return {symbol: code for symbol, code in huffman_code}


def shannon_encoding(messages, probabilities):
    """香农编码"""

    sorted_pairs = sorted(
        zip(messages, probabilities), key=lambda x: x[1], reverse=True
    )
    sorted_messages, sorted_probabilities = zip(*sorted_pairs)
    cumulative_prob = 0
    shannon_code = {}
    for message, prob in zip(sorted_messages, sorted_probabilities):
        code_length = ceil(-log2(prob))
        cumulative_code = cumulative_prob
        cumulative_prob += prob
        binary_code = bin(int(cumulative_code * (2**code_length)))[2:].zfill(
            code_length
        )
        shannon_code[message] = binary_code
    return shannon_code


def encoding_info(probabilities, codes):
    """编码信息"""

    # 平均码长
    average_length = sum(
        len(code) * prob for code, prob in zip(codes.values(), probabilities)
    )

    # 信源熵
    source_entropy = -sum(p * log2(p) for p in probabilities if p > 0)

    # 编码效率
    efficiency = source_entropy / average_length

    # 冗余度
    redundancy = 1 - efficiency

    print(f"编码效率：{efficiency:.4f}")
    print(f"冗余度：{redundancy:.4f}")


# 输出信源概率分布
print("<===========信源信息===========>")
msg_source = dict(zip(messages, probabilities))
print(f"概率分布：{msg_source}")

# 信源信息
print_info(probabilities)

# 生成消息序列
sequence1 = generate_message(messages, probabilities, length=10)
print("随机生成长度为10的序列：", sequence1)


# 三大编码输出

huffman_codes = huffman_encoding(messages, probabilities)
print("\n<===========哈夫曼编码===========>")
print(f"编码：{huffman_codes}")
encoding_info(probabilities, huffman_codes)

fano_codes = fano_encoding(messages, probabilities)
print("\n<===========费诺编码===========>")
print(f"费诺编码：{fano_codes}")
encoding_info(probabilities, fano_codes)

shannon_codes = shannon_encoding(messages, probabilities)
print("\n<===========香农编码===========>")
print(f"香农编码：{shannon_codes}")
encoding_info(probabilities, shannon_codes)
