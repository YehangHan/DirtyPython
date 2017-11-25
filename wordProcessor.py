from google.cloud import translate  
from docx import Document

translate_client = translate.Client()  

target = 'zh-CN'  

document = Document('example.docx')
for para in document.paragraphs:
    text = para.text
    translation = translate_client.translate(text,target_language=target)
    print(u'Text:{}'.format(text))  
    print(u'translation:{}'.format(translation['translatedText']))    
   