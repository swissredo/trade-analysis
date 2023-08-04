import tkinter as tk
import matplotlib.pyplot as plt

def analyze_trade_results(trading_table):
    # Placeholder analysis logic - replace this with your actual analysis
    total_trades = len(trading_table)
    num_profit_trades = trading_table.count('1')
    num_loss_trades = trading_table.count('0')

    if total_trades > 0:
        percentage_profit_trades = (num_profit_trades / total_trades) * 100
        percentage_loss_trades = (num_loss_trades / total_trades) * 100
        longest_streak_profit = find_longest_streak(trading_table, '1')
        longest_streak_loss = find_longest_streak(trading_table, '0')
    else:
        percentage_profit_trades = 0
        percentage_loss_trades = 0
        longest_streak_profit = 0
        longest_streak_loss = 0

    return total_trades, num_profit_trades, num_loss_trades, percentage_profit_trades, percentage_loss_trades, longest_streak_profit, longest_streak_loss

def find_longest_streak(trading_table, target_value):
    streaks = trading_table.split('0' if target_value == '1' else '1')
    longest_streak = max(len(streak) for streak in streaks if streak and streak[0] == target_value)
    return longest_streak

def analyze():
    trading_table = entry.get("1.0", tk.END).strip()
    if not trading_table:
        result_label.config(text="Please enter the trading table.")
        return

    total_trades, num_profit, num_loss, percentage_profit, percentage_loss, longest_streak_profit, longest_streak_loss = analyze_trade_results(trading_table)

    result_label.config(text=f"Total Trades: {total_trades}\n"
                             f"Number of Profit Trades: {num_profit}\n"
                             f"Number of Loss Trades: {num_loss}\n"
                             f"Percentage of Profit Trades: {percentage_profit:.2f}%\n"
                             f"Percentage of Loss Trades: {percentage_loss:.2f}%\n"
                             f"Longest Continuous Streak of Profit Trades: {longest_streak_profit}\n"
                             f"Longest Continuous Streak of Loss Trades: {longest_streak_loss}")

def visualize():
    trading_table = entry.get("1.0", tk.END).strip()
    if not trading_table:
        result_label.config(text="Please enter the trading table.")
        return

    num_profit = trading_table.count('1')
    num_loss = trading_table.count('0')

    # Plot the bar chart
    plt.bar(['Profit', 'Loss'], [num_profit, num_loss])
    plt.xlabel('Trade Type')
    plt.ylabel('Number of Trades')
    plt.title('Trading Results')
    plt.show()

def clear_input():
    entry.delete("1.0", tk.END)

root = tk.Tk()
root.title("Ben Trade Analysis 4.0")

window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

entry_label = tk.Label(root, text="请输入交易结果,1为胜,0为败:")
entry_label.pack(pady=5)

entry = tk.Text(root, height=10, wrap=tk.WORD)
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

analyze_button = tk.Button(button_frame, text="Analyze", command=analyze)
analyze_button.pack(side=tk.LEFT, padx=5)

visualize_button = tk.Button(button_frame, text="Visualize", command=visualize)
visualize_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Input", command=clear_input)
clear_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()
