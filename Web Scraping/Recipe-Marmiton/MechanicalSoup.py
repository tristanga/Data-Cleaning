# Tutorial - Using MechanicalSoup to scrape one page of recipe for one ingredient on the best French Website Marmiton 
# for educational purposes

import mechanicalsoup

# Connect to marmiton
browser = mechanicalsoup.StatefulBrowser()
ingredient = 'oignon'
startpage = 1
myurl = 'https://www.marmiton.org/recettes/recherche.aspx?aqt='+ingredient+'&start='+str(startpage)
browser.open(myurl)

# Response = 200 => OK

# Get recipes from the page (Title + Url Link)
tt = []
ur = []
for link in browser.get_current_page().select('a.recipe-card'):
    h4 = link.select('h4')
    mytitle = h4[0].text.replace('<br />','')
    myurl = 'https://www.marmiton.org'+link.attrs['href']
    tt.append(mytitle)
    ur.append(myurl)
    
# Create and Save csv
import numpy as np
import pandas as pd
recipe = pd.DataFrame(np.column_stack([tt, ur]), 
                               columns=['Title', 'Url'])
                               
recipe.to_csv('recipe.csv', index = False)
