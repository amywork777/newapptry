#!/usr/bin/env python3
"""
Script to create "T" logo images to replace Omi logos
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_t_logo(width, height, output_path, teal_color="#14B8A6", background="transparent"):
    """Create a "T" logo image"""
    # Create image
    if background == "transparent":
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    else:
        img = Image.new('RGB', (width, height), background)

    draw = ImageDraw.Draw(img)

    # Calculate font size - make it proportional to image size
    font_size = int(min(width, height) * 0.8)

    # Try to use a system font, fallback to default
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/helvetica.ttf", font_size)
        except:
            font = ImageFont.load_default()

    # Calculate text position to center the "T"
    bbox = draw.textbbox((0, 0), "T", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) // 2
    y = (height - text_height) // 2 - bbox[1]  # Adjust for font baseline

    # Draw the "T"
    draw.text((x, y), "T", fill=teal_color, font=font)

    # Save the image
    img.save(output_path, format='PNG')
    print(f"Created {output_path} ({width}x{height})")

def main():
    """Create all the T logo variants"""
    assets_dir = "assets/images"

    # Teal color matching the app theme
    teal_color = "#14B8A6"

    # Logo files to replace (with their dimensions)
    logos_to_create = [
        ("herologo.png", 260, 260),
        ("herologo_v1.png", 260, 260),
        ("herologo_v3.png", 260, 260),
        ("herologo_v4.png", 260, 260),
        ("logo_transparent.png", 500, 500),
        ("logo_transparent_v1.png", 500, 500),
        ("logo_transparent_v2.png", 500, 500),
        ("Logo Text White.png", 500, 200),  # This might be wider/shorter
    ]

    # Create backup directory
    backup_dir = f"{assets_dir}/original_logos_backup"
    os.makedirs(backup_dir, exist_ok=True)

    for filename, width, height in logos_to_create:
        original_path = f"{assets_dir}/{filename}"
        backup_path = f"{backup_dir}/{filename}"

        # Backup original if it exists
        if os.path.exists(original_path):
            if not os.path.exists(backup_path):
                os.system(f'cp "{original_path}" "{backup_path}"')
                print(f"Backed up {filename}")

        # Create new T logo
        create_t_logo(width, height, original_path, teal_color, "transparent")

    print("All T logos created successfully!")
    print(f"Original logos backed up to: {backup_dir}")

if __name__ == "__main__":
    main()