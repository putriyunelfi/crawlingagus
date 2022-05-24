#!/usr/bin/python

import argparse
# TorCrawl Modules
from modules.crawler import crawler
from modules.checker import *

help = '''
Umum:
-h, --help         : Bantuan
-u, --url *.onion  : Untuk menentukan URL awal yang akan di crawl 

Crawler:
-d, --cdepth      : Mengatur tingkat kedalaman crawl (Default: 1)
-p, --cpause      : Untuk mengatur lama waktu pause saat crawling (Default: 0)
'''




def main():
	# inisialisasi nilai default  variabel
	cdepth = 1
	cpause = 0

	parser = argparse.ArgumentParser(
		description="AlphaCrawl.py adalah crawler berbahasa python yang dapat digunakan untuk melakukan crawling pada Darkweb.")

	parser.add_argument(
		'-u',
		'--url',
		help='Untuk menentukan URL awal yang akan di crawl'
	)
	parser.add_argument(
		'-d',
		'--cdepth',
		help='Mengatur tingkat kedalaman crawl (Default: 1)'
	)
	parser.add_argument(
        '-p',
        '--cpause',
        help='Untuk mengatur lama waktu pause saat crawling (Default: 0)'
    )

	args = parser.parse_args()

	# mengubah argumen parser menjadi variabel
	if args.cdepth:
		cdepth = args.cdepth
	if args.cpause:
		cpause = args.cpause

	# Cek Layanan TOR
	checktor()

	# Perbaikan link, pembuatan outpath dan pemanggilan proses crawling
	if len(args.url) > 0:
		global website
		global outpath
		website = urlcanon(args.url)
		outpath = folder(extract_domain(website))
		crawler(website, cdepth, cpause, outpath)
		print(("\n## File hasil berada pada : " + os.getcwd() + "/" + outpath))
		print("\n\n** Proses Crawling Selesai **\n")

if __name__ == "__main__":
    main()
