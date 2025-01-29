import streamlit as st
import pandas as pd

primaryColor = "purple"
backgroundColor = "#F5F5F5"
secondaryBackgroundColor = "#E0E0E0"
textColor = "#262730"
font = "sans serif"

# Title of the app
st.title("Kelebohile Lehloenya's Talking Stage Page")

# Collect basic information
st.header("Basic Information")
st.write("Name : Kelebohile Lehloenya")
st.write("Field : Environmental & Geospatial Sciences")
st.write("Institution : North West University")

# Display basic profile information
st.header("Bachelorette Overview")
st.image("lebo.jpg", caption="Physical attributes of species", use_column_width=True)
st.write("**About Kelebohile:** Kelebohile also fondly known as Lebo, is female. Her interests are chess, jazz, RnB, South African pop and Gospel. Her favourite colour is purple. Her favourite sports are tennis and chess (she cannot play either). On her down time, she enjoys to nap. She enjoys romantic, pyscho-thrillers, Black History and religious movies. Lebo does not have a star sign, she is a child of GOD. But if interested on buying her a present, her birthday is on May 12th.")
st.write("**Height:** 170 cm")
st.write("**Weight:** 50 kg")

st.header("Bachelorette's Best Moments")
images = ["lebo2.jpg", "lebo3.jpg", "lebo4.jpg", "lebo5.jpg"]
for image in images:
    st.image(image, use_column_width=True)
    
st.header("Hurry Up! Its Almost Valentine's Day")
    
from datetime import datetime

valentines_day = datetime(2025, 2, 14)

now = datetime(2025, 1, 29)  

time_difference = valentines_day - now

days = time_difference.days
hours, remainder = divmod(time_difference.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.write(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds left until Valentine's Day!")

if time_difference.total_seconds() <= 0:
    st.write("Happy Valentine's Day!")

# Display the countdown
st.write(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds left until Valentine's Day!")

if time_difference.total_seconds() <= 0:
    st.write("Happy Valentine's Day!")
# Add a section for publications
st.header("Apply to Date the Bachelorette")
name = st.text_input("Name")
age = st.number_input("Age", min_value=23, max_value=100)
interests = st.text_area("Tell us about your interests")

st.header("Potential CV submissions")
uploaded_file = st.file_uploader("Upload your CV here (including matric certficate, 3 months bank statement and at least 2 affidavits from previous relationships)", type="pdf")
if st.button("Submit"):
    st.write("Thank you for your submission!")
if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    

# Add a contact section
st.header("Contact Information")
email = "kelebohilelehloenya@gmail.com"
st.write(f"You can reach Kelebohile at {+27747057039}.")

st.write("Thank you for your submission!")


