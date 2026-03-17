# import re
# import pandas as pd
# def preprocess(data):
#     pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s*(?:am|pm)\s-\s"
#
#     messages = re.split(pattern, data)[1:]  # drop first empty split
#     dates = re.findall(pattern, data)
#
#     df = pd.DataFrame(
#         list(zip(messages, dates)),
#         columns=['user_message', 'message_date']
#     )
#
#     # Fix WhatsApp unicode space
#     df['message_date'] = df['message_date'].str.replace('\u202f', ' ', regex=False)
#
#     # Convert to datetime
#     df['date'] = pd.to_datetime(
#         df['message_date'],
#         format='%d/%m/%Y, %I:%M %p - '
#     )
#
#     # User & message extraction
#     users = []
#     texts = []
#
#     for message in df['user_message']:
#         message = str(message)
#
#         entry = re.split(r'^([^:]+):\s', message, maxsplit=1)
#
#         if len(entry) == 3:
#             users.append(entry[1])
#             texts.append(entry[2])
#         else:
#             users.append('group_notification')
#             texts.append(message)
#
#     df['user'] = users
#     df['message'] = texts
#
#     # Drop unused column
#     df.drop(columns=['user_message', 'message_date'], inplace=True)
#
#     # Time features
#     df['year'] = df['date'].dt.year
#     df['hour'] = df['date'].dt.hour
#     df['minute'] = df['date'].dt.minute
#
#     return df
import re
import pandas as pd

def preprocess(data):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s*(?:am|pm)\s-\s"

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame(list(zip(messages, dates)),
                      columns=['user_message', 'message_date'])

    df['message_date'] = df['message_date'].str.replace('\u202f', ' ', regex=False)

    df['date'] = pd.to_datetime(
        df['message_date'],
        format='%d/%m/%Y, %I:%M %p - '
    )

    users = []
    texts = []

    for message in df['user_message']:
        entry = re.split(r'^([^:]+):\s', str(message), maxsplit=1)

        if len(entry) == 3:
            users.append(entry[1])
            texts.append(entry[2])
        else:
            users.append('group_notification')
            texts.append(message)

    df['user'] = users
    df['message'] = texts

    df.drop(columns=['user_message', 'message_date'], inplace=True)

    # basic time features
    df['year'] = df['date'].dt.year
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # ===== REQUIRED EXTRA FEATURES =====
    df['only_date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month

    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append("23-00")
        elif hour == 0:
            period.append("00-01")
        else:
            period.append(f"{hour}-{hour+1}")

    df['period'] = period

    return df


