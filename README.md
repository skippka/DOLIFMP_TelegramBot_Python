# DOLIFMP Telegram Bot

Welcome to the **DOLIFMP Telegram Bot** repository! This is an interactive and fun Telegram bot designed to entertain users with various games. It features a variety of mini-games and functionalities such as bug reporting, game management, and user interaction, providing a delightful experience for everyone.

**Note**: Currently, the bot is in Ukrainian, but it will be switched to English in the near future.

## Features

- **Games**: Users can play various games such as Tic-Tac-Toe (Crosses and Noughts) against the bot or with friends.
- **Bug Reporting**: Users can report bugs they encounter in the bot. The bot will handle the report and send it to the admin.
- **Commands**:
  - `/start` - Start interacting with the bot.
  - `/help` - Get a list of available commands.
  - `/game` - Start a new game (e.g., Tic-Tac-Toe).
  - `/reportbug` - Report a bug to the admin.
  - `/ID` - Get your Telegram user ID.
  - `/info` - Information about the bot.
  - `/authors` - View the authors of the bot.

## Installation

To run the **DOLIFMP Telegram Bot**, follow these steps:

### Prerequisites

- **Python 3.x** installed on your machine.
- **pip** for managing Python packages.
- A **Telegram Bot Token** (create your bot using [BotFather](https://core.telegram.org/bots#botfather)).

### Steps to Install

1. Clone this repository:

   ```bash
   git clone https://github.com/skippka/DOLIFMP_TelegramBot_Python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DOLIFMP_TelegramBot_Python
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Replace the placeholder **YOUR_BOT_TOKEN** with your actual Telegram Bot token in the `bot.py` file.

5. Run the bot:

   ```bash
   python bot.py
   ```

### Dependencies

- `pyTelegramBotAPI` (for Telegram Bot API)
- `random` (for random selections in games)
- `datetime` (for timestamping bug reports)

## Usage

Once the bot is up and running, you can interact with it on Telegram. Here are the main commands you can use:

- `/start` - Start the bot and receive a welcome message.
- `/help` - Get a list of commands available.
- `/game` - Start a new game (e.g., Tic-Tac-Toe).
- `/reportbug` - Report a bug encountered in the bot.
- `/ID` - Get your unique Telegram ID.

The bot will guide you through all the steps needed to play games, report bugs, and use other commands.

## Contributing

Contributions are welcome! If you have suggestions or improvements for the bot, feel free to fork this repository, make changes, and submit a pull request.

Please ensure that your code follows proper conventions and is thoroughly tested before submitting.
