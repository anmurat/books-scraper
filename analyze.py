import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv("books.csv")

print("=== SUMMARY ===")
print(f"Total books: {len(df)}")
print(f"Average price: £{df['price'].mean():.2f}")
print(f"Cheapest: £{df['price'].min()} — {df.loc[df['price'].idxmin(), 'title']}")
print(f"Most expensive: £{df['price'].max()} — {df.loc[df['price'].idxmax(), 'title']}")
print(f"\nRating distribution:\n{df['rating'].value_counts().sort_index()}")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Books to Scrape — Data Analysis", fontsize=14, fontweight="bold")

# 1. Books per rating
rating_counts = df["rating"].value_counts().sort_index()
bars = axes[0].bar(rating_counts.index, rating_counts.values, color="#4A90D9", edgecolor="white", linewidth=0.5)
axes[0].set_title("Books per rating")
axes[0].set_xlabel("Rating (1-5)")
axes[0].set_ylabel("Number of books")
for bar in bars:
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 str(int(bar.get_height())), ha="center", va="bottom", fontsize=9)

# 2. Price distribution
axes[1].hist(df["price"], bins=15, color="#E8845A", edgecolor="white", linewidth=0.5)
axes[1].set_title("Price distribution")
axes[1].set_xlabel("Price (£)")
axes[1].set_ylabel("Number of books")
axes[1].xaxis.set_major_formatter(ticker.FormatStrFormatter("£%.0f"))

# 3. Average price per rating
avg_price = df.groupby("rating")["price"].mean()
bars2 = axes[2].bar(avg_price.index, avg_price.values, color="#6BBF8E", edgecolor="white", linewidth=0.5)
axes[2].set_title("Average price per rating")
axes[2].set_xlabel("Rating (1-5)")
axes[2].set_ylabel("Average price (£)")
for bar in bars2:
    axes[2].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                 f"£{bar.get_height():.1f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("analysis.png", dpi=150, bbox_inches="tight")
print("\nChart saved to analysis.png")
plt.show()