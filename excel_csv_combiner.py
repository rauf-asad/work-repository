import pandas as pd
import os
import PySimpleGUI as sg
sg.theme('Light Blue 2')


path = sg.popup_get_folder('Please select the folder that has your excel and/or csv files', title='Path to Folder?')

counter = 0
for folder, subfolders, files in os.walk(path):
    for file in files:
        if counter == 0:
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join(folder, file))
                counter += 1
            elif file.endswith('.xls') or file.endswith('.xlsx'):
                df = pd.read_excel(os.path.join(folder, file))
                counter += 1
        else:
            if file.endswith('.csv'):
                _ = pd.read_csv(os.path.join(folder, file))
                df = df.append(_, ignore_index=True)
            elif file.endswith('.xls') or file.endswith('.xlsx'):
                _ = pd.read_excel(os.path.join(folder, file))
                df = df.append(_, ignore_index=True)

os.chdir(path)

df.to_csv('merged.csv')
sg.popup('Your file has been merged and saved as merged.csv in your specified path')