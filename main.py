import streamlit as st 
from gpt_connection import chat_with_chatgpt
# main code comes here

st.header("Demo E-commerce platform")
# putting one dropdown here
with st.expander(label = "how app works",expanded=False):
    st.write("""This app uses customer order history and personal profile to provide targeted  description of the
             product user is searching for. This technology increases the consumer engagment and likliehod of consumer buying the 
             product. The reason is personalized product description and not the general one , giving the feel 
             that product is meant for the customer
             """)

user_type = st.text_input("Enter the Customer profession, i.e , doctor , student, None") # info - 1
order_history = st.text_input("Enter user order hstory i.e , books, markers, shoes , t-shirt")  # info - 2



user_input =  st.selectbox("Select Product", ['', '5 AM CLUB BOOK','Smart Watch','Laptop','Protein Powder',
                                              'Shoes','Peanut Butter'])
run_button =   st.button("Run")
# sidebar
with st.sidebar:
    st.subheader("Steps to Use the app")
    st.write("1. Enter the user profession , or leave is blank")
    st.write("2. Enter the user previous order history")
    st.write("3. select the demo product")
    # result
    st.subheader("Result")
    st.write("A PERSONALIZED PRODUCT DESCRIPTION CAN BE SEEN !!!")
# inserting image
col1 , col2, col3 = st.columns([3,4,2])


if(run_button and user_input != "" and order_history  != ""):
    print(user_input, order_history)
    # inserting image here
    product_details = "" 
    if(user_input == "5 AM CLUB BOOK"):
        with col2:
            st.image("images/5_am/1.jpg",width = 200)
            product_details = ""

            
    if(user_input == "Smart Watch"):
        with col2:
            st.image("images/smart_watch/1.jpg",width = 200)
            product_details = "Apple Watch SE (2nd Gen) [GPS 44 mm] Smart Watch w/Midnight Aluminium Case & Midnight Sport Band. Fitness & Sleep Tracker, Crash Detection, Heart Rate Monitor, Retina Display, Water Resistant"
            
    
    if(user_input == "Laptop"):
        with col2:
            st.image("images/laptop/1.jpg",width = 200)
            product_details = "HP Victus Gaming Laptop, 12th Gen Intel Core i5-12450H, NVIDIA RTX 3050 GPU, 15.6-inch (39.6 cm), FHD, IPS, 144Hz, 9 ms Response time, 16GB DDR4, 512GB SSD, Backlit KB (MSO, Blue, 2.29 kg) fa0666TX"
    if(user_input == "Protein Powder"):
        with col2:
            st.image("images/protein/1.jpg",width = 200)
            product_details = "ptimum Nutrition (ON) Gold Standard 100% Whey (2 lbs/907 g) (Double Rich Chocolate) Protein Powder for Muscle Support & Recovery, Vegetarian - Primary Source Whey Isolate"
    if(user_input == "Shoes"):

        with col2:
            st.image("images/shoes/1.jpg",width = 200)
            product_details = "Mens Run Steady M Running Shoe"
    
    if(user_input == "Peanut Butter"):
        with col2:
            st.image("images/peanut_butter/1.jpg",width =200)
            product_details = "MYFITNESS Chocolate Peanut Butter Smooth 1250g | 22g Protein | Tasty & Healthy Nut Butter Spread |Vegan| Dark Chocolate | Cholesterol Free, Gluten Free| Smooth Peanut Butter | Zero Trans Fat"


    
    # framing the querry for result
    query = "Write a  effictive and engaging description under 200 words product description   of {} our target customer are {}, product details are {}  , user had order history of {}".format(user_input, user_type,product_details, product_details)
    #        Write a  effictive and engaging description under 200 words product description , of Peanut Butter our main customers are old people, product details are MYFITNESS Chocolate Peanut Butter Smooth 1250g | 22g Protein | Tasty & Healthy Nut Butter Spread |Vegan| Dark Chocolate | Cholesterol Free, Gluten Free| Smooth Peanut Butter | Zero Trans Fat
    data = chat_with_chatgpt(query)
    st.write(data)
    st.button("buy")