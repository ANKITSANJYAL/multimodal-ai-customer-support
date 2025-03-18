from transformers import CLIPProcessor, CLIPModel
from PIL import Image

# Load pre-trained CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def analyze_image(image_path, query):
    """
    Analyze an image using CLIP and return the result.
    """
    image = Image.open(image_path)
    inputs = processor(text=query, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    return logits_per_image.argmax().item()

# Example usage
if __name__ == "__main__":
    print(analyze_image("images/product.jpg", "Is this product covered under warranty?"))