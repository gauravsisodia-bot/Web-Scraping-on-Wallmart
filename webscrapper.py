#!/usr/bin/env python
# coding: utf-8

# In[133]:


import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime


# In[134]:


link = "https://www.walmart.com/reviews/product/14898365"


# In[135]:


page=requests.get(link)


# In[136]:


page


# In[137]:


page.content


# In[101]:


soup = bs(page.content, "html.parser")


# In[102]:


print(soup.prettify())


# In[189]:


date = soup.find_all("span", class_="review-date-submissionTime")


# In[190]:


date


# In[192]:


datenew=[]
for i in range(0,len(date)):
    datenew.append(date[i].get_text())
datenew


# In[197]:


revdate=[]
for i in range(0, len(date)):
    revdate.append(datetime.strptime(date[i].get_text(), '%B %d, %Y'))
#    dates.skey = lambda date: datetime.strptime(date, '%B %d, %Y'))


# In[ ]:





# In[198]:


revdate.sort()


# In[ ]:





# In[199]:


revdate


# In[200]:


from datetime import datetime


# In[201]:


def printDates(dates):

    for i in range(len(dates)):
        print(dates[i])


if __name__ == "__main__":

    dates = ['April 10 2021',
             'April 26 2020',
             'April 3 2021',
             'August 21 2020',
             'August 29 2020',
             'August 3 2020',
             'December 21 2020',
             'December 23 2020',
             'December 27 2020',
             'January 12 2014',
             'July 13 2021',
             'July 27 2020',
             'July 27 2021',
             'July 28 2021',
             'July 29 2020',
             'March 12 2021',
             'March 17 2021',
             'May 13 2021',
             'May 16 2020',
             'September 3 2020']
dates.sort(key = lambda date: datetime.strptime(date, '%B %d %Y'))


# In[202]:


printDates(dates)


# In[203]:


title = soup.find_all("h3", class_="review-title font-bold")


# In[204]:


title


# In[205]:


titlenew=[]
for i in range(0, len(title)):
    titlenew.append(title[i].get_text())


# In[206]:


titlenew


# In[207]:


body= soup.find_all("p")


# In[208]:


body


# In[209]:


bodynew=[]
for i in range(0, len(body)):
    bodynew.append(body[i].get_text())


# In[210]:


bodynew


# In[211]:


stars = soup.find_all("div", class_="arranger stars stars-small arranger--items-center")


# In[212]:


stars


# In[213]:


starsnew=[]
for i in range(0, len(stars)):
    starsnew.append(stars[i].get_text())


# In[214]:


starsnew


# In[215]:


purchaser = soup.find_all("div", class_="verified")


# In[216]:


purchaser


# In[217]:


purchasernew=[]
for i in range(0, len(purchaser)):
    purchasernew.append(purchaser[i].get_text())


# In[218]:


purchasernew


# In[219]:


revdate
titlenew
bodynew
starsnew
purchasernew


# In[230]:


hs = pd.DataFrame()


# In[231]:


hs["Sorted Date"]=dates


# In[232]:


hs


# In[234]:


hs.to_csv(r"E:\webscrapdatesort.csv", index=True)


# In[221]:


hs["Review Date"]=pd.Series(datenew)
hs["Title"]=pd.Series(titlenew)
hs["Review Body"]=pd.Series(bodynew)
hs["Stars"]=pd.Series(starsnew)
hs["Purchaser"]=pd.Series(purchasernew)


# In[222]:


hs


# In[233]:


hs.to_csv(r"E:\webscrapwallmart.csv", index=True)


# In[ ]:





# In[ ]:




