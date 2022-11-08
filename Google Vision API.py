import os
import io
from google.cloud import vision_v1
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Cognizant Key.json'


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    compoundString = ''

    print(len(texts))

    for text in texts:
        # print('\n"{}"'.format(text.description))
        compoundString += text.description
        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])

        # print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return compoundString


df = pd.DataFrame(columns=['Time', 'Frame Number', 'Content'])
time = 0

# 17760
# for x in range(10620, 17760, 60):

#     FOLDER_PATH = r'C:\Users\Leon\Desktop\Cognizant\Data\frame' + \
#         str(x) + '.jpg'
#     text = detect_text(FOLDER_PATH)
#     print('type ', type(text), len(text))
#     print(text)
#     print('')
#     text = text.rsplit(' ', 1)[0]
#     print(text)
#     df.loc[time/2] = [str(time), 'Frame: ' + str(x), text]
#     time += 2

# FOLDER_PATH = r'C:\Users\Leon\Desktop\Cognizant\Data\frame12120.jpg'
# detect_text(FOLDER_PATH)

df.to_csv(
    r'C:\Users\Leon\Desktop\Cognizant\data\All Transcriptions\OCR Transcription.csv', index=False)

# df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv')
