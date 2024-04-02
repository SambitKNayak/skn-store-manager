# example--

# import streamlit as st
# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI

# # Select database and collection
# db = client["store_manager"]
# collection = db["inventory"]

# # Function to insert data into MongoDB
# def insert_data(name, quantity, price):
#     data = {"name": name, "quantity": quantity, "price": price}
#     try:
#         collection.insert_one(data)
#         st.success("Data inserted successfully")
#     except Exception as e:
#         st.error(f"Error: {e}")

# # Main function
# def main():
#     st.title("Store Manager with MongoDB")

#     # Get user input for inserting data
#     name = st.text_input("Product Name")
#     quantity = st.number_input("Quantity", min_value=0, step=1)
#     price = st.number_input("Price", min_value=0.0, step=0.01)

#     # Insert data when the user clicks the button
#     if st.button("Add Product"):
#         insert_data(name, quantity, price)

# # Run the main function
# if __name__ == "__main__":
#     main()

# ------------------------------------------
# import streamlit as st
# from pymongo import MongoClient
# import os

# # Load secrets
# st.secrets.load_config()

# # Get MongoDB connection string from secrets
# MONGODB_URI = st.secrets["my_mongodb_secrets"]["uri"]

# # Connect to MongoDB
# client = MongoClient(MONGODB_URI)

# # Select database and collection
# db = client["your_database_name"]
# collection = db["your_collection_name"]

# # Function to insert data into MongoDB
# def insert_data(name, quantity, price):
#     data = {"name": name, "quantity": quantity, "price": price}
#     try:
#         collection.insert_one(data)
#         st.success("Data inserted successfully")
#     except Exception as e:
#         st.error(f"Error: {e}")

# # Main function
# def main():
#     st.title("Store Manager with MongoDB")

#     # Get user input for inserting data
#     name = st.text_input("Product Name")
#     quantity = st.number_input("Quantity", min_value=0, step=1)
#     price = st.number_input("Price", min_value=0.0, step=0.01)

#     # Insert data when the user clicks the button
#     if st.button("Add Product"):
#         insert_data(name, quantity, price)

# # Run the main function
# if __name__ == "__main__":
#     main()

# -- with this create --> .stream folder --> secret.toml file--> 
# [my_mongodb_secrets]
# uri = "mongodb+srv://skntuserate:IM7VSGtvs24aNjKC@skn.vqbhvfp.mongodb.net/"
# -------------------------------------------------------------------------------------------

import streamlit as st
from pymongo import MongoClient

# MongoDB connection string
MONGODB_URI = "mongodb+srv://skntuserate:IM7VSGtvs24aNjKC@skn.vqbhvfp.mongodb.net/"

# Connect to MongoDB
client = MongoClient(MONGODB_URI)

# Select database and collection
db = client["store"]  # Replace "your_database_name" with your actual database name
collection = db["inventory"]  # Replace "your_collection_name" with your actual collection name

# Function to insert data into MongoDB
def insert_data(name, quantity, price):
    data = {"name": name, "quantity": quantity, "price": price}
    try:
        collection.insert_one(data)
        st.success("Data inserted successfully")
    except Exception as e:
        st.error(f"Error: {e}")

# Main function
def main():
    st.title("Store Manager with MongoDB")

    # Get user input for inserting data
    name = st.text_input("Product Name")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    price = st.number_input("Price", min_value=0.0, step=0.01)

    # Insert data when the user clicks the button
    if st.button("Add Product"):
        insert_data(name, quantity, price)

# Run the main function
if __name__ == "__main__":
    main()
