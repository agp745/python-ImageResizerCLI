import os
import subprocess

# ffmpeg -i imageName.jpg -vf scale=20:-1 imageName-small.jpg

def resize_images(files: list[str], output_folder: str, scale: int):
    try:
        for filename in files:

            if(filename == 'main.py' or filename.startswith('small-')):
                pass

            output_file = f"{output_folder}/small-{filename.split('.')[0]}.jpeg"

            cmd = [
                'ffmpeg',
                '-i', filename,
                '-vf', f"scale={scale}:-1",
                output_file
            ]

            subprocess.run(cmd)

    except subprocess.CalledProcessError as e:
        print("Command failed with error:", e)

if __name__ == "__main__":
    path = os.getcwd()
    directory = os.listdir(path)
    scale = 20

    resize_images(directory, path, scale)