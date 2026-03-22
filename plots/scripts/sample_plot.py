"""
Sample plot script demonstrating the cthan blog matplotlib styles.
Generates both light and dark versions of the same chart.

Usage:
    python plots/scripts/sample_plot.py
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Resolve paths relative to repo root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
STYLE_DIR = REPO_ROOT / "plots"
OUTPUT_DIR = REPO_ROOT / "public" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def make_plot():
    """Generate a sample plot showing the MASO workflow optimization curves."""
    # Walking speed range (m/s)
    v = np.linspace(0.5, 3.0, 200)
    
    # Walking time (seconds) — 468m distance
    T_walk = 468 / v
    
    # Average waiting time (seconds)
    T_wait = 300  # expected value for 600s interval
    
    T_total = T_walk + T_wait
    
    # Energy model (simplified Kuo walking model)
    m, g, L = 70, 9.81, 0.9  # mass, gravity, leg length
    P_walk = (m * g / np.pi) * np.sqrt(3 * g * L / 2) * (1 - np.sqrt(np.pi**2 * v**2 / (6 * g * L)))
    E_total = P_walk * T_walk
    
    # Normalize both for the goodness metric
    T_norm = (T_total - T_total.min()) / (T_total.max() - T_total.min())
    E_norm = (E_total - E_total.min()) / (E_total.max() - E_total.min())
    
    # Goodness metric (weighted sum)
    alpha = 0.6  # weight for time
    goodness = alpha * T_norm + (1 - alpha) * E_norm
    
    # Find optimum
    opt_idx = np.argmin(goodness)
    
    fig, ax = plt.subplots()
    
    ax.plot(v, T_norm, label="Time (normalized)", linestyle="-")
    ax.plot(v, E_norm, label="Energy (normalized)", linestyle="--")
    ax.plot(v, goodness, label=f"Goodness (α={alpha})", linewidth=2.5)
    ax.axvline(v[opt_idx], color="#78716C", linestyle=":", linewidth=1, alpha=0.7)
    ax.annotate(
        f"Optimal: {v[opt_idx]:.2f} m/s",
        xy=(v[opt_idx], goodness[opt_idx]),
        xytext=(v[opt_idx] + 0.4, goodness[opt_idx] + 0.15),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="#78716C", lw=1.2),
    )
    
    ax.set_xlabel("Walking Speed (m/s)")
    ax.set_ylabel("Normalized Cost")
    ax.set_title("Commute Optimization: The MASO Goodness Metric")
    ax.legend()
    
    return fig


# ── Generate light version ──
plt.style.use(str(STYLE_DIR / "cthan_light.mplstyle"))
fig = make_plot()
fig.savefig(OUTPUT_DIR / "maso-goodness-light.svg")
fig.savefig(OUTPUT_DIR / "maso-goodness-light.png")
plt.close(fig)
print(f"✅ Saved light plot to {OUTPUT_DIR / 'maso-goodness-light.svg'}")

# ── Generate dark version ──
plt.style.use(str(STYLE_DIR / "cthan_dark.mplstyle"))
fig = make_plot()
fig.savefig(OUTPUT_DIR / "maso-goodness-dark.svg")
fig.savefig(OUTPUT_DIR / "maso-goodness-dark.png")
plt.close(fig)
print(f"✅ Saved dark plot to {OUTPUT_DIR / 'maso-goodness-dark.svg'}")

print("\nDone! Use in your markdown like:")
print('  ![Goodness Metric](/figures/maso-goodness-light.svg)')
print("\nOr for automatic dark/light switching in Astro HTML:")
print('  <picture>')
print('    <source srcset="/figures/maso-goodness-dark.svg" media="(prefers-color-scheme: dark)">')
print('    <img src="/figures/maso-goodness-light.svg" alt="MASO Goodness Metric">')
print('  </picture>')
