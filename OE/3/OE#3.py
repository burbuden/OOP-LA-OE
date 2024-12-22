print ("OE#3\nArdent Azrael Sayson\nBSIT2B\n")

class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return f"{self.username} logged in."

    def post(self, content):
        return f"Posted: {content}"


class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story_content):
        return f"Story shared: {story_content}"


class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        return f"Tweeted: {tweet_content}"


# Demonstration of functionality
instagram_user = InstagramAccount("user_instagram", "password123", 1500)
twitter_user = TwitterAccount("user_twitter", "password456", 300)

print(instagram_user.login())
print(instagram_user.post("Hello Instagram!"))
print(instagram_user.share_story("My first story!"))

print(twitter_user.login())
print(twitter_user.post("Hello Twitter!"))
print(twitter_user.tweet("My first tweet!"))
