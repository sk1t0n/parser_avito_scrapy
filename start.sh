#!/bin/sh

pages_file="pages.json"
[ -f $pages_file ] && rm $pages_file
data_file="data.json"
[ -f $data_file ] && rm $data_file
python3 -m scrapy runspider spider_pages.py -a search=ps5 -o $pages_file -L WARNING
python3 -m scrapy runspider spider_items.py -a search=ps5 -o $data_file -L WARNING
