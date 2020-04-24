"Convert txt files to npy."

import os
from multiprocessing.dummy import Pool
import numpy as np

SRC_DIR = "../data/telco/txt"
DST_DIR = "../data/telco/npy"


def convert_file(f):
    basename = f.split(".")[0]
    src = os.path.join(SRC_DIR, f)
    dst = os.path.join(DST_DIR, basename + ".npy")
    with open(src) as f:
        data = np.genfromtxt(f, delimiter="\t")
    np.save(dst, data)


if __name__ == "__main__":
    files = os.listdir(SRC_DIR)
    with Pool(4) as p:
        p.map(convert_file, files)