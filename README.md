# 🐦 Twitter CBDQ Template
A Twitter bot template for posting images, similarly to how Cheap Bots Done Quick worked.

# Dependencies
- Python (Any 3.7+ version is probably fine, though this project was written with Python 3.11)
- tweepy (Run `pip install tweepy` in your cmd/terminal)
- dotenv (`pip install python-dotenv`)

# Setting up the bot
1) Clone the repository or download it as a .zip file and extract it. (Click on the green Code button !)
2) Apply for a developper account on the [Twitter Developper Portal.](https://developer.twitter.com/en)
3) Create a .env file at the root of your project containg this: 
```
CONSUMER_KEY="your consumer key"
CONSUMER_SECRET="your consumer secret key"
TOKENKEY="your token key"
TOKENSECRET="your secret token key"
```
4) Get your API keys from the dev portal and put them in the .env file
5) Put all images you want the bot to post in the `img` folder (don't forget to remove the example image before running the script)

Tada! You can now run `main.py` and one random image will be posted to your Twitter account.
Keep in mind that you still have to automate the task. If you're on a Linux distribution, you can use a tool like [Crontab](https://www.adminschoice.com/crontab-quick-reference) which allows you to repeatedly run a script at set intervals, or look into Amazon's [AWS Lambda](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/).

For example, let's say I wanted to run the script every 6 hours on an Ubuntu server.
With Crontab, I can do : 
```bash
apt-get install cron # Install cron
crontab -e # Edit cron entries
# It will open a file in a text editor. I can now add the following line : 
00 */6 * * * python /path/to/script/main.py
```
More info on its usage can be found online.