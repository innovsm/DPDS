import streamlit as st 
from gpt_connection import chat_with_chatgpt


# main code comes here

st.header("Descriva")
# user - type ---> 
user_type = st.text_input("Enter the Customer professio","i.e Student, Businessman, etc")
user_input =  st.selectbox("Select Product", ['', '5 AM CLUB BOOK','Smart Watch','Laptop','Protein Powder',
                                              'Shoes','Peanut Butter'])
run_button =   st.button("Run")
# sidebar
with st.sidebar:
    st.subheader("About Internal Working")
    st.write("Imagine exploring a product, and within moments, the description mirrors your interests, uses your preferred tone, and highlights features that matter to you most. This personal touch is made possible by our advanced AI, which constantly learns from your interactions and feedback So, how does it work? It's simple yet powerful: Descriva listens to your digital cues, understands your unique needs, and crafts descriptions that speak directly to you. With Descriva, your online shopping experience is not just personalized; it's an enjoyable journey designed with you in mind.")

# inserting image
col1 , col2, col3 = st.columns([3,4,2])


if(run_button and user_input != "" and user_type  != ""):
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
    query = "Write a  effictive and engaging description under 200 words product description   of {} our target customer are {}, product details are {}".format(user_input, user_type,product_details)

    data = chat_with_chatgpt(query)
    st.write(data)

