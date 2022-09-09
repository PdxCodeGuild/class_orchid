import os
import pathlib
from pick import pick
import re
import time

PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "
PIPE = "│"
ELBOW = "└──"
TEE = "├──"

def generate_directory(tree, item, index, len_diritems, prefix, connector):
    tree.append(f"{prefix}{connector} {item.name}{os.sep}")
    if index != len_diritems - 1:
        prefix += PIPE_PREFIX
    else:
        prefix += SPACE_PREFIX
    add_body(tree, item, prefix)
    tree.append(prefix.rstrip())

def add_root(tree, root_directory):
    tree.append(f"{root_directory.name}{os.sep}")
    tree.append(PIPE)

def add_body(tree, root_directory, prefix=""):
    dir_iter = root_directory.iterdir()
    diretory_items = sorted(dir_iter, key=lambda item: item.is_file())
    len_diritems = len(diretory_items)
    for index, item in enumerate(diretory_items):
        connector = ELBOW if index == len_diritems - 1 else TEE
        if item.is_dir():
            generate_directory(
                tree, item, index, len_diritems, prefix, connector)
        else:
            tree.append(f"{prefix}{connector} {item.name}")

def make_tree(root_directory):
    tree = []
    add_root(tree, root_directory)
    add_body(tree, root_directory)
    tree.append('exit')

    return tree

def navigate_tree(path):
    nav_path = []
    nav_path = path.split('\\')
    nav_path = [x + '/' for x in nav_path]
    while True:
        path =  "".join(nav_path)
        root_directory = pathlib.Path(path)
        tree = make_tree(root_directory)
        option, index = pick(tree, directory)
        new_option = re.sub(r"[^a-zA-Z0-9_. ]", "", option).strip()
        back_again = ''
        if option == 'exit':
            break
        if not option.endswith('\\'):
            print('not a directory')
            time.sleep(4)
        elif option == tree[0]:
            nav_path.pop()
        elif option.endswith('\\'):
            nav_path.append(new_option + '/')
        
        

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
directory = f'Entry point is {dirpath}\nin the {foldername} folder.'

try:
    navigate_tree(dirpath)
except Exception as e:
    raise e
