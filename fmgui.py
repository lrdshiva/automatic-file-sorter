import os
import shutil
import PySimpleGUI as sg

source_folder = sg.popup_get_folder('Choose source location:', default_path='')
destination_folder = sg.popup_get_folder('Choose destination folder:', default_path='')
#
# if not img_folder:
#     sg.popup_cancel('Cancelling')
#     raise SystemExit()
#
# img_types = (".png")
#
# file_list = os.listdir(img_folder)
#
# fnames = [f for f in file_list if os.path.isfile(
#     os.path.join(img_folder, f)) and f.lower().endswith(img_types)]
#
# num_files = len(fnames)
#
# if num_files == 0:
#     sg.popup('No files in folder!')
#     raise SystemExit()
#
# del file_list

folders = {source_folder: destination_folder}
file_type = []

def fmGUI():
    layout = [
        [sg.Text("Choose filetype:")],
        [sg.Combo(['.zip', '.png'], key='FILETYPE', enable_events=True)],
        [sg.Ok(), sg.Cancel()]
    ]
    window = sg.Window('Choose filetype to move', layout, default_element_size=(40, 1))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event in 'Ok':
            if values['FILETYPE'] not in file_type:
                file_type.append(values['FILETYPE'])
                filemover()
    window.close()


def filemover():
    source = folders.keys()
    destination = folders.values()
    while True:
        num_files = len(os.listdir(*source))
        if num_files == 0:
            sg.PopupError("No files in folder!")
            raise SystemExit()
        else:
            for file in os.listdir(*source):
                file_ending = str(file_type)[2:-2]
                # "".join(repr(f) for f in file_type)
                # str(file_type)[1:-1]
                if file.endswith(file_ending):
                    result = shutil.move(str(*source) + "/" + file, str(*destination) + "/" + file)
                    is_file_in_curr_dir = os.path.isfile(file)
                    current_dir = os.listdir(*destination)
                    # print(f"File(s) moved to '{str(*destination)}'")
                    if is_file_in_curr_dir not in current_dir:
                        file_type.pop()
        return sg.PopupOK(f"File transfer successful!\nFile(s) moved to '{str(*destination)}'")

fmGUI()