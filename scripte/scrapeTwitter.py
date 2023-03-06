# install snscrape using pip
# !pip3 install snscrape

# import libraries
import snscrape.modules.twitter as sntwitter
import snscrape.modules.twitter
import pandas as pd

# define a function to scrape tweets
def crawl_tweets(query, csv_name):
    TWEET_PATH = './ori_data/tweets'
    save_path = '{}/{}.csv'.format(TWEET_PATH, csv_name)

    print("Scraping using query > {} <".format(query))
    print("Data will be saved to > {} >".format(save_path))

    # create a list to append twitter data to
    tweets_list = []

    # use TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        tweets_list.append(
            [
                tweet.id,
                tweet.url,
                tweet.date,
                tweet.content,
                tweet.user.username,
                tweet.replyCount,
                tweet.retweetCount,
                tweet.likeCount,
                tweet.retweetedTweet,
                tweet.mentionedUsers,
            ]
        )
        if i % 200 == 0:
            print("====== Scrapped {} =======".format(i))

    print("====== Scrapped {} in total =======".format(len(tweets_list)))

    # create a dataframe to view the result
    tweets_df = pd.DataFrame(
        tweets_list,
        columns=[
            "id",
            "url",
            "date",
            "content",
            "username",
            "replyCount",
            "retweetCount",
            "likeCount",
            "retweetedTweet",
            "mentionedUsers",
        ],
    )
    tweets_df.to_csv(save_path)
    return tweets_df


def crawl_tweets_contains(keyword_1, keyword_2, min_favor=5):
    query = '{} {} min_faves:{} lang:en'.format(keyword_1, keyword_2, min_favor)
    csv_name = 'contain_{}_{}'.format(keyword_1, keyword_2.replace(' ', '_'))
    return crawl_tweets(query, csv_name)


def crawl_tweets_contains_serial(keyword_1, keyword_2_list, min_favor=5):
    for keyword_2 in keyword_2_list:
        crawl_tweets_contains(keyword_1, keyword_2, min_favor)


# from user
crawl_tweets('from:NFTethics', 'from_nftethics')

# contains keywords
keywords = ['ethic', 'informed consent', 'transparency', 'accountability', 'privacy', 'fairness', 'trust',
            'gender', 'ethnicity', 'skin tone', 'skin color']

## contains nft and one keyword
crawl_tweets_contains_serial('nft', keywords)

## contains cryptopunk and one keyword
crawl_tweets_contains_serial('cryptopunk', keywords, min_favor=2)