**Data Dictionary**

Data dictionary can be found [here](./Data_Dictionary.md).


### The Data Science Process

**Problem Statement**

The All-NBA Team selection is one of the most prestigious accolades in the NBA, recognizing the league's top players each season. Being named to an All-NBA Team can significantly impact a player's career, influencing their legacy, contract negotiations, and marketability. It can also heavily influence the trade market and how a general manager constructs a team. 

Predicting which players will be selected for the All-NBA Teams is a complex task that involves analyzing a variety of performance metrics, player attributes, and team dynamics. It requires analyzing different sets of statistical categories, ranging from traditional metrics like points, rebounds, and assists to advanced analytics such as Player Efficiency Rating (PER), Win Shares, and Value Over Replacement Player (VORP). 

The objective of this capstone project is to develop a predictive model that accurately forecasts the players who will be selected to all three All-NBA Teams at the end of the season. This model will utilize player statistics and historical data to make informed predictions. By doing so, it aims to give players, teams, and fans useful insights to help them make better decisions, evaluate talent, and improve performance.

**Scraping/Cleaning**

To gather the necessary data for this project, web scraping techniques were used to extract player statistics and awards information from a reliable source, Basketball Reference. These statistics encompass a wide range of player performance metrics and advanced metrics.

Once the data is collected, thorough cleaning and preprocessing were essential to ensure its quality and usability for analysis and modeling. This involved handling missing values, converting data types as needed, and dealing with duplicate entries for players that were traded mid-season. Cleaning also involved standardizing player names, team names, and other categorical variables to maintain consistency across the dataset. This ensured that the data is ready for analysis and modeling.

All scraping was done on the Basketball Reference website. Player data was scraped back to the 1979-1980 season as that was when the three point line was introduced. More information on the scraping process can be found in the jupyter notebook [Scraping](./01_Functions_EDA.ipynb).

**Model**

Before running any models the correlation between each of the columns and our target variable was looked at [here](./Images/correlation.png). As anticipated, several key variables strongly correlated with All-NBA team selection, including advanced analytics like VORP, Win Shares, and Offensive Win Shares. These metrics provide deeper insights into a player's overall contribution to their team's success, capturing aspects beyond traditional box score statistics. Additionally, traditional metrics such as free throws attempted/made per game, points scored, and made field goals also emerged as significant factors influencing All-NBA team selection. These metrics reflect a player's scoring efficiency and offensive impact, which are essential criteria for evaluating elite performers in the NBA. These correlations confirmed our hypothesis that predicting All-NBA teams involves analyzing a variety of performance metrics, player attributes, and team dynamics. [Here's](./Images/VORP_vs_WS) a scatter plot depicting VORP against win shares, two of our highest correlated metrics. The dotted line serves as a threshold where any data point above or to the right of this line, indicating higher values for both metrics, strongly suggests that the player associated with that point is likely to be on an All-NBA team.

The data was then processed using transformers, specifically applying a standard scaler to normalize the features. In addition, the data underwent multiple pipelines, each incorporating different estimators and oversampling techniques. The oversampling step was crucial to address class imbalance issues within the dataset, ensuring that all classes were adequately represented in the training process. Many pipeliines were then searched over in order to hypertune the parameters using F1 score as our target metric. The most effective model ultimately emerged as a pipeline featuring a standard scaler, SMOTEENN oversampler, and random forest estimator. More information can be found in the jupyter notebook [Modeling](./03_Modeling.ipynb).

**Results**

The pipeline with the standard scaler, SMOTEENN oversampler, and random forest estimator yielded the highest F1 score across all three NBA classes. The F1 score is a measure that combines precision and recall, offering a balanced assessment of a model's accuracy. It considers both false positives and false negatives, making it particularly useful for imbalanced datasets like this one. his pipeline led to a slight decrease in the F1 score for the All-NBA first team by 0.04 compared to our baseline. However, it resulted in improvements of 0.14 and 0.25 in the F1 scores for the All-NBA second team and third team, respectively. despite the slight decrease in the F1 score for the All-NBA first team, the model exhibited no misclassifications of true first-team selections as "no award." Instead, it occasionally misclassified them as second or third-team selections. This indicates that while the model may have marginally missed some first-team selections, it still accurately recognized the elite players deserving of All-NBA recognition. [The confusion matrix for the best pipeline is shown here](./Images/cmd.png)

**Conclusion and Recommendations**

In conclusion, this capstone project aimed to develop a predictive model for forecasting All-NBA team selections based on player performance metrics. By leveraging machine learning techniques and advanced analytics, we successfully built a model that demonstrates promising predictive accuracy. Through data scraping, cleaning, and feature engineering, we extracted meaningful insights from the NBA dataset. The utilization of pipelines, oversampling techniques, and model evaluation strategies enabled us to mitigate class imbalances and optimize model performance.

Moving forward, there are several ways to enhance the predictive model. First being additional feature engineering. Incorporating additional features such as injury data, salary information, and team performance metrics could provide a more comprehensive understanding of player performance and its influence on All-NBA team selections. Additionally, exploring a wider range of machine learning algorithms and continuing to fine-tune hyperparameters to optimize the model's predictive accuracy. Lastly, implementing dynamic modeling techniques to incorporate real-time updates of player statistics throughout the NBA season would enable the model to adapt to changing dynamics and provide up-to-date predictions as the season progresses.