# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game is a number guessing game where the player tries to guess a secret number within a limited number of attempts.
- Bugs found: backwards hints, attempts starting at 1 instead of 0, secret number switching to a string on even attempts, and wrong guesses giving points.
- Fixes applied: moved all logic into logic_utils.py, fixed the hints direction, fixed attempts to start at 0, removed the type-switching bug, and fixed scoring so wrong guesses never give points.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User opens the game and sees a prompt to guess a number between 1 and 200 on Hard difficulty
2. User enters a guess of 40 → game returns "Too Low, Go Higher"
3. User enters a guess of 150 → game returns "Too High, Go Lower"
4. User enters a guess of 95 → game returns "Too Low, Go Higher"
5. User enters the correct number → game shows "Correct!" with balloons and displays final score

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
platform win32 -- Python 3.12.5, pytest-9.1.1
collected 7 items
tests\test_game_logic.py ....... [100%]
7 passed in 0.03s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
