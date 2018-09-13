#!/usr/bin/python
# -*- coding: utf-8 -*-

"""DEC CODE"""

import os
from git.repo import Repo
import time

BASE_DIR = "../../../gitdumbtest"
while True:
    bare_repo = Repo(os.path.join(BASE_DIR, 'test-repo'))
    # bare_repo.create_remote("origin", "https://github.com/nklapste/gittestdumb.git")
    origin = bare_repo.remote("origin")
    origin.set_url("https://github.com/nklapste/gittestdumb.git")

    index = bare_repo.index
    index.add(["test.txt"])
    time.sleep(0.5)
    if bare_repo.index.diff(bare_repo.head.commit):
        print("commiting")
        index.commit("ignore")
        origin.push()

    for fetch_info in origin.fetch():

        if bare_repo.commit().hexsha == fetch_info.commit.hexsha:
            print("up to date with origin")
        else:
            print("out of date with origin")
            origin.pull()
