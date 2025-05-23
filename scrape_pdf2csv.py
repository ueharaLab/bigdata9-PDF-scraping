from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBox, LTTextLine, LTImage,LTFigure, LAParams, LTTextBoxHorizontal,LTTextContainer,LTChar
import pandas as pd
import codecs
import pickle
import collections

resourceManager = PDFResourceManager()
device = PDFPageAggregator(resourceManager, laparams=LAParams())

with open('cinnamon.pdf', 'rb') as fp:
    interpreter = PDFPageInterpreter(resourceManager, device)
    
    pdf_data=[]
    for i,page in enumerate(PDFPage.get_pages(fp)):
    
    
        interpreter.process_page(page)
        layout = device.get_result()
        print('page:',i+1)                
        

        for k,lobj in enumerate(layout):
            # LTTextContainerの場合だけ標準出力
            
            if isinstance(lobj, LTTextBox):
                print('start -------------------------------------------')
                line=''
                
                for element in lobj:
                    if isinstance(element, LTTextLine):
                        text = element.get_text().strip()
                        bx = element.bbox
                        print(bx,text)
                        line += text +' '
                print('end -------------------------------------------')
                pdf_data.append([i+1,line])
    
    pdf_data_df = pd.DataFrame(pdf_data, columns=['page','sentence'])
    with open("cninnamon.csv", mode="w", encoding="cp932", errors="ignore", newline="") as f:
        pdf_data_df.to_csv(f)  
            
device.close()


