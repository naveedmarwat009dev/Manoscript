import os
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np

# Publication Typography Setup
plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "figure.autolayout": False,
    }
)

# Broad canvas setup for high-visibility 3D components
fig, ax = plt.subplots(figsize=(26, 20), dpi=300, facecolor="#FFFFFF")
ax.set_facecolor("#FFFFFF")

# -------------------------------------------------------------
# 1. Premium 3D Beveled Box Builder
# -------------------------------------------------------------
def draw_3d_box(x, y, w, h, dx=0.45, dy=0.32, f_col="#FFFFFF", s_col="#CBD5E1", t_col="#F1F5F9", e_col="#94A3B8", z=4):
    """Draws a premium 3D beveled block with ambient drop shadow, front, top, and side faces."""
    # Ambient Drop Shadow
    shadow = patches.FancyBboxPatch(
        (x + dx + 0.15, y - dy - 0.15), w, h,
        boxstyle="round,pad=0.04,rounding_size=0.35",
        facecolor="#CBD5E1", edgecolor="none", alpha=0.55, zorder=z - 2
    )
    ax.add_patch(shadow)

    # Front Face
    front = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    ax.add_patch(patches.Polygon(front, closed=True, facecolor=f_col, edgecolor=e_col, linewidth=2.6, zorder=z))
    
    # Top Face (Lighter Highlight)
    top = [(x, y + h), (x + w, y + h), (x + w + dx, y + h + dy), (x + dx, y + h + dy)]
    ax.add_patch(patches.Polygon(top, closed=True, facecolor=t_col, edgecolor=e_col, linewidth=2.2, zorder=z))
    
    # Right Side Face (Deeper Shading)
    side = [(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)]
    ax.add_patch(patches.Polygon(side, closed=True, facecolor=s_col, edgecolor=e_col, linewidth=2.2, zorder=z))


# -------------------------------------------------------------
# 2. Conceptual Hierarchy Coordinates & Color Grading
# -------------------------------------------------------------
# Stage 1: Origin (Far Right)
n_origin = {
    "title": "Fuzzy Sets",
    "sub": "Foundation / Baseline Model",
    "x": 22.0, "y": 7.0, "w": 5.6, "h": 2.8,
    "f": "#EFF6FF", "s": "#BFDBFE", "t": "#DBEAFE", "e": "#2563EB", "badge": "#1D4ED8"
}

# Stage 2: Dual Core Extensions (Upper & Lower)
n_core_up = {
    "title": "Intuitionistic\nFuzzy Sets",
    "sub": "Membership & Non-membership",
    "x": 14.4, "y": 10.4, "w": 6.0, "h": 3.0,
    "f": "#F0FDFA", "s": "#99F6E4", "t": "#CCFBF1", "e": "#0D9488", "badge": "#0F766E"
}

n_core_lo = {
    "title": "Bipolar Fuzzy\nSets",
    "sub": "Bipolar Valuation",
    "x": 14.4, "y": 3.4, "w": 6.0, "h": 3.0,
    "f": "#FAF5FF", "s": "#DDD6FE", "t": "#EDE9FE", "e": "#7C3AED", "badge": "#6D28D9"
}

# Stage 3: Direct Linguistic Intermediate
n_mid_up = {
    "title": "Linguistic Intuitionistic\nFuzzy Sets",
    "sub": "Qualitative Degree Modeling",
    "x": 7.8, "y": 8.8, "w": 6.0, "h": 3.2,
    "f": "#FFFBEB", "s": "#FDE68A", "t": "#FEF3C7", "e": "#D97706", "badge": "#B45309"
}

# Stage 4: Unified Convergence (The Final Proposed Model - Far Left)
n_target = {
    "title": "Linguistic Bipolar\nFuzzy Sets",
    "sub": "Comprehensive Unified Output",
    "x": 0.8, "y": 6.0, "w": 5.4, "h": 3.8,
    "f": "#FFF1F2", "s": "#FECDD3", "t": "#FFE4E6", "e": "#E11D48", "badge": "#BE123C"
}

all_nodes_defs = [n_origin, n_core_up, n_core_lo, n_mid_up, n_target]

# -------------------------------------------------------------
# 3. Connection Pipelines (Executing Right-to-Left Convergence)
# -------------------------------------------------------------
# Pipeline: Fuzzy Sets splitting to Intuitionistic & Bipolar
bus_x_origin = n_origin["x"] + n_origin["w"] + 0.3
y_origin_mid = n_origin["y"] + n_origin["h"] / 2
y_upper_mid = n_core_up["y"] + n_core_up["h"] / 2
y_lower_mid = n_core_lo["y"] + n_core_lo["h"] / 2

# Vertical split from Fuzzy Sets
ax.plot([bus_x_origin, n_origin["x"] + n_origin["w"]], [y_origin_mid, y_origin_mid], color="#1D4ED8", lw=3.0, zorder=1)
ax.plot([bus_x_origin, bus_x_origin], [y_upper_mid, y_lower_mid], color="#1D4ED8", lw=3.0, zorder=1)

# Horizontal pipelines with arrows to the Core Extensions
ax.annotate(
    "",
    xy=(n_core_up["x"] + n_core_up["w"] + 0.45, y_upper_mid),
    xytext=(bus_x_origin, y_upper_mid),
    arrowprops=dict(arrowstyle="-|>", color="#0D9488", lw=3.0, mutation_scale=20),
    zorder=3
)

ax.annotate(
    "",
    xy=(n_core_lo["x"] + n_core_lo["w"] + 0.45, y_lower_mid),
    xytext=(bus_x_origin, y_lower_mid),
    arrowprops=dict(arrowstyle="-|>", color="#7C3AED", lw=3.0, mutation_scale=20),
    zorder=3
)

# Pipeline: Intuitionistic -> Linguistic Intuitionistic (Clean Step-Down)
x_upper_core_mid = n_core_up["x"] + n_core_up["w"] / 2
x_lifs_target = n_target["x"] + n_target["w"] / 2
bus_x_upper = 14.1
y_mid_up_in = n_mid_up["y"] + n_mid_up["h"] * 0.65

ax.plot([n_core_up["x"], bus_x_upper], [y_upper_mid, y_upper_mid], color="#0D9488", lw=3.0, zorder=1)
ax.plot([bus_x_upper, bus_x_upper], [y_upper_mid, y_mid_up_in], color="#0D9488", lw=3.0, zorder=1)
ax.annotate(
    "",
    xy=(n_mid_up["x"] + n_mid_up["w"] + 0.45, y_mid_up_in),
    xytext=(bus_x_upper, y_mid_up_in),
    arrowprops=dict(arrowstyle="-|>", color="#D97706", lw=3.0, mutation_scale=20),
    zorder=3
)

# Pipeline: Linguistic Intuitionistic & Bipolar Fuzzy Sets converging to Target
# 1. From LIFSets to Target
y_target_upper = n_target["y"] + n_target["h"] * 0.72
bus_x_target = 6.6
ax.plot([n_mid_up["x"], bus_x_target], [y_mid_up_in, y_mid_up_in], color="#D97706", lw=3.2, zorder=1)
ax.plot([bus_x_target, bus_x_target], [y_mid_up_in, y_target_upper], color="#D97706", lw=3.2, zorder=1)

ax.annotate(
    "",
    xy=(n_target["x"] + n_target["w"] + 0.45, y_target_upper),
    xytext=(bus_x_target, y_target_upper),
    arrowprops=dict(arrowstyle="-|>", color="#E11D48", lw=3.4, mutation_scale=24),
    zorder=6
)

# 2. From Bipolar to Target (Hollow Pipeline through the center arena)
y_target_lower = n_target["y"] + n_target["h"] * 0.28
# Use dashed pipe for visual distinctness during convergence
path_lower = patches.Path(
    [
        (n_core_lo["x"], y_lower_mid),
        (bus_x_target, y_lower_mid),
        (bus_x_target, y_target_lower),
        (n_target["x"] + n_target["w"] + 0.45, y_target_lower),
    ],
    [patches.Path.MOVETO, patches.Path.LINETO, patches.Path.LINETO, patches.Path.LINETO]
)
ax.add_patch(patches.PathPatch(path_lower, facecolor="none", edgecolor="#7C3AED", lw=3.2, linestyle="--", zorder=3))

ax.annotate(
    "",
    xy=(n_target["x"] + n_target["w"] + 0.45, y_target_lower),
    xytext=(n_target["x"] + n_target["w"] + 1.2, y_target_lower),
    arrowprops=dict(arrowstyle="-|>", color="#E11D48", lw=3.4, mutation_scale=24),
    zorder=6
)

# -------------------------------------------------------------
# 4. Render 3D Boxes, Badges & Large High-Contrast Typography
# -------------------------------------------------------------
# Main Title Plinth
draw_3d_box(
    1.2, 17.6, 24.0, 1.8,
    dx=0.50, dy=0.35,
    f_col="#0B2545", s_col="#07192E", t_col="#134074", e_col="#93C5FD",
    z=8
)

ax.text(
    13.2, 17.6 + 0.9,
    "Conceptual Evolution and Convergence Pipeline of Fuzzy Set Models",
    color="#FFFFFF", ha="center", va="center",
    fontsize=21.0, fontweight="bold",
    path_effects=[pe.withStroke(linewidth=2.5, foreground="#000000")],
    zorder=12
)

# Main theoretical convergence area (The Funnel Arena)
draw_3d_box(
    6.4, 2.2, 13.8, 12.8,
    dx=0.60, dy=0.45,
    f_col="#F8FAFC", s_col="#E2E8F0", t_col="#FFFFFF", e_col="#CBD5E1",
    z=2
)

# Title for the synthesis space
ax.text(
    6.4 + 13.8 / 2, 2.2 + 12.8 - 0.70,
    "THEORETICAL GENERALIZATION & SYNTHESIS ARENA",
    color="#64748B", ha="center", va="center",
    fontsize=13.0, fontweight="bold", zorder=3
)

# Render all the nodes in 3D
for nd in all_nodes_defs:
    draw_3d_box(
        nd["x"], nd["y"], nd["w"], nd["h"],
        dx=0.45, dy=0.32,
        f_col=nd["f"], s_col=nd["s"], t_col=nd["t"], e_col=nd["e"],
        z=5
    )

    # Floating 3D Badge on Top Edge
    tag_w = min(nd["w"] - 1.0, 4.2)
    tag_h = 0.60
    badge = patches.FancyBboxPatch(
        (nd["x"] + nd["w"] / 2 - tag_w / 2, nd["y"] + nd["h"] - tag_h / 2),
        tag_w, tag_h,
        boxstyle="round,pad=0.04,rounding_size=0.28",
        facecolor=nd["badge"], edgecolor="#FFFFFF", linewidth=1.6,
        zorder=8
    )
    ax.add_patch(badge)

    tag_label = "ROOT CONCEPT" if nd == n_origin else ("UNIFIED MODEL" if nd == n_target else "EXTENSION")
    ax.text(
        nd["x"] + nd["w"] / 2, nd["y"] + nd["h"],
        tag_label,
        color="#FFFFFF", ha="center", va="center",
        fontsize=9.5, fontweight="bold", zorder=9
    )

    # Core Heading (Bold, Large, Clear Black Text)
    # Using specific fsize for target to ensure visibility.
    fsize_heading = 16.5 if nd != n_target else 18.0
    ax.text(
        nd["x"] + nd["w"] / 2, nd["y"] + nd["h"] / 2 + 0.18,
        nd["title"],
        color="#000000", ha="center", va="center",
        fontsize=fsize_heading, fontweight="bold", linespacing=1.20,
        path_effects=[pe.withStroke(linewidth=2.4, foreground="#FFFFFF")],
        zorder=8
    )

    # Subtitle Scope
    ax.text(
        nd["x"] + nd["w"] / 2, nd["y"] + 0.45,
        nd["sub"],
        color="#475569", ha="center", va="center",
        fontsize=10.0, fontstyle="italic", fontweight="semibold",
        zorder=8
    )

# -------------------------------------------------------------
# 5. Global Viewport & Export Settings
# -------------------------------------------------------------
# Figure caption/label
ax.text(
    13.2, 0.85,
    "Fig. 6. Structural roadmap modeling the conceptual evolution and integration of fuzzy set extensions.",
    color="#0F172A", ha="center", va="center",
    fontsize=14.0, fontweight="bold"
)

# Standardize visible area
ax.set_xlim(0.0, 28.0)
ax.set_ylim(0.0, 20.2)
ax.axis("off")

plt.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)

# Define output path based on script directory
base_path = os.getcwd()
png_path = os.path.join(base_path, "Conceptual_Convergence_Map_3D.png")
pdf_path = os.path.join(base_path, "Conceptual_Convergence_Map_3D.pdf")

plt.savefig(png_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.savefig(pdf_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())

print(f"Roadmap generated successfully:\n- {png_path}\n- {pdf_path}")
plt.show()