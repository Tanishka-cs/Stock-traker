# Stock-traker
# 📈 Stock Portfolio Tracker

A beginner-friendly Python project that calculates the total value of a stock portfolio based on user input. The program allows users to enter stock names and quantities, computes the investment value, and saves the total investment to a text file.

## 📌 Features

- Track investments in multiple stocks.
- Calculates the value of each stock based on predefined prices.
- Displays the total investment value.
- Saves the result to a file (`investment.txt`).
- Handles invalid stock names gracefully.
- Simple command-line interface.

## 🛠️ Technologies Used

- Python 3
- File Handling

## 📂 Project Structure

```
stock-portfolio-tracker/
│
├── stock_tracker.py
├── investment.txt   (generated after running)
└── README.md
```

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Save the code as `stock_tracker.py`.
3. Open a terminal in the project directory.
4. Run the program:

```bash
python stock_tracker.py
```

## 🎮 How It Works

1. Enter the number of different stocks you own.
2. Enter the stock symbol (AAPL, TSLA, GOOG, or MSFT).
3. Enter the quantity of shares.
4. The program calculates the investment value for each stock.
5. It displays the total portfolio value.
6. The total investment is saved in `investment.txt`.

## 💬 Sample Output

```
Enter number of stocks: 2

Enter stock 1 name (AAPL, TSLA, GOOG, MSFT): AAPL
Enter quantity: 5
AAPL: 5 shares × $180 = $900

Enter stock 2 name (AAPL, TSLA, GOOG, MSFT): MSFT
Enter quantity: 3
MSFT: 3 shares × $400 = $1200

Total Investment Value = $2100
Result saved in investment.txt
```

## 📄 Example `investment.txt`

```
Total Investment Value = $2100
```

## 📖 Code Overview

The program:

- Stores stock prices in a Python dictionary.
- Accepts stock names and quantities from the user.
- Calculates the investment value for each stock.
- Adds all investments to compute the total portfolio value.
- Writes the total investment value to a text file.

## 🚀 Future Improvements

- Fetch live stock prices using an API.
- Support more stock symbols.
- Read portfolio details from a CSV file.
- Save transaction history.
- Display investment summaries with charts.
- Add profit/loss calculations.
- Build a graphical interface using Tkinter.

## 📚 Concepts Used

- Dictionaries
- Loops
- Conditional Statements
- User Input
- Arithmetic Operations
- File Handling
- String Formatting

## 👩‍💻 Author

**Tanishka Yadav**

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
