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

fig, ax = plt.subplots(figsize=(24, 18), dpi=300, facecolor="#F8FAFC")
ax.set_facecolor("#F8FAFC")

# -------------------------------------------------------------
# 1. 3D Isometric Stepped Tier Renderer
# -------------------------------------------------------------
def draw_3d_tier(xc, y_bot, w_front, h_front, dx=1.1, dy=0.85, 
                 f_col="#FFFFFF", s_col="#CBD5E1", t_col="#F1F5F9", 
                 e_col="#0F172A", lw=2.4, z=5):
    """Renders an isometric 3D tiered block with clean drop shadow."""
    half_w = w_front / 2.0
    
    # Ambient Drop Shadow
    shadow_poly = [
        (xc - half_w + 0.4, y_bot - 0.35),
        (xc + half_w + 0.8, y_bot - 0.35),
        (xc + half_w + dx + 0.5, y_bot + dy * 0.7),
        (xc - half_w + dx * 0.5, y_bot + dy * 0.7)
    ]
    ax.add_patch(patches.Polygon(shadow_poly, closed=True, facecolor="#94A3B8", alpha=0.30, zorder=z - 3))

    # Front Face
    front_verts = [
        (xc - half_w, y_bot),
        (xc + half_w, y_bot),
        (xc + half_w, y_bot + h_front),
        (xc - half_w, y_bot + h_front)
    ]
    ax.add_patch(patches.Polygon(front_verts, closed=True, facecolor=f_col, edgecolor=e_col, linewidth=lw, zorder=z))

    # Top Cap (Deck)
    top_verts = [
        (xc - half_w, y_bot + h_front),
        (xc + half_w, y_bot + h_front),
        (xc + half_w + dx, y_bot + h_front + dy),
        (xc - half_w + dx, y_bot + h_front + dy)
    ]
    ax.add_patch(patches.Polygon(top_verts, closed=True, facecolor=t_col, edgecolor=e_col, linewidth=lw, zorder=z + 1))

    # Right Side Face
    side_verts = [
        (xc + half_w, y_bot),
        (xc + half_w + dx, y_bot + dy),
        (xc + half_w + dx, y_bot + h_front + dy),
        (xc + half_w, y_bot + h_front)
    ]
    ax.add_patch(patches.Polygon(side_verts, closed=True, facecolor=s_col, edgecolor=e_col, linewidth=lw, zorder=z))


# -------------------------------------------------------------
# 2. Ranking Hierarchy Data: S4 > S3 > S2 > S1
# -------------------------------------------------------------
tiers = [
    {
        "id": r"\(S_1\)", "rank": "Rank 4", "desc": "Baseline Candidate",
        "w": 18.0, "h": 2.2, "y": 3.0,
        "f": "#E2E8F0", "s": "#94A3B8", "t": "#F1F5F9", "edge": "#475569", "badge": "#64748B"
    },
    {
        "id": r"\(S_2\)", "rank": "Rank 3", "desc": "Moderate Competitiveness",
        "w": 14.2, "h": 2.2, "y": 5.8,
        "f": "#BAE6FD", "s": "#0284C7", "t": "#E0F2FE", "edge": "#0369A1", "badge": "#0284C7"
    },
    {
        "id": r"\(S_3\)", "rank": "Rank 2", "desc": "High Performing Runner-up",
        "w": 10.6, "h": 2.2, "y": 8.6,
        "f": "#A7F3D0", "s": "#059669", "t": "#D1FAE5", "edge": "#047857", "badge": "#059669"
    },
    {
        "id": r"\(S_4\)", "rank": "Rank 1 ★", "desc": "Optimal Selected Solution",
        "w": 7.0, "h": 2.4, "y": 11.4,
        "f": "#FECDD3", "s": "#E11D48", "t": "#FFE4E6", "edge": "#BE123C", "badge": "#BE123C"
    }
]

center_x = 10.5

# -------------------------------------------------------------
# 3. Render 3D Stepped Pyramid Tiers
# -------------------------------------------------------------
for i, t in enumerate(tiers):
    draw_3d_tier(
        center_x, t["y"], t["w"], t["h"],
        dx=1.1, dy=0.85,
        f_col=t["f"], s_col=t["s"], t_col=t["t"],
        e_col=t["edge"], lw=2.6, z=4 + i * 4
    )

    # Inset Left Badge (Alternative ID)
    badge_w, badge_h = 2.6, 1.25
    bx = center_x - t["w"] / 2.0 + 1.8
    by = t["y"] + t["h"] / 2.0
    
    badge = patches.FancyBboxPatch(
        (bx - badge_w / 2, by - badge_h / 2), badge_w, badge_h,
        boxstyle="round,pad=0.04,rounding_size=0.35",
        facecolor=t["badge"], edgecolor="#FFFFFF", linewidth=2.0, zorder=20 + i
    )
    ax.add_patch(badge)

    ax.text(
        bx, by,
        t["id"],
        color="#FFFFFF", ha="center", va="center",
        fontsize=28, fontweight="heavy",
        path_effects=[pe.withStroke(linewidth=1.8, foreground="#000000")],
        zorder=22 + i
    )

    # Center-Right Text (Rank and Description)
    ax.text(
        center_x + 0.5, by + 0.32,
        t["rank"],
        color=t["badge"], ha="left", va="center",
        fontsize=28, fontweight="heavy",
        zorder=20 + i
    )
    ax.text(
        center_x + 0.5, by - 0.35,
        t["desc"],
        color="#1E293B", ha="left", va="center",
        fontsize=28, fontweight="semibold",
        zorder=20 + i
    )

# -------------------------------------------------------------
# 4. Ascending Preference Indicator (Right Side Arrow)
# -------------------------------------------------------------
arrow_x = center_x + 10.8
ax.annotate(
    "",
    xy=(arrow_x, 13.8),
    xytext=(arrow_x, 3.2),
    arrowprops=dict(
        arrowstyle="-|>",
        color="#E11D48",
        lw=4.5,
        mutation_scale=32
    ),
    zorder=10
)

ax.text(
    arrow_x + 0.6, 8.5,
    "Ascending Preference Order\n(Relative Closeness Convergence)",
    color="#9F1239", ha="left", va="center",
    fontsize=28, fontweight="bold", linespacing=1.25,
    rotation=270, zorder=12
)

# -------------------------------------------------------------
# 5. Top Header Banner & Base Summary Card
# -------------------------------------------------------------
header_patch = patches.FancyBboxPatch(
    (2.0, 15.6), 20.0, 1.4,
    boxstyle="round,pad=0.04,rounding_size=0.35",
    facecolor="#0B2545", edgecolor="#38BDF8", linewidth=2.4, zorder=30
)
ax.add_patch(header_patch)

ax.text(
    12.0, 16.3,
    "Hierarchical Pyramid Ranking of Decision Alternatives",
    color="#FFFFFF", ha="center", va="center",
    fontsize=28, fontweight="bold",
    path_effects=[pe.withStroke(linewidth=2.2, foreground="#000000")],
    zorder=32
)

panel_patch = patches.FancyBboxPatch(
    (2.0, 0.6), 20.0, 1.3,
    boxstyle="round,pad=0.06,rounding_size=0.35",
    facecolor="#EFF6FF", edgecolor="#2563EB", linewidth=1.8, zorder=30
)
ax.add_patch(panel_patch)

ax.text(
    12.0, 1.42,
    "Confirmed Ranking Hierarchy:  S4 > S3 > S2 > S1",
    color="#1E3A8A", ha="center", va="center",
    fontsize=28, fontweight="heavy", zorder=32
)
ax.text(
    12.0, 0.95,
    "Alternative S4 achieves apex rank (optimal choice) over runner-up S3 and lower-order alternatives",
    color="#334155", ha="center", va="center",
    fontsize=28, fontweight="semibold", zorder=32
)

# -------------------------------------------------------------
# 6. Viewport & Save Options
# -------------------------------------------------------------
ax.set_xlim(0.0, 24.0)
ax.set_ylim(0.0, 18.0)
ax.axis("off")

plt.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)

out_dir = os.getcwd()
png_out = os.path.join(out_dir, "Figure4_Ranking_Pyramid_3D.png")
pdf_out = os.path.join(out_dir, "Figure4_Ranking_Pyramid_3D.pdf")

plt.savefig(png_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.savefig(pdf_out, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())

print(f"Figure 4 successfully generated:\n- {png_out}\n- {pdf_out}")
plt.show()