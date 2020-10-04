import zipfile
import sys
import os


def zip_folder(folder_path, output_path):
    """Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.
    """
    parent_folder = os.path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + "\\", "")
                print(f"Adding {absolute_path} to archive.")
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + "\\", "")
                print(f"Adding {absolute_path} to archive.")
                zip_file.write(absolute_path, relative_path)
        print(f"{output_path} created successfully.")
    except IOError as message:
        print(message)
        sys.exit(1)
    except OSError as message:
        print(message)
        sys.exit(1)
    except zipfile.BadZipfile as message:
        print(message)
        sys.exit(1)
    finally:
        zip_file.close()


# TEST
if __name__ == "__main__":
    zip_folder(
        r"D:\[STORAGE]\Software\TrueCrypt", r"D:\[STORAGE]\Software\TrueCrypt.zip"
    )
