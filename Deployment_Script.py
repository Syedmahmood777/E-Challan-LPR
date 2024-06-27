
import string
import cv2
from ultralytics import YOLO
import easyocr
from google.cloud import storage
import base64



from PIL import Image
import numpy as np
import requests


def format_license(text):


    """
    Formatting license plate as per Indian Standards to optimize character recogniton

    Indian License Plates follow a format of :
    XX01 YY 1234

    XX -> State in which the car is registered
    01-> Specific District Number
    YY 1234-> Random Alphanumeric Number


    """

    if len(text)!=10:
        return False

    license_plate_ = ''





    mapping = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char,
               2: dict_char_to_int, 3: dict_char_to_int, 6:dict_char_to_int, 7: dict_char_to_int, 8: dict_char_to_int, 9: dict_char_to_int}

    for j in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if text[j] in mapping[j].keys():
            license_plate_ += mapping[j][text[j]]
        else:
            license_plate_ += text[j]

    return license_plate_





#Mappin Dictionaries
dict_char_to_int={'O':'0',
                  'I':'1',
                  'J':'3',
                  'A':'4',
                  'G':'6',
                  'S':'5',
                  'Z':'2',
                  'U':'1',
                  'Q':'0'}

dict_int_to_char={'0':'O',
                  '1':'I',
                  '3':'J',
                  '4':'A',
                  '6':'G',
                  '5':'S'}


def license_complies_format(text):


    if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and\
       (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and\
       (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
       (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
       (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
       (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
       (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
       (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
       (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
       (text[9] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()):

        return text



def read_ls_plate(lplate_thresh):
    reader=easyocr.Reader(['en'])

    detections=reader.readtext(lplate_thresh)

    if(len(detections)==0):
      detections=reader.readtext(lplate_thresh)
      return "None Detected",0

    for detection in detections:
        bbox,text,score=detection
        text=text.upper().replace(' ','')
        text=text.upper().replace('.','')
        text=text.upper().replace('-','')
        text=text.upper().replace('`','')
        text=text.upper().replace('!','')
        text=text.upper().replace('@','')
        text=text.upper().replace('#','')
        text=text.upper().replace('$','')
        text=text.upper().replace('%','')
        text=text.upper().replace('^','')
        text=text.upper().replace('&','')
        text=text.upper().replace('*','')
        text=text.upper().replace('(','')
        text=text.upper().replace(')','')
        text=text.upper().replace('-','')
        text=text.upper().replace('_','')
        text=text.upper().replace('+','')
        text=text.upper().replace('=','')
        text=text.upper().replace('|','')
        text=text.upper().replace(']','')
        text=text.upper().replace('}','')
        text=text.upper().replace('[','')
        text=text.upper().replace('{','')
        text=text.upper().replace('(','')
        text=text.upper().replace(';','')
        text=text.upper().replace(':','')
        text=text.upper().replace(',','')
        text=text.upper().replace('.','')
        text=text.upper().replace('<','')
        text=text.upper().replace('>','')
        text=text.upper().replace('/','')
        text=text.upper().replace('?','')
        text=text.upper().replace('"','')
        text=text.upper().replace("'",'')
        text=text.upper().replace('~','')


        dummy=format_license(text)


        if dummy:
            return license_complies_format(dummy),score
        else:
            return  "None Detected",21

def predict_fn(request):

    request_json=request.get_json()
    storage_client=storage.Client()
    bucket=storage_client.get_bucket('ec_lpr')
    blob_model=bucket.blob('models/model1.pt')
    blob_model.download_to_filename('/tmp/model1.pt')

    model=YOLO('/tmp/model1.pt')


    image_base64=request_json['image']
    # response = requests.get(url)
    # img_array = np.array(bytearray(response.content), dtype=np.uint8)
    # source = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if(image_base64.startswith('data:image')):
        image_base64=image_base64.split(',')[1]

    img_data=base64.b64decode(image_base64)
    image_np=np.frombuffer(img_data,dtype=np.uint8)
    source=cv2.imdecode(image_np,cv2.IMREAD_COLOR)



    #Detect License Plates
    results=model(source)[0]

# Cropping and Processing detected plates
    for result in results.boxes.data.tolist():

        #Cropping
        x1,y1,x2,y2,score,class_id=result


        #Cropped Image
        lplate_crop=source[int(y1):int(y2),int(x1):int(x2),:]


        #Processing & Threshold
        lplate_gray=cv2.cvtColor(lplate_crop,cv2.COLOR_BGR2GRAY)
       

        lplate_text,lplate_score=read_ls_plate(lplate_crop)
        return lplate_text

        



