import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if st.session_state["setting_top_bottom"] == "bottom of the list":
        todos.append(todo)
    elif st.session_state["setting_top_bottom"] == "top of the list":
        todos.insert(0, todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

def update_top_bottom():
    index = settings_top_bottom_options.index(st.session_state["setting_top_bottom"])
    settings["setting_top_bottom"] = index
    functions.write_settings(settings)


todos = functions.get_todos()
settings = functions.get_settings()
settings_top_bottom_options = ["top of the list", "bottom of the list"]

col1, col2 = st.columns([0.8,0.2])

with col1:
    st.title("todos")

with col2:
    with st.popover("Settings", icon=":material/settings:", use_container_width=True):
        st.selectbox(label="Add new items to the", label_visibility="visible",
                     options=settings_top_bottom_options,
                     index=settings["setting_top_bottom"], key="setting_top_bottom", on_change=update_top_bottom)

st.write("Enter and complete todos")

st.text_input(label="Enter a new todo", label_visibility="collapsed", placeholder="Enter a new todo...",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
