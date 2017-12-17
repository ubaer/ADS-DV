import pandas as pd

dataset = pd.read_csv('F:\Skool\Data visualisatie\Project\BPD_Part_1_Victim_Based_Crime_Data.csv')

dataset['dateforreal'] = dataset['CrimeDate']
dataset['dateforreal'] = pd.to_datetime(dataset['dateforreal'], format='%m/%d/%Y')

year = 2017

newyear = dataset[dataset['dateforreal'].dt.year == year]
newyear.columns = ['date','CrimeTime','CrimeCode','Location','Description','Inside/Outside','Weapon','Post','District','Neighborhood','Longitude','Latitude','Location 1','Premise','Total Incidents','dateforreal'
]

jan = newyear[dataset['dateforreal'].dt.month == 1]
feb = newyear[dataset['dateforreal'].dt.month == 2]
ma = newyear[dataset['dateforreal'].dt.month == 3]
apr = newyear[dataset['dateforreal'].dt.month == 4]
mei = newyear[dataset['dateforreal'].dt.month == 5]
juni = newyear[dataset['dateforreal'].dt.month == 6]
juli = newyear[dataset['dateforreal'].dt.month == 7]
aug = newyear[dataset['dateforreal'].dt.month == 8]
sept = newyear[dataset['dateforreal'].dt.month == 9]
okt = newyear[dataset['dateforreal'].dt.month == 10]
nov = newyear[dataset['dateforreal'].dt.month == 11]
dec = newyear[dataset['dateforreal'].dt.month == 12]

jan.to_csv(str(year)+'/'+'01.csv',index = False)
feb.to_csv(str(year)+'/'+'02.csv',index = False)
ma.to_csv(str(year)+'/'+'03.csv',index = False)
apr.to_csv(str(year)+'/'+'04.csv',index = False)
mei.to_csv(str(year)+'/'+'05.csv',index = False)
juni.to_csv(str(year)+'/'+'06.csv',index = False)
juli.to_csv(str(year)+'/'+'07.csv',index = False)
aug.to_csv(str(year)+'/'+'08.csv',index = False)
sept.to_csv(str(year)+'/'+'09.csv',index = False)
okt.to_csv(str(year)+'/'+'10.csv',index = False)
nov.to_csv(str(year)+'/'+'11.csv',index = False)
dec.to_csv(str(year)+'/'+'12.csv',index = False)