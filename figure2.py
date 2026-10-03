import os
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Publication Typography Setup (Elsevier / Springer Academic Style)
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

# Closeness coefficient matrix: shape (4 alternatives, 7 parameter combinations)
# Rows: S1, S2, S3, S4 across the 7 parameter combinations
cc_matrix = np.array([
    [0.448275, 0.466462, 0.468682, 0.472846, 0.477582, 0.486464, 0.492574],  # S1
    [0.464052, 0.482551, 0.486342, 0.489832, 0.492861, 0.494368, 0.497624],  # S2
    [0.587065, 0.593024, 0.598538, 0.604688, 0.609256, 0.609543, 0.616276],  # S3
    [0.587097, 0.599065, 0.602381, 0.608624, 0.614359, 0.618229, 0.628422],  # S4 (Winner)
])

alt_labels = [r"\(S_1\)", r"\(S_2\)", r"\(S_3\)", r"\(S_4\)"]
alt_names = ["Alternative 1", "Alternative 2", "Alternative 3", "Alternative 4 (Optimal)"]

# Professional publication palette: Cool Slate -> Sky -> Emerald -> Crimson
face_colors = ["#64748B", "#0284C7", "#10B981", "#E11D48"]
edge_colors = ["#334155", "#0369A1", "#047857", "#9F1239"]

# -------------------------------------------------------------
# 2. Canvas & 3D Axes Setup
# -------------------------------------------------------------
fig = plt.figure(figsize=(26, 17), dpi=300, facecolor="#FFFFFF")
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("#FFFFFF")

# Bar Geometry (Compact footprint for maximum depth readability)
dx_bar = 0.50
dy_bar = 0.42

# Render 3D Bars in order from S1 (back) to S4 (front)
for i in range(4):
    y_idx = i * 1.05
    for j in range(n_params):
        x_idx = j * 1.25
        z_val = cc_matrix[i, j]

        ax.bar3d(
            x_idx - dx_bar / 2.0,
            y_idx - dy_bar / 2.0,
            0.0,
            dx_bar,
            dy_bar,
            z_val,
            color=face_colors[i],
            edgecolor=edge_colors[i],
            linewidth=1.1,
            alpha=0.88,
            shade=True,
        )

# -------------------------------------------------------------
# 3. 3D Trajectory Ribbons & Value Callouts for Optimal S4
# -------------------------------------------------------------
# Plot connecting trend splines across parameter variations for each alternative
for i in range(4):
    y_line = np.full(n_params, i * 1.05)
    x_line = np.arange(n_params) * 1.25
    z_line = cc_matrix[i, :]

    ax.plot(
        x_line, y_line, z_line + 0.002,
        color=edge_colors[i], lw=2.4,
        marker="o", markersize=6, markerfacecolor="#FFFFFF", markeredgecolor=edge_colors[i],
        markeredgewidth=1.8, zorder=20
    )

# Floating Value Badges strictly on the apex alternative S4
for j in range(n_params):
    xj = j * 1.25
    yj = 3 * 1.05
    zj = cc_matrix[3, j]

    ax.text(
        xj, yj, zj + 0.024,
        f"{zj:.4f}",
        color="#9F1239", ha="center", va="bottom",
        fontsize=11.5, fontweight="heavy",
        path_effects=[pe.withStroke(linewidth=3.0, foreground="#FFFFFF")],
        zorder=30
    )

# -------------------------------------------------------------
# 4. View Angle, Pane Styling & Axis Customization
# -------------------------------------------------------------
ax.view_init(elev=26, azim=-62)

# X-Axis: Control Parameters
x_ticks = np.arange(n_params) * 1.25
ax.set_xticks(x_ticks)
ax.set_xticklabels(param_labels, fontsize=14.5, fontweight="bold", color="#0F172A")
ax.set_xlabel(r"\(\mathbf{Combinations\ of\ Control\ Parameters}\ (p, q)\)", fontsize=15.0, fontweight="bold", labelpad=18, color="#0F172A")

# Y-Axis: Alternatives
y_ticks = np.arange(4) * 1.05
ax.set_yticks(y_ticks)
ax.set_yticklabels(alt_labels, fontsize=16.0, fontweight="bold", color="#0F172A")
ax.set_ylabel(r"\(\mathbf{Alternatives}\)", fontsize=15.0, fontweight="bold", labelpad=18, color="#0F172A")

# Z-Axis: Closeness Coefficient values
ax.set_zlim(0.0, 0.74)
ax.set_zticks(np.arange(0.0, 0.71, 0.10))
ax.tick_params(axis="z", labelsize=13.0)
ax.set_zlabel(r"\(\mathbf{Closeness\ Coefficient\ } CC(S_i)\)", fontsize=15.0, fontweight="bold", labelpad=16, color="#0F172A")

# Soft publication pane backgrounds
ax.xaxis.pane.set_facecolor("#F8FAFC")
ax.yaxis.pane.set_facecolor("#FFFFFF")
ax.zaxis.pane.set_facecolor("#F1F5F9")
ax.xaxis.pane.set_edgecolor("#CBD5E1")
ax.yaxis.pane.set_edgecolor("#FFFFFF")
ax.zaxis.pane.set_edgecolor("#CBD5E1")

ax.grid(True, linestyle="--", linewidth=0.7, color="#CBD5E1", alpha=0.75)

# -------------------------------------------------------------
# 5. Header Title & Synthesis Note Box
# -------------------------------------------------------------
plt.title(
    "Sensitivity Analysis & Robustness Assessment Across Parameter Spaces (Table 11)\n",
    fontsize=23.0,
    fontweight="bold",
    color="#0B2545",
    pad=25,
)

summary_message = (
    "Robustness Invariance Proof:  S4 > S3 > S2 > S1 holds strictly invariant across all (p, q) combinations.\n"
    "Alternative S4 consistently achieves optimal closeness CC(S4) ∈ [0.587097, 0.628422], verifying decision stability."
)

fig.text(
    0.50,
    0.045,
    summary_message,
    ha="center",
    va="center",
    fontsize=16.0,
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
# 6. Save & Display Output
# -------------------------------------------------------------
plt.subplots_adjust(left=0.03, right=0.97, bottom=0.10, top=0.92)

out_dir = os.getcwd()
png_out = os.path.join(out_dir, "Figure5_Table11_Sensitivity_3D.png")
pdf_out = os.path.join(out_dir, "Figure5_Table11_Sensitivity_3D.pdf")

plt.savefig(png_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.savefig(pdf_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())

print(f"Publication-ready Figure 5 saved successfully:\n- {png_out}\n- {pdf_out}")
plt.show()