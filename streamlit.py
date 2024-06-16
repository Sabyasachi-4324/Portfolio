import streamlit as st
import webbrowser as wb
import time
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_javascript import st_javascript

# Set page configuration
icon = Image.open("images/portfolio_icon.png")
st.set_page_config(page_title="Portfolio", page_icon=icon, layout="centered")

# Function to load CSS
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file {file_name} not found.")

# Load CSS
load_css("assets/style.css")

# Custom CSS Styles
custom_css = """
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

body {
  padding: 0;
  margin: 0;
  background: #000 !important;
  background-size: cover;
}

button {
  background: #04AA6D !important;
  color: #ffffff;
  border: none !important;
}

button:hover {
  background: #048555 !important;
  border: none !important;
  color: #ffffff !important;
}

#typewrite {
  background: transparent !important;
  position: relative;
  color: transparent;
  font-family: "Courier New", Courier, "Lucida Sans Typewriter", "Lucida Typewriter", monospace;
  font-weight: 700;
  display: flex;
  box-sizing: border-box;
  text-align: justify; /* Justify text */
}
  
#typewrite:after {
  background-color: transparent !important;
  content: attr(data-content);
  line-height: 30px;
  color: #ffffff;
  position: absolute;
  left: 0;
  top:0;
  text-align: justify; /* Justify text */
}

input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; 
  padding: 12px; 
  border: 1px solid #ccc; 
  border-radius: 4px;
  box-sizing: border-box; 
  margin-top: 6px; 
  margin-bottom: 16px; 
  resize: vertical 
}

button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 7px 25px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
"""

# Apply custom CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Sidebar navigation menu
with st.sidebar:       
    navigation = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Competitions", "Contact"],
        icons=["house", "stars", "book", "award", "person-rolodex"],
        orientation="vertical",
        default_index=0,
        styles={
            "container": {
                "align-items": "center",
                "text-align": "center",
                "background": "transparent",
                "margin-top": "20px"
            },
            "icon": {
                "color": "#000", 
                "font-size": "20px"
            },
            "nav-link": {
                "display": "flex",
                "justify-content": "center",
                "align-items": "center",
                "text-align": "center",
                "font-size": "15px",
                "--hover-color": "#7FB1AF",
                "font-weight": "bold",
            },
            "nav-link-selected": {"background-color": "#04AA6D"},
        }
    )

    st.markdown(
        """
        <div style="background-color: transparent; margin-top: 150px; text-align: center;">
            <p style="font-size: 15px; font-weight: bold">
                &copy; 2024 Sabyasachi Mohanty. All Rights Reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Home section
if navigation == "Home":
    def typewrite(text: str):
        try:
            with open("assets/style.css") as f:
                css = f.read()

            with open("assets/main.js") as f:
                js = f.read()

            html = f"""
            <!DOCTYPE html>
            <head>
            <style>
                {css}
            </style>
            </head>
            <body>
                <p id="typewrite" data-content="" style="background-color: transparent;">{text}</p>
                <script>
                    {js}
                </script>
            </body>
            </html>
            """
            return html
        except FileNotFoundError as e:
            st.error(f"File not found: {e}")

    text = "WELCOME TO MY PORTFOLIO WEBSITE.."
    typewrite_txt = typewrite(text)
    components.html(typewrite_txt, height=40)

    about = """I am Sabyasachi Mohanty, a highly motivated and detail-oriented individual with a strong foundation in Computer Engineering, having MCA graduated from ITER, S'O'A University. 
    My passion lies in the vast and evolving realm of artificial intelligence. In addition to my academic background, 
    I have honed my skills in various domains, including C, Java, Machine Learning, Deep Learning, and web development.
    """
    typewrite_abt = typewrite(about)
    col1, col2 = st.columns(2)

    try:
        profile = Image.open("images/profile.jpg")
    except FileNotFoundError:
        st.error("Profile image not found.")
        profile = None
    
    time.sleep(2)

    st.markdown("""
        <style>
            img {
                margin-top: 50px;
                border-radius: 10px; /* Square shape with rounded corners */
                width: 300px;
                height: 300px;
                object-fit: cover; /* Ensure image maintains aspect ratio */
            }
        </style>
        """, unsafe_allow_html=True)
    
    with col1:
        if profile:
            st.image(profile, caption="Profile Image", use_column_width=True)
    with col2:
        components.html(typewrite_abt, height=400)

# Skills section
if navigation == "Skills":

    skills = {
        "Java": 80,
        "C": 60,
        "Visualization": 85,
        "Machine Learning": 75,
        "Deep Learning": 70,
        "SQL": 70,
        "Python": 80,
        "HTML": 85,
        "CSS": 75,
        "Javascript": 60,
    }

    progress_bar_styles = """
        <style>
        p {
            color: white !important;
            margin: 7px 0;
        }
        .progress-bar {
            background-color: #ddd;
            border-radius: 10px;
            margin: 7px 0;
        }
        .progress-bar div {
            background-color: #04AA6D;
            color: white;
            text-align: center;
            border-radius: 10px;
            transition: width 0.3s ease-in-out;
        }
        </style>
    """

    st.write("### :star: Skills")

    # Display skills with progress bars
    st.markdown(progress_bar_styles, unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    for skill, level in skills.items():
        col1.write(skill)
        progress_bar = f'<div style="width: {level}%;"><b>{level}%</b></div>'
        col2.markdown(f'<div class="progress-bar">{progress_bar}</div>', unsafe_allow_html=True)

# Projects section
if navigation == "Projects":
    st.write("### :book: Projects")
    st.markdown(
        """
        <style>
        a {
            text-align: center !important;
            color: white !important;
            text-decoration: none;
        }

        a:hover {
            color: #04AA6D !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    cards = [
        {
            "title": "Plant Disease Prediction",
            "image": "images/plant.jpeg",
            "link": "https://plant-disease-prediction-using-cnn.streamlit.app/"
        },
        {
            "title": "Car Drive-train Prediction",
            "image": "images/car.jpg",
            "link": ""
        },
        {
            "title": "Electricity Demand Forecasting",
            "image": "images/time-series.png",
            "link": "https://github.com/ahmetdzdrr/Time-Series-Forecasting-Electricity-Demand"
        }
    ]

    col1, col2, col3 = st.columns(3)

    for i, card in enumerate(cards):
        image, title, link = card["image"], card["title"], card["link"]
        try:
            img = Image.open(image)
        except FileNotFoundError:
            st.error(f"Image {image} not found.")
            img = None

        if img:
            with [col1, col2, col3][i % 3]:
                st.image(img, use_column_width=True)
                st.markdown(f"[{title}]({link})", unsafe_allow_html=True)
