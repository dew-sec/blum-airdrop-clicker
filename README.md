# Blum Airdrop Clicker

Blum Airdrop Clicker is a Python-based tool that automates gameplay for the Blum Airdrop mini-game by simulating human-like interactions. This clicker helps players quickly progress through the game by automatically detecting and clicking in-game objects, allowing for more efficient play without manual intervention. It's designed to mimic real user behavior, ensuring the interaction is safe, untraceable, and compliant with game guidelines.

## How It Works

Blum Airdrop Clicker operates by scanning the game window, detecting in-game elements by color, and interacting with them through mouse clicks. Unlike typical bots that interact with the game's API, this clicker works solely through the user interface (UI), making it indistinguishable from a human player.

The clicker leverages a combination of:

- **Image Processing**: Using live screenshots of the game to identify objects and interactions.
- **Mouse Simulation**: Moving the mouse and clicking in specific locations based on real-time analysis of the game.
- **Game Detection**: Continuously monitoring the game state to determine when to start and stop the automation.

## Key Features

- **Human-Like Interaction**: Mimics human behavior, making it undetectable by the game’s anti-bot mechanisms.
- **Multi-Game Support**: Configurable to automate a specific number of games, allowing for repeated gameplay without manual input.
- **Auto-Detection**: Automatically detects the game window and interacts with the game without needing complex setup.
- **User-Friendly**: Simply run the script and let the clicker handle the rest.

## Requirements

- **Python 3.10 or higher** (on Windows).
- **Telegram Desktop** must be installed and running:
  - The bot uses Telegram Desktop for certain triggers related to game events.
- **dxcam**: For capturing live screenshots of the game window in real time.
- **mouse & keyboard libraries**: To simulate mouse clicks and keyboard inputs.
- Other dependencies specified in `requirements.txt`.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/blum-airdrop-clicker.git
    cd blum-airdrop-clicker
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure Telegram Desktop is installed and running**.

## Usage

1. Open the Blum Airdrop mini-game on your desktop.
2. Run the clicker script:

    ```bash
    python main.py
    ```

3. You can also specify the number of games to automate by passing an argument:

    ```bash
    python main.py [amount_of_games]
    ```

    Replace `[amount_of_games]` with the desired number of games to automate.

4. **Exiting the program**: Press `Ctrl + X` at any time to stop the script and exit.

## Why is This Script Safe to Use?

Blum Airdrop Clicker does not interact directly with the game’s API, making it much safer to use compared to traditional bots. By simply automating clicks on the game’s UI, it mimics regular player behavior, making it untraceable and compliant with standard game policies.
