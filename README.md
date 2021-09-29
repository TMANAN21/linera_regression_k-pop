This project is a very basic prediction model based on bar graphs to predict when K-pop groups will disband by popularity based on data found on the website: https://www.ranker.com/list/kpop-disbanded-groups/ranker-music?ref=listed_on&pos=2. This website has the disbanded groups ranked based on popularity. 

I use two platform to complete the project: Automation 360 and Python. I used Automation 360 to do webscraping of the data from the website above and store it in a csv file. In terms of the webscraping, I used Browser package to get the source code of the website and then used a beautifier to beautify the json file then I used the JSON Object Manager:Query packag to get the data that I wanted and logged to a csv file.

With Python, I used Pandas DataFrame and Matplotlib inorder to read data from csv file and then create a bar graph split in 6 groups based on popularity. The first group is the most popular and the 6th one is the least popular. I used mean to calculate the average number of years before disbanding based on different groups and then created a bar chart based on that. Lastly, the project communicated with the user on their favorite group and based on the data, it predicts how long till the group will disband. 


