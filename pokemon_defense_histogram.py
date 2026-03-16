import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Pokemon data
df = pd.read_csv('Pokemon.csv')

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Overall defense distribution across all generations
ax1 = axes[0]
ax1.hist(df['Defense'], bins=30, color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Defense Value', fontsize=12)
ax1.set_ylabel('Frequency', fontsize=12)
ax1.set_title('Distribution of Pokémon Defense Values Across All Generations', fontsize=14, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Plot 2: Defense values by generation (side-by-side histograms)
ax2 = axes[1]
generations = sorted(df['Generation'].unique())
colors = plt.cm.tab10(np.linspace(0, 1, len(generations)))

# Create grouped histogram by generation
for i, gen in enumerate(generations):
    gen_data = df[df['Generation'] == gen]['Defense']
    ax2.hist(gen_data, bins=20, alpha=0.6, label=f'Gen {int(gen)}', color=colors[i])

ax2.set_xlabel('Defense Value', fontsize=12)
ax2.set_ylabel('Frequency', fontsize=12)
ax2.set_title('Defense Values Distribution by Generation', fontsize=14, fontweight='bold')
ax2.legend(loc='upper right', ncol=3)
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('pokemon_defense_histogram.png', dpi=300, bbox_inches='tight')
print("Histogram saved as 'pokemon_defense_histogram.png'")

# Print summary statistics
print("\n" + "="*60)
print("POKÉMON DEFENSE STATISTICS")
print("="*60)
print(f"Overall Defense - Mean: {df['Defense'].mean():.2f}, Median: {df['Defense'].median():.2f}")
print(f"Overall Defense - Min: {df['Defense'].min()}, Max: {df['Defense'].max()}")
print("\nDefense Statistics by Generation:")
print("-"*60)
for gen in generations:
    gen_data = df[df['Generation'] == gen]['Defense']
    print(f"Gen {int(gen):2d}: Mean={gen_data.mean():6.2f}, Median={gen_data.median():6.1f}, Min={gen_data.min():3d}, Max={gen_data.max():3d}, Count={len(gen_data):3d}")
print("="*60)

# Display the plot
plt.show()
