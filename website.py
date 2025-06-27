import streamlit as st
from datetime import datetime

# Main Content
st.title("Welcome to My Streamlit App")
st.write("This is a simple Streamlit application.")

st.button("Click Me!")
st.text_input("Enter some text:")
st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.slider("Select a value:", 0, 100, 50)
st.checkbox("Check me out!")
st.radio("Pick one:", ["Choice A", "Choice B", "Choice C"])
st.text_area("Type your message here:")
st.date_input("Select a date:")
st.time_input("Select a time:")
st.file_uploader("Upload a file:")

st.image("https://via.placeholder.com/150", caption="Sample Image")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.markdown("## This is a Markdown section")
st.code("print('Hello, Streamlit!')", language='python')
st.json({"key": "value", "number": 42, "boolean": True})
st.progress(50)

with st.spinner("Loading something..."):
    st.write("Content loaded.")

st.balloons()

# Sidebar Content
with st.sidebar:
    st.title("Sidebar Title")
    st.write("This is a sidebar section.")
    st.button("Sidebar Button")
    st.selectbox("Sidebar Selectbox", ["Item 1", "Item 2", "Item 3"])
    st.slider("Sidebar Slider", 0, 100, 25)
    st.checkbox("Sidebar Checkbox")
    st.radio("Sidebar Radio", ["Option X", "Option Y", "Option Z"])
    st.text_input("Sidebar Text Input")
    st.text_area("Sidebar Text Area")
    st.date_input("Sidebar Date Input")
    st.time_input("Sidebar Time Input")
    st.file_uploader("Sidebar File Uploader")
    st.image("https://via.placeholder.com/100", caption="Sidebar Image")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    st.markdown("### Sidebar Markdown")
    st.code("print('Hello from the sidebar!')", language='python')
    st.json({"sidebar_key": "sidebar_value", "sidebar_number": 100, "sidebar_boolean": False})
    st.progress(75)

    with st.spinner("Loading sidebar content..."):
        st.write("Sidebar content loading...")

    st.balloons()
    st.header("Sidebar Header")
    st.subheader("Sidebar Subheader")
    st.caption("This is a sidebar caption.")
    with st.expander("Sidebar Expander", expanded=True):
        st.write("This is an expandable section in the sidebar.")

    # Use global st.message functions inside sidebar context
    st.success("This is a success message in the sidebar.")
    st.error("This is an error message in the sidebar.")
    st.warning("This is a warning message in the sidebar.")
    st.info("This is an informational message in the sidebar.")

    # Markdown Styling
    st.markdown("**Bold Text in Sidebar**")
    st.markdown("*Italic Text in Sidebar*")
    st.markdown("[Link to Streamlit Documentation](https://docs.streamlit.io/)")
    st.markdown("~~Strikethrough Text in Sidebar~~")
    st.markdown("`Inline Code in Sidebar`")
    st.markdown("```python\n# Code block in sidebar\nprint('Hello, Sidebar!')\n```")
    st.json({"sidebar_data": [1, 2, 3, 4, 5], "sidebar_info": {"key": "value"}})
    st.progress(80)

    st.header("Another Sidebar Header")
    st.subheader("Another Sidebar Subheader")
    st.balloons()
    st.button("Another Sidebar Button")
    st.selectbox("Another Sidebar Selectbox", ["Item A", "Item B", "Item C"])
    st.slider("Another Sidebar Slider", 10, 200, 100)
    st.checkbox("Another Sidebar Checkbox")
    st.radio("Another Sidebar Radio", ["Choice 1", "Choice 2", "Choice 3"])
    st.text_input("Another Sidebar Text Input")
    st.text_area("Another Sidebar Text Area")
    st.date_input("Another Sidebar Date Input")
    st.time_input("Another Sidebar Time Input")
    st.file_uploader("Another Sidebar File Uploader")
    st.image("https://via.placeholder.com/150", caption="Another Sidebar Image")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.markdown("### Another Sidebar Markdown")
