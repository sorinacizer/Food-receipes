'''Generate food receipes by giving an examples of what ingredients do you have in the fridger'''

__auther__ = 'Sorina Ivan'
__maintainer__ = 'Sorina Ivan'
__email__ = 'sorina.cizer@gmail.com'

__all__ = []

from st_pages import hide_pages
import streamlit as st
import sqlite3
st.image("food.jpg")
st.title("Food receipes")

def app():
    st.title(f'Welcome to Generator of food receipes!')


    menu = ["Home", "Login", "Register"]
    choise = st.sidebar.selectbox("Menu", menu)
    hide_pages("receipes.py")

    if choise == "Home":
        st.subheader(f"This is an app, that help you prepare your meal! \n Just enter your favorites ingredients that you want to use in your dish."
                     " \n First you need to make sure you are registered and the logged in!")
    elif choise == "Login":
        st.subheader("Login")

        username = st.text_input("User Name: ")
        password = st.text_input("Password: ", type='password')
        if st.button("Login"):
            conn = sqlite3.connect('food_receipes_db.db')

            cur = conn.cursor()
            find_user = 'SELECT * from Users_Data WHERE user_name = ? and password = ?'
            cur.execute(find_user, [username, password])
            result = cur.fetchall()
            for rez in result:
                st.success("{} succesfully logged in!".format(username))
                st.switch_page("pages/receipes.py")
            else:
                st.text("{} user is not registered!".format(username))

            conn.commit()
            conn.close()

    elif choise == "Register":
        st.subheader("Create new account")

        new_user = st.text_input("Username: ")
        new_password = st.text_input("Password: ", type='password')
        new_email = st.text_input("Email: ")

        if st.button("Register"):
            if new_password:
                #Create DB or connect to DB
                conn = sqlite3.connect("food_receipes_db.db")

                #Create cursor
                curs = conn.cursor()

                #Create table
                curs.execute('''CREATE TABLE IF NOT EXISTS Users_Data
                (user_name TEXT,
                password TEXT,
                email TEXT)''')

                curs.execute('INSERT INTO Users_Data VALUES(?, ?, ?)',
                             (new_user, new_password, new_email))

                conn.commit()
                conn.close()

            st.success("You have successfully created an valid account!")
            st.info("Go to Login menu to login!")

if __name__ == "__main__":
    app()