#!/usr/bin/env python
# coding: utf-8

# In[7]:


AB=int(input("Enter the value of side AB:"))
BC=int(input("Enter the value of side BC: "))
CA=int(input("Enter the value of side CA: "))
if 1<=AB<=50 and 1<=BC<=50 and 1<=CA<=50 :
    if (AB**2==BC**2+CA**2):
        print ("Right angle triangle")
    elif (AB==BC or BC==CA or CA==AB):
        print("Invalid input")
    else: print ("Not a right angle triangle")
else:
    print ("Out of range")
    


# In[ ]:





# In[ ]:




