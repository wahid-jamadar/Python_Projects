import os
import shutil


source_dir ="D:\code alpha task automation" # Changes the  directory path

# File_categories to organize files into folders
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

#Create folders if they don't already exist
for folder in file_categories.keys():
    folder_path = os.path.join(source_dir, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

#This function moves the files based on their extensions
def organize_files():
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        #Ignore folders and only work with files
        if os.path.isfile(file_path):
            moved = False
            #Checks the file extension and moves it to corresponding folder
            for folder, extensions in file_categories.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    dest_path = os.path.join(source_dir, folder, filename)
                    shutil.move(file_path, dest_path)
                    moved = True
                    print(f"Moved: {filename} to {folder}")
                    break
            
            # Moves uncategorized files to 'Others' folder
            if not moved:
                others_folder = os.path.join(source_dir, 'Others')
                if not os.path.exists(others_folder):
                    os.mkdir(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved: {filename} to Others")

if __name__ == "__main__":
    organize_files()
    print("File organization complete!")