__auther__ = 'Sorina Ivan'
__maintainer__ = 'Sorina Ivan'
__email__ = 'sorina.cizer@gmail.com'

__all__ = []

import streamlit as st
import requests
import pandas as pd


def get_receipe(ingredients, diet):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": st.secrets["api_key"],
        "query": ingredients,
        "diet": diet,
        "addRecipeInstructions": True,
        "addRecipeInformation": True,
        "number": 14,
    }

    response = requests.get(url, params=params)
    return response.json()


def receipe():
    ingredients = st.text_input("Enter your ingredients(comma separated):")
    diet = st.selectbox("Dietary restrictions", ["None", "Vegetarian", "Vegan", "Gluten-Free"])

    if st.button("Generate receipes"):
        if ingredients:
            response = get_receipe(ingredients, diet)
            results = response["results"]
            if len(results) == 0:
                st.write("No receipe found with specified ingredients!")
            else:
                df = pd.DataFrame(results)
                df = df["title"]
                st.write(df)
        else:
            st.write("Enter at least 1 ingredient!")


if __name__ == "__main__":
    receipe()


