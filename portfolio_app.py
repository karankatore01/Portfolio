import streamlit as st
from PIL import Image
import base64


# ---- PAGE CONFIG ----
st.set_page_config(page_title="Karan Katore | Data Scientist", layout="wide")

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
#         background-attachment: fixed;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# ---- SIDEBAR ----
with st.sidebar:
    st.image("profile.jpg", width=400)  # optional
    st.title("Karan Katore")
    st.markdown("📧 karankatore01@gmail.com")
    st.markdown("📞 +91 8956069192")
    st.markdown("[LinkedIn](https://linkedin.com/in/karan-katore-3a3280243)")
    st.markdown("[GitHub](https://github.com/karankatore01)")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>👋 Hi, I'm Karan Katore</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>AI Developer | Machine Learning Engineer | Data Scientist</h4>", unsafe_allow_html=True)
st.markdown("---")

# ---- HEADER WITH GIF ----

# def gif_header(gif_path):
#     file_ = open(gif_path, "rb")
#     contents = file_.read()
#     data_url = base64.b64encode(contents).decode("utf-8")
#     file_.close()

#     st.markdown(
#         f"""
#         <div style="position: relative; text-align: center;">
#             <img src="data:image/gif;base64,{data_url}" 
#                  style="width: 100%; max-height: 300px; object-fit: cover; border-radius: 10px;" />
#             <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white;">
#                 <h1 style="font-size: 3em; margin: 0;">👋 Hi, I'm Karan Katore</h1>
#                 <h4 style="font-size: 1.5em; margin-top: 10px;">AI Developer | ML Engineer | Data Scientist</h4>
#             </div>
#         </div>
#         <br>
#         """,
#         unsafe_allow_html=True
#     )

# # Call the function with your GIF filename
# gif_header("cover_img.gif")



# ---- ABOUT ----
st.header("🧑‍💻 About Me")
st.write("""
I am an aspiring software engineer with expertise in AI, Machine Learning, and NLP.  
I build real-world solutions using LLMs, RAG, and predictive modeling, and have deployed projects using Flask, FastAPI, and AWS Lambda.
""")

# ---- SKILLS ----
st.header("🛠️ Technical Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Languages")
    st.write("Python, C++, Java, SQL, HTML/CSS, JavaScript")

with col2:
    st.subheader("AI/ML Tools")
    st.write("TensorFlow, Scikit-learn, Keras, PyTorch, Transformers, Hugging Face")

with col3:
    st.subheader("Other Tools")
    st.write("Flask, FastAPI, LangChain, Git, AWS (Lambda, EC2, S3), Power BI")

# ---- PROJECTS ----
st.header("📊 Projects")

# Project 1
with st.expander("🔹 Retrieval-Augmented Generation (RAG) AI Chatbot"):
    st.write("""
    - Built an intelligent chatbot using **LangChain**, **FAISS**, and **OpenAI API**  
    - Deployed on **AWS Lambda** via **Flask** for scalable responses  
    - Improved context relevance by 30% over baseline
    """)
    st.markdown("[GitHub Repo](https://github.com/karankatore01/rag-chatbot)")

# Project 2
with st.expander("🔹 Detecting Deceptive Feedback Using AI"):
    st.write("""
    - Trained SVM and Random Forest models on 50,000+ feedback samples  
    - Deployed with Flask + JavaScript dashboard for real-time monitoring  
    - Achieved 25% better fraud detection than traditional methods
    """)
    st.markdown("[GitHub Repo](https://github.com/karankatore01/Detecting_deceptive_feedback_using-_AI)")

# Project 3
with st.expander("🔹 Age and Gender Detection"):
    st.write("""
    - Used **VGG-16 + Keras** to predict age & gender from images  
    - Deployed on cloud for real-time inference  
    - Accuracy: 90% (gender), 85% (age)
    """)
    st.markdown("[GitHub Repo](https://github.com/karankatore01/Age-and-Gender-detection)")

# ---- EDUCATION ----
st.header("🎓 Education")
st.write("""
**B.Tech in Computer Science and Engineering**  
Sandip University, Nashik (2022–2025)  
CGPA: 8.07/10

**Diploma in Computer Engineering**  
Guru Gobind Singh Polytechnic, Nashik (2019–2022)  
Percentage: 82.57%
""")

# ---- RESUME DOWNLOAD ----
st.header("📄 Download My Resume")

with open("Karan-Katore.pdf", "rb") as file:
    st.download_button(
        label="📥 Download Resume (PDF)",
        data=file,
        file_name="Karan-Katore.pdf",
        mime="application/pdf"
    )

# ---- CONTACT ----
st.header("📬 Contact Me")
contact_form = """
<form action="https://formsubmit.co/karankatore01@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required><br><br>
     <input type="email" name="email" placeholder="Your email" required><br><br>
     <textarea name="message" placeholder="Your message" rows="4" required></textarea><br><br>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)




# ---- FOOTER ----
st.markdown("---")
st.markdown(" Karan Katore ")

