from openai import OpenAI
import requests
import os
from PIL import image

client = OpenAI(api_key=os.getenv("OpenAI_API_KEY", ""))
image_dir = "./images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

prompt = "生成一张孤独摇滚波奇酱的图片"

import re


def main(text: str) -> dict:
    # 提取小节标题，无需任何库
    text_lines = text.splitlines()

    subtitles = []
    for line in text_lines:
        line = line.strip()
        if line.startswith("#### **") and line.endswith("**"):
            title = line[6:-2]
            if title != "引言" and title != "结论":
                subtitles.append(title)
    return {
        "subtiltes": subtitles
    }
