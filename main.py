from google import genai  # Google GenAI SDK
import os
import json  # for parsing JSON responses
from dotenv import load_dotenv

# Load .env variables (e.g. GEMINI_API_KEY, MainPrompt)
load_dotenv()

# Initialize the client with your API key
client = genai.Client(api_key=os.getenv("geminiApiKey"))

def describe_image(image_path: str) -> str:
    """
    Uploads the image at `image_path` and asks Gemini to describe it.
    Returns the text description.
    """
    # 1) Upload the image and get a file reference
    uploaded = client.files.upload(file=image_path)

    # 2) Build the prompt, falling back to an empty string if MainPrompt isn't set
    prompt = os.getenv("MainPrompt", "")

    # 3) Generate content
    resp = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, uploaded],
    )

    # 4) Return the raw text
    return resp.text()

def detect_object_on_gripper(image_path: str, description: str) -> dict:
    """
    Uses the image description to determine whether the gripper is
    holding an object.
    """
    # Describe the image first
    description = description

    # (Optional) Re-upload the same image, or reuse the upload handle
    uploaded = client.files.upload(file=image_path)

    # Build a more specific prompt, instructing JSON output
    base_prompt = os.getenv("MainPrompt", "")
    prompt = (
        f"{base_prompt}\n"
        f"Object description: {description}\n"
    )

    # Ask Gemini again
    resp = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, uploaded],
    )
    response = resp.text()
    return(response
           )
if __name__ == "__main__":
    # Example: describe a generic object image
    img_path = "images/objectimage.jpg"
    desc = describe_image(img_path)
    print("Image description:\n", desc, "\n")

    # Example: detect whether the gripper is holding something
    img_path = "images/gripper_image.jpg"
    result = detect_object_on_gripper(img_path, desc)
    print("Gripper detection result:\n", result, "\n")
