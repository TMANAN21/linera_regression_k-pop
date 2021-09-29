This project is a very basic prediction model based on bar graphs to predict when K-pop groups will disband by popularity based on data found on the website: https://www.ranker.com/list/kpop-disbanded-groups/ranker-music?ref=listed_on&pos=2. This website has the disbanded groups ranked based on popularity. 

I use two platform to complete the project: Automation 360 and Python. I used Automation 360 to do webscraping of the data from the website above and store it in a csv file. In terms of the webscraping, I used Browser package to get the source code of the website and then used a beautifier to  then I used the JSON Object Manager Query to get the 

With Python, I used Pandas DataFrame and Matplotlib inorder to read data from csv file and then create a bar graph split in 6 groups based on popularity. The first group is the most popular and the 6th one is the least popular. 
