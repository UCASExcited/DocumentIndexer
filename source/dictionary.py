# -*- coding: utf-8 -*-
__author__ = 'zhsl'


class Dictionary:

    def __init__(self):
        return

    @staticmethod
    def compression(dic_sorted):
        """
        压缩词典
        :param dic_sorted:
        :return:
        """
        ret = ''
        for term in dic_sorted:
            ret += str(len(term))
            ret += term
        return ret

    @staticmethod
    def write_dictionary(dic, file_path):
        """
        把词典从内存写入到磁盘中
        :param dic:
        :param file_path:
        :return:
        """
        dic_compression = Dictionary.compression(dic)
        with open(file_path, 'w') as write_file:
            write_file.writelines(dic_compression)

    @staticmethod
    def read_dictionary(file_path):
        """
        从瓷盘中读取词典到内存中
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as read_file:
            dic_encode = read_file.readline()
        return Dictionary.decompression(dic_encode)

    @staticmethod
    def decompression(dic_encode):
        """
        对词典进行解压缩, 原来是单一字符串的词典压缩,
        一次遍历字符串, 把每个词项独取出来, 构建词典
        :param dic_encode:
        :return:
        """
        ret = []
        len_dic = len(dic_encode)
        i = 0
        len_term = ''
        while i < len_dic:
            while dic_encode[i].isdigit():
                len_term += dic_encode[i]
                i += 1
            len_term = int(len_term)
            ret.append(dic_encode[i:i+len_term])
            i += len_term
            len_term = ''
        return ret


if __name__ == '__main__':
    print Dictionary.decompression('1a2ab3abc')
