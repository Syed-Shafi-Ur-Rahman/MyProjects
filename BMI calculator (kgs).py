#!/usr/bin/env python
# coding: utf-8

# In[30]:


name = input("Enter your name : ")
weight = int(input("Enter your weight in kilograms : "))
height = int(input("Enter your height in feet : "))
inch = int(input("Enter inches : "))

BMI = (weight)/((height*0.3048+inch*0.0254)**2)
print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name+", you are Underweight, Have some hyderabadi Nahari Paya and gain weight.")
    elif(BMI<=24):
        print(name+", you are Normal weight, Congratulations you are healthy.")
    elif(BMI<=29.9):
        print(name+", you are Overweight, you need to reduce your weight.")
    elif(BMI>=30):
        print(name+", you are Obese, you need to reduce your weight as an emergency measure.")
    else:
        print("Enter a valid Input.")
else:
        print("Enter a valid Input.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




