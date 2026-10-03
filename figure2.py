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

# Wide landscape canvas focused strictly on the ranking order
fig, ax = plt.subplots(figsize=(26, 12), dpi=300, facecolor="#F8FAFC")
ax.set_facecolor("#F8FAFC")

# -------------------------------------------------------------
# 1. 3D Isometric Chevron Wedge Renderer
# -------------------------------------------------------------
def draw_3d_chevron_wedge(x_tip, y_mid, w, h, indent=1.8, dx=1.2, dy=0.8,
                          f_col="#FFFFFF", s_col="#CBD5E1", t_col="#F1F5F9",
                          e_col="#0F172A", lw=2.8, z=5):
    """
    Draws a 3D extruded chevron block pointing in the direction of preference (>).
    """
    x_back = x_tip - w
    y_top = y_mid + h / 2.0
    y_bot = y_mid - h / 2.0

    # Ambient drop shadow
    shadow_poly = [
        (x_back + indent + 0.3, y_mid - 0.4),
        (x_back + 0.3, y_bot - 0.4),
        (x_tip - indent + 0.3, y_bot - 0.4),
        (x_tip + 0.3, y_mid - 0.4),
        (x_tip + dx + 0.3, y_mid + dy * 0.7),
        (x_back + indent + dx + 0.3, y_mid + dy * 0.7)
    ]
    ax.add_patch(patches.Polygon(shadow_poly, closed=True, facecolor="#94A3B8", alpha=0.35, zorder=z - 3))

    # Front Chevron Face
    front_verts = [
        (x_back, y_top),
        (x_tip - indent, y_top),
        (x_tip, y_mid),
        (x_tip - indent, y_bot),
        (x_back, y_bot),
        (x_back + indent, y_mid)
    ]
    ax.add_patch(patches.Polygon(front_verts, closed=True, facecolor=f_col, edgecolor=e_col, linewidth=lw, zorder=z))

    # Top Edge Facet
    top_verts = [
        (x_back, y_top),
        (x_tip - indent, y_top),
        (x_tip - indent + dx, y_top + dy),
        (x_back + dx, y_top + dy)
    ]
    ax.add_patch(patches.Polygon(top_verts, closed=True, facecolor=t_col, edgecolor=e_col, linewidth=lw, zorder=z + 1))

    # Upper Slanted Right Facet
    upper_right = [
        (x_tip - indent, y_top),
        (x_tip, y_mid),
        (x_tip + dx, y_mid + dy),
        (x_tip - indent + dx, y_top + dy)
    ]
    ax.add_patch(patches.Polygon(upper_right, closed=True, facecolor=s_col, edgecolor=e_col, linewidth=lw, zorder=z + 1))


# -------------------------------------------------------------
# 2. Pure Ranking Order Sequence: S4 > S3 > S2 > S1
# -------------------------------------------------------------
elements = [
    {
        "id": "\(S_4\)",
        "f": "#FECDD3", "s": "#E11D48", "t": "#FFE4E6",
        "edge": "#BE123C", "text_col": "#9F1239"
    },
    {
        "id": "\(S_3\)",
        "f": "#A7F3D0", "s": "#059669", "t": "#D1FAE5",
        "edge": "#047857", "text_col": "#065F46"
    },
    {
        "id": "\(S_2\)",
        "f": "#BAE6FD", "s": "#0284C7", "t": "#E0F2FE",
        "edge": "#0369A1", "text_col": "#075985"
    },
    {
        "id": "\(S_1\)",
        "f": "#E2E8F0", "s": "#64748B", "t": "#F1F5F9",
        "edge": "#475569", "text_col": "#334155"
    }
]

y_center = 5.2
chevron_w = 4.8
chevron_h = 3.6
indent_val = 1.3
dx_val, dy_val = 1.1, 0.8

x_positions = [6.5, 12.0, 17.5, 23.0]

# -------------------------------------------------------------
# 3. Render 3D Chevrons and Preference Connectors
# -------------------------------------------------------------
for i, el in enumerate(elements):
    xt = x_positions[i]

    draw_3d_chevron_wedge(
        xt, y_center, chevron_w, chevron_h,
        indent=indent_val, dx=dx_val, dy=dy_val,
        f_col=el["f"], s_col=el["s"], t_col=el["t"],
        e_col=el["edge"], lw=2.8, z=5 + i * 2
    )

    # Center alternative ID inside each chevron block
    text_x = xt - chevron_w / 2.0 + indent_val * 0.4
    ax.text(
        text_x, y_center,
        el["id"],
        color=el["text_col"], ha="center", va="center",
        fontsize=38.0, fontweight="heavy",
        path_effects=[pe.withStroke(linewidth=3.0, foreground="#FFFFFF")],
        zorder=20 + i
    )

    # 3D relational ">" symbol between chevrons
    if i < 3:
        next_x = x_positions[i + 1]
        mid_rel_x = (xt + (next_x - chevron_w)) / 2.0 + 0.1
        ax.text(
            mid_rel_x, y_center + 0.1,
            ">",
            color="#0F172A", ha="center", va="center",
            fontsize=40.0, fontweight="heavy",
            path_effects=[pe.withStroke(linewidth=2.5, foreground="#FFFFFF")],
            zorder=25
        )

# -------------------------------------------------------------
# 4. Figure Header Banner
# -------------------------------------------------------------
header_patch = patches.FancyBboxPatch(
    (2.5, 9.2), 21.0, 1.6,
    boxstyle="round,pad=0.05,rounding_size=0.4",
    facecolor="#0B2545", edgecolor="#38BDF8", linewidth=2.6, zorder=30
)
ax.add_patch(header_patch)

ax.text(
    13.0, 10.0,
    "3D Representation of Ranking Order",
    color="#FFFFFF", ha="center", va="center",
    fontsize=24.0, fontweight="bold",
    path_effects=[pe.withStroke(linewidth=2.2, foreground="#000000")],
    zorder=32
)

# -------------------------------------------------------------
# 5. Clean Baseline Equation
# -------------------------------------------------------------
ax.text(
    13.0, 1.4,
    "\(S_4 > S_3 > S_2 > S_1\)",
    color="#0B2545", ha="center", va="center",
    fontsize=32.0, fontweight="bold",
    path_effects=[pe.withStroke(linewidth=3.0, foreground="#FFFFFF")],
    zorder=30
)

# -------------------------------------------------------------
# 6. Viewport & Export Options
# -------------------------------------------------------------
ax.set_xlim(0.0, 26.0)
ax.set_ylim(0.0, 12.0)
ax.axis("off")

plt.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)

out_dir = os.getcwd()
png_out = os.path.join(out_dir, "Figure4_Ranking_Order_3D.png")
pdf_out = os.path.join(out_dir, "Figure4_Ranking_Order_3D.pdf")

plt.savefig(png_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.savefig(pdf_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())

print(f"Figure 4 saved successfully:\n- {png_out}\n- {pdf_out}")
plt.show()