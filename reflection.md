# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Well the first time i ran it the game was working fine with the attempt counter going down after each guess as well as the hint was showing up
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The game was giving the wrong hint
the game said to guess a number from 1 to 100 while the secret number was below 0 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|--50---|-------Too High----|---Too Low-------|--------None------------|
| 0|  Error| GO lower | none |
| -10 | Error |  Go lower| none |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggested that the session starts at 1 (attempt 1) and not 0 (attmpt 0) whe initialy starting the game and I checked it by replaying the game and looking at 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
In check_guess, the fix for the backwards hints is to swap the return values so that "Too High" returns "Go LOWER!" and "Too Low" returns "Go HIGHER!".
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
