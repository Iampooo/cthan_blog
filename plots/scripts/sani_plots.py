"""
Sani Article Plots — All 5 figures
Generates light + dark versions of each plot for the blog.

Usage:
    python plots/scripts/sani_plots.py
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# ── Paths ──
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
STYLE_DIR = REPO_ROOT / "plots"
OUTPUT_DIR = REPO_ROOT / "public" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Shared constants ──
m = 90       # kg
L = 1.05     # m
g = 9.8      # m/s^2
pi = math.pi
distance = 468  # m
alpha = 30.0    # Joule/s


def effort(v):
    K1 = (m * g / pi) * np.sqrt(3 * g * L / 2)
    K2 = (1 - np.sqrt(1 - np.square(pi * v) / (6 * g * L)))
    return K1 * K2 * distance / v


def time_deterministic(v):
    return 300 + distance / v


def metric_deterministic(v, a):
    return a * time_deterministic(v) + effort(v)


def time_stochastic(v):
    TW = np.random.uniform(0, 600, len(v))
    return TW + distance / v


def metric_stochastic(v, a):
    return a * time_stochastic(v) + effort(v)


# =========================================================================
# FIG 1 — Goodness Metric (deterministic)
# =========================================================================
def plot_fig1(style_name, suffix):
    import matplotlib
    matplotlib.rcdefaults()
    plt.style.use(str(STYLE_DIR / style_name))
    v = np.linspace(0.1, 1.5, 200)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(v, effort(v), label="Effort E(v)")
    ax.plot(v, time_deterministic(v) * alpha, label=f"Time × α (α={int(alpha)})")
    ax.plot(v, metric_deterministic(v, alpha), label="Goodness Metric G(v)", linewidth=2.5)
    
    ax.set_xlabel("Walking Speed v (m/s)")
    ax.set_ylabel("Cost")
    ax.set_title("Goodness Metric: Balancing Time and Energy")
    ax.legend()
    ax.set_xlim(0.1, 1.5)

    fig.savefig(OUTPUT_DIR / f"sani-fig1-goodness-{suffix}.svg")
    fig.savefig(OUTPUT_DIR / f"sani-fig1-goodness-{suffix}.png")
    plt.close(fig)
    print(f"  ✅ Fig1 ({suffix})")


# =========================================================================
# FIG 2 — Monte Carlo Box Plot + KKT optimal point
# =========================================================================
def plot_fig2(style_name, suffix):
    import matplotlib
    matplotlib.rcdefaults()
    plt.style.use(str(STYLE_DIR / style_name))
    np.random.seed(42)

    V = np.linspace(0.1, 1.5, 10)
    D = np.zeros((1000, 10))
    for idx, foo in enumerate(V):
        vu = foo
        vs = 0.1 * foo
        v = np.random.normal(vu, vs, 1000)
        D[:, idx] = metric_stochastic(v, alpha)

    fig, ax = plt.subplots(figsize=(7, 5))
    
    bp = ax.boxplot(D, showfliers=False, patch_artist=True)

    # Style the boxes
    is_dark = "dark" in suffix
    box_color = "#4F5EA8" if not is_dark else "#99AAEE"
    median_color = "#2D3A7A" if not is_dark else "#D0DDFF"
    for box in bp['boxes']:
        box.set_facecolor(box_color)
        box.set_alpha(0.25)
        box.set_edgecolor(box_color)
    for median in bp['medians']:
        median.set_color(median_color)
        median.set_linewidth(2)
    for whisker in bp['whiskers']:
        whisker.set_color(box_color)
        whisker.set_alpha(0.6)
    for cap in bp['caps']:
        cap.set_color(box_color)
        cap.set_alpha(0.6)

    ax.set_xticklabels([f"{x:.1f}" for x in V])
    ax.set_xlabel("Walking Speed v (m/s)")
    ax.set_ylabel("Stochastic Goodness Metric G")
    ax.set_title("Monte Carlo Simulation of G(v)")

    # Mark optimal v ≈ 0.52 from KKT conditions
    # v_opt = sqrt(alpha * distance / 52790) ≈ 0.52 for alpha=30
    v_opt = math.sqrt(alpha * distance / 52790)
    # Find which box index is closest
    opt_box_idx = np.argmin(np.abs(V - v_opt))
    
    # Draw annotation
    annotation_color = "#1C1917" if not is_dark else "#F0EBE0"
    accent = "#7C6F5B" if not is_dark else "#D4C4A0"
    
    ax.annotate(
        f"KKT optimal\nv ≈ {v_opt:.2f} m/s",
        xy=(opt_box_idx + 1, np.median(D[:, opt_box_idx])),
        xytext=(opt_box_idx + 3.5, np.median(D[:, opt_box_idx]) - 3000),
        fontsize=10,
        color=annotation_color,
        arrowprops=dict(arrowstyle="->", color=accent, lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", facecolor=accent, alpha=0.15, edgecolor=accent),
    )

    fig.savefig(OUTPUT_DIR / f"sani-fig2-montecarlo-{suffix}.svg")
    fig.savefig(OUTPUT_DIR / f"sani-fig2-montecarlo-{suffix}.png")
    plt.close(fig)
    print(f"  ✅ Fig2 ({suffix})")


# =========================================================================
# FIG 3 — Ring Oscillator regression that doesn't pass through origin
# =========================================================================
def plot_fig3(style_name, suffix):
    import matplotlib
    matplotlib.rcdefaults()
    plt.style.use(str(STYLE_DIR / style_name))

    csv_path = REPO_ROOT / "plots" / "scripts" / "EX4.csv"
    df = pd.read_csv(csv_path)
    df = df.dropna()

    x = df["psro_40c"].values
    y = df["psro"].values

    # Simple linear regression (naive — does NOT force through origin)
    coeffs = np.polyfit(x, y, 1)
    poly = np.poly1d(coeffs)
    x_fit = np.linspace(x.min() - 0.3, x.max() + 0.3, 100)
    y_fit = poly(x_fit)

    is_dark = "dark" in suffix
    scatter_color = "#4F5EA8" if not is_dark else "#99AAEE"
    line_color = "#7C6F5B" if not is_dark else "#D4C4A0"

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(x, y, s=18, alpha=0.5, color=scatter_color, edgecolors="none", label="Data points")
    ax.plot(x_fit, y_fit, color=line_color, linewidth=2, label=f"Linear fit: y = {coeffs[0]:.3f}x + ({coeffs[1]:.3f})")

    ax.set_xlabel("Ring Oscillator Frequency at −40°C")
    ax.set_ylabel("Ring Oscillator Frequency at 25°C")
    ax.set_title("Ring Oscillator Correlation: Simple Linear Regression")
    ax.legend(fontsize=9)

    fig.savefig(OUTPUT_DIR / f"sani-fig3-regression-{suffix}.svg")
    fig.savefig(OUTPUT_DIR / f"sani-fig3-regression-{suffix}.png")
    plt.close(fig)
    print(f"  ✅ Fig3 ({suffix})")


# =========================================================================
# FIG 4 — Power of Linear Regression (showcase)
# =========================================================================
def plot_fig4(style_name, suffix):
    import matplotlib
    matplotlib.rcdefaults()
    plt.style.use(str(STYLE_DIR / style_name))
    np.random.seed(7)

    is_dark = "dark" in suffix
    scatter_color = "#4F5EA8" if not is_dark else "#99AAEE"
    line_color = "#7C6F5B" if not is_dark else "#D4C4A0"
    bad_color = "#B04040" if not is_dark else "#F08080"

    n = 50
    x = np.linspace(1, 10, n)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    # Left: truly linear data — good fit
    y_lin = 2.3 * x + 1.5 + np.random.normal(0, 1.5, n)
    c1 = np.polyfit(x, y_lin, 1)
    axes[0].scatter(x, y_lin, s=25, alpha=0.6, color=scatter_color, edgecolors="none")
    axes[0].plot(x, np.poly1d(c1)(x), color=line_color, linewidth=2,
                 label=f"y = {c1[0]:.2f}x + {c1[1]:.2f}")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].set_title("Linear Data → Linear Fit ✓")
    axes[0].legend(fontsize=9)

    # Right: curved data (log) — linear fit is visibly wrong
    y_log = 8 * np.log(x) + 2 + np.random.normal(0, 0.8, n)
    c2 = np.polyfit(x, y_log, 1)
    axes[1].scatter(x, y_log, s=25, alpha=0.6, color=scatter_color, edgecolors="none")
    axes[1].plot(x, np.poly1d(c2)(x), color=bad_color, linewidth=2, linestyle="--",
                 label=f"Linear fit (wrong model)")
    # also show the correct log fit for contrast
    x_smooth = np.linspace(1, 10, 200)
    # fit log model: y = a*ln(x) + b
    from numpy.linalg import lstsq
    A = np.column_stack([np.log(x), np.ones(n)])
    log_coeffs, _, _, _ = lstsq(A, y_log, rcond=None)
    axes[1].plot(x_smooth, log_coeffs[0] * np.log(x_smooth) + log_coeffs[1],
                 color=line_color, linewidth=2,
                 label=f"Log fit: y = {log_coeffs[0]:.1f}·ln(x) + {log_coeffs[1]:.1f}")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("y")
    axes[1].set_title("Curved Data → Linear Fit ✗")
    axes[1].legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / f"sani-fig4-linreg-{suffix}.svg")
    fig.savefig(OUTPUT_DIR / f"sani-fig4-linreg-{suffix}.png")
    plt.close(fig)
    print(f"  ✅ Fig4 ({suffix})")


# =========================================================================
# FIG 5 — Residuals revealing a missing x² term
# =========================================================================
def plot_fig5(style_name, suffix):
    import matplotlib
    matplotlib.rcdefaults()
    plt.style.use(str(STYLE_DIR / style_name))
    np.random.seed(12)

    is_dark = "dark" in suffix
    scatter_color = "#4F5EA8" if not is_dark else "#99AAEE"
    line_color = "#7C6F5B" if not is_dark else "#D4C4A0"
    residual_color = "#78716C" if not is_dark else "#C0B8A8"
    accent_color = "#B04040" if not is_dark else "#F08080"

    n = 80
    x = np.linspace(-3, 3, n)
    # True model: y = 1.5x² + 2x + 3 + noise
    y_true = 1.5 * x**2 + 2 * x + 3
    noise = np.random.normal(0, 1.2, n)
    y = y_true + noise

    # Fit only linear (intentionally missing the x² term)
    c_lin = np.polyfit(x, y, 1)
    y_fit_lin = np.poly1d(c_lin)(x)
    residuals = y - y_fit_lin

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    # Left: data + linear fit (visibly bad)
    ax1 = axes[0]
    ax1.scatter(x, y, s=20, alpha=0.6, color=scatter_color, edgecolors="none", label="Data (quadratic)")
    ax1.plot(x, y_fit_lin, color=accent_color, linewidth=2, linestyle="--",
             label=f"Linear fit: y = {c_lin[0]:.2f}x + {c_lin[1]:.2f}")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("Fitting a Line to Quadratic Data")
    ax1.legend(fontsize=9)

    # Right: residuals show the parabolic pattern
    ax2 = axes[1]
    ax2.scatter(x, residuals, s=20, alpha=0.6, color=residual_color, edgecolors="none")
    ax2.axhline(0, color=line_color, linewidth=1.2, linestyle="--")
    # Overlay a quadratic fit to the residuals to highlight the pattern
    c_res = np.polyfit(x, residuals, 2)
    x_s = np.linspace(-3, 3, 200)
    ax2.plot(x_s, np.poly1d(c_res)(x_s), color=accent_color, linewidth=1.5, alpha=0.7,
             label=f"Hidden pattern: ~{c_res[0]:.1f}x²")
    ax2.set_xlabel("x")
    ax2.set_ylabel("Residual (y − ŷ)")
    ax2.set_title("Residuals Reveal the Missing x² Term")
    ax2.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / f"sani-fig5-residual-{suffix}.svg")
    fig.savefig(OUTPUT_DIR / f"sani-fig5-residual-{suffix}.png")
    plt.close(fig)
    print(f"  ✅ Fig5 ({suffix})")


# ── Run everything ──
if __name__ == "__main__":
    for style, suffix in [("cthan_light.mplstyle", "light"), ("cthan_dark.mplstyle", "dark")]:
        print(f"\n🎨 Generating {suffix} plots...")
        plot_fig1(style, suffix)
        plot_fig2(style, suffix)
        plot_fig3(style, suffix)
        plot_fig4(style, suffix)
        plot_fig5(style, suffix)

    print(f"\n🎉 All plots saved to {OUTPUT_DIR}")
