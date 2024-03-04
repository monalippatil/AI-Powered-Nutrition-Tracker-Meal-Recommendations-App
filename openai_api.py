import json
from openai import OpenAI
import pandas as pd
import streamlit as st

class OpenAIAssistant:
    def __init__(self, openai_client) -> None:
        self.openai_client = openai_client

    def estimate_ingredients(self, prompt) -> dict:
        '''
            - To get this running, you should have your OPENAI_API_KEY stored in your environment variables.
                Details at: 
                    - https://platform.openai.com/docs/quickstart?context=python#:~:text=write%20any%20code.-,MacOS,-Windows
                    - https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key
            - Tutorial: https://platform.openai.com/docs/quickstart?context=python
        '''
        seed = 1234 # to get deterministic estimation
        try:

            completion = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant designed to output JSON with format ingredient: weight (interger type)."},
                    {"role": "user", "content": prompt}
                ],
                seed=seed,
                response_format={ "type": "json_object"}
            )
            estimation = completion.choices[0].message.content
            result = {
                "status": 200,
                "value": estimation
            }
            print(result)
        except Exception as e:
            result = {
                "status": 400,
                "value": "Unfortunately, our app is sleeping now 😴 Please try again when it wakes up 🫣",
                "exception": e
            }
        return result

    def extract_estimation_to_dataframe(self, estimation, df=None, headers=None) -> pd.DataFrame:
        """
            Input: json-like string
            Output: dataframe
        """
        if df is None:
            df = pd.DataFrame()
        if headers is None:
            headers = ["Ingredient", "Estimated weight (g)"]
        try:
            if estimation:
                estimation_dict = json.loads(estimation)
                df = pd.DataFrame(estimation_dict.items(), columns=headers)
        except Exception as e:
            print(e)
        return df

    def estimate_and_extract_dish_info(self, dish_description, prompt, df=None) -> pd.DataFrame:
        """
            Get user's input: str - description of the dish.
            Return a dataframe containin info regarding weights of dish's ingredients.
        """
        if df is None:
            df = pd.DataFrame()
        if dish_description:
            result = self.estimate_ingredients(prompt=prompt)
            if result.get("status") == 200:
                df = self.extract_estimation_to_dataframe(estimation=result.get("value"))
                if not df.empty:
                    st.write(f'Here is our estimated weight of each ingredient for one serving of 🍕 {dish_description} 🍳:')
                    st.dataframe(df)
                else:
                    message = "Sorry, we've tried our best but cannot estimate the ingredients of your dish. Can you try to describe it differently?"
                    st.write(message)
            else:
                st.write(result.get("value"))
                print(result.get("exception"))
        return df