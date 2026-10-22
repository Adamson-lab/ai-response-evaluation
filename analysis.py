import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate mock dataset for 100 prompts to simulate the full portfolio project
np.random.seed(42)
domains = ['Reasoning', 'Coding', 'Creative', 'Factual']

data = {
    'prompt_id': range(1, 101),
    'domain': np.random.choice(domains, 100),
    'model_a_score': np.random.randint(3, 6, 100),
    'model_b_score': np.random.randint(1, 6, 100)
}
df = pd.DataFrame(data)

# Determine the winner
conditions = [
    (df['model_a_score'] > df['model_b_score']),
    (df['model_a_score'] < df['model_b_score'])
]
choices = ['Model A', 'Model B']
df['winner'] = np.select(conditions, choices, default='Tie')

# Chart 1: Win Rate Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='winner', data=df, palette='viridis', order=['Model A', 'Model B', 'Tie'])
plt.title('Overall Win Rate: Model A vs Model B')
plt.ylabel('Number of Prompts')
plt.savefig('win_rate.png')

# Chart 2: Average Score by Domain
plt.figure(figsize=(10, 6))
df_melted = df.melt(id_vars=['domain'], value_vars=['model_a_score', 'model_b_score'],
                    var_name='Model', value_name='Score')
sns.barplot(x='domain', y='Score', hue='Model', data=df_melted, errorbar=None, palette='mako')
plt.title('Average Performance Score by Domain')
plt.ylim(0, 5)
plt.savefig('domain_scores.png')

print("Evaluation analysis complete. Charts saved as win_rate.png and domain_scores.png.")
