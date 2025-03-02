import os

label_base_path = 'labels'
image_base_path = 'images'
transformed_dir_list = os.listdir(f'{label_base_path}\\transformed_files')
image_dir = os.listdir(image_base_path)

keep_classl_list = ['0','7','5']

def list_all_empty_files(directory_files_list: list, base_path):
    empty_files = []
    for file_name in directory_files_list:
        file_path = os.path.join(base_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                read_file = file.read()
                if read_file == '':
                    empty_files.append(file_name)
    return empty_files

def get_all_images(images_directory: list) -> list:
    store_images = list()
    for image in images_directory:
        store_images.append(image)
    return store_images

def remove_ununsed_images(list_of_empty_files: list, list_of_images: list) -> list:
    
    updates_list_of_images = []
    for image in list_of_images:
        image_to_txt_extension = image.replace('.jpg', '.txt')
        if image_to_txt_extension in list_of_empty_files:
            image_path = os.path.join(image_base_path, image)
            os.remove(image_path)
        else:
            updates_list_of_images.append(image)
    return updates_list_of_images

list_of_empty_files = list_all_empty_files(transformed_dir_list, label_base_path)
get_all_images_from_file = get_all_images(image_dir)

remove_ununsed_images(list_of_empty_files, get_all_images_from_file)