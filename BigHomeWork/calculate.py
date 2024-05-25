import string
from collections import Counter
import math

# 读取文本文件内容
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# 统计字母出现的次数
def count_letters(text):
    text = text.lower()  # 转换为小写
    letters = Counter(c for c in text if c in string.ascii_lowercase)
    return letters

# 计算字母出现的概率
def calculate_probabilities(letter_counts, total_count):
    return {letter: count / total_count for letter, count in letter_counts.items()}

# 计算信息熵
def calculate_entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities.values())

# 主函数
def main(filename):
    text = read_file(filename)
    letter_counts = count_letters(text)
    total_letters = sum(letter_counts.values())
    probabilities = calculate_probabilities(letter_counts, total_letters)
    entropy = calculate_entropy(probabilities)
    
    print(f"Letter probabilities: {probabilities}")
    print(f"Information entropy: {entropy}")

# 示例使用
if __name__ == "__main__":
    filename = 'BHW\Origin.txt'  # 替换为你的文件名
    main(filename)
