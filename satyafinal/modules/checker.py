#!/usr/bin/python

import sys
import re
import subprocess
import os
from urllib.parse import urlparse

#Pengecekan dan/ Perbaikan link input
def urlcanon(website):
	if not website.startswith("http"):
		if not website.startswith("www."):
			website = "www." + website
		website = "http://" + website
		print(("## URL diperbaiki : " + website))
	return website


def extract_domain(url):
	uri = urlparse(url)
	domain_name = f"{uri.netloc}"
	return domain_name


# Pembuatan Folder Output
def folder(website):
	outpath = website
	if not os.path.exists(outpath):
		os.makedirs(outpath)
		print(("## Folder terbuat : " + outpath))
	return outpath


# Pengecekan TOR Service 
def checktor():
	checkfortor = subprocess.check_output(['ps', '-e'])

	def findwholeword(w):
		return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

	if findwholeword('tor')(str(checkfortor)):
		print("## Layanan TOR telah berjalan!")
	else:
		print("## Layanan TOR BELUM berjalan!")
		print('## Aktifkan tor menggunakan perintah \'service tor start\'')
		sys.exit(2)

