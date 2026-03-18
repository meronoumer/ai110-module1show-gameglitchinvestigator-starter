# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---

The app kept prompting me to guess lower than even 0 as an input however it doesn't accept an input lower than 0. 

The ranges for normal and difficlt seem to be switched as it doesn't make sense to have a larger range for normal than for hard.

The show hint button doesn't work.

It keeps asking me to go lower.



## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot as my main AI teammate throughout this debugging project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
**Correct suggestion:** Copilot identified and fixed a string conversion bug where the secret number was being converted to a string on even attempts, causing wrong comparisons. The AI suggested removing the `if st.session_state.attempts % 2 == 0: secret = str(st.session_state.secret)` logic and always keeping secret as an integer. This was correct because string comparisons like `"5" > "50"` don't work the same as number comparisons. I verified it by running pytest tests that check guess comparisons work with integers only, and by testing the game to ensure hints are now accurate instead of backwards.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
**Incorrect/misleading suggestion:** The original AI-generated code had hint messages backwards - it said "Go HIGHER!" when your guess was too high and "Go LOWER!" when your guess was too low. This was misleading because it gave wrong directions to players. I verified this by creating pytest tests that check the hint messages are correct, and by testing the game manually to ensure hints now point in the right direction.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed by running pytest tests that specifically target each bug, and by playing around in the game to see if the problem went away. If the tests passed and the game behaved correctly, I considered the bug fixed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran pytest tests like `test_normal_vs_hard_range_bug` which checks that Normal difficulty has a smaller range than Hard difficulty. This test showed that the ranges are now logically ordered (Easy: 1-20, Normal: 1-50, Hard: 1-100) instead of the buggy reverse order.

- Did AI help you design or understand any tests? How?
Copilot helped me design specific pytest test cases that target each bug we fixed. For example, Copilot suggested creating `test_hint_messages_correct_for_high_guess` which verifies that when a guess is too high, the message says "Go LOWER!" not "Go HIGHER!". This helped me understand how to write tests that catch regressions.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit automatically reruns your entire Python script from top to bottom every time a user interacts with a widget, and st.session_state acts as a dictionary-like memory to save variables so they don't reset to their original values as they update. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I want to keep writing small, specific tests for each bug before and after fixing it.

- What is one thing you would do differently next time you work with AI on a coding task?

I would double-check every AI suggestion before trusting it, especially logic that affects game rules.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI is really helpful for spotting bugs and suggesting fixes, but I learned I still need to verify everything carefully because it can give wrong advice. Additionally I think that as helpful as AI is it is important to remember that this is a smaller scale project but it may not be as effective for large codebases. 