# import streamlit as st
# import preprocessor
# st.sidebar.title("Watsupp Chat Analyzer")
# uploaded_file = st.sidebar.file_uploader("Choose a file")
# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data = bytes_data.decode("utf-8")
#     df=preprocessor.preprocess(data)
#     st.dataframe(df)
# #     fetch unique users
#     user_list=df['user'].unique().tolist()
#     user_list.remove("group_notification")
#     user_list.sort()
#     user_list.insert(0,"Overall")
#     st.sidebar.selectbox("Show Analysis WRT", user_list)
#     if st.sidebar.button("Show Analysis"):
#         pass
#
# import streamlit as st
# import preprocessor, helper
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# st.sidebar.title("WhatsApp Chat Analyzer")
#
# uploaded_file = st.sidebar.file_uploader("Choose a file")
#
# if uploaded_file is not None:
#     data = uploaded_file.getvalue().decode("utf-8")
#     df = preprocessor.preprocess(data)
#
#     # Fetch unique users
#     user_list = df['user'].unique().tolist()
#     if 'group_notification' in user_list:
#         user_list.remove('group_notification')
#
#     user_list.sort()
#     user_list.insert(0, "Overall")
#
#     selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)
#
#     if st.sidebar.button("Show Analysis"):
#
#         # ====== TOP STATISTICS ======
#         num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
#
#         st.title("Top Statistics")
#         col1, col2, col3, col4 = st.columns(4)
#
#         col1.metric("Total Messages", num_messages)
#         col2.metric("Total Words", words)
#         col3.metric("Media Shared", num_media_messages)
#         col4.metric("Links Shared", num_links)
#
#         # ====== MONTHLY TIMELINE ======
#         st.title("Monthly Timeline")
#         timeline = helper.monthly_timeline(selected_user, df)
#         fig, ax = plt.subplots()
#         ax.plot(timeline['time'], timeline['message'], color='green')
#         plt.xticks(rotation='vertical')
#         st.pyplot(fig)
#
#         # ====== DAILY TIMELINE ======
#         st.title("Daily Timeline")
#         daily_timeline = helper.daily_timeline(selected_user, df)
#         fig, ax = plt.subplots()
#         ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
#         plt.xticks(rotation='vertical')
#         st.pyplot(fig)
#
#         # ====== ACTIVITY MAP ======
#         st.title('Activity Map')
#         col1, col2 = st.columns(2)
#
#         with col1:
#             st.subheader("Most Busy Day")
#             busy_day = helper.week_activity_map(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.bar(busy_day.index, busy_day.values, color='purple')
#             plt.xticks(rotation='vertical')
#             st.pyplot(fig)
#
#         with col2:
#             st.subheader("Most Busy Month")
#             busy_month = helper.month_activity_map(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.bar(busy_month.index, busy_month.values, color='orange')
#             plt.xticks(rotation='vertical')
#             st.pyplot(fig)
#
#         # ====== HEATMAP ======
#         st.title("Weekly Activity Map")
#         user_heatmap = helper.activity_heatmap(selected_user, df)
#         fig, ax = plt.subplots()
#         sns.heatmap(user_heatmap, ax=ax)
#         st.pyplot(fig)
#
#         # ====== BUSIEST USERS ======
#         if selected_user == 'Overall':
#             st.title('Most Busy Users')
#             x, new_df = helper.most_busy_users(df)
#
#             col1, col2 = st.columns(2)
#             with col1:
#                 fig, ax = plt.subplots()
#                 ax.bar(x.index, x.values, color='red')
#                 plt.xticks(rotation='vertical')
#                 st.pyplot(fig)
#             with col2:
#                 st.dataframe(new_df)
#
#         # ====== WORDCLOUD ======
#         st.title("WordCloud")
#         df_wc = helper.create_wordcloud(selected_user, df)
#         fig, ax = plt.subplots()
#         ax.imshow(df_wc)
#         ax.axis("off")
#         st.pyplot(fig)
#
#         # ====== MOST COMMON WORDS ======
#         st.title('Most Common Words')
#         most_common_df = helper.most_common_words(selected_user, df)
#         fig, ax = plt.subplots()
#         ax.barh(most_common_df[0], most_common_df[1])
#         st.pyplot(fig)
#
#         # ====== EMOJI ANALYSIS ======
#         st.title("Emoji Analysis")
#         emoji_df = helper.emoji_helper(selected_user, df)
#
#         col1, col2 = st.columns(2)
#         with col1:
#             st.dataframe(emoji_df)
#
#         with col2:
#             if not emoji_df.empty:
#                 fig, ax = plt.subplots()
#                 ax.pie(
#                     emoji_df[1].head(),
#                     labels=emoji_df[0].head(),
#                     autopct="%0.2f"
#                 )
#                 st.pyplot(fig)
#
import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    data = uploaded_file.getvalue().decode("utf-8")
    df = preprocessor.preprocess(data)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')

    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        # ====== TOP STATISTICS ======
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Messages", num_messages)
        col2.metric("Total Words", words)
        col3.metric("Media Shared", num_media_messages)
        col4.metric("Links Shared", num_links)

        # ====== MONTHLY TIMELINE ======
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # ====== DAILY TIMELINE ======
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # ====== ACTIVITY MAP ======
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.subheader("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # ====== HEATMAP ======
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        sns.heatmap(user_heatmap, ax=ax)
        st.pyplot(fig)

        # ====== BUSIEST USERS ======
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)

            col1, col2 = st.columns(2)
            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # ====== WORDCLOUD ======
        st.title("WordCloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        ax.axis("off")
        st.pyplot(fig)

        # ====== MOST COMMON WORDS ======
        st.title('Most Common Words')
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        st.pyplot(fig)

        # ====== EMOJI ANALYSIS (FIXED) ======
        st.title("Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)

        with col2:
            if not emoji_df.empty:
                fig, ax = plt.subplots()
                ax.pie(
                    emoji_df['count'].head(),
                    labels=emoji_df['emoji'].head(),
                    autopct="%0.2f"
                )
                st.pyplot(fig)
