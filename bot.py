import time
import requests
import tweepy

API_KEY = "M2kalPmmBVNlO8hxeGt1YSCVW"
API_SECRET = "gsnuUkakBYTbktbam8E1EIVv1Euzgdifo3dAWm3oCUgP0RfT9g"
ACCESS_TOKEN = "2043261499670503424-u9TcWNJa1VsaKRFmCTQHb9dSgNy34u"
ACCESS_SECRET = "GuKblHlRymLZdT9eOUbg3CHFu1kHwokpXUnyzadreiPw9"

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url).json()
    price = float(response['price'])
    return f"${price:,.2f}" if price >= 1 else f"${price:.4f}"

def post_update():
    try:
        btc = get_crypto_price("BTCUSDT")
        eth = get_crypto_price("ETHUSDT")
        sol = get_crypto_price("SOLUSDT")

        tweet_text = f"LIVE CRIPTO MARKET UPDATE\n\n$BTC: {btc}\n$ETH: {eth}\n$SOL: {sol}"
        
        client.create_tweet(text=tweet_text)
        print("Tweet posted successfully!")
    except Exception as e:
        print("Error posting tweet:", e)

if __name__ == "__main__":
    post_update()