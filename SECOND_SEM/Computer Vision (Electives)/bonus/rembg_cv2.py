from rembg import remove
import os

def process_folder(input_dir, output_dir):
    """Processes images in a folder and saves the results in a new folder.

    Args:
        input_dir: Path to the input folder.
        output_dir: Path to the output folder.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.jpg', '.JPG', '.png')):
                image_path = os.path.join(root, file)
                relative_path = os.path.relpath(image_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                print(image_path)
                
                with open(image_path, 'rb') as i:
                    print(output_dir+'/'+file)
                    with open(output_dir+'/'+file, 'wb') as o:
                        input = i.read()
                        output = remove(input)
                        o.write(output)

                #remove_background(image_path, output_dir)

# Example usage
input_folder = "/Users/christhaliyath/Google Drive/My Drive/ONGOING_PROJECTS/WOODTECH/JAISON/Original_images/"
output_folder = "/Users/christhaliyath/Google Drive/My Drive/ONGOING_PROJECTS/WOODTECH/Background_removed"
process_folder(input_folder, output_folder)