# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## MMA Fighter Statistical Analysis

# Overview
This project explores the relationship between fighter attributes and success metrics in MMA (Mixed Martial Arts). By analyzing key performance indicators such as striking accuracy, takedown defense, and physical attributes, we aim to uncover what differentiates elite fighters from the rest.

Through statistical analysis and data visualization, this project provides insights into which factors contribute to a fighter's success.

# Objectives
* Identify performance indicators that correlate with higher win percentages.

* Analyze striking vs. grappling efficiency and their impact on fight outcomes.

* Determine if physical attributes like reach-to-height ratio influence success.

* Visualize trends and comparisons between fighters to uncover key patterns.

# Hypotheses

We tested the following five hypotheses using statistical methods:

* Reach-to-Height Ratio – Fighters with a higher reach-to-height ratio tend to have a higher win percentage.

* Strike Accuracy – Fighters with better strike accuracy have higher win percentages.

* Weight Class Impact – Heavyweights may have lower win percentages than lighter fighters due to endurance factors.

* Takedown Defense – Fighters with better takedown defense tend to win more fights.

* Strikes Absorbed – Fighters who absorb fewer strikes per minute have a higher win rate.

# Dataset & Data Preparation

We used a dataset of MMA fighters that includes key statistics such as:

* Physical Attributes: Height, reach, weight class.

* Striking Stats: Significant strikes landed per minute, striking accuracy, strikes absorbed per minute.

* Grappling Stats: Takedown accuracy, takedown defense, submission attempts.

* Win/Loss Records: Total fights, wins, losses, and win percentages.
Dataset obtained from kaggle. https://www.kaggle.com/datasets/asaniczka/ufc-fighters-statistics

# Data Cleaning & Preparation

Data preparation involved:

* Handling missing values and inconsistencies.

* Standardizing numerical values for better comparisons.

* Creating new calculated fields, such as reach-to-height ratio.

* Filtering data to focus on fighters with sufficient fight history.

# Data Visualization & Analysis

Our analysis was conducted in Jupyter Notebooks, focusing on:

* Comparing Fighter Attributes – Box plots and histograms to compare reach, height, and weight class distributions.

* Performance Trends – Scatter plots and regression analysis to examine correlations.

* Striking vs. Grappling Efficiency – Bar charts and heatmaps to compare successful vs. unsuccessful attempts.

* Statistical Testing – Using T-tests to validate hypotheses.#

# Key Findings & Conclusions

* Fighters with a higher reach-to-height ratio showed a slight advantage in striking success, but the correlation was weak.

* Striking accuracy had a strong positive correlation with win percentage, highlighting the importance of precision.

* Heavyweights had negative results, with a clear trend suggesting a disadvantage compared to lighter fighters which could be due many factors such as endurance, mass and skill.

* Takedown defense played a significant role in win rates, as fighters who could keep fights standing generally performed better.

* Strikes absorbed per minute was a crucial factor—fighters who took less damage had significantly higher win rates.

# Next Steps

* Expand the dataset to include more fighters and historical fight data for deeper analysis.

* Incorporate machine learning models to predict fight outcomes based on fighter statistics.

* Opponent-Based Insights: Analyze head-to-head matchups to determine which styles work best against different fighter archetypes.

* Automate Data Updates: Create a pipeline to pull updated fight statistics automatically for continuous analysis.

# Tools & Technologies Used

* Jupyter Notebook for data analysis and visualization.

* Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy) for data manipulation, visualization, and statistical analysis.

* Power BI (Future Enhancement) for interactive reporting.

* Streamlit for building interactive web applications.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

* Set the runtime.txt Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.
