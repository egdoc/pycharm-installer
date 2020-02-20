#!/usr/bin/env python3
import sys
import tarfile

from urllib.request import urlopen
from xml.etree import ElementTree as ET

APPLICATIONS_XML = "https://www.jetbrains.com/updates/updates.xml"
DOWNLOAD_URL = "https://download.jetbrains.com/python/pycharm-community"
CHANNEL = "PC-PY-RELEASE-licensing-RELEASE"

if __name__ == '__main__':
    with urlopen(APPLICATIONS_XML) as xml:
        tree = ET.parse(xml)
        latest_pycharm = tree.find(f".//channel[@id='{CHANNEL}']/build").get('version')

    print(f"Downloading and extracting pycharm {latest_pycharm}", file=sys.stderr)
    with urlopen(f"{DOWNLOAD_URL}-{latest_pycharm}.tar.gz") as response:
        with tarfile.open(fileobj=response, mode="r:gz") as tarball:
            for member in tarball:
                namesplit = member.name.split("/")
                namesplit[0] = "pycharm"
                member.name = "/".join(namesplit)
                tarball.extract(member)
