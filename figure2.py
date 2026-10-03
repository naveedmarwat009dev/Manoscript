import os
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import make_interp_spline
import numpy as np

# --- Publication Typography Setup (Nature / IEEE / Elsevier Standard) ---
plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "figure.autolayout": False,
        "axes.edgecolor": "#334155",
        "axes.linewidth": 1.2,
    }
)

# -------------------------------------------------------------
# 1. Dataset Extraction (Table 11: Sensitivity Analysis)
# -------------------------------------------------------------
param_labels = ["(1,1)", "(1,2)", "(2,2)", "(2,3)", "(3,3)", "(4,4)", "(5,5)"]
n_params = len(param_labels)
x_discrete = np.arange(n_params)

# Raw metric values from Table 11
# Rows: S1, S2, S3, S4 across parameter combinations
cc_raw = np.array([
    [0.448275, 0.466462, 0.468682, 0.472846, 0.477582, 0.486464, 0.492574],  # S1
    [0.464052, 0.482551, 0.486342, 0.489832, 0.492861, 0.494368, 0.497624],  # S2
    [0.587065, 0.593024, 0.598538, 0.604688, 0.609256, 0.609543, 0.616276],  # S3
    [0.587097, 0.599065, 0.602381, 0.608624, 0.614359, 0.618229, 0.628422],  # S4 (Optimal)
])

alt_labels = [r"\(S_1\)", r"\(S_2\)", r"\(S_3\)", r"\(S_4\)"]
alt_titles = ["Alternative 1", "Alternative 2", "Alternative 3", "Alternative 4 (Optimal)"]

# Professional palette: Cool Slate, Cobalt Navy, Mint Emerald, Vibrant Ruby
curve_colors = ["#475569", "#0284C7", "#059669", "#E11D48"]
fill_colors = ["#94A3B8", "#38BDF8", "#34D399", "#FB7185"]

# -------------------------------------------------------------
# 2. 3D Canvas Configuration
# -------------------------------------------------------------
fig = plt.figure(figsize=(26, 17), dpi=300, facecolor="#FFFFFF")
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("#FFFFFF")

# Dense spline interpolation for continuous 3D ribbon manifolds
x_fine = np.linspace(0, n_params - 1, 140)

# Render each alternative as an extruded 3D curtain/ribbon manifold
ribbon_depth = 0.35  # thickness in Y dimension

for i in range(4):
    y_center = i * 1.4
    y_front = y_center - ribbon_depth / 2.0
    y_back = y_center + ribbon_depth / 2.0

    # Spline interpolation for smooth curve
    spline = make_interp_spline(x_discrete, cc_raw[i, :], k=3)
    z_fine = spline(x_fine)

    # 1. 3D Surface Top Deck (Meshgrid ribbon)
    X_mesh, Y_mesh = np.meshgrid(x_fine, [y_front, y_back])
    Z_mesh = np.vstack([z_fine, z_fine])

    ax.plot_surface(
        X_mesh, Y_mesh, Z_mesh,
        color=fill_colors[i],
        alpha=0.82,
        edgecolor=curve_colors[i],
        linewidth=0.5,
        shade=True,
        zorder=10 + i * 4
    )

    # 2. 3D Extruded Front Shadow Wall (Drop to baseline 0.38)
    z_floor = 0.38
    for xi in range(len(x_fine) - 1):
        x_seg = [x_fine[xi], x_fine[xi+1], x_fine[xi+1], x_fine[xi]]
        y_seg = [y_front, y_front, y_front, y_front]
        z_seg = [z_floor, z_floor, z_fine[xi+1], z_fine[xi]]
        ax.plot_surface(
            np.array([[x_seg[0], x_seg[1]], [x_seg[3], x_seg[2]]]),
            np.array([[y_seg[0], y_seg[1]], [y_seg[3], y_seg[2]]]),
            np.array([[z_seg[0], z_seg[1]], [z_seg[3], z_seg[2]]]),
            color=curve_colors[i],
            alpha=0.28,
            shade=False,
            zorder=8 + i * 4
        )

    # 3. Discrete Benchmark Points & Outlines
    ax.plot(
        x_discrete, np.full(n_params, y_center), cc_raw[i, :],
        color=curve_colors[i],
        lw=3.0,
        marker="o",
        markersize=7.5,
        markerfacecolor="#FFFFFF",
        markeredgecolor=curve_colors[i],
        markeredgewidth=2.2,
        zorder=25 + i * 4
    )

    # 4. Floating Callout Values for Optimal S4 (Apex Layer)
    if i == 3:
        for j in range(n_params):
            val_txt = f"{cc_raw[3, j]:.4f}"
            ax.text(
                x_discrete[j], y_center, cc_raw[3, j] + 0.024,
                val_txt,
                color="#9F1239", ha="center", va="bottom",
                fontsize=11.5, fontweight="heavy",
                path_effects=[pe.withStroke(linewidth=3.0, foreground="#FFFFFF")],
                zorder=35
            )

    # 5. Floor Projection Contour Line (Projected on bottom pane)
    ax.plot(
        x_fine, np.full_like(x_fine, y_center), np.full_like(x_fine, z_floor),
        color=curve_colors[i],
        lw=1.6,
        linestyle=":",
        alpha=0.6,
        zorder=2
    )

# -------------------------------------------------------------
# 3. Camera Angle, Axis & Pane Styling
# -------------------------------------------------------------
ax.view_init(elev=24, azim=-58)

# X-Axis (Parameter Combinations)
ax.set_xticks(x_discrete)
ax.set_xticklabels(param_labels, fontsize=14.5, fontweight="bold", color="#0F172A")
ax.set_xlabel(r"\(\mathbf{Control\ Parameter\ Sets}\ (p, q)\)", fontsize=15.0, fontweight="bold", labelpad=18, color="#0F172A")

# Y-Axis (Decision Alternatives)
ax.set_yticks([i * 1.4 for i in range(4)])
ax.set_yticklabels(alt_labels, fontsize=17.0, fontweight="bold", color="#0F172A")
ax.set_ylabel(r"\(\mathbf{Decision\ Alternatives}\)", fontsize=15.0, fontweight="bold", labelpad=18, color="#0F172A")

# Z-Axis (Closeness Coefficient CC)
ax.set_zlim(0.38, 0.68)
ax.set_zticks(np.arange(0.40, 0.66, 0.05))
ax.tick_params(axis="z", labelsize=13.0)
ax.set_zlabel(r"\(\mathbf{Closeness\ Coefficient\ } CC(S_i)\)", fontsize=15.0, fontweight="bold", labelpad=16, color="#0F172A")

# Subtle panes styling
ax.xaxis.pane.set_facecolor("#F8FAFC")
ax.yaxis.pane.set_facecolor("#FFFFFF")
ax.zaxis.pane.set_facecolor("#F1F5F9")
ax.xaxis.pane.set_edgecolor("#CBD5E1")
ax.yaxis.pane.set_edgecolor("#FFFFFF")
ax.zaxis.pane.set_edgecolor("#CBD5E1")

ax.grid(True, linestyle="--", linewidth=0.7, color="#CBD5E1", alpha=0.75)

# -------------------------------------------------------------
# 4. Header Banner & Synthesis Panel
# -------------------------------------------------------------
plt.title(
    "Figure 5. 3D Parameter-Manifold Continuous Response Surface (Table 11)\n",
    fontsize=20.0,
    fontweight="bold",
    color="#0B2545",
    pad=24,
)

summary_message = (
    "Monotonic Convergence & Invariance Verification:  S4 > S3 > S2 > S1 across all parameter spaces.\n"
    "The 3D topology demonstrates zero manifold intersection, validating total solution stability under varying (p, q)."
)

fig.text(
    0.50,
    0.045,
    summary_message,
    ha="center",
    va="center",
    fontsize=14.0,
    fontweight="bold",
    color="#0B2545",
    linespacing=1.35,
    bbox=dict(
        boxstyle="round,pad=0.75,rounding_size=0.35",
        facecolor="#F0F9FF",
        edgecolor="#0284C7",
        linewidth=1.8,
    ),
)

# -------------------------------------------------------------
# 5. Save & Export Options
# -------------------------------------------------------------
plt.subplots_adjust(left=0.03, right=0.97, bottom=0.10, top=0.92)

out_dir = os.getcwd()
png_out = os.path.join(out_dir, "Figure5_Table11_SurfaceManifold_3D.png")
pdf_out = os.path.join(out_dir, "Figure5_Table11_SurfaceManifold_3D.pdf")

plt.savefig(png_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.savefig(pdf_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())

print(f"3D Continuous Manifold Figure successfully generated:\n- {png_out}\n- {pdf_out}")
plt.show()