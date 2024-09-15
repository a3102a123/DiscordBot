import os

def load_folder(folder_name):
    file_list = os.listdir(folder_name)
    content_dict = dict()
    for file_name in file_list:
        key = file_name.split(".")[0]
        f = open(os.path.join(folder_name, file_name) , 'r')
        content_dict[key] = f.read()
        
    return content_dict
                
            
if __name__ == "__main__":
    load_folder("docs")