import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import spacy
from spacy.lang.el.stop_words import STOP_WORDS
import base64
#import mysql.connector  ##history
import pandas as pd
#import webbrowser
import nltk.sentiment.vader as vd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


# mydb = mysql.connector.connect(host = "remotemysql.com",  #connect to database
#             user = "ywNaDEUMs0",
#             password = "z3FwsBlKs8" , 
#             database = "ywNaDEUMs0"      
#         )
main_bg = "bg3.png"
main_bg_ext = "png"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: white
    }}
    """,
    unsafe_allow_html=True
)  
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: ##000000;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)


@st.cache(allow_output_mutation=True)
def get_nlp_model(path):
    return spacy.load(path)

def generate_output(text):
     cats = nlp(text).cats
     c="Real"
     if cats['FAKE'] > cats['REAL']:
         st.markdown("<h1><span style='color:red'>❌ This Is A Fake News Article!👎</span></h1>",
                     unsafe_allow_html=True)
         c="Fake"
     else:
         st.markdown("<h1><span style='color:green'>✅ This is a real news article!👍</span></h1>",
                     unsafe_allow_html=True)
    
    #  mycursor = mydb.cursor()                      #getting the username 
    #  mycursor.execute("SELECT username FROM ywNaDEUMs0.current WHERE number='1'")
    #  y=mycursor.fetchall()  
    #  x=y[0]
    #  x=list(x)
    #  x=str(x[0])
    #  sql = "INSERT INTO ywNaDEUMs0.users (text,class,username) VALUES (%s,%s,%s)"  #storing
    #  val = (text,c,x)
    #  mycursor.execute(sql, val)
    #  mydb.commit()
     q_text = '> '.join(text.splitlines(True))
     q_text = '> ' + q_text
   

def generate_output1(text):
     cats = nlp1(text).cats
     c="Real"
     if cats['FAKE'] > cats['REAL']:
         st.markdown("<h1><span style='color:red'>❌ This Is A Fake News Article!👎</span></h1>",
                     unsafe_allow_html=True)
         c="Fake"
     else:
         st.markdown("<h1><span style='color:green'>✅ This is a real news article!👍</span></h1>",
                     unsafe_allow_html=True)

    #  import mysql.connector  ##history
    #  mydb = mysql.connector.connect(host = "remotemysql.com",
    #         user = "ywNaDEUMs0",
    #         password = "z3FwsBlKs8" , 
    #         database = "ywNaDEUMs0"      
    #     )
    #  mycursor = mydb.cursor()
    #  sql = "INSERT INTO ywNaDEUMs0.users (text,class,username) VALUES (%s,%s,%s)"  #storing
    #  val = (text,c,x)
    #  mycursor.execute(sql, val)
    #  mydb.commit()
     q_text = '> '.join(text.splitlines(True))
     q_text = '> ' + q_text
    

def view_senti(text):
    score=sid.polarity_scores(text)
    sentiment = max(zip(score.values(), score.keys()))[1]
    if(sentiment=="pos"):
        st.markdown("<h2><span style='color:red'>The Sentiment of the news article is Positive 😊 </span></h2>",
                     unsafe_allow_html=True)
    elif(sentiment=="neg"):
        st.markdown("<h2><span style='color:red'>The Sentiment of the news article is Negative 😞 </span></h2>",
                     unsafe_allow_html=True)

    elif(sentiment=="neu"):
        st.markdown("<h2><span style='color:red'>The Sentiment of the news article is Neutral 😐 </span></h2>",
                     unsafe_allow_html=True)


#def log_out():
    

    #mycursor = mydb.cursor()                      #deleting in currenty
    #mycursor.execute("DELETE FROM mydatabase.current WHERE number='1'")
    #mydb.commit()
    #chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
    #webbrowser.get(chrome_path).open('login.html') 

# def view(x):
#     mycursor = mydb.cursor() 
#     sql = "SELECT text,class from ywNaDEUMs0.users WHERE username IN(SELECT username FROM ywNaDEUMs0.users INTERSECT SELECT username FROM ywNaDEUMs0.current)"
#     mycursor.execute(sql)
#     df=pd.DataFrame()
#     myresult = mycursor.fetchall()
#     t=[]
#     c=[]
#     for i in myresult:
#         t.append(i[0])
#         c.append(i[1])
#     df["Searches"]=t
#     df["Class"]=c
#     df = df.style.set_properties(**{
#     'background-color': 'white',
#     'font-size': '20pt',
#     'border-size': '2px',
#     'border-color':'black'
#     })
#     st.table(df)



  


#      wc = WordCloud(width = 1000, height = 600,
#                     random_state = 1, background_color = 'white',
#                     stopwords = STOP_WORDS).generate(text)

#      fig, ax = plt.subplots()
#      ax.imshow(wc)
#      ax.axis('off')
#      st.pyplot(fig)
#      print(cats)

nlp = get_nlp_model('model')
nlp1=get_nlp_model('modeltaliban')

# import mysql.connector  ##history
# mydb = mysql.connector.connect(host = "remotemysql.com",
#             user = "ywNaDEUMs0",
#             password = "z3FwsBlKs8" , 
#             database = "ywNaDEUMs0"      
#         )
# mycursor = mydb.cursor()                      #getting the username 
# mycursor.execute("SELECT username FROM ywNaDEUMs0.current WHERE number='1'")
# y=mycursor.fetchall()  
# x=y[0]
# x=list(x)
# x=str(x[0])

st.set_option('deprecation.showfileUploaderEncoding', False)   
strwelcome="WELCOME! "#+str(x)  

st.sidebar.title(strwelcome)
st.sidebar.image: st.sidebar.image("side.png", use_column_width=True)
add_selectbox = st.sidebar.radio("Go to", ("Home","COVID-19", "Afghanistan","My History","About Us"))  



# if st.sidebar.button("Log out"):
#     mycursor = mydb.cursor()                      #deleting in current 
#     mycursor.execute("DELETE FROM ywNaDEUMs0.current WHERE number='1'")
#     mydb.commit()
#     url = 'https://github.com/aryashah2k/FakeNewsDetectionSpacy/blob/main/login.html'        #Paste the URL for login.html
#     webbrowser.open_new_tab(url)


    #st.balloons()
if add_selectbox=="Home":
    st.markdown("<h1 style='text-align: center; color: black;'>WHY FAKE NEWS DETECTION?</h1>", unsafe_allow_html=True)
    st.subheader("  \n")
    st.subheader("\nWith our world producing an ever-growing huge amount of data exponentially per second by machines, there is a concern that this data can be false. Fake news is not new, but it's never been so pervasive or harder to spot."+"\n It is mainly propagated through digital forms of communication such as edited videos, memes, unverified advertisements and social media propagated rumours. Fake news spread through social media in the country has become a serious problem, with the potential of it resulting in mob violence, as was the case where at least 20 people were killed in 2018 as a result of misinformation circulated on social media. Many people have also been arrested for spreading fake news about sensitive issues such as the coronavirus pandemic. The following bar graph shows the number of fake news propagation offences recorded across India in 2020. ")
    st.image("cov.png", use_column_width=True)
    st.subheader("An easy guide to help you detect fake news:")
    st.image("bar.png", width=520)


elif add_selectbox == "COVID-19":
    st.markdown("<h2 style='text-align: center; color: black;'>FAKE NEW DETECTION SYSTEM</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: orange;'>COVID-19</h1>", unsafe_allow_html=True)
    text = st.text_input("Enter the headline here")

    if st.button("Run"):
        generate_output(text)
        st.balloons()
    if st.button("View Sentiment"):
        view_senti(text)
        
elif add_selectbox == "Afghanistan":
    st.markdown("<h2 style='text-align: center; color: black;'>FAKE NEW DETECTION SYSTEM</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: blue;'>AFGHANISTAN</h1>", unsafe_allow_html=True)
    text = st.text_input("Enter the headline here")
    if st.button("Run"):
        generate_output1(text)
    if st.button("View Sentiment"):
        view_senti(text)

# elif add_selectbox == "My History":
#     st.markdown("<h2 style='text-align: center; color: black;'>FAKE NEW DETECTION SYSTEM</h2>", unsafe_allow_html=True)
#     st.markdown("<h1 style='text-align: center; color: green;'>MY HISTORY</h1>", unsafe_allow_html=True)
#     view(x)
elif add_selectbox=="About Us":
    st.markdown("<h1 style='text-align: center; color: black;'><u>ABOUT US</u></h1>", unsafe_allow_html=True)
    st.subheader("  \n")
    st.write("\n\nThis website was created with an aim to help combat the growing problem of fake news, especially the kind that creates panic and causes distress in already difficult times.")
    st.write("Keeping in sync with the current events, we have created specially designed fake news detection models for the topics of COVID-19 and the current events of Afghanistan.The models are trained on topic-specific data in order to be able to deliver an output that is closest to the truth. A sentiment analysis is also added, in order to help the user gauge a fake new's intention, so that the fake news spread to trigger hatred or false hope is identified as it is.")
    st.write("In the future, we hope to expand the scope of our project to encompass other topics and contribute further to the greater cause , that is to combat fake news.")
    st.subheader("  \n")
    st.subheader("  \n")
    st.markdown("<h3 style='text-align: center; color: black;'><u>OUR TEAM</u></h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>\n Rajashree Pati | Aishwarya Pimplikar | Khushi Vora | Arya Shah</h3>", unsafe_allow_html=True)







