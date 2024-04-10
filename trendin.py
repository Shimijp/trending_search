from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Connect to Google
pytrend = TrendReq()

# Get daily search trends in Israel
trending_searches_df = pytrend.trending_searches(pn='united_states')

# Print the trending searches
print(trending_searches_df.head())

# For simplicity, this example just plots the index against the row number,
# assuming each trend has a uniform "interest" value, which in practice isn't true.
# For actual interest over time, you would need to use pytrend.interest_over_time()
# for specific keywords.

plt.figure(figsize=(20, 10))
plt.plot(trending_searches_df.index, range(len(trending_searches_df)), marker='o')
plt.title('Daily Trending Searches in usa')
plt.ylabel('Trend Index')
plt.xlabel('Trends')
plt.xticks(rotation=0)
#plt.tight_layout()

# Adjust the tick labels to show the trend names
plt.xticks(range(len(trending_searches_df)), trending_searches_df[0], )

plt.show()
print(trending_searches_df[0])