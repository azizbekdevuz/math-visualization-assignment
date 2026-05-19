"""
--------------------------------------
22013143
Azizbek
OSS Assignment Task 8 | Week 11
--------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt

# task 1. math function visualization
def save_function_plot():
    x = np.linspace(-10, 10, 400)
    y1 = x
    y2 = x**2
    y3 = np.sin(x)
    y4 = np.exp(-0.1 * x) * np.cos(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label="y = x", linestyle="-")
    plt.plot(x, y2, label="y = x²", linestyle="--")
    plt.plot(x, y3, label="y = sin(x)", linestyle=":")
    plt.plot(x, y4, label="y = e^(-0.1x) cos(x)", linestyle="-.")
    plt.title("Mathematical Function Visualization")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("function_plot.png", dpi=300)
    plt.close()

# task 2. own equation visualization
def save_own_equation_plot():
    x = np.linspace(-10, 10, 400)
    # This mixed equation combines a cubic trend with sine and cosine waves.
    y = 0.02 * x**3 + 0.8 * np.sin(2 * x) - 1.5 * np.cos(0.5 * x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="y = 0.02x³ + 0.8sin(2x) - 1.5cos(0.5x)")
    plt.title("Own Mixed Equation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("own_equation.png", dpi=300)
    plt.close()

# task 3. student score
def save_score_visualizations():
    students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
    midterm = np.array([85, 72, 90, 66, 78, 92, 60, 74, 88, 95])
    final = np.array([80, 70, 94, 68, 75, 90, 65, 72, 84, 96])
    total = 0.4 * midterm + 0.6 * final

    plt.figure(figsize=(8, 6))
    plt.scatter(midterm, final)
    plt.title("Midterm Score vs Final Score")
    plt.xlabel("Midterm Score")
    plt.ylabel("Final Score")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("score_scatter.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.hist(total, bins=6, edgecolor="black")
    plt.title("Distribution of Total Scores")
    plt.xlabel("Total Score")
    plt.ylabel("Number of Students")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("score_histogram.png", dpi=300)
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(students, total)
    plt.title("Total Score by Student")
    plt.xlabel("Student")
    plt.ylabel("Total Score")
    plt.ylim(0, 100)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig("score_bar_chart.png", dpi=300)
    plt.close()

    return midterm, final

# task 4. best-fit line
def save_prediction_plot(midterm, final):
    slope, intercept = np.polyfit(midterm, final, 1)
    x_line = np.linspace(midterm.min(), midterm.max(), 200)
    y_line = slope * x_line + intercept

    plt.figure(figsize=(8, 6))
    plt.scatter(midterm, final, label="Original data points")
    plt.plot(x_line, y_line, label="Best-fit prediction line", linestyle="--")
    plt.title("Final Score Prediction from Midterm Score")
    plt.xlabel("Midterm Score")
    plt.ylabel("Final Score")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("score_prediction.png", dpi=300)
    plt.close()

    for score in [50, 75, 100]:
        predicted_final = slope * score + intercept
        print(f"Predicted final score for midterm = {score}: {predicted_final:.2f}")

# this is main function to perform all assignment tasks and save files
def main():
    save_function_plot()
    save_own_equation_plot()
    midterm, final = save_score_visualizations()
    save_prediction_plot(midterm, final)


if __name__ == "__main__":
    main()
