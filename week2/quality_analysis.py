import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Data ──────────────────────────────────────────────
categories = [
    'Functional\nSuitability', 'Performance\nEfficiency',
    'Compatibility', 'Usability', 'Reliability',
    'Security', 'Maintainability', 'Portability'
]
weights     = [15, 12, 10, 15, 15, 15, 8, 10]
app1_scores = [4,  4,  4,  4,  4,  4,  4,  4]   # inDrive
app2_scores = [3.5, 3.5, 3, 3,  3,  3,  3,  3]  # BYKEA

N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]   # close the polygon

def close(lst): return lst + lst[:1]

# ── Plot ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#F8F9FA')
ax.set_facecolor('#F8F9FA')

# Grid styling
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8, color='grey')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax.tick_params(pad=15)
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.5)
ax.spines['polar'].set_visible(False)

# inDrive (green)
ax.plot(angles, close(app1_scores), color='#1D9E75', linewidth=2.5, linestyle='solid')
ax.fill(angles, close(app1_scores), color='#1D9E75', alpha=0.2)

# BYKEA (blue)
ax.plot(angles, close(app2_scores), color='#378ADD', linewidth=2.5, linestyle='dashed')
ax.fill(angles, close(app2_scores), color='#378ADD', alpha=0.15)

# Legend & title
p1 = mpatches.Patch(color='#1D9E75', label='inDrive  (Weighted: 4.00)')
p2 = mpatches.Patch(color='#378ADD', label='BYKEA   (Weighted: 3.14)')
ax.legend(handles=[p1, p2], loc='upper right', bbox_to_anchor=(1.3, 1.15), fontsize=11)
ax.set_title('Experiment D — Radar Chart\ninDrive vs BYKEA Quality Profile',
             fontsize=14, fontweight='bold', pad=25)

plt.tight_layout()
plt.savefig('radar_chart.png', dpi=150, bbox_inches='tight')
plt.show()
print("Saved as radar_chart.png")