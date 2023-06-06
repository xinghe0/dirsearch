# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/6 5:17 PM
@Auth ： xinghe
@File ：dirsearch_api.py
@IDE ：PyCharm
@Motto:但行好事，莫问前程
"""
import os
def dirsearch_cmd(path):
    os.system(f'python common/dirsearch/dirsearch.py -l {path} -e "*" -i 200,301,302 --format html -o {path}_dir_result.html')