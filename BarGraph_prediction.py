import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

data = pd.read_csv('Years.csv',encoding='cp1252')

# Mean of every 13 groups; G1 is the most popular and G6 is the least popular
g1_mean = data['G1'].mean()
g2_mean = data['G2'].mean()
g3_mean = data['G3'].mean()
g4_mean = data['G4'].mean()
g5_mean = data['G5'].mean()
g6_mean = data['G6'].mean()


# The Bar graph
fig = plt.figure()
ax = fig.add_axes([0,0,2,2])
X = ['G1','G2','G3','G4','G5','G6']
Y= [g1_mean, g2_mean, g3_mean, g4_mean, g5_mean, g6_mean]
plt.title('Debut Years by Popularity', fontsize=20, color = '#1306c6')
plt.xlabel('Kpop groups by popularity', fontsize=20, color = '#1306c6')
plt.ylabel('Average Debut Years', fontsize=20, color = '#1306c6')
ax.bar(X, Y, color = '#Eb4022')
plt.show()


# communication with the user
print('This program will try to predict how long a K-pop group remains until it is disbanded.')
band_name = input('Please type the name of your favorite K-pop group that hasn\'t disbanded yet: ')
debut_start = input ('Please type the year when the K-pop group started their debut: ')
rating = input ('How would you rate the K-pop group in term of popularity from 1-6, 1 being very popular and 6 being ok popular?: ')
time_since_debut = date.today().year - int(debut_start)
if rating == '1':
    print ("Based on my predicition the K-pop group will be a group for " + str(int(g1_mean) - time_since_debut) + ' years.')

elif rating == '2':
    print ("Based on my predicition the K-pop group will be a group for " + str(int(g2_mean) - time_since_debut) + ' years.')

elif rating == '3':
    print ("Based on my predicition the K-pop group will be a group for " + str(int(g3_mean) - time_since_debut) + ' years.')

elif rating == '4':
    print ("Based on my predicition the K-pop group will be a group for " + str(int(g4_mean) - time_since_debut) + ' years.')

elif rating == '5':
    print ("Based on my predicition the K-pop group will be a group for " + str(int(g5_mean) - time_since_debut) + ' years.')

elif rating == '6':
    print ("Based on my predicition the K-pop group will be a group for " + str(int(g6_mean) - time_since_debut) + ' years.')


