#!/usr/bin/env python
"""Test Bitly OAuth2 Proxy session"""
from __future__ import print_function
import os
from BitlyOAuth2ProxySession import Session as bses


def main():
    """Do the thing"""
    username = os.environ["GITHUB_USERNAME"]
    password = os.environ["GITHUB_PASSWORD"]
    # Unless you have an LSST account you'd want to change these
    baseurl = "https://logging.lsst.codes/oauth2/start"
    authpage = "https://logging.lsst.codes/app/kibana"
    session = bses.Session(oauth2_username=username,
                           oauth2_password=password,
                           authentication_base_url=baseurl)
    resp = session.get(authpage)
    print(resp)
    if resp.status_code == 200:
        print(resp.content)


if __name__ == "__main__":
    main()
