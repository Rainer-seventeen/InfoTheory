import string
from collections import Counter

# 英文字母频率表
english_letter_freq = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074
}

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
    return {letter: count / total_count * 100 for letter, count in letter_counts.items()}

# 解密函数
def decrypt_text(encrypted_text, decryption_map):
    result = []
    for char in encrypted_text:
        if char.lower() in decryption_map:
            if char.isupper():
                result.append(decryption_map[char.lower()].upper())
            else:
                result.append(decryption_map[char])
        else:
            result.append(char)
    return ''.join(result)

# 主函数
def main(encrypted_filename, decrypted_filename):
    # 读取加密文本
    encrypted_text = read_file(encrypted_filename)
    
    # 统计加密文本中的字母频率
    letter_counts = count_letters(encrypted_text)
    total_letters = sum(letter_counts.values())
    encrypted_probabilities = calculate_probabilities(letter_counts, total_letters)
    
    # 对提供的频率表和计算得到的频率进行排序
    sorted_english_freq = sorted(english_letter_freq.items(), key=lambda item: item[1], reverse=True)
    sorted_encrypted_freq = sorted(encrypted_probabilities.items(), key=lambda item: item[1], reverse=True)
    
    # 建立解密映射表
    decryption_map = {enc_letter: eng_letter for (enc_letter, _), (eng_letter, _) in zip(sorted_encrypted_freq, sorted_english_freq)}
    
    # 解密文本
    decrypted_text = decrypt_text(encrypted_text, decryption_map)
    
    # 写入解密后的内容到新文件
    write_file(decrypted_filename, decrypted_text)
    print(f'File "{encrypted_filename}" has been decrypted and saved as "{decrypted_filename}".')

# 写入文件内容
def write_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# 示例使用
if __name__ == "__main__":
    encrypted_filename = 'BHW\Encode.txt'  # 替换为你的加密文件名
    decrypted_filename = 'BHW\Decode.txt'  # 替换为你的解密后输出文件名
    main(encrypted_filename, decrypted_filename)
