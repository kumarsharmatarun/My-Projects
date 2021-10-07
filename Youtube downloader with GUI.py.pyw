import threading
import time
from tkinter import *
from pytube import YouTube
import os,requests
from pathlib import Path
import tkinter.messagebox as tmsg
from threading import Thread
home = str(Path.home())
# print(home)
os.chdir(home)


def mydownloades():
    os.chdir(f"{home}\YoTUBE Downloader")

    path = os.getcwd()
    import subprocess
    subprocess.Popen(f'explorer {path}')

def quiter():
    quit()
def helpwindow():
    helpw = Tk()
    helpw.geometry("1080x1980")
    helpw.title("YoTUBE Help")
    helpw.minsize(1080, 1980)
    maxwidth = helpw.winfo_screenwidth()
    maxheight = helpw.winfo_screenheight()
    helpw.maxsize(maxwidth, maxheight)
    helpw.configure(bg="grey")
    l1 = Label(helpw, text="How it Works", font="verdana 40 bold", fg="gold", bg="grey")
    l1.pack()
    space = Label(helpw, text="")
    space.pack()
    l2 = Label(helpw, text="What is URL:", font="helvetica 30 bold", fg="orange",bg="grey")
    l2.pack(anchor="w", fill=X)

    l3 = Label(helpw, text="URL is a specific link of a video on youtube. Every\n"
                          " video on youtube has a unique URL from which all users\n "
                          "of youtube can access that video. ", font="Helvetica 18 bold", fg="black")
    l3.pack()
    sapce1 = Label(helpw, text="")
    sapce1.pack()
    l4 = Label(helpw, text="How to get URL of any video:", font="Helvetica 30 bold", fg="orange",bg="grey")
    l4.pack(anchor="w", fill=X)
    l5 = Label(helpw, text="To get a URL of any video on Youtube follow the steps below:\n"
                          "\n1. Open youtube on any browser like (Chrome,Firefox,Edge etc)\n"
                          "\n2. Play any video on Youtube which you want to download \n"
                          "\n3. Now on the Top in browser there is a box where URL is present\n"
                          "\nlike 'https://www.youtube.com/watch?v=CHjbJ9OirO4'  \n"
                          "\n4. Now Copy that link and paste in the YoTUBE software  \n"
                          "\n5. Click on Download Button  \n"
                          "\nBoom your video is downloaded as soon as possible\n", font="Helvetica 18 bold", fg="black")
    l5.pack()
    helpw.mainloop()


def aboutwindow():
    about = Tk()
    about.geometry("800x600")
    about.title("About YoTUBE")
    about.minsize(800, 600)
    about.configure(bg="grey")
    maxwidth = about.winfo_screenwidth()
    maxheight = about.winfo_screenheight()
    about.maxsize(maxwidth, maxheight)
    l1 = Label(about, text="About the Software.", font="Verdana 35 bold", fg="orange", bg="grey")
    l1.pack(fill=X)
    sapce1 = Label(about, text="")
    sapce1.pack()
    l2 = Label(about, text="Thank You for using YoTUBE\n"
                           "This software 'YoTUBE' is a property of 'Warm Creators' \n"
                           "This Software is made for Education purposes only \n"
                           "and does not promoting any illigal activities \n"
                           "please use the software wisely we are not responsible\n"
                           "for any Non-Educational use of that software. If you have any\n"
                           "Doubt,Suggestions, or any Complaints regarding the software \n"
                           "please write us on:\n", font="Helvetica 20 ", fg="white",bg="grey")
    l2.pack()
    l3 = Label(about, text="Warmcreators@gmail.com", font="verdana 25 bold ", fg="orange",bg="grey")
    l3.pack()


def main():
    urltocheck = "http://www.kite.com"
    timeout = 5
    global connection
    try:
        request = requests.get(urltocheck, timeout=timeout)
        connection=True
    except (requests.ConnectionError, requests.Timeout) as exception:
        connection=False
    try:
        os.chdir(f"{home}\YoTUBE Downloader")
    except Exception as ee:
        os.chdir(home)
        os.mkdir("YoTUBE Downloader")
        os.chdir(f"{home}\YoTUBE Downloader")
    global root
    root = Tk()
    root.title("YoTUBE ")
   
    maxwidth = root.winfo_screenwidth()
    maxheight = root.winfo_screenheight()
    os.chdir(f"{home}\YoTUBE Downloader")

    aaa = os.listdir()
    if len(aaa) < 10:

        root.geometry("1000x600")


    else:

        root.geometry(f"{maxwidth}x{maxheight}")

    root.minsize(800, 700)
    root.maxsize(maxwidth, maxheight)
    f1 = Frame(root, bg="grey", borderwidth=2)
    f1.pack(side=TOP, fill=X)
    logo = Label(f1, text="Welcome to YoTUBE Video Downloader ", fg="black", font="verdana 30 bold", pady=22,
                 bg="lightblue")
    logo.pack(fill=X)
    mymenu = Menu(root)
    mymenu.add_command(label="My Downloads", font="Helvetica 10 bold", command=mydownloades)
    mymenu.add_command(label="Exit", font="Helvetica 10 bold", command=quiter)
    mymenu.add_command(label="Help", font="Helvetica 10 bold", command=helpwindow)
    mymenu.add_command(label="About", font="Helvetica 10 bold", command=aboutwindow)

    root.config(menu=mymenu)

    f2 = Frame(root)
    f2.pack(pady=23, padx=2, fill=X)
    l1 = Label(f2, text="Enter URL of Video: ", fg="black", font="Helvetica 15 bold", padx=11, pady=11)
    # l1.pack(side=LEFT)
    l1.grid(row=1, column=1)

    global url
    url = StringVar()

    userenrty = Entry(f2, textvariable=url, font="vardana 20")

    userenrty.grid(row=1, column=2, ipady=5)
    b1 = Button(f2, text="Download As Video", font="Helvetica 26 bold", fg="black", bg="#7EB2DD",
                command=videodownloader)
    b1.grid(row=8, column=2, padx=5, pady=5)
    b2 = Button(f2, text="Download As Audio", font="Helvetica 26 bold", fg="black", bg="#7EB2DD",
                command=audiodownloader)
    b2.grid(row=8, column=3, padx=5, pady=5)
    global label2
    label2=StringVar()
    label2.set("To Download a Video Just enter the URL and click on Any Download Button.")
    global label22
    label22=Label(root,textvariable=label2,font="Helvetica 14 bold", bg="orange")
    label22.pack()
    global statusvar
    statusvar = StringVar()
    statusvar.set("Ready")
    global sbar
    sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w", font="Helvetica 12 bold", bg="orange",
                 fg="blue")
    sbar.pack(side=BOTTOM, fill=X)
    space1 = Label(root, text="")
    space1.pack()
    fr2 = Frame(root, bg="grey", borderwidth=4)
    fr2.pack(fill=X)

    frtitle = Label(fr2, text="Downloaded Items:", fg="gold", bg="grey", font="verdana 20 bold")
    frtitle.pack()
    os.chdir(f"{home}\YoTUBE Downloader")

    a = os.listdir()

    def clicked(event):
        import subprocess
        os.chdir(f"{home}\YoTUBE Downloader")

        path = os.getcwd()
        subprocess.Popen(f'Explorer {path}')

    if len(a) == 0:
        fritem = Label(fr2, text="Looks like you didn't' download anything yet start downloading NOW....", bg="grey",
                       fg="white", font="helvetica 15 bold")
        fritem.pack(anchor="w")
    else:
        for items in a:
            fritems = Label(fr2, text=items, bg="grey", fg="white", font="vardana 10 bold")
            fritems.pack(anchor="w")
            fritems.bind('<Button-1>', clicked)

    if connection == False:
        aa3 = tmsg.showinfo("Connection Required",
                            "Dear User Internet Connection is required to use the YoTUBE please connect to Internet.")
    def checkinglink():
        while True:
            ch = url.get()
            if len(ch)!=0:
                try:
                    vid = YouTube(ch)
                    t1 = vid.title
                    label2.set(t1)
                    label22.update()
                    break
                except Exception as sa:
                    label2.set(f"{ch} is not a valid url")
                    label22.update()
            else:
                label2.set("To Download a Video Just enter the URL and click on Any Download Button.")
                label22.update()

    t1=threading.Thread(target=checkinglink())
    t1.start()
    root.mainloop()

def audiodownloader():
    os.chdir(f"{home}\YoTUBE Downloader")
    url2 = url.get()
    try:

        os.chdir(f"{home}\YoTUBE Downloader")

        video = YouTube(url2)
        statusvar.set("Downloading Audio...Please wait")
        sbar.update()
        video2 = video.streams.filter(only_audio=True).first()
        title2 = video.title
        label2.set(f"Downloading {title2} Audio")
        print(title2)
        a = os.listdir()
        label22.update()
        video2.download()
        statusvar.set("Download Successful")
        sbar.update()
        a = tmsg.askyesno("Download Completed", f"{title2} is Downloaded do you want to open it?")
        if a is False:
            root.destroy()
            main()
        else:

            os.chdir(f"{home}\YoTUBE Downloader")

            path = os.getcwd()
            import subprocess
            subprocess.Popen(f'explorer {path}')
            root.destroy()
            main()
    except Exception as e:

        tmsg.showerror("Error", f"Enter a valid URL or Try Again")
        # print("its in audio download", e)


def videodownloader():
    os.chdir(f"{home}\YoTUBE Downloader")

    url2 = f"{url.get()}"
    try:

        os.chdir(f"{home}\YoTUBE Downloader")

        video = YouTube(url2)
        statusvar.set("Downloading Video...Please wait")
        sbar.update()
        video2 = video.streams.filter(progressive=True)
        title2 = video.title
        label2.set(f"Downloading {title2} Video")
        label22.update()


        video2.get_highest_resolution().download()
        statusvar.set("Download Successful")
        sbar.update()
        a = tmsg.askyesno("Download Completed", f"{title2} is Downloaded do you want to open it?")
        if a is False:
            root.destroy()
            main()
        else:
            os.chdir(f"{home}\YoTUBE Downloader")

            path = os.getcwd()
            import subprocess
            subprocess.Popen(f'explorer {path}')
            root.destroy()
            main()

    except Exception as ea:
        # print("its in video dowlload", e)
        tmsg.showerror("Error", f"Enter a valid URL or Try Again")


if __name__ == '__main__':
    main()
