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
elif conversion_type == 'Weight':
    weight_type = st.selectbox('Select Weight Type', ['Kilograms to Pounds', 'Pounds to Kilograms'])
    if weight_type == 'Kilograms to Pounds':
        kilograms = st.number_input('Enter Kilograms:')
        if st.button('Convert'):
            pounds = kilograms * 2.20462
            st.write(f'{kilograms} Kilograms is equal to {pounds} Pounds')
    elif weight_type == 'Pounds to Kilograms':
        pounds = st.number_input('Enter Pounds:')
        if st.button('Convert'):
            kilograms = pounds / 2.20462
            st.write(f'{pounds} Pounds is equal to {kilograms} Kilograms')
elif conversion_type == 'Temperature':
    temperature_type = st.selectbox('Select Temperature Type', ['Celsius to Fahrenheit', 'Fahrenheit to Celsius'])
    if temperature_type == 'Celsius to Fahrenheit':
        celsius = st.number_input('Enter Celsius:')
        if st.button('Convert'):
            fahrenheit = (celsius * 9/5) + 32
            st.write(f'{celsius} Celsius is equal to {fahrenheit} Fahrenheit')
    elif temperature_type == 'Fahrenheit to Celsius':
        fahrenheit = st.number_input('Enter Fahrenheit:')
        if st.button('Convert'):
            celsius = (fahrenheit - 32) * 5/9
            st.write(f'{fahrenheit} Fahrenheit is equal to {celsius} Celsius')
# elif conversion_type == 'Temperature':
#     temperature_type = st.selectbox('Select Temperature Type', ['Celsius to Fahrenheit', 'Fahrenheit to Celsius'])
#     if temperature_type == 'Celsius to Fahrenheit':
#         celsius = st.number_input('Enter Celsius:')   