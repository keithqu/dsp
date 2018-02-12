# Keith Qu - Data Science with Python

### Prediction and Analysis

<a href="https://github.com/keithqu/dsp/blob/master/yelp/Yelp%20Stars%20Prediction.ipynb">Yelp Star Prediction</a><br>
I wanted to see how much exterior weather and a business' relative price affects star ratings in addition to comment text. So I do some classification with Keras on 630,000+ reviews of businesses in the Toronto area. (only the basic comment classification completed so far)

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/credit%20risk/Credit%20Risk%20Predictions.ipynb">Credit Risk Classification</a><br>
Risk classification with 150,000 training and 100,000 test observations from Kaggle's <a href="https://www.kaggle.com/c/GiveMeSomeCredit">Give Me Some Credit</a> competition. Highest private leaderboard score so far is 0.866752.

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/manhattanofficelease/Manhattan%20Office%20Real%20Estate.ipynb">Estimating Manhattan Office Rental Rates</a><br>
I construct an 11 feature dataset of 1369 Manhattan office rentals, of which 539 have listed rental rates in $/sqft/year. With the 539 observation training set, I convert addresses and strings into quantitative data, and engineer features to try to create a predictive model of the remaining 830 prices.

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/mercariprice/Price%20Suggestions.ipynb">Mercari Price Suggestion</a><br>
With data from the <a href="https://www.kaggle.com/c/mercari-price-suggestion-challenge">Mercari Price Suggestion Challenge</a>, I... uh challenge myself to suggest prices. Currently in the top 33% after one submission, a lot of room to improve. If only I could use the same batch sizes on my computer as the Kaggle kernel. Time to get that GTX 1080ti...

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/toxiccomments/Toxic%20Comments%20Classification.ipynb">Toxic Comments Classification</a><br>
A quick look at multilabel classification with different forms of <a href="https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge">toxic internet comments</a> using logistic regression, NB-SVM, as well as convolutional and recurrent neural networks with the Keras API running on a TF backend. There were a bunch of problems with this competition: first the original test set was leaked, then the new test set had a different distribution than the original, leading to useless validation scores, and a lot of focus on making adjustments to the prediction results (to fit the new distribution), then finally a switch over to AUC that messed up all the scores.

### Visualization and Other Stuff

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/yfsent/Yahoo%20Finance%20Headlines.ipynb">Scoring Yahoo Finance Headlines</a><br>
Yahoo Finance is one of the company's few remaining products that is actually very good, but support has been reduced greatly, and it no longer lets us specify a date range for headlines. By default, the page only displays 25 and more is injected onto the page when you scroll down, so I use Selenium and Google's net logging to get the json URLs and access them directly. The json contains more data than what actually shows up on the page (and the exact date), so this could be pretty useful. These headlines are then converted into sentiment scores.

<a href="http://nbviewer.jupyter.org/github/keithqu/dsp/blob/master/gasprices/gas%20prices.ipynb">Greater Toronto Area Gas Map</a><br>
Scrapes a comprehensive set of gas price information for the Toronto area and visualizes it with Folium. Includes some light analysis: gas stations within 100m of a Starbucks tend to charge 0.6 cents more for regular gas!

<a href="http://nbviewer.jupyter.org/github/keithqu/illustrative/blob/master/K%20Means%20Iteration.ipynb">Iterative K Means</a><br>Showcases how K Means clustering finds new centroids and labels with each iteration.
