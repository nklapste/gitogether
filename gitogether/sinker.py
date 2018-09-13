#!/usr/bin/python
# -*- coding: utf-8 -*-

"""DEC CODE"""

import os
import time

import git

BASE_DIR = "../../../gitdumbtest2"
GIT_REPO_URL = "https://github.com/nklapste/gittestdumb.git"


def main():
    while True:
        os.makedirs(BASE_DIR, exist_ok=True)
        test_repo = git.Repo.init(os.path.join(BASE_DIR, 'empty'))
        try:
            origin = test_repo.create_remote('origin', GIT_REPO_URL)
        except:
            origin = test_repo.remote("origin")

        assert origin.exists()
        assert origin == test_repo.remotes.origin == test_repo.remotes['origin']
        origin.fetch()
        test_repo.create_head('master', origin.refs.master)
        test_repo.heads.master.set_tracking_branch(origin.refs.master)
        test_repo.heads.master.checkout()
        test_repo.index.add(["test.txt"])

        time.sleep(0.5)
        if test_repo.index.diff(test_repo.head.commit):
            print("commiting")
            test_repo.index.commit("ignore")
            origin.push()

        for fetch_info in origin.fetch():

            if test_repo.commit().hexsha == fetch_info.commit.hexsha:
                print("up to date with origin")
            else:
                print("out of date with origin")
                origin.pull()


if __name__ == "__main__":
    main()
