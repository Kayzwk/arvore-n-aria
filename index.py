# -*- coding: utf-8 -*-

import json
import os

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def generate_tree(node, prefix, is_last):
    print(prefix + ('└── ' if is_last else '├── ') + node.name)
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        sub_prefix = prefix + ('    ' if is_last else '│   ')
        generate_tree(child, sub_prefix, i == child_count - 1)

# Obter o caminho absoluto para o arquivo test.json
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'dist', 'test.json')

# Abrir e ler o arquivo JSON
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Função para construir a árvore a partir dos dados
def build_tree(data):
    node = Node(data['name'])
    if 'children' in data:
        for child_data in data['children']:
            child_node = build_tree(child_data)
            node.add_child(child_node)
    return node

# Construir a árvore a partir dos dados do arquivo JSON
root = build_tree(data)

# Exibir a árvore n-ária
generate_tree(root, '', True)
