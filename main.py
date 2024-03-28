import os
import mimetypes
import shutil

def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext

def select_folder():
    folder = input()
    if os.path.isdir(folder):
        return folder
    else:
        return -1

def sorter(folder, terminal_load):

    dir_list = os.listdir(folder)
    dir_list_update = list()

    for entity in dir_list:
        if entity not in ("Folders", "Videos", "Audio", "Photos", "Text & Code", "Documents & Application Files", "Others"):
            dir_list_update.append(entity)

    if len(dir_list_update) != 0:

        # Terminal GUI Initialize Condition
        if terminal_load == 1:
            count = 0
            pbar = "----------"

        for entity in dir_list_update:

            # Terminal GUI Condition
            if terminal_load == 1:
                count += 1
                print(f"\rSorting...|{('#'*(int(count // (len(dir_list_update)/10)))) + pbar[int(count // (len(dir_list_update)/10)):]}|{int(count // (len(dir_list_update)/100))}%", end = "")
            
            if os.path.isfile(f"{folder}\{entity}"):
                transfer_file(folder, entity)
            elif os.path.isdir(f"{folder}\{entity}"):
                transfer_folder(folder, entity)
        return 1
    else:
        return -1

# FOLDER TRANSFER

def transfer_folder(folder, entity):

    if os.path.isdir(f"{folder}\Folders") == False:
        os.mkdir(f"{folder}\Folders")

    transfer_entity(folder, entity, "Folders")

# FILE TRANSFER

def transfer_file(folder, entity):

    mimetypes.init()
    
    VIDEO = tuple(get_extensions_for_type('video'))
    AUDIO = tuple(get_extensions_for_type('audio'))
    IMAGE = tuple(get_extensions_for_type('image'))
    TEXT = tuple(get_extensions_for_type('text'))
    APPLICATION = tuple(get_extensions_for_type('application'))

    if f".{entity.split('.')[-1]}" in VIDEO:
        if os.path.isdir(f"{folder}\Videos") == False:
            os.mkdir(f"{folder}\Videos")
        transfer_entity(folder, entity, "Videos")

    elif f".{entity.split('.')[-1]}" in AUDIO:
        if os.path.isdir(f"{folder}\Audio") == False:
            os.mkdir(f"{folder}\Audio")
        transfer_entity(folder, entity, "Audio")

    elif f".{entity.split('.')[-1]}" in IMAGE:
        if os.path.isdir(f"{folder}\Photos") == False:
            os.mkdir(f"{folder}\Photos")
        transfer_entity(folder, entity, "Photos")

    elif f".{entity.split('.')[-1]}" in TEXT:
        if os.path.isdir(f"{folder}\Text & Code") == False:
            os.mkdir(f"{folder}\Text & Code")
        transfer_entity(folder, entity, "Text & Code")

    elif f".{entity.split('.')[-1]}" in APPLICATION:
        if os.path.isdir(f"{folder}\Documents & Application Files") == False:
            os.mkdir(f"{folder}\Documents & Application Files")
        transfer_entity(folder, entity, "Documents & Application Files")
    
    else:
        if os.path.isdir(f"{folder}\Others") == False:
            os.mkdir(f"{folder}\Others")
        transfer_entity(folder, entity, "Others")
    
# FUNCTIONALITIES

def transfer_entity(folder, entity, dest):

    source_file = f"{folder}\{entity}"
    destination_file = f"{folder}\{dest}"

    cut_paste(source_file, destination_file)

def cut_paste(source, destination):
  """
  Cuts a file or directory (renames and moves) from source to destination using shutil.move()

  Args:
      source: Path to the file or directory to be cut.
      destination: Path to the destination for the cut file or directory.

  Raises:
      OSError: If there are issues during the move operation.
  """
  try:
    shutil.move(source, destination)
  except OSError as e:
    raise OSError(f"Error cutting {source} to {destination}. Reason: {e}")
