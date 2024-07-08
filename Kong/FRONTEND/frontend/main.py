import streamlit as st
import requests
import os

# Define the FastAPI backend URL from the environment variable
backend_url = os.getenv("API_URL", "http://localhost:8000")

def fetch_todos():
    response = requests.get(f"{backend_url}/todos/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch todos")
        return []

def create_todo(content):
    todo = {"content": content}
    response = requests.post(f"{backend_url}/todos/", json=todo)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to create todo")
        return None

# Streamlit app
st.title("Todo App with Streamlit")

# Input form for new todos
new_todo = st.text_input("Enter a new todo")

if st.button("Add Todo"):
    if new_todo:
        created_todo = create_todo(new_todo)
        if created_todo:
            st.success(f"Todo added: {created_todo['content']}")
            new_todo = ""
    else:
        st.error("Todo content cannot be empty")

# Display the list of todos
st.subheader("Todo List")
todos = fetch_todos()

for todo in todos:
    st.write(f"- {todo['content']}")
