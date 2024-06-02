# 实验四：循环码编码器与译码器
import numpy as np


def gf2_div(dividend, divisor):
    # 多项式二进制除法的
    dlen = len(divisor)
    msg_out = dividend.copy()
    for i in range(len(dividend) - len(divisor) + 1):
        if msg_out[i] == 1:
            msg_out[i: i + dlen] ^= divisor
    return msg_out[-(dlen - 1):]  # 返回余数


def encode_7_4(message):
    msg = np.append(message, [0, 0, 0])

    #  (7, 4) 循环码多项式形式: x^3 + x + 1 => [1, 0, 1, 1]
    generator = np.array([1, 0, 1, 1])
    # 计算余数
    remainder = gf2_div(msg, generator)
    # 末尾添加上余数
    codeword = np.append(message, remainder)
    return codeword


def correct_7_4(codeword):
    generator = np.array([1, 0, 1, 1])
    remainder = gf2_div(codeword, generator)
    return remainder


def decode_7_4(codeword):
    correction = correct_7_4(codeword)
    generator = np.array([1, 0, 1, 1])
    # 计算余数
    remainder = gf2_div(codeword, generator)
    if np.count_nonzero(remainder) == 0:
        # 如果全0就是有错
        return codeword[:4], True
    else:
        # 出现错误
        for i in range(7):
            error_vector = np.zeros(7, dtype=int)
            error_vector[i] = 1
            error_correction = correct_7_4(error_vector)
            if np.array_equal(correction, error_correction):
                corrected_codeword = (codeword + error_vector) % 2
                return corrected_codeword[:4], True
        return codeword[:4], False


message = np.array([0, 0, 1, 1])
encoded_message = encode_7_4(message)
print("编码后信息:", encoded_message)

received_message = encoded_message.copy()
decoded_message, is_valid = decode_7_4(received_message)
print("解码后信息:", decoded_message)

# 制造错误
received_message[3] ^= 1


print("收到错误消息", received_message)
decoded_message, is_valid = decode_7_4(received_message)
print("解码后信息:", decoded_message)