import streamlit as st
st.title('Welcome To The Unit Converter')
st.subheader('Select the type of conversion you want to do:')
conversion_type = st.selectbox('Conversion Type', ['Length', 'Weight', 'Temperature'])
if conversion_type == 'Length':
    length_type = st.selectbox('Select Length Type', ['Kilometers to Miles', 'Miles to Kilometers'])
    if length_type == 'Kilometers to Miles':
        kilometers = st.number_input('Enter Kilometers:')
        if st.button('Convert'):
            miles = kilometers * 0.621371
            st.write(f'{kilometers} Kilometers is equal to {miles} Miles')
    elif length_type == 'Miles to Kilometers':
        miles = st.number_input('Enter Miles:')
        if st.button('Convert'):
            kilometers = miles / 0.621371
            st.write(f'{miles} Miles is equal to {kilometers} Kilometers')