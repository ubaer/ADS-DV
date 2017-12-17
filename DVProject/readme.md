# Summary
The visualisation will be about crime in Baltimore City, Maryland USA, the dataset is provided by the Baltimore Police Department and is updated monthly.<br>
The most interesting data is the combination of dates, times, locations, and the type of crime. Visualising this on a map with some sort of time line can give us more insight on the issue.
#Story
Baltimore is the 7th most dangerous city in the U.S. according to Forbes but it does also have its good sides. It is home to one of the most important harbors in the United States and it has an amazing Art and music scene.
The Rolling stones even choose Baltimore as the Best Music Scene in the country in 2008. This in combination with its diversity and rich history makes it a city people want to visit for a bunch of reasons. 
<br><br>
This visualisation is all about the amount of crime that is committed on certain times. This can help people choose when to visit and when to avoid Baltimore.
<br>At first its all about a very top level view in which you can see the parts of the year in which the crime rates are the highest or lowest.
When you want more information about a specific part and day of a year you can do a deep dive on it.
<br><br>
The timeline of a selected period is filled with nine different types of crime, ranging from vehicle theft to murder. They are placed on a timeline in which you are able to freely scroll through.
Within a time period you can see clusters of crimes committed, looking deeper into these clusters you can see exactly what happened for each individual incident.
<br><br>
Clicking on an incident will give you as much information about it as there is available within in the data set.

# Exploring and cleaning the data
I did some exploring of the data in tableau. I found out that the time and date tell a lot about the crime rate in the city. Most crimes are committed in broad daylight and there is always a dip in the amount of time during the winter months.
Because the dataset is so large I had to split it up to properly load it in javascript, I created my own python script for this.

# Design
In the first design of the timeline viewer I assigned the same color to every crime but I quickly saw that this has no value at all.
I followed up by assigning colors to them randomly, even though the color now useful because it could be used to differentiate between crimes, it did still not have the meaning which I wanted it to have.
To eventually give the colors real meaning I made a color scheme which goes from light to dark. The crimes are ranked by the amount of prison time you get.

For the calendar view I choose to keep the colors ranging from green to red to indicate the amount of crimes committed.
I had tried to also change them to the same color scheme as I used for the timeline viewer but it didn't make the message as clear that there are some periods which are safer to go to Baltimore than others.

# Feedback
One of the most important feedback points was about the 'why?'. Whats the use of this visualisation? That question made me look into the city of Baltimore, I found out that it has a bunch of reasons why people would visit the city.
Then I thought about the fact that I would not want to visit a city that is so dangerous, but looking at certain times a year it's not bad at all. 
Other people will probably have the same feeling as I have in that aspect which makes it a useful visualisation for people who want to visit Baltimore but are afraid of the dangers.
<br><br>
I received a suggestion to add an option to book a hotel for the selected date which I thought was very clever, this way you could even compare prices but unfortunately there aren't any free API's that lets you look at prices more than a month in advance 

#  Resources
BPD Part 1 Victim Based Crime Data 
https://data.baltimorecity.gov/Public-Safety/BPD-Part-1-Victim-Based-Crime-Data/wsfq-mvij
<br>
Maryland sentencing guidelines
http://msccsp.org/Files/Guidelines/offensetable.pdf
