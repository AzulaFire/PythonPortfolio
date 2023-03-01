import feedparser
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import matplotlib.pyplot as plt
import os
# nltk.download('vader_lexicon')

st.set_page_config(page_title="Daily News - Sentiment Analysis", initial_sidebar_state="collapsed", layout="wide")

path = os.path.dirname(__file__)
logo = path + '/logo.png'
oops = path +'/oops.png'
css = path + '/style.css'

with open(css) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

analyzer = SentimentIntensityAnalyzer()


# CBS was the fastest-growing news site in the US for another month
# Year-on-year change in visits (%), fastest growing sites in the US top 50
# cbsnews.com
# 79%

st.image(logo, width=150)
st.header("Daily News - Sentiment Analysis")

blurp = """Sentiment Analysis is the process of ‘computationally’ determining 
whether a piece of writing is positive, negative or neutral. It’s also known as 
opinion mining, deriving the opinion or attitude of a speaker.
"""

details = """<h3>Why sentiment analysis?</h3> 
 
<p><b>Business:</b> In marketing field companies use it to develop their strategies, to 
understand customers’ feelings towards products or brand, how people respond to 
their campaigns or product launches and why consumers don’t buy some products.</p>
 
<p><b>Politics:</b> In the political field, it is used to keep track of political view, 
to detect consistency and inconsistency between statements and actions at the 
government level. It can be used to predict election results as well!</p>

<p><b>Public Actions:</b> Sentiment analysis also is used to monitor and analyse social 
phenomena, for the spotting of potentially dangerous situations and determining 
the general mood of the blogosphere.</p>
"""

rss_feeds = ['https://www.cbsnews.com/latest/rss/main',
             'https://www.cbsnews.com/latest/rss/world',
             'https://www.cbsnews.com/latest/rss/us',
             'https://www.japantimes.co.jp/feed/topstories/']

st.write(blurp, unsafe_allow_html=True)

with st.expander("Why sentiment analysis?"):
    st.write(details, unsafe_allow_html=True)

title = 'CBS - MAIN'
def load_feed():
    custom_feed = st.session_state['-CUSTOM-']
    if len(custom_feed) == 0:
        feed = st.session_state['-UPDATE-']
        if feed == rss_feeds[0]:
            title = 'CBS - MAIN'
        elif feed == rss_feeds[1]:
            title = 'CBS - WORLD'
        elif feed == rss_feeds[2]:
            title = 'CBS - US'
        elif feed == rss_feeds[3]:
            title = 'JAPAN TODAY'
    else:
        feed = custom_feed
        title = 'CUSTOM FEED'
    feeds = feedparser.parse(feed)
    st.subheader(f"Headlines From {title}")
    return feeds


feedlist = st.selectbox('Select a Feed', rss_feeds, key='-UPDATE-', on_change=load_feed)
st.text_input('Custom Feed', key='-CUSTOM-')

col1, col2 = st.columns([2, 2])

try:    
    with col1:  
        results = {'positive': 0, 'negative': 0, 'neutral': 0}
        feeds = load_feed()
        count = len(feeds['entries'])
        st.text("Analyizing " + str(count) + " Articles")
        for feed in feeds['entries']:
            scores = analyzer.polarity_scores(feed['title'])
            title = feed['title']
            source = f"[{title}]({feed['link']})"
            if scores['compound'] > 0:
                st.markdown(f':orange[{source}]\n\n' + str(scores) + '\n')
                results['positive'] += 1
            elif scores['compound'] < 0:
                st.markdown(f':violet[{source}]\n\n' + str(scores) + '\n')
                results['negative'] += 1
            else:
                st.markdown(f':blue[{source}]\n\n' + str(scores) + '\n')
                results['neutral'] += 1


    with col2:
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Positive', 'Negative', 'Neutral'
        sizes = [results['positive'], results['negative'], results['neutral']]
        explode = (0.1, 0, 0)  # only "explode" the 1st slice (i.e. 'Positive')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90, colors={'#F7C8E0', '#95BDFF', '#FAD9A1'})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
except:
    st.image(oops)        