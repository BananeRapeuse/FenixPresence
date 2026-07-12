from PIL import Image
import os
import sys

SCALE = 3

def upscale_png(input_file, output_file):
    img = Image.open(input_file)

    # Garde le canal alpha si le PNG en possède un
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")

    new_size = (
        img.width * SCALE,
        img.height * SCALE
    )

    upscaled = img.resize(new_size, Image.Resampling.LANCZOS)

    upscaled.save(output_file, "PNG")

    print(f"✅ {input_file} -> {output_file} ({new_size[0]}x{new_size[1]})")


def main():
    if len(sys.argv) < 2:
        print("Utilisation : python upscale_png.py image.png")
        print("Ou : python upscale_png.py dossier/")
        return

    target = sys.argv[1]

    if os.path.isfile(target):
        name, ext = os.path.splitext(target)
        upscale_png(target, name + "_x3.png")

    elif os.path.isdir(target):
        output_dir = os.path.join(target, "upscaled")
        os.makedirs(output_dir, exist_ok=True)

        for file in os.listdir(target):
            if file.lower().endswith(".png"):
                input_path = os.path.join(target, file)
                output_path = os.path.join(
                    output_dir,
                    os.path.splitext(file)[0] + "_x3.png"
                )

                upscale_png(input_path, output_path)

        print("\n🎉 Tous les PNG ont été agrandis !")

    else:
        print("❌ Fichier ou dossier introuvable")


if __name__ == "__main__":
    main()