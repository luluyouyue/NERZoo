# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

_self_define_words = ["虚拟手机号", "toutiao.user.info"]


def combine_self_define_word(words):
    """
    前项最大匹配算法：
    利用自定义字典修正分词错误，如虚拟 手机号 -> 虚拟手机号, toutiao . user . info -> toutiao.user.info
    """
    if len(words) < 1 or words is None:
        return words

    new_words = []
    start = 0
    max_match = -1
    end = 1
    combine_word = words[start]
    while start < len(words) - 1:
        if end < len(words):
            combine_word = combine_word + words[end]
        else:
            if max_match != -1:
                new_words.append(''.join(words[start:max_match + 1]))
                start = max_match + 1
            else:
                new_words.append(words[start])
                start += 1

            if start >= (len(words) - 1):
                if start == len(words) - 1:
                    new_words.append(words[start])
                break
            end = start + 1
            max_match = -1
            combine_word = words[start] + words[end]

        if combine_word not in _self_define_words:
            end += 1
        else:
            max_match = end
            end += 1
    return new_words


if __name__ == "__main__":
    # 读取第一行的n
    words = ["虚拟", "手机号a"]
    print '#'.join(combine_self_define_word(words))

