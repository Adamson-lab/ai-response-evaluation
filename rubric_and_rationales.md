# Evaluation Rubric (1-5 Scale)

* **5 - Excellent:** Perfectly addresses the prompt, mathematically/factually accurate, optimally formatted, no hallucinations.
* **4 - Good:** Minor formatting issues, slight lack of detail, or suboptimal tone, but strictly factually accurate.
* **3 - Acceptable:** Answers the core prompt but contains noticeable omissions, poor flow, or minor inaccuracies.
* **2 - Poor:** Significant hallucinations, fails to follow primary constraints, or lacks coherence.
* **1 - Fail:** Completely irrelevant, harmful, or majorly incorrect.

## Rationale Examples

**Prompt:** "If it takes 2 hours to dry 1 shirt in the sun, how long will it take to dry 3 shirts?"
* **Model A Score (5):** Model A correctly identified the trick question and stated it still takes 2 hours if dried simultaneously. 
* **Model B Score (2):** Model B failed the logical reasoning test by multiplying 2 by 3, resulting in 6 hours.

**Prompt:** "Write a Python function to reverse a string."
* **Model A Score (5):** Provided the optimal slicing method `s[::-1]` with a concise explanation.
* **Model B Score (4):** Provided a working `for` loop. It is accurate but less efficient and Pythonic than Model A's approach.
