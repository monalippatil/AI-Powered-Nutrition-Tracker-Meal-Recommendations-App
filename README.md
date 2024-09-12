# A Generative AI Powered Nutrition Tracking and Meal Recommendations App Employing OpenAI API (GPT 3.5) 

## Project Overview

MealMinder is an AI-powered web application designed to simplify nutritional tracking and provide personalized meal recommendations. Built using Streamlit for the frontend and OpenAI's API for personalized meal recommendations, the app offers users a way to easily track their diet, estimate the nutritional content of their meals, and monitor their nutrient intake over time. The app integrates machine learning algorithms to predict health risks such as diabetes based on users' dietary and health habits.

## Business Problem

Chronic diseases driven by poor nutrition pose a significant global health challenge. MealMinder tackles this issue by helping users track their dietary intake and providing actionable insights into their eating habits. Using AI, the app simplifies the process of logging meals, offering personalized guidance to meet nutritional goals.

MealMinder uses data from the Australian Food Composition Database and other reliable health sources to estimate the nutritional content of meals based on user inputs. It also leverages a machine learning model to predict health risks, offering early detection of potential issues such as diabetes.

## Project Objectives

- **Raise Nutritional Awareness**: Translate complex nutritional information into easy-to-understand data for users to improve their health.
  
- **Deliver Personalized Guidance**: Provide custom meal recommendations based on users' dietary preferences and health goals.
  
- **Enable Informed Decision-Making**: Visualize users’ eating habits and trends over time to help them make healthier choices.
  
- **Early Detection of Health Issues**: Use machine learning to predict and highlight potential health risks based on users' data.

## Dataset 

The project integrates several datasets:

- **1. Recommended Nutrient Intake**: Data from the Eat for Health program offering guidance on food portions based on age, gender, and health.
  
- **2. Australian Food Composition Database (AFCD)** : Contains nutritional information for various food items.
  
- **3. Behavioral Risk Factor Surveillance System (BRFSS)**: Survey data on health-related risk behaviors used to train the app's diabetes prediction model.

## Features

- **Nutrient Estimation Using AI**: Estimate nutritional content based on meal names using OpenAI API.

- **Personalized Meal Recommendations**: Recommend meals based on users’ missing nutrients, dietary restrictions, and preferences.

- **Visualizations**: Display intuitive charts showing nutrient intake trends and comparisons to recommended intake.

- **Diabetes Risk Prediction**: Predict health risks such as diabetes using a machine learning model.

- **Secure Authentication**: User authentication system to ensure the privacy and security of sensitive dietary information.


##  Data Science Techniques

- **Data Collection and Preprocessing**: Cleaning data, handling missing values, encoding categorical variables, and feature engineering.

- **Recommendation System**: Powered by the OpenAI GPT-3.5 model to generate meal recommendations based on user preferences and nutritional needs.

- **Visualizations**: Built using Altair to present trends in users' nutrient intake.

- **Machine Learning**: Random Forest Algorithm to predict users’ diabetes risk based on dietary and lifestyle information. The model's performance is evaluated using metrics such as F1-score and confusion matrix.


## Tools and Technologies Used

- **Python**: The core programming language used for data processing, machine learning, and app development.

- **Streamlit**: Used to develop the web-based frontend interface for the application.

- **DuckDB**: Embedded database used to store user and nutritional data securely.

- **OpenAI API**: Utilized to estimate meal ingredients and provide personalized recommendations.

- **Scikit-learn**: Machine learning library used to develop the diabetes risk prediction model.

- **Altair**: Used for creating visualizations of users' nutrient intake data.


This repo is the main source code for our MealMinder App, a nutrition tracking app built and deployed on Streamlit Cloud with the following features:

- User-friendly tools to interpret complex nutritional information: This involves intuitive visualisations, summaries, and comparisons to established dietary guidelines. We developed a clear and easy-to-use interface for entering meals, focusing on simplicity and minimising manual data entry.

- Robust ingredient database and historical nutrient tracking: We built a comprehensive database of foods and their nutritional values by leveraging reliable datasets provided by the Australian government. We enable users to access their historical nutrient intake data from the database and gain personalised insights.

- Ingredient estimation: Our app utilises OpenAI to estimate ingredients based on simple dish names (user input) as opposed to providing a whole list of ingredients manually

- Informative charts: The app developed intuitive charts, and graphs that display historical dietary intake, highlighting trends, deficiencies, and successes.

- Secure authentication: Given the confidential nature of personal nutrition data, we implemented robust login systems with options for authentication.

- Early health issues detection: We also enable users to detect health issues by incorporating external survey data and users’ historical nutrition data using Classification (Random Forest Algorithm).

Here is our little demo video on Youtube, check it out!
[![MealMinder](https://github.com/phamthiminhtu/ilab/assets/56192840/a1218196-8feb-4bea-be93-e3cab18c1206)](https://youtu.be/aIandiLboPo"MealMinder")


# **Prerequisites**
- Install the requirements.txt
- Have an OpenAPI API KEY. Docs:
    - https://platform.openai.com/docs/quickstart?context=python#:~:text=write%20any%20code.-,MacOS,-Windows
    - https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-keyx

- Python 3.7+
-	numpy
-	pandas
- openai
- duckdb
- pytz
- Jinja2
- streamlit
- streamlit-authenticator
- scikit-learn
- altair
- python-Levenshtein
- watchdog

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

The repository is organized as follows:


Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── core
    │   ├── ml_models       <- Random forest model to access diabetes.
    │   ├── sql        		<- Files to interact with the database.
    │   └── *.py            <- All the python notebooks related to project.
    │
    ├── data
    │   ├── images       	<- General Images
    │   └── csv          	<- Below are the dataset files in the csv format.  
    │							nutrients_data.csv
    │							nutrients_per_ingredient.csv
    │							daily_nutrients_recommendation.csv
    │
    │
    ├── images        		<- Images and diagrams form README.md
    │
    ├── unittests          <- Python notebook                           
    │
    ├── reports            <- Final Project Report.pdf
    │ 
    │ 
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, 
                              e.g. generated with `pip freeze > requirements.txt`
                              
