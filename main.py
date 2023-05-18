from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_open = filedialog.askopenfilename()


if file_open:
    file_name = file_open.split("/")[-1]
    file_path = "./".join(file_open.split("/")[:-1])

else:
    raise FileNotFoundError("YOu didn't specify the file")

audio = AudioSegment.from_file(file_open)


def audioTrimmer():
    beginning_part = input("Enter the starting of the Sound(in seconds)\n")

    try:
        bp_inMSecs = int(beginning_part) * 1000
    except ValueError:
        print(" Oops ! Please enters numbers in seconds.. Since wrong input , clip will be processed from beginning")
        bp_inMSecs = 0

    ending_part = input("Enter the ending duration of the file(in seconds)\n")

    try:
        ep_inMSecs = int(ending_part) * 1000
    except ValueError:
        print(" Oops ! Please enters numbers in seconds.. Since wrong input , clip will be processed till ending")
        ep_inMSecs = None

    trimmed_audio = audio[bp_inMSecs:ep_inMSecs]

    trimmed_audio.export(file_open[:-4] + "_trimmed.mp3", format="mp3")
    print("Task Completed")
    print(f"Destination Directory is : {file_path} ")


def audio_conv():
    select_format = input("Enter 'W' for wav, 'M' for mp3, 'O' for ogg\n")
    if select_format.upper() == "W":
        dot_pos = file_open.split("/")[-1].find(".")
        final_name = file_open.split("/")[-1][:dot_pos] + ".wav"
        post_format = "wav"
    elif select_format.upper() == "M":
        dot_pos = file_open.split("/")[-1].find(".")
        final_name = file_open.split("/")[-1][:dot_pos] + ".mp3"
        post_format = "mp3"
    elif select_format.upper() == "O":
        dot_pos = file_open.split("/")[-1].find(".")
        final_name = file_open.split("/")[-1][:dot_pos] + ".ogg"
        post_format = "ogg"
    else:
        raise KeyError

    exported_file = file_path + '/' + final_name
    audio.export(exported_file, format=post_format)
    print("Task Completed")
    print(f"Destination Directory is : {file_path} ")


decision = input("Enter 'T' for audio trimming and 'C' for audio converting\n")

if decision.upper() == 'T':
    audioTrimmer()
elif decision.upper() == 'C':
    audio_conv()
