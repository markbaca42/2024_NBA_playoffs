<h1>2024 NBA Playoffs</h1>

<p1>As an avid fan of the NBA and the Dallas Mavericks, I wanted to generate new insights into the Mavericks playoff run. I primarily wanted to find what have been their key to success so far int he playoffs, by exploring which player staticts correlated most with win. Furthermore, I wanted to train a machine learning model on past playoff games in order to predict who will the 2024 NBA Finals. Finally, I wanted to explore the team statics of past champions over the course of the NBA.</p1>

<h2>Data Collection</h2>
<p2>My first step was to collect and clean the data to be used. I was able to collect data from a third party API which had several endpoints to send past and present NBA data. The code I used to collect and store this data into a csv file can be found in getStats.py and getAdvancedStats.py. These files collect data specifc to the 2024 Mavericks playoff run and past data for each NBA team respectfully. The data collect can be found in properally labeled csv files located int the same directory.</p2>

<h2>Correlation Exploration</h2>
<table style="width:100%">
  <tr>
    <th>Player</th>
    <th>Player Statistic</th>
    <th>Correlation Coefficient</th>
  </tr>
  <tr>
    <td>Dereck Lively</td>
    <td>Personal Fouls</td>
    <td>0.60</td>
  </tr>
  <tr>
    <td>Dereck Lively</td>
    <td>Points</td>
    <td>0.55</td>
  </tr>
  <tr>
    <td>Dereck Lively</td>
    <td>Free throw %</td>
    <td>0.48</td>
  </tr>
  <tr>
    <td>Luka Doncic</td>
    <td>Field Goal %</td>
    <td>0.52</td>
  </tr>
  <tr>
    <td>Luka Doncic</td>
    <td>Points %</td>
    <td>0.41</td>
  </tr>
</table>
<p2>To determine what have been the Mavericks' key to winning in the playoffs, I explored which player stats closely correlated to the team winning. In the table above I highlight some of the most interesting findings. First are the stats of the Mavs' eletric rookie. Lively's presesne this season has been what the team has been missing for the past couple of seasons and his effects are highlted in this expierement. His personal fouls and points correlation coefficient reflect the importance the big man brings to the team. His personal fouls correlation coefficient of 0.6 suggest that when the rookie plays aggressive, the mavs' are also likely to win the game. The importance of his dominate play in the paint is furhter highlighted by the correlation coefficient of his points at 0.55. Through exploring these stats, it is clear that the mavs' rookie should  to continue his aggressive play in order to succeed.</p2>
<br></br>
<p2>The correlation coefficients found between Luka's stats and the team winning revealed some interesting findings. As the primary ball handler and scorer on the team, Luka's scoreing stats should correlate highly with the team's success. The data reflected this, however it also revelead that his shot selection may be even more imporant. This is suggested as his field goal percentage more stronlgy correlated with the team winning than his total number of points. Due to this, Mavs' fans should hope he takes smart shots rather than try to force more shots despite having the scoring prowess to warrant low-percentage shots.</p2>
<br></br>
<p2>While the correlation coefficients may be a good indicator of which stats correlate with the Mavericks winning, they do not imply causation. These stats only suggest that as the player statics change, the likelihood of the team winnning trends the same. </p2>

<h2>Logistic Regression</h2>
<table style="width:100%">
  <tr>
    <th></th>
    <th>Precision</th>
    <th>Recal</th>
    <th>F1-score</th
    <th>Support</th>
  </tr>
  <tr>
    <th>Loss</th>
    <th>0.80</th>
    <th>0.83</th>
    <th>0.82</th
    <th>102</th>
  </tr>
  <tr>
    <th>win</th>
    <th>0.83</th>
    <th>0.80</th>
    <th>0.82</th
    <th>106</th>
  </tr>
  <tr>
    <th>accuracy </th>
    <th></th>
    <th></th>
    <th>0.82</th
    <th>208</th>
  </tr>
  <tr>
    <th>macro avg</th>
    <th>0.82</th>
    <th>0.82</th>
    <th>0.82</th
    <th>208</th>
  </tr>
  <tr>
    <th>weighted avg</th>
    <th>0.82</th>
    <th>0.82</th>
    <th>0.82</th
    <th>208</th>
  </tr>
</table>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> </p>

