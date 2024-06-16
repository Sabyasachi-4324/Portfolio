import streamlit as st
import webbrowser as wb
import time
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_javascript import st_javascript

icon = Image.open("images/portfolio_icon.png")
st.set_page_config(page_title="Portfolio", page_icon=icon, layout="centered")


def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css("assets/style.css")

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

if navigation == "Home":
    def typewrite(text:str):
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

    text = "WELCOME TO MY PORTFOLIO WEBSITE.."
    typewrite_txt = typewrite(text)
    components.html(typewrite_txt, height=40)

    about = """I am Sabyasachi Mohanty, a highly motivated and detail-oriented individual with a strong foundation in Computer Engineering, having MCA graduated from ITER, S'O'A University. 
    My passion lies in the vast and evolving realm of artificial intelligence. In addition to my academic background, 
    I have honed my skills in various domains, including C, Java, Machine Learning, Deep Learning, and web development.
    """
    typewrite_abt = typewrite(about)
    col1, col2 = st.columns(2)

    profile = Image.open("images/profile.jpg")
    
    time.sleep(2)

    st.markdown("""
        <style>
                img {
                    margin-top: 50px;
                    border-radius: 50%;
                    width: 300px;
                }

        </style>
        """, unsafe_allow_html=True)
    
    with col1:
        st.image(profile)
    with col2:
        components.html(typewrite_abt, height=400)
    

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

    with col1:
        st.image(cards[0]['image'], width=220)
        st.markdown(f"[{cards[0]['title']}]({cards[0]['link']})")

    with col2:
        st.image(cards[1]['image'], width=220)
        st.markdown(f"[{cards[1]['title']}]({cards[1]['link']})")

    with col3:
        st.image(cards[2]['image'], width=210)
        st.markdown(f"[{cards[2]['title']}]({cards[2]['link']})")

    if st.button("Learn More..."):
        url = "https://www.linkedin.com/in/sabyasachi-mohanty-42234528b/"
        js = f'window.open("{url}", "_blank").then(r => window.parent.location.href);'
        st_javascript(js)


if navigation == "Competitions":
    st.write("### :medal: Competitions")
    st.markdown(
    """
    <style>
    a {
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
        "title": "Kaggle ML Challenge",
        "image": "images/kaggle.jpg",
        "link": ""
    },
    {
        "title": "BTK Academy Datathon",
        "image": "images/btk.png",
        "link": "https://github.com/ahmetdzdrr/Apple-Stock-Price-Forecasting"
    },
]

    col1, col2 = st.columns(2)

    with col1:
        st.image(cards[0]['image'])
        st.markdown(f"[{cards[0]['title']}]({cards[0]['link']})")

    with col2:
        st.image(cards[1]['image'])
        st.markdown(f"[{cards[1]['title']}]({cards[1]['link']})")


if navigation == "Contact":
    st.write("### :mailbox_closed: Get In Touch With Me!")

    contact_form = """
    <form action="https://formsubmit.co/mohanty.sabyasachi16@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" style="resize: none;" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    media = [
    {
        "title": "Linkedin",
        "image": "images/linkedin.png",
        "link": "https://www.linkedin.com/in/sabyasachi-mohanty-42234528b/"
    },
    {
        "title": "GitHub",
        "image": "images/github.png",
        "link": "https://github.com/Sabyasachi-4324"
    },
    {
        "title": "Kaggle",
        "image": "images/kaggle.png",
        "link": "https://www.kaggle.com/calumdemon"
    },
]

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    st.markdown(
    """
    <style>
    img {
        margin-top: 80px;
        width: 40px;
        margin-left: 50px;
    }
    p {
        margin-top: 85px;
        margin-right: 25px;
        color: white !important;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True)

    col1.image(media[0]['image'])
    col2.markdown(f"[{media[0]['title']}]({media[0]['link']})")

    col3.image(media[1]['image'])
    col4.markdown(f"[{media[1]['title']}]({media[1]['link']})")

    col5.image(media[2]['image'])
    col6.markdown(f"[{media[2]['title']}]({media[2]['link']})")

    
