# Instagram Bot

**Instagram Bot** is an automated Python script for logging into Instagram and liking posts based on hashtags. It uses Selenium WebDriver to simulate user interaction with Instagram, making it useful for automating engagement with posts related to specific topics or trends.

## Features

- Logs into Instagram with your username and password.
- Automatically accepts cookies pop-ups.
- Likes posts under a specific hashtag.
- Scrolls through posts and likes a set number of posts.
- Pauses between actions to mimic human behavior.
  
## Requirements

- Python 3.x
- `selenium` library: Install with `pip install selenium`
- `geckodriver` (for Firefox): Download from [Mozilla](https://github.com/mozilla/geckodriver/releases) and place it in the specified path.
  
## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/metodiangelov/instagram_hashtag_like_bot

2. Install the required dependencies:
   pip install selenium

3. Download the latest version of Geckodriver (for Firefox) and specify its path in the script (webdriver.Firefox(executable_path='path_to_geckodriver')).

4. Open the script and replace @yourUser and @yourPassword with your Instagram login credentials.

## Usage

1. Run the script:
   python instagram_bot.py

##The bot will:
    1. Log into Instagram using the provided credentials.
    2. Automatically accept cookies (if prompted).
    3. Like posts under a specific hashtag (in this case, 'underwater').
    4. Scroll through the page and like a defined number of posts (you can adjust the count in the like_posts() method).
    5. Wait between actions to avoid getting flagged as a bot.

## How It Works

  1. The bot uses Selenium WebDriver to simulate logging into Instagram and interacting with the website.
  2. It scrolls through posts related to a given hashtag and likes them.
  3. The bot mimics human behavior by pausing between likes to avoid being flagged by Instagram as a bot.

## Customization

 1. You can modify the hashtag that the bot uses to find posts by changing the argument passed to like_posts().
 2. You can adjust the number of times the bot scrolls and the time it waits between likes by editing the relevant parameters in the code.

Important Notes

    Use with caution: Automating actions on Instagram can violate their Terms of Service. Make sure you are aware of the risks before using this bot.
    Instagram may block or restrict your account if they detect abnormal activity. Use the bot responsibly and avoid overuse.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Inspired by the need to automate social media engagement with specific hashtags.


---

### Steps to Upload to GitHub:

1. **Create the repository**:
   - Go to [GitHub](https://github.com) and create a new repository, for example, `instagram-bot`.

2. **Upload Files**:
   - If you haven't already, make sure your Python script (`instagram_bot.py`) and `README.md` file are in the same directory on your local machine.
   - Initialize the directory as a Git repository:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     ```

3. **Push to GitHub**:
   - Add your remote repository URL:
     ```bash
     git remote add origin [https://github.com/your-username/instagram-bot.git](https://github.com/metodiangelov/instagram_hashtag_like_bot)
     ```
   - Push the changes:
     ```bash
     git push -u origin main
     ```

Let me know if you need further assistance!
