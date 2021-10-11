
from tkinter import *
from pytube import YouTube
import os
from pathlib import Path
import tkinter.messagebox as tmsg


home = str(Path.home())
# print(home)
os.chdir(home)
global thread_flag


def gmailsender():
    try:
        import smtplib as s

        ob = s.SMTP("smtp.gmail.com", 587)
        ob.starttls()
        ob.login("warmcreators@gmail.com", "get.password(Warmcreators)")
        subject = "Welcome to YoTUBE "
        body = "\nWelcome to YoTUBE. The Simplest youtube video downloader.\n" \
               "Thank you for Registering at YoTUBE \t" \
               "\nWe are very thrilled by your joining at YoTUBE \t" \
               "\nPlease let us know if you have any suggestion \n" \
               "and issue with that software \n"

        message = "Subject:{}\n\n{}".format(subject, body)

        ob.sendmail("warmcreators@gmail.com", email, message)
        ob.quit()
    except Exception as nio:
        print(nio)


def mydownloades():
    os.chdir(f"{home}\YoTUBE Downloader")

    path = os.getcwd()
    import subprocess
    subprocess.Popen(f'explorer {path}')


def quiter():
    quit()


def helpwindow():
    helpw = Tk()
    helpw.geometry("800x700")
    helpw.title("YoTUBE Help")

    maxwidth = helpw.winfo_screenwidth()
    maxheight = helpw.winfo_screenheight()
    helpw.maxsize(maxwidth, maxheight)
    helpw.configure(bg="grey")
    l1 = Label(helpw, text="How it Works", font="verdana 35 bold", fg="gold", bg="grey")
    l1.pack()
    space = Label(helpw, text="")
    space.pack()
    l2 = Label(helpw, text="What is URL:", font="helvetica 25 bold", fg="orange", bg="grey")
    l2.pack(anchor="w", fill=X)

    l3 = Label(helpw, text="URL is a specific link of a video on youtube. Every\n"
                           " video on youtube has a unique URL from which all users\n "
                           "of youtube can access that video. ", font="Helvetica 15 bold", fg="black")
    l3.pack()
    sapce1 = Label(helpw, text="")
    sapce1.pack()
    l4 = Label(helpw, text="How to get URL of any video:", font="Helvetica 25 bold", fg="orange", bg="grey")
    l4.pack(anchor="w", fill=X)
    l5 = Label(helpw, text="To get a URL of any video on Youtube follow the steps below:\n"
                           "\n1. Open youtube on any browser like (Chrome,Firefox,Edge etc)\n"
                           "\n2. Search any video on Youtube which you want to download \n"
                           "\n3. Now on the Top in browser there is a box where URL is present\n"
                           "\nlike 'https://www.youtube.com/watch?v=CHjbJ9OirO4' "
                           "\nor Right CLick on that video and hit 'Copy Link Address' \n"
                           "\n4. Now Paste that link in the YoTUBE software  \n"
                           "\n5. Click on Any Download Button like as Audio and Video \n"
                           "\nBoom your video is downloaded as soon as possible\n", font="Helvetica 15 bold",
               fg="black")
    l5.pack()
    helpw.mainloop()
def registeruser():
    register = Tk()
    register.title("Register")
    register.geometry("750x600")

    r1 = Frame(register)
    r1.pack(fill=Y)
    logo = Label(r1, text="Please Register First to use YoTUBE ", fg="black", font="verdana 25 bold",
                 bg="lightblue")
    logo.pack(fill=X)
    logo1 = Label(r1, text="")
    logo1.pack()
    n1 = Label(r1, text="Name: ")
    n1.pack()
    namet1 = StringVar()

    nameenrty = Entry(r1, textvariable=namet1, font="vardana 20")

    nameenrty.pack(fill=X, pady=20)
    n2 = Label(r1, text="Email: ")
    n2.pack()
    emailidt1 = StringVar()

    emailenrty = Entry(r1, textvariable=emailidt1, font="vardana 20")

    emailenrty.pack(fill=X, pady=20)
    n3 = Label(r1, text="Password: ")
    n3.pack()
    passwordt1 = StringVar()

    passwordenrty = Entry(r1, textvariable=passwordt1, font="vardana 20")

    passwordenrty.pack(fill=X, pady=20)

    def submitdetails():

        global connectionwithdatabase
        connectionwithdatabase = False
        global email
        name = nameenrty.get()
        email = emailenrty.get()
        password = passwordenrty.get()

        if email != "" and password != "" and name != "":
            if email.endswith("@gmail.com") == False:
                statusvar32.set("Enter G-mail id in email section!")
                statusbar32.configure(font="vardana 15 bold", fg="red")
                statusbar32.update()
            elif len(password) < 8:
                statusvar32.set("Password should be 8 characters!")
                statusbar32.configure(font="vardana 15 bold", fg="red")
                statusbar32.update()

            else:
                try:
                    os.chdir(f"{home}\.YoTUBE data")
                except EXCEPTION as FileNotFoundError:

                    os.chdir(f"{home}")
                    os.mkdir(".YoTUBE data")
                    os.chdir(f"{home}\.YoTUBE data")
                file = open(".userdata.txt", "w+")
                file.write(str(name))
                file.write("\n")
                file.write(str(email))
                file.write("\n")
                file.write(str(password))
                file.write("\n")
                file.close()
                import mysql.connector

                try:

                    db = mysql.connector.connect(
                        host="127.0.0.1",
                        user="root",
                        passwd="tarunsh2908",
                        port="3306",
                        database="localdata")
                    mycursor = db.cursor()
                    try:
                        mycursor.execute("INSERT INTO YoTUBE (Name,Email,Password) VALUES (%s,%s,%s)",
                                         (name, email, password))

                        db.commit()
                    except Exception as aeurh:
                        os.chdir(f"{home}\.YoTUBE data")
                        file = open(".temp.txt", "w+")
                        file.write(str(aeurh))
                        file.close()
                    mycursor.close()
                except Exception as asda:
                    os.chdir(f"{home}\.YoTUBE data")
                    file = open(".temp.txt", "w+")
                    file.write(str(asda))
                    file.close()

                statusvar32.set("Registering please wait...")
                gmailsender()
                statusbar32.configure(font="vardana 15 bold", fg="green")
                statusbar32.update()
                import time
                time.sleep(2)
                statusvar32.set("Registered Successfully...")
                statusbar32.configure(font="vardana 15 bold", fg="green")
                statusbar32.update()
                register.destroy()

        else:
            statusvar32.set("Enter All details correctly!")
            statusbar32.configure(font="vardana 15 bold", fg="red")
            statusbar32.update()

    submit = Button(r1, text="Submit Details", font="vardana 20 bold", bg="lightgreen", fg="black",
                    command=submitdetails)
    submit.pack(pady=20)
    statusvar32 = StringVar()
    statusvar32.set("Enter All details to Register...")
    statusbar32 = Label(r1, textvariable=statusvar32, font="vardana 15 bold", fg="green")
    statusbar32.pack()
    register.mainloop()

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
                           "please write us on:\n", font="Helvetica 20 ", fg="white", bg="grey")
    l2.pack()
    l3 = Label(about, text="Warmcreators@gmail.com", font="verdana 25 bold ", fg="orange", bg="grey")
    l3.pack()


# def connection_check():
#     urltocheck = "http://www.kite.com"
#     timeout = 5
#     global connection
#     try:
#         request = requests.get(urltocheck, timeout=timeout)
#         connection = True
#     except (requests.ConnectionError, requests.Timeout) as exception:
#         connection = False
#     if connection is False:
#         aa3 = tmsg.showinfo("Connection Required",
#                             "Dear User Internet Connection is required to use the YoTUBE please connect to Internet.")
def listenonline():
    url3 =url.get()
    os.chdir(f"{home}\.YoTUBE data")
    try:
        video44 = YouTube(url3)

        video244 = video44.streams.filter(only_audio=True).first()

        title244 = video44.title
        label2.set(f"Trying to play it Online please wait...")

        label22.update()
        audio_download = video244.download()
        import subprocess

        file =title244 +".mp4"


        subprocess.Popen(f'Explorer {audio_download}')
        label2.set(f"Playing {title244} ")

        label22.update()

    except Exception as gotwrong:
        tmsg.showerror("Something went wrong" ,gotwrong)
        print(gotwrong)
def myprofile():
    os.chdir(f"{home}\.YoTUBE data")
    file=open(".userdata.txt","r")
    details=file.readlines()
    profile = Tk()
    profile.title("User Details")
    profile.geometry("800x650")
    file.close()
    password=details[2]
    passlen=len(password)
    password2=""
    for i in range(passlen):
        password2+="x"
    # r1 = Frame(profile)
    # r1.pack(fill=BOTH)

    logo = Label(profile, text="User Details:", fg="black", font="verdana 22 bold",
                 bg="lightblue")
    logo.pack(fill=X)
    logo1 = Label(profile, text=" ")
    logo1.pack()
    logo1 = Label(profile, text=f"Name: \t {details[0]}",font="verdana 15 bold")
    logo1.pack()
    logo1 = Label(profile, text=f"Email: \t {details[1]}",font="verdana 15 bold")
    logo1.pack()
    logo1 = Label(profile, text=f"Password: \t {password2}",font="verdana 15 bold")
    logo1.pack()


    profile.mainloop()
def main():


    # urltocheck = "http://www.kite.com"
    # timeout = 5
    # global connection
    # try:
    #     request = requests.get(urltocheck, timeout=timeout)
    #     connection = True
    # except (requests.ConnectionError, requests.Timeout) as exception:
    #     connection = False
    try:
        os.chdir(f"{home}\YoTUBE Downloader")
        try:
            os.chdir(f"{home}\.YoTUBE data")
            f4 =os.listdir()

            if len(f4)==0:
                registeruser()
            else:
                for abs in f4:
                    if abs!=".userdata.txt":
                        os.remove(abs)


        except Exception as enrer:
            userfound =True


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
    mymenu.add_command(label="Profile ", font="Helvetica 10 bold", command=myprofile)

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
    b3 = Button(f2, text="Listen/Watch Online", font="Helvetica 26 bold", fg="black", bg="#7EB2DD",
                command=listenonline)
    b3.grid(row=8, column=4, padx=5, pady=5)
    global label2
    label2 = StringVar()
    label2.set("To Download a Video Just enter the URL and click on Any Download Button.")
    global label22
    label22 = Label(root, textvariable=label2, font="Helvetica 14 bold", bg="orange")
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

    frtitle = Label(fr2, text="Downloaded Items:", fg="gold", bg="grey", font="verdana 25 bold")
    frtitle.pack()
    os.chdir(f"{home}\YoTUBE Downloader")

    a = os.listdir()

    def clicked(event):
        x = mylist.curselection()[0]
        file = mylist.get(x)

        import subprocess
        os.chdir(f"{home}\YoTUBE Downloader")
        try:
            path = f"{home}\YoTUBE Downloader\{file}"
            subprocess.Popen(f'Explorer {path}')
        except Exception as issue:
            path = f"{home}\YoTUBE Downloader"
            subprocess.Popen(f'Explorer {path}')


    if len(a) == 0:
        fritem = Label(fr2, text="Looks like you didn't' download anything yet start downloading NOW....", bg="grey",
                       fg="white", font="helvetica 15 bold")
        fritem.pack(anchor="w")
    else:
        sb = Scrollbar(fr2)
        sb.pack(side=RIGHT, fill=Y)
        mylist = Listbox(fr2, width=300, height=300, yscrollcommand=sb.set, bg="lightgrey", font="helvetica 12 bold"
                         ,fg="green")
        for i in a:
            mylist.insert(END, str(i))
        mylist.pack(side=LEFT, fill=X)
        mylist.bind("<<ListboxSelect>>", clicked)
        sb.config(command=mylist.yview())

    # def checkinglink():
    #     # connection_check()
    #     global thread_flag
    #
    #     while True:
    #         if thread_flag is False:
    #
    #             ch = url.get()
    #             if len(ch) != 0:
    #
    #                 try:
    #                     vid = YouTube(ch)
    #                     t1 = vid.title
    #                     label2.set(t1)
    #                     label22.update()
    #                     break
    #                 except Exception as sa:
    #                     label2.set(f"{ch} is not a valid url")
    #                     label22.update()
    #             else:
    #                 label2.set("To Download a Video Just enter the URL and click on Any Download Button.")
    #                 label22.update()
    #         else:
    #
    #             break


    root.mainloop()


def audiodownloader():
    global thread_flag
    thread_flag = True
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

        label22.update()

        audio_download = video2.download()
        new = audio_download.split(".")
        newfile = new[0]
        newfilename = newfile + ".mp3"
        os.rename(audio_download, newfilename)
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
        print(e)


def videodownloader():
    global thread_flag
    thread_flag = True
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

