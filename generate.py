from requests import post
from PIL import Image
from io import BytesIO

user_prompt = input("Enter text to generate image: ")

response = post("https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
                headers= {
                    "Authorization": "Bearer your_hugging_face_api"
                },
                json= {
                    "inputs": user_prompt,
                }
)

img = Image.open(BytesIO(response.content))

img.show()

img.save("output.png")
