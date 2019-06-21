# -*- cocoding:utf-8 -*-
from tqdm import tqdm, tnrange, tqdm_notebook
from time import sleep

item = ["aaa", "bbb", "ccc", "ddd", "eee"]
for i in tqdm(item, desc="1nd loop"):
    for j in tqdm(item, desc="2nd loop", leave=False):
        sleep(1)
        print(j)
