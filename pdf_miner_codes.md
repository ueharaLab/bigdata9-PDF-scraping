# PDF minerコード解説

PDFのオブジェクトマイにPDFMinerのクラスが対応するので、一見そうとう複雑なコーディングに見える
（以下のように多くのクラスをimportする）

```python
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBox, LTTextLine, LTImage,LTFigure, LAParams, LTTextBoxHorizontal,LTTextContainer,LTChar

resourceManager = PDFResourceManager()
device = PDFPageAggregator(resourceManager, laparams=LAParams()) #PDF全体を操作対象の外部デバイスのように見立ててオブジェクトにする

with open('cinnamon.pdf', 'rb') as fp:
    interpreter = PDFPageInterpreter(resourceManager, device) # 外部デバイスをPDFスクレイピングできる状態にする①
   
    for i,page in enumerate(PDFPage.get_pages(fp)):#cinnamon.pdf をページオブジェクトに変換して1ページづつ取り出す
   
        if i+1==3 or i+1==4:
            interpreter.process_page(page)　# ページオブジェクトをinterpreterオブジェクト①でページオブジェクトをスクレイピングする（結果は仮想端末deviceにデータとして保管される）
            layout = device.get_result() # deviceオブジェクトに保管されたスクレイピングデータを取り出す（ページ内のstreamオブジェクトに、文字列のまとまり単位にオブジェクトとして
　　　　　　　　　　　　　　　　　　　保管されるので、リスト型になっている。
            print('page:',i+1)                
           
            for k,lobj in enumerate(layout):# streamオブジェクト内の文字列のまとまり単位オブジェクトを逐次とりだす。
                
                if isinstance(lobj, LTTextBox): # これは、BT~ETのテキストボックスかどうかを判定する条件文（このほかに、イメージや表オブジェクトがありうる）
                    print('start -------------------------------------------')
                    for element in lobj:# さらに、BT-ET内の文字列を1行毎に取り出す
                        if isinstance(element, LTTextLine):#文字列かどうかを確認
                            text = element.get_text()# テキストを取り出す　lxml の　xpathオブジェクト.text_content() とよく似ている
                            x = element.x0　# このテキストのx座標位置を取り出す。
                            print(x,text)
                    print('end -------------------------------------------')

```
参考サイト
https://qiita.com/mczkzk/items/894110558fb890c930b5

https://note.com/kamakiriphysics/n/nd3381b48d4b5

https://www.learning-nao.com/?p=1272

https://note.com/kamakiriphysics/n/nd3381b48d4b5

https://www.shibutan-bloomers.com/python_library_pdfminer-six/2124/

https://stackoverflow.com/questions/65926516/pdfminer-extract-text-behind-ltfigure-object
