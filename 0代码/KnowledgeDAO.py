# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:43:47 2023

@author: shuliu586_1247163556
"""
import json
import os

#读取和保存json文件

def load_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_jsonl(data, jsonl_file):
    with open(jsonl_file, 'w', encoding='utf-8') as file:
        for entry in data:
            json.dump(entry, file, ensure_ascii=False)
            file.write('\n')

def save_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def load_json_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                json_obj = json.loads(line)
                data.append(json_obj)
            except json.JSONDecodeError:
                pass
    return data
        
#统计汉字数，按json文件或string统计，注意不是jsonl文件

def count_chinese_chars(jsonl_file):
    chinese_char_count = 0
    with open(jsonl_file, 'r', encoding='utf-8') as file:
        for line in file:
            json_obj = json.loads(line)
            for key, value in json_obj.items():
                if isinstance(value, str):
                    chinese_char_count += count_chinese_chars_in_string(value)
    return chinese_char_count

def count_chinese_chars_in_string(string):
    count = 0
    for char in string:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count

#合并与拆分json文件，注意不是jsonl文件
def merge_json(folder_name):
    input_folder = folder_name
    files = os.listdir(input_folder)
    
    merged_data = []
    
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(input_folder, file)
            data = load_json(file_path)
            merged_data.extend(data)
    return merged_data

def split_json(json_file,size):
    result = load_json(json_file)
    chunk_size = size  # 每个文件保存的元素数量
    num_files = len(result) // chunk_size + 1  # 计算需要创建的文件数量
    
    for i in range(num_files):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        chunk_data = result[start_index:end_index]
    
        file_name = f"data_{i+1}.jsonl"  # 文件名格式为data_1.jsonl, data_2.jsonl, ...
        with open(file_name, "w") as file:
            for item in chunk_data:
                json.dump(item, file)
                file.write("\n")
