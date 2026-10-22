from huggingface_hub import InferenceClient
from datetime import datetime
from config import HF_API_KEY

MODEL="ByteDance/SDXL-Lightning"

client=InferenceClient(api_key=HF_API_KEY)
print("type quit to exit")
while True:
    prompt=input("Enter prompts:").strip().lower()
    if prompt=="quit":
        break
    if not prompt:
        continue
    try:
        print("Generating...")
        image=client.text_to_image(prompt,model=MODEL)
        filename=f"generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image.save(filename)
        image.show()
        print("file saved", filename)
    except Exception as e:
        print("ERROR could not generate image:", e)

print("good bye")
