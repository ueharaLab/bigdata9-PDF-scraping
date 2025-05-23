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
    
    for i,page in enumerate(PDFPage.get_pages(fp)):
    
        if i+1==3 or i+1==4:
            interpreter.process_page(page)
            layout = device.get_result()
            print('page:',i+1)                
            
            for k,lobj in enumerate(layout):
                # LTTextContainerの場合だけ標準出力
                if isinstance(lobj, LTTextBox):
                    print('start -------------------------------------------')
                    for element in lobj:
                        if isinstance(element, LTTextLine):
                            text = element.get_text()
                            bx = element.bbox
                            print(bx,text)
                    print('end -------------------------------------------')
                '''
                elif isinstance(lobj, LTFigure):
                    for element in lobj:
                        if isinstance(element, LTImage):
                            text = element.get_text()
                            print('figure',text)
                    print('figure-------------------------------------------')
                '''
            '''
            if isinstance(lt, LTTextContainer) :
                
                
                line = lt.get_text().lstrip().replace('\n',' ').replace(' ','')#.strip()
                print(line)
            if isinstance(lt,LTFigure):

                ine = lt.get_text().lstrip().replace('\n',' ').replace(' ','')#.strip()
                print(line)
            '''
device.close()


