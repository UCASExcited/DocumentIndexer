# -*- coding: utf-8 -*-
__author__ = 'zhsl'
import os
from index import Index
from search import Search
from dictionary import Dictionary
from gama_encode import Gamma

# data_dir
data_dir = os.path.join(os.getcwd(), '../data')

# build index init data
print '\nShakespear-Merchant Information Retrieval'
print 'Begin building index...'
ind = Index(os.path.join(data_dir, 'document'))
ind.build_index()
document_num = ind.get_document_num()
print 'Index creation success!'
inverted_index = Gamma.reade_inverted_index_encode(os.path.join(
                            data_dir, 'index/doc_index_encode'))
dic = Dictionary.read_dictionary(os.path.join(data_dir, 'index/dictionary'))
engine = Search(dic, inverted_index, document_num)

# Main
print """-r: retrieval document.
    e.g: 1. -r able
         2. -r able & above
         3. -r able | above"""
print '-s: document statistics'
print '-q: quit'
while True:
    print 'Please input...'
    input_info = raw_input()
    if input_info[:2] == '-q':
        break
    elif input_info[:2] == '-s':
        ind.get_statistic().display_statistic()
    elif input_info[:2] == '-r':
        engine.search(input_info[3:])
    else:
        print 'Input error!'
print 'Successful exit!'
