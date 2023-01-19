import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import string

# import stopwords

insta_data = pd.read_csv("Instagramdata.csv", encoding='latin1')
insta_data.drop_duplicates(inplace=True)
insta_data['Caption'] = insta_data['Caption'].str.lower()
insta_data['Caption'] = insta_data['Caption'].str.strip()
insta_data['Hashtags'] = insta_data['Hashtags'].str.lower()
insta_data['Hashtags'] = insta_data['Hashtags'].str.strip()


def analyzing_content():
    st.title("Analyzing Content")
    from nltk.tokenize import word_tokenize
    import nltk

    from nltk.corpus import stopwords

    nltk.download('punkt')

    def remove_puctuation(text):
        for i in string.punctuation:
            if i in text:
                text = text.replace(i, '')

        return text

    insta_data['Caption'] = insta_data['Caption'].apply(remove_puctuation)

    insta_data['Tokenized_Caption'] = insta_data['Caption'].apply(word_tokenize)

    def remove_stopwords(text):

        nltk.download('stopwords')
        L = []
        for word in text:
            if word not in stopwords.words('english'):
                L.append(word)

        return L

    insta_data['Tokenized_Caption'] = insta_data['Tokenized_Caption'].apply(remove_stopwords)
    insta_data['Tokenized_Caption'] = insta_data['Tokenized_Caption'].apply(lambda x: " ".join(x))

    from wordcloud import WordCloud

    fig12 = plt.figure(figsize=(14, 10))
    wc = WordCloud(width=800, height=400).generate(" ".join(insta_data['Tokenized_Caption']))

    plt.imshow(wc)
    plt.axis("off")
    st.subheader("Captions")
    st.pyplot(fig12)

    def remove_puctuation(text):

        for i in string.punctuation:
            if i in text:
                text = text.replace(i, '')

        return text

    insta_data['Hashtags'] = insta_data['Hashtags'].apply(remove_puctuation)
    insta_data['tokenized_hashtags'] = insta_data['Hashtags'].apply(word_tokenize)

    def remove_stopwords(text):

        L = []
        for word in text:
            if word not in stopwords.words('english'):
                L.append(word)

        return L

    insta_data['tokenized_hashtags'] = insta_data['tokenized_hashtags'].apply(remove_stopwords)
    insta_data['tokenized_hashtags'] = insta_data['tokenized_hashtags'].apply(lambda x: " ".join(x))

    from wordcloud import WordCloud

    fig13 = plt.figure(figsize=(12, 8))
    wc1 = WordCloud(width=1600, height=800).generate(" ".join(insta_data['tokenized_hashtags']))
    plt.imshow(wc1)
    plt.axis("off")
    st.subheader("Hashtags")
    st.pyplot(fig13)


def instagram_analysis():
    st.title("Analyzing Instagram Reach")
    col1, col2 = st.columns(2)
    with col1:
        fig1 = plt.figure(figsize=(10, 8))
        plt.style.use('fivethirtyeight')
        sns.distplot(insta_data['From Home'])
        plt.title("Distribution of Impressions From Home", fontsize=22)
        st.pyplot(fig1)
        st.write("Conclusion:The impressions I get from the home section on Instagram shows how much my posts reach "
                 "my followers. Looking at the impressions from home, I can say it’s hard to reach all my followers "
                 "daily")

    with col2:
        fig2 = plt.figure(figsize=(10, 8))
        plt.style.use('fivethirtyeight')
        sns.distplot(insta_data['From Hashtags'], color='red')
        plt.title("Distribution of Impressions From Hashtags", fontsize=22)
        st.pyplot(fig2)
        st.write("Conclusion:Hashtags are tools we use to categorize our posts on Instagram so that we can reach more "
                 "people based on the kind of content we are creating. Looking at hashtag impressions shows that not "
                 "all posts can be reached using hashtags, but many new users can be reached from hashtag")

    col3, col4 = st.columns(2)
    with col3:
        fig3 = plt.figure(figsize=(10, 8))
        plt.style.use('fivethirtyeight')
        sns.distplot(insta_data['From Explore'], color='orange')
        plt.title("Distribution of Impressions From Explore", fontsize=22)
        st.pyplot(fig3)
        st.write("Conclusion:The explore section of Instagram is the recommendation system of Instagram. It "
                 "recommends posts to the users based on their preferences and interests. By looking at the "
                 "impressions I have received from the explore section, I can say that Instagram does not recommend "
                 "our posts much to the users. Some posts have received a good reach from the explore section, "
                 "but it’s still very low compared to the reach I receive from hashtags.")

    with col4:
        fig4 = plt.figure(figsize=(10, 8))
        plt.style.use('fivethirtyeight')
        sns.distplot(insta_data['From Other'], color='green')
        plt.title("Distribution of Impressions From Other", fontsize=22)
        st.pyplot(fig4)

    st.subheader("Now let’s have a look at the percentage of impressions I get from various sources on Instagram:")
    home = insta_data['From Home'].sum()
    hashtag = insta_data['From Hashtags'].sum()
    explore = insta_data['From Explore'].sum()
    other = insta_data['From Other'].sum()

    labels = ['From Home', 'From Hashtags', 'From Explore', 'Other']
    values = [home, hashtag, explore, other]
    explode = [0.1, 0, 0, 0]
    fig5 = plt.figure(figsize=(4, 4))
    plt.pie(values, labels=labels,
            autopct="%1.2f%%", explode=explode)
    st.pyplot(fig5)


def analyzing_relationship():
    st.title('Analyzing Relationship')
    col5, col6 = st.columns(2)
    with col5:
        fig6 = plt.figure(figsize=(10, 8))
        sns.regplot(x='Likes', y='Impressions', data=insta_data, color='red')
        plt.title("Relationships between likes and Impressions", fontsize=28)
        st.pyplot(fig6)
    with col6:
        fig7 = plt.figure(figsize=(10, 8))
        sns.regplot(x='Comments', y='Impressions', data=insta_data, color='blue')
        plt.title("Relationships between comments and Impressions", fontsize=28)
        st.pyplot(fig7)

    col7, col8 = st.columns(2)
    with col7:
        fig8 = plt.figure(figsize=(10, 8))
        sns.regplot(x='Shares', y='Impressions', data=insta_data, color='purple')
        plt.title("Relationships between shares and Impressions", fontsize=28)
        st.pyplot(fig8)

    with col8:
        fig8 = plt.figure(figsize=(10, 8))
        sns.regplot(x='Saves', y='Impressions', data=insta_data, color='green')
        plt.title("Relationships between Saves and Impressions", fontsize=28)
        st.pyplot(fig8)

    st.subheader(" Now let’s have a look at the correlation of all the columns with the Impressions column:")
    fig10 = plt.figure(figsize=(16, 10))
    correlation = insta_data.corr()
    sns.heatmap(correlation)
    st.pyplot(fig10)


st.sidebar.title("Instagram Reach Analysis")
option = st.sidebar.selectbox('Pick one', ['Analyzing Instagram Reach', 'Analyzing Relationship', 'Analyzing Content'])
if option == "Analyzing Instagram Reach":
    instagram_analysis()
elif option == 'Analyzing Relationship':
    analyzing_relationship()
else:
    analyzing_content()
