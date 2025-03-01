import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4,5,6,7"

import cv2
import llama
import torch
from PIL import Image
import torchvision.transforms as transforms

device = "cuda" if torch.cuda.is_available() else "cpu"

llama_dir = "/APP/DriveLM/challenge/model_weights/llama_model_weights"

# # choose from BIAS-7B, LORA-BIAS-7B, LORA-BIAS-7B-v21
model, preprocess = llama.load("/APP/DriveLM/challenge/model_weights/LLaMA-Adapter_V2/7fa55208379faf2dd862565284101b0e4a2a72114d6490a95e432cf9d9b6c813_BIAS-7B.pth", 
                               llama_dir, 
                               llama_type="7B", 
                               device=device
)
model.half()
model.eval()

prompt = llama.format_prompt("Please introduce this painting.")
img = Image.fromarray(cv2.imread("/APP/DriveLM/challenge/model_weights/test.png"))

transform_img = transforms.Compose([
        transforms.Resize((224, 224), interpolation=Image.BICUBIC),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.48145466, 0.4578275, 0.40821073], std=[0.26862954, 0.26130258, 0.27577711])])


img = transform_img(img).unsqueeze(0).unsqueeze(0).to(device)

print(img.shape)
result = model.generate(img, [prompt])[0]

print(result)