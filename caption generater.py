from transformers import BlipProcessor,BlipForConditionalGeneration
from PIL import Image
import torch
a=BlipProcessor.from_pretrained("salesforce/blip-image-captioning-base")
b=BlipForConditionalGeneration.from_pretrained("salesforce/blip-image-captioning-base")
image_path="C:\\Users\\musun\\OneDrive\\Pictures\\keasava.jpg"
c=Image.open(image_path)
inputs=a(c,return_tensors="pt")
output=b.generate(**inputs)
result=a.decode(output[0],skip_special_tokens=True)
print("Image caption:",result)