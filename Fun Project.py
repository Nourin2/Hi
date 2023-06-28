#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle


# In[2]:


from turtle import*


# In[3]:


wn = Screen()


# In[4]:


wn.bgcolor('black')


# In[5]:


t = turtle.Turtle()


# In[6]:


t.pencolor('white')


# In[7]:


def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)


# In[8]:


def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(115)
    curve()
    t.lt(120)
    curve()
    t.fd(115)
    t.end_fill()


# In[9]:


heart()
t.ht()


# In[10]:


def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style=('Stencil std', 18, "italic")
    t.write (message,font=style)
    


# In[11]:


write('I',(-75,95))
write('L',(-60,95))
write('O',(-47,95))
write('V',(-30,95))
write('E',(-15,95))

write('Y',(5,95))
write('O',(15,95))
write('U',(30,95))


# In[ ]:


wn.mainloop()


# In[ ]:




