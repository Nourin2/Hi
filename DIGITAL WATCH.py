#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import datetime


# In[2]:


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    


# In[ ]:





# In[3]:


clock = Tk()


# In[4]:


clock.title('Digital Watch')


# In[5]:


clock.geometry('1000x500')


# In[6]:


clock.config(bg='blue')


# In[7]:


lab_hr=Label(clock,text='00',font=('Times New Roman',60,'bold'),bg='white',fg='black')


# In[8]:


lab_hr.place(x=120,y=45,height=110,width=100)


# In[9]:


lab_min=Label(clock,text='00',font=('Times New Roman',60,'bold'),bg='white',fg='black')
lab_min.place(x=340,y=45,height=110,width=100)


# In[10]:


lab_sec=Label(clock,text='00',font=('Times New Roman',60,'bold'),bg='white',fg='black')
lab_sec.place(x=560,y=45,height=110,width=100)


# In[11]:


lab_am=Label(clock,text='AM',font=('Times New Roman',45,'bold'),bg='white',fg='black')
lab_am.place(x=780,y=45,height=110,width=100)


# In[12]:


lab_hr_text=Label(clock,text='Hour',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_hr_text.place(x=120,y=190,height=35,width=100)


# In[13]:


lab_min_text=Label(clock,text='Minute',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_min_text.place(x=340,y=190,height=35,width=100)


# In[14]:


lab_second_text=Label(clock,text='Second',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_second_text.place(x=560,y=190,height=35,width=100)


# In[15]:


lab_am_text=Label(clock,text='AM/PM',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_am_text.place(x=780,y=190,height=35,width=100)


# In[16]:


#DATe


# In[17]:


lab_date=Label(clock,text='00',font=('Times New Roman',60,'bold'),bg='white',fg='black')
lab_date.place(x=120,y=260,height=110,width=100)
lab_date_text=Label(clock,text='Date',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_date_text.place(x=120,y=400,height=35,width=100)


# In[18]:


#Month


# In[19]:


lab_month=Label(clock,text='00',font=('Times New Roman',60,'bold'),bg='white',fg='black')
lab_month.place(x=340,y=260,height=110,width=100)
lab_month_text=Label(clock,text='Month',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_month_text.place(x=340,y=400,height=35,width=100)


# In[20]:


#year


# In[21]:


lab_year=Label(clock,text='00',font=('Times New Roman',60,'bold'),bg='white',fg='black')
lab_year.place(x=560,y=260,height=110,width=100)
lab_year_text=Label(clock,text='Year',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_year_text.place(x=560,y=400,height=35,width=100)


# In[22]:


#Day


# In[23]:


lab_day=Label(clock,text='Day',font=('Times New Roman',45,'bold'),bg='white',fg='black')
lab_day.place(x=780,y=260,height=110,width=100)

lab_day_text=Label(clock,text='Day',font=('Times New Roman',18,'bold'),bg='white',fg='black')
lab_day_text.place(x=780,y=400,height=35,width=100)


# In[24]:


date_time()


# In[25]:


clock.mainloop()


# In[ ]:





# In[ ]:




