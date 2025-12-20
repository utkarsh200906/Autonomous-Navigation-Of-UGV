import os
import json
import base64
from PIL import Image, ImageDraw
import io

json_folder = r"C:\Users\utkar\Downloads\Archive\label"
output_folder = r"C:\Users\utkar\Downloads\Archive\Final"

os.makedirs(output_folder, exist_ok=True)

# Fixed colors for labels (you can expand)
DEFAULT_COLOR = (255, 0, 0)  # red

for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        json_path = os.path.join(json_folder, filename)
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        base_name = os.path.splitext(filename)[0]

        # Load image
        imageData = data.get("imageData")
        if imageData:
            image = Image.open(io.BytesIO(base64.b64decode(imageData)))
        else:
            image_path = data.get("imagePath")
            if image_path:
                image_path_full = os.path.join(json_folder, image_path)
                image = Image.open(image_path_full)
            else:
                print(f"No image found in {filename}")
                continue

        # Draw labeled polygons
        draw = ImageDraw.Draw(image)
        for shape in data.get("shapes", []):
            points = shape.get("points", [])
            if not points:
                continue

            # Always use default color (or generate your own per label)
            label_color = DEFAULT_COLOR

            polygon = [(x, y) for x, y in points]
            draw.line(polygon + [polygon[0]], fill=label_color, width=2)

        # Save labeled image
        output_path = os.path.join(output_folder, base_name + "_label.jpg")
        image.convert("RGB").save(output_path, "JPEG")
        print(f"Saved labeled image: {output_path}")

print("All JSON files processed!")
