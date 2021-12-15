import tkinter as GUI
from takeFramesFromVideo import VideoCapturer

def execute():
    obj = VideoCapturer(videoPath.get())
    obj.start(10, int(timePeriod.get()))






# Create and customize main window
mainWindow = GUI.Tk()
mainWindow.title("Video Capturer")
mainWindow.resizable(False, False)
mainWindow.geometry("400x480+400+50")

label_pathToVideo = GUI.Label(mainWindow,text="Enter the path to \
the video")
label_pathToVideo.pack()

videoPath = GUI.StringVar()
entry_videoPath = GUI.Entry(mainWindow, width=50, textvariable=videoPath)
entry_videoPath.pack()



label_timePeroid = GUI.Label(mainWindow,text="Enter the time peroid between 2 saved images")
label_timePeroid.pack()


timePeriod = GUI.StringVar()
entry_timePeroid = GUI.Entry(mainWindow, width=50, textvariable=timePeriod)
entry_timePeroid.pack()


button_execute = GUI.Button(mainWindow, text="Execute",
command=execute)
button_execute.pack()

mainWindow.mainloop()