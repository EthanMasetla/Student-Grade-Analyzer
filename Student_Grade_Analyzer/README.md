#  Student Grade Analyzer

A beginner Python project that analyzes student marks, calculates averages, and flags subjects that need attention.

---

## Project Structure

```
├── main.py        # Collects student name, subjects and marks from user
├── Analyzer.py    # Processes and displays the results
└── README.md      # Project documentation
```

---

## How It Works

1. User enters their student name
2. User enters the number of subjects they are enrolled in
3. For each subject the user enters:
   - Test 1 mark
   - Test 2 mark
   - Assignment mark
4. The analyzer calculates:
   - Average per subject
   - Overall average across all subjects
   - Flags any subject below 50% as needing attention

---

##  Sample Output

```
Enter your student name: John
Enter the number of subjects enrolled in: 2
Enter subject name: Maths
Test1: 23
Test2: 45
Assignment: 2

Student: John
__________________________________________________
Average in Maths: 23.3%
Average in Science: 72.0%

Overall Average: 47.7%
__________________________________________________

Maths: 23.3% (This subject needs your attention!!)
```

---

##  Technologies Used

- **Python 3** — core programming language
- **Dictionaries** — for storing subject marks
- **Functions** — for separating logic into modules
- **F-strings** — for formatted output
- **Loops** — for iterating over subjects

---

## How To Run

1. Clone the repository:
```
git clone https://github.com/yourusername/student-marks-analyzer.git
```

2. Navigate to the project folder:
```
cd student-marks-analyzer
```

3. Run the main file:
```
python main.py
```

---

##  What I Learned

- How to use **dictionaries** to store and retrieve data
- How to **split code** across multiple files using imports
- How to use **loops** to iterate over data
- How to **calculate averages** and apply conditional logic
- How to **format output** using f-strings and round()

---

##  Future Improvements

- Add input validation to handle incorrect entries
- Export results to a CSV or PDF file
- Build a GUI interface
- Connect to a database to store multiple students

---

##  Author

**Masetla Kgabiso Ethen**  
Computer Science and Maths Student  
[LinkedIn](https://www.linkedin.com/in/kgabiso-masetla-a22524319/) | [GitHub](https://github.com/EthanMasetla)

