from tkinter import *
from PIL import ImageTk



#This is the root Part
curriculum_vitae = Tk()
curriculum_vitae.geometry("455x560")
curriculum_vitae.title("CURRICULUM VITAE")
curriculum_vitae.resizable(0,0)


#This is the Frame part
top_frm = Frame(curriculum_vitae,width=455,height=225,bg="black")
top_frm.place(x=0,y=0)
right_frm = Frame(curriculum_vitae, width=180,height=335,bg="gray")
right_frm.place(x=0,y=225)
left_frm = Frame(curriculum_vitae,width=280,height=335,bg="white")
left_frm.place(x=175,y=225)

#This is the Design Part
#Top Frame
Tp_wht_box1 = Frame(top_frm,width=20,height=20,bg="white")
Tp_wht_box1.place(x=195,y=80)
Tp_wht_box2 = Frame(top_frm,width=20,height=20,bg="white")
Tp_wht_box2.place(x=235,y=80)
Tp_wht_box3 = Frame(top_frm,width=20,height=20,bg="white")
Tp_wht_box3.place(x=275,y=80)
Tp_wht_box4 = Frame(top_frm,width=20,height=20,bg="white")
Tp_wht_box4.place(x=315,y=80)
Tp_wht_box5 = Frame(top_frm,width=20,height=20,bg="white")
Tp_wht_box5.place(x=355,y=80)
Tp_wht_box6 = Frame(top_frm,width=20,height=20,bg="white")
Tp_wht_box6.place(x=395,y=80)
Tp_wht_box7 = Frame(top_frm,width=20,height=20,bg="white")
Tp_wht_box7.place(x=435,y=80)
Tp_wht_mainBox = Frame(top_frm,width=280,height=125,bg="white")
Tp_wht_mainBox.place(x=175,y=100)
Tp_blck_box1 = Frame(top_frm,width=20,height=20,bg="black")
Tp_blck_box1.place(x=175,y=120)
Tp_blck_box2 = Frame(top_frm,width=20,height=20,bg="black")
Tp_blck_box2.place(x=175,y=160)
Tp_blck_box3 = Frame(top_frm,width=20,height=20,bg="black")
Tp_blck_box3.place(x=175,y=200)
Tp_blck_box4 = Frame(top_frm,width=20,height=20,bg="black")
Tp_blck_box4.place(x=175,y=240)

#This is the picture part
cv_picture = ImageTk.PhotoImage(file="C:\\Users\\Me\\Pictures\\CV_Image.jpg")
cvPic_lbl = Label(top_frm,image=cv_picture)
cvPic_lbl.place(x=15,y=10)

#Right Frame
Rt_blck_box1 = Frame(right_frm, width=20,height=20,bg="black")
Rt_blck_box1.place(x=0,y=0)
Rt_blck_box2 = Frame(right_frm, width=20,height=20,bg="black")
Rt_blck_box2.place(x=35,y=0)
Rt_blck_box3 = Frame(right_frm, width=20,height=20,bg="black")
Rt_blck_box3.place(x=75,y=0)
Rt_blck_box4 = Frame(right_frm, width=20,height=20,bg="black")
Rt_blck_box4.place(x=115,y=0)
Rt_blck_box5 = Frame(right_frm, width=20,height=20,bg="black")
Rt_blck_box5.place(x=155,y=0)

#Lining the right frame
Rt_wht_line1 = Frame(right_frm,width=150,height=1,bg="white")
Rt_wht_line1.place(x=10,y=135)

#Left Frame
Lt_gry_box1 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box1.place(x=0,y=20)
Lt_gry_box2 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box2.place(x=0,y=60)
Lt_gry_box3 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box3.place(x=0,y=100)
Lt_gry_box4 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box4.place(x=0,y=140)
Lt_gry_box5 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box5.place(x=0,y=180)
Lt_gry_box6 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box6.place(x=0,y=220)
Lt_gry_box7 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box7.place(x=0,y=260)
Lt_gry_box8 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box8.place(x=0,y=300)
Lt_gry_box9 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box9.place(x=0,y=340)
Lt_gry_box10 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box10.place(x=0,y=380)
Lt_gry_box11 = Frame(left_frm,width=20,height=20,bg="gray")
Lt_gry_box11.place(x=0,y=420)

#This is the text part
#Name
myName_lbl = Label(top_frm,text="Carl El Cedrik T. Rebosura",font=("Poppins",16,"bold"),fg="white",bg="black")
myName_lbl.place(x=175,y=25)

#Personal Information
personalInfo_lbl = Label(Tp_wht_mainBox,text="Personal Information",font=("Poppins",10,"bold"),fg="black",bg="white")
personalInfo_lbl.place(x=40,y=5)
birthday_lbl = Label(Tp_wht_mainBox,text="Birthday:",font=("Poppins",10,"bold"),fg="black",bg="white")
birthday_lbl.place(x=60,y=25)
con_birthday_lbl = Label(Tp_wht_mainBox,text="September 26, 2004",font=("Poppins",10),fg="black",bg="white")
con_birthday_lbl.place(x=120,y=25)
gender_lbl = Label(Tp_wht_mainBox,text="Gender:",font=("Poppins",10,"bold"),fg="black",bg="white")
gender_lbl.place(x=60,y=45)
con_gender_lbl = Label(Tp_wht_mainBox,text="Male",font=("Poppins",10),bg="white")
con_gender_lbl.place(x=115,y=45)
status_lbl = Label(Tp_wht_mainBox,text="Status:",font=("Poppins",10,"bold"),fg="black",bg="white")
status_lbl.place(x=60,y=65)
con_status_lbl = Label(Tp_wht_mainBox,text="Single",font=("Poppins",10),fg="black",bg="white")
con_status_lbl.place(x=105,y=65)
religion_lbl = Label(Tp_wht_mainBox,text="Religion:",font=("Poppins",10,"bold"),fg="black",bg="white")
religion_lbl.place(x=60,y=85)
con_religion_lbl = Label(Tp_wht_mainBox,text="Religion: Roman Catholic",font=("Poppins",10),fg="black",bg="white")
con_religion_lbl.place(x=120,y=85)
nationality_lbl = Label(Tp_wht_mainBox,text="Nationality:",font=("Poppins",10,"bold"),fg="black",bg="white")
nationality_lbl.place(x=60,y=105)
con_nationality_lbl = Label(Tp_wht_mainBox,text="Filipino",font=("Poppins",10),fg="black",bg="white")
con_nationality_lbl.place(x=135,y=105)

#Educational Background
educBckgrd_lbl = Label(left_frm,text="Educational Background",font=("Poppins",10,"bold"),fg="black",bg="white")
educBckgrd_lbl.place(x=40,y=10)

#This is for Tertiary
tertiary_lbl = Label(left_frm,text="Tertiary:",font=("Poppins",10,"bold"),fg="black",bg="white")
tertiary_lbl.place(x=60,y=30)
nemsu_lbl = Label(left_frm,text="North Eastern Mindanao",font=("Poppins",10),fg="black",bg="white")
nemsu_lbl.place(x=120,y=30)
con1_nemsu_lbl = Label(left_frm,text="State University - Main",font=("Poppins",10),fg="black",bg="white")
con1_nemsu_lbl.place(x=120,y=50)
con2_nemsu_lbl = Label(left_frm,text="Campus",font=("Poppins",10),fg="black",bg="white")
con2_nemsu_lbl.place(x=120,y=70)
nemsu_address = Label(left_frm,text="Rosario, Tandag City",font=("Poppins",10),fg="black",bg="white")
nemsu_address.place(x=120,y=90)

#This is for Secondary
secondary_lbl = Label(left_frm,text="Secondary:",font=("Poppins",10,"bold"),fg="black",bg="white")
secondary_lbl.place(x=60,y=110)
hs_lbl = Label(left_frm,text="Lingig National",font=("Poppins",10),fg="black",bg="white")
hs_lbl.place(x=140,y=110)
con1_hs_lbl = Label(left_frm,text="High School",font=("Poppins",10),fg="black",bg="white")
con1_hs_lbl.place(x=140,y=130)
con2_hs_lbl = Label(left_frm,text="Poblacion, Lingig",font=("Poppins",10),fg="black",bg="white")
con2_hs_lbl.place(x=140,y=150)
con3_hs_lbl = Label(left_frm,text="Surigao del Sur",font=("Poppins",10),fg="black",bg="white")
con3_hs_lbl.place(x=140,y=170)
con4_hs_lbl = Label(left_frm,text="S.Y. 2017 - 2023",font=("Poppins",10),fg="black",bg="white")
con4_hs_lbl.place(x=140,y=190)

#This is for Elementary
elementary_lbl = Label(left_frm,text="Elementary:",font=("Poppins",10,"bold"),fg="black",bg="white")
elementary_lbl.place(x=60,y=210)
hs_lbl = Label(left_frm,text="Lingig Central",font=("Poppins",10),fg="black",bg="white")
hs_lbl.place(x=140,y=210)
con1_el_lbl = Label(left_frm,text="Elementary School",font=("Poppins",10),fg="black",bg="white")
con1_el_lbl.place(x=140,y=230)
con2_el_lbl = Label(left_frm,text="Poblacion, Lingig",font=("Poppins",10),fg="black",bg="white")
con2_el_lbl.place(x=140,y=250)
con3_el_lbl = Label(left_frm,text="Surigao del Sur",font=("Poppins",10),fg="black",bg="white")
con3_el_lbl.place(x=140,y=270)
con3_el_lbl = Label(left_frm,text="S.Y. 2011 - 2017",font=("Poppins",10),fg="black",bg="white")
con3_el_lbl.place(x=140,y=290)

#This is for address
address_lbl = Label(right_frm,text="Address: Poblacion,Lingig ",font=("Poppins",9,"bold"),fg="white",bg="gray")
address_lbl.place(x=5,y=25)
con_address_lbl = Label(right_frm,text="Surigao del Sur ",font=("Poppins",9,"bold"),fg="white",bg="gray")
con_address_lbl.place(x=60,y=45)
#This is for contact number
contactNo_lbl = Label(right_frm,text="Contact no. 09652338670",font=("Poppins",9,"bold"),fg="white",bg="gray")
contactNo_lbl.place(x=5,y=70)
#This is for email address
emailAdd_lbl = Label(right_frm,text="Email add:",font=("Poppins",9,"bold"),fg="white",bg="gray")
emailAdd_lbl.place(x=5,y=100)
con_emailAdd_lbl = Label(right_frm,text="cec@yahoo.com",font=("Poppins",9,"bold"),fg="blue",bg="gray")
con_emailAdd_lbl.place(x=70,y=100)

#This is for Awards and honors part
awad_hon_lbl = Label(right_frm,text="Awards & Honors",font=("Poppins",9,"bold"),fg="white",bg="gray")
awad_hon_lbl.place(x=5,y=150)
date_lbl = Label(right_frm,text="June 16, 2023",font=("Poppins",7,"bold"),fg="white",bg="gray")
date_lbl.place(x=20,y=175)
research_lbl = Label(right_frm,text="Research Competition Finalist ",font=("Poppins",7,"bold"),fg="white",bg="gray")
research_lbl.place(x=20,y=190)
con_research_lbl = Label(right_frm,text="Municipal SHS Expo cum ",font=("Poppins",7,"bold"),fg="white",bg="gray")
con_research_lbl.place(x=20,y=205)
con1_research_lbl = Label(right_frm,text="Lingig Municipal",font=("Poppins",7,"bold"),fg="white",bg="gray")
con1_research_lbl.place(x=20,y=220)

date2_lbl = Label(right_frm,text="June 17, 2023",font=("Poppins",7,"bold"),fg="white",bg="gray")
date2_lbl.place(x=20,y=255)
research2_lbl = Label(right_frm,text="2nd Place Research Booth ",font=("Poppins",7,"bold"),fg="white",bg="gray")
research2_lbl.place(x=20,y=270)
con3_research_lbl = Label(right_frm,text="Municipal SHS Expo cum ",font=("Poppins",7,"bold"),fg="white",bg="gray")
con3_research_lbl.place(x=20,y=285)
con4_research_lbl = Label(right_frm,text="Lingig Municipal",font=("Poppins",7,"bold"),fg="white",bg="gray")
con4_research_lbl.place(x=20,y=300)

curriculum_vitae.mainloop()