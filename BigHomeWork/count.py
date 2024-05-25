import string
from collections import Counter
import matplotlib.pyplot as plt


# 读取文本文件内容
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


# 统计字母出现的次数
def count_letters(text):
    text = text.lower()  # 转换为小写
    letters = Counter(c for c in text if c in string.ascii_lowercase)
    return letters


# 计算字母出现的概率
def calculate_probabilities(letter_counts, total_count):
    return {letter: count / total_count for letter, count in letter_counts.items()}


# 绘制柱状图
def plot_probabilities(probabilities):
    # 按概率排序
    sorted_probabilities = dict(
        sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
    )

    letters = list(sorted_probabilities.keys())
    probabilities = list(sorted_probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(letters, probabilities, color="blue")
    plt.xlabel("Letters")
    plt.ylabel("Probability")
    plt.title("Letter Probability Distribution")
    plt.show()


# 主函数
def main(filename):
    text = read_file(filename)
    letter_counts = count_letters(text)
    total_letters = sum(letter_counts.values())
    probabilities = calculate_probabilities(letter_counts, total_letters)
    plot_probabilities(probabilities)


# 示例使用
if __name__ == "__main__":
    filename = "BHW\Origin.txt"  # 替换为你的文件名
    main(filename)
