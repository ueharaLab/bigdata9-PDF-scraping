import codecs
import pickle
import pandas as pd
import tabula



dfs = tabula.read_pdf("japanese_soy_sauce.pdf",  encoding="cp932",stream=True, pages = 'all')



with codecs.open("scrape_data.csv", "w", "ms932", "ignore") as f: 
    #header=Trueで、見出しを書き出す
    dfs[0].to_csv(f, index=False, encoding="ms932", mode='w', header=True)