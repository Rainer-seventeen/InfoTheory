# 实验三：汉明码编码与译码
import numpy as np


class Hamming74:
    def __init__(self):
        # 生成矩阵 G
        self.G = np.array(
            [
                [1, 0, 0, 0, 0, 1, 1],
                [0, 1, 0, 0, 1, 0, 1],
                [0, 0, 1, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 1, 1],
            ]
        )

        # 校验矩阵 H
        self.H = np.array(
            [[1, 0, 1, 0, 1, 0, 1],
             [0, 1, 1, 0, 0, 1, 1],
             [0, 0, 0, 1, 1, 1, 1]]
        )

        # 校验表
        self.syndrome_table = {
            (0, 0, 0): -1,  # 没有错误
            (1, 0, 0): 0,
            (0, 1, 0): 1,
            (1, 1, 0): 2,
            (0, 0, 1): 3,
            (1, 0, 1): 4,
            (0, 1, 1): 5,
            (1, 1, 1): 6,
        }

        # # 第二组数据
        # # 生成矩阵 G
        # self.G = np.array(
        #     [
        #         [1, 0, 0, 0, 0, 1, 1],
        #         [0, 1, 0, 0, 1, 0, 1],
        #         [0, 0, 1, 0, 1, 1, 0],
        #         [0, 0, 0, 1, 1, 1, 1],
        #     ]
        # )

        # # 校验矩阵 H
        # self.H = np.array(
        #     [[0, 1, 1, 1, 1, 0, 0],
        #      [1, 0, 1, 1, 0, 1, 0],
        #      [1, 1, 0, 1, 0, 0, 1]]
        # )

        # # 校验表
        # self.syndrome_table = {
        #     (0, 0, 0): -1,
        #     (0, 1, 1): 0,
        #     (1, 0, 1): 1,
        #     (1, 1, 0): 2,
        #     (1, 1, 1): 3,
        #     (1, 0, 0): 4,
        #     (0, 1, 0): 5,
        #     (0, 0, 1): 6,
        # }

    def encode(self, data):
        data = np.array(data)
        encoded = np.dot(data, self.G) % 2
        return encoded

    def decode(self, encoded):
        encoded = np.array(encoded)
        syndrome = np.dot(self.H, encoded) % 2
        syndrome_tuple = tuple(syndrome)

        error_position = self.syndrome_table.get(syndrome_tuple, -1)
        if error_position != -1:
            print(f"第{error_position}位出错,已修正")
            encoded[error_position] = (encoded[error_position] + 1) % 2
        else:
            print("没有出错")

        decoded = encoded[[0, 1, 2, 3]]
        return decoded


if __name__ == "__main__":
    hamming = Hamming74()

    # 编码示例
    data = [1, 0, 1, 1]
    print(f"原消息: {data}")
    encoded_data = hamming.encode(data)
    print(f"（正确）编码后: {encoded_data}")

    # 没有错
    encoded_error0 = encoded_data.copy()
    print(f"（没有错）编码：{encoded_error0}")

    decoded_data0 = hamming.decode(encoded_error0)
    print(f"解码后消息: {decoded_data0}")

    # 一个错
    encoded_error1 = encoded_data.copy()
    encoded_error1[0] = (encoded_error1[0] + 1) % 2
    print(f"（错一位）编码：{encoded_error1}")

    decoded_data1 = hamming.decode(encoded_error1)
    print(f"解码后消息: {decoded_data1}")

    # 两个错
    encoded_error2 = encoded_data.copy()
    encoded_error2[3] = (encoded_error2[3] + 1) % 2
    encoded_error2[4] = (encoded_error2[4] + 1) % 2
    print(f"（错两位）编码：{encoded_error2}")

    decoded_data2 = hamming.decode(encoded_error2)
    print(f"解码后消息: {decoded_data2}")
