# Keith Qu - Data Science with Python

### Prediction and Analysis

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/credit%20risk/Credit%20Risk%20Predictions.ipynb">Credit Risk Classification</a><br>
Risk classification  with hundreds of thousands of observations from Kaggle's <a href="https://www.kaggle.com/c/GiveMeSomeCredit">Give Me Some Credit</a> competition. Using only gradient boosting, the model has a high score of 0.866752 on the private leaderboard.

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/manhattanofficelease/Manhattan%20Office%20Real%20Estate.ipynb">Estimating Manhattan Office Rental Rates</a><br>
I create a dataset of 1369 Manhattan office rentals with 11 features, of which 539 have listed rental rates in $/sqft/year, which I convert into monthly rental rates. With the 539 observation training set, I convert addresses and strings into quantitative data, and engineer features to try to create a predictive model of the remaining 830 prices.

### Visualization and Fun

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/gasprices/gas%20prices.ipynb">Greater Toronto Area Gas Map</a><br>
Web scraping for gas prices, and plots locations and prices with Folium. Includes some light analysis: gas stations within 100m of a Starbucks tend to charge 0.6 cents more for regular gas!

<a href="http://nbviewer.jupyter.org/github/keithqu/illustrative/blob/master/K%20Means%20Iteration.ipynb">Iterative K Means</a><br>Showcases how K Means  clustering finds new centroids and labels in each iteration.

### Scraping

Yahoo Finance Headlines<br>
Yahoo no longer lets us specify a date range for headlines, and the top page only displays 25. More is injected onto the page when you scroll down, so I use Selenium and Google's net logging to get the json URLs and access them directly. The json contains more data than what actually shows up on the page (and the exact date), so this could be pretty useful.
