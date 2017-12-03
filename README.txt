Created for MLH Hack Day 2 Dec 2017 

# MLH Local Hack Day 2017
# Tennessee Technological University group
# 2 December, 2017
# 
# Chris S, Caroline E,
# Ethan L, John B, Lane S, 
# Maria, Paula B, Seth D
#
# Description:  Examine Middle Tennessee rain data and predict if a day will be rainy or sunny.
#               Currently bases decision off of the historical average for that day.
# 
# To use: Run server.py and open index.html in a browser.  Select a day and push the button.
#      Set the IP addresses in server.py and index.html if desired, or set these to 127.0.0.1 if
#      you are only running on your computer.
#
# Future Work: Create data analysis, prediction, and possibly machine learning algorithms to predict rainfall.
#      Clean up many of the files of old debugging and example code.
#      Make the prediction work for multiple cities.
#      Cross-check multiple databases for accuracy and robustness.

Overview of tools used:
Google:  Hands down the best programming tool available, second only to the computer you're actually
      using to program.  Anytime you have problems, LOOK THEM UP!  You may find someone who had a similar
	  question or issue, and you may get answers in a few seconds rather than spend hours on your own.
	  
Postman:  Convenient way to access webpages that are not meant for mouse clicks.  This
      was used extensively to check the server's response to dates with the required POST 
	  request.
	  
REST:  A convenient, semi-standardized way to communicate across the web with relatively few headaches.

JSON:  A way to format data for easy access across progamming languages and platforms.  
	  
React, Angular, Node.js:  Very powerful tools for hosting servers and running fancy, powerful web pages.
	  
Wireshark:  Very powerful way to view network traffic to and from your computer.  
      Used for troubleshooting the server connection for our purposes.
	  
Inspect Element:  Many browsers allow you to use this feature, or the View Page Source feature,
      to see exactly what is running the current web page.  You can add or delete lines of code 
	  in real time to see what this changes if you like, or you can use this to find data you would
	  like to get later with beautifulsoup or some other method.

Flask:  A commonly-used server framework to get a send data to and from a webpage.  See the code
      for details, but it was relatively painless to use and requires little additional code.
	  Also try Django for more features.

SimpleHTTPServer:  Run a simple web server on your computer.  If an index.html file exists
      in the folder you run this, it will display that page.  Otherwise, it makes a convenient
	  file server.  Run it in python 2.7 with "python -m SimpleHTTPServer" or in Python 3.x as
	  "python -m http.server"

BeautifulSoup4:  Getting useful data from websites can be hard. Use beautifulsoup
      to take much of the hard work out of it.  Use it for tables, weather, sports
	  scores, or whatever you want to get from a web page.  Use the Inspect feature 
	  or the View Source in your browser to see what information you have available.
	 	 
Path:  If your computer says python does not exist, try looking up the error message on Google.  
      Something about the path will probably come up. 