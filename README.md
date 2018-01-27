# Keith Qu - Data Science with Python

### Prediction and Analysis

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/credit%20risk/Credit%20Risk%20Predictions.ipynb">Credit Risk Classification</a><br>
Risk classification with 150,000 training and 100,000 test observations from Kaggle's <a href="https://www.kaggle.com/c/GiveMeSomeCredit">Give Me Some Credit</a> competition. Highest private leaderboard score so far is 0.866752.

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/manhattanofficelease/Manhattan%20Office%20Real%20Estate.ipynb">Estimating Manhattan Office Rental Rates</a><br>
I construct an 11 feature dataset of 1369 Manhattan office rentals, of which 539 have listed rental rates in $/sqft/year. With the 539 observation training set, I convert addresses and strings into quantitative data, and engineer features to try to create a predictive model of the remaining 830 prices.

### Natural Language

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/toxiccomments/Toxic%20Comments%20Classification.ipynb">Toxic Comments Classification</a><br>
A quick look at multilabel classification with different forms of <a href="https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge">toxic internet comments</a> using logistic regression, NB-SVM, as well as convolutional and recurrent neural networks with the Keras API running on a TF backend.

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/yfsent/Yahoo%20Finance%20Headlines.ipynb">Yahoo Finance Headlines</a><br>
Yahoo Finance is one of the company's few remaining products that is actually very good, but support has been reduced greatly, and it no longer lets us specify a date range for headlines. By default, the page only displays 25 and more is injected onto the page when you scroll down, so I use Selenium and Google's net logging to get the json URLs and access them directly. The json contains more data than what actually shows up on the page (and the exact date), so this could be pretty useful. These headlines are then converted into sentiment scores.

### Visualization and Other Stuff

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/gasprices/gas%20prices.ipynb">Greater Toronto Area Gas Map</a><br>
Scrapes a comprehensive set of gas price information for the Toronto area and visualizes it with Folium. Includes some light analysis: gas stations within 100m of a Starbucks tend to charge 0.6 cents more for regular gas!

<a href="http://nbviewer.jupyter.org/github/keithqu/illustrative/blob/master/K%20Means%20Iteration.ipynb">Iterative K Means</a><br>Showcases how K Means clustering finds new centroids and labels with each iteration.
