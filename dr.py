import streamlit as st

def main():
    st.title("Streamlit POST Request Example")

    with st.form(key='my_form'):
        text_input = st.text_input("Enter some text:")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            # Handle the POST request data
            st.success(f"Received POST request with text: {text_input}")

if __name__ == '__main__':
    main()


