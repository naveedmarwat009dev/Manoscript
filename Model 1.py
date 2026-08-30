import os
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt

# Global typography setup for journal publishing
plt.rcParams.update(
    {
        "font.family": "serif",
        "figure.autolayout": False,
    }
)

# Large expanded canvas for prominent typography and 3D bevels
fig, ax = plt.subplots(figsize=(28, 22), dpi=300, facecolor="#FFFFFF")
ax.set_facecolor("#FFFFFF")

# -------------------------------------------------------------
# 1. 3D Isometric Beveled Box Renderer
# -------------------------------------------------------------
def draw_3d_card(x, y, w, h, dx=0.45, dy=0.35, f_col="#FFFFFF", s_col="#CBD5E1", t_col="#F1F5F9", e_col="#94A3B8", z=4):
    # Front Face
    front_verts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    ax.add_patch(
        patches.Polygon(
            front_verts,
            closed=True,
            facecolor=f_col,
            edgecolor=e_col,
            linewidth=2.0,
            zorder=z,
        )
    )

    # Top Lighted Face
    top_verts = [
        (x, y + h),
        (x + w, y + h),
        (x + w + dx, y + h + dy),
        (x + dx, y + h + dy),
    ]
    ax.add_patch(
        patches.Polygon(
            top_verts,
            closed=True,
            facecolor=t_col,
            edgecolor=e_col,
            linewidth=1.8,
            zorder=z,
        )
    )

    # Right Shaded Face
    side_verts = [
        (x + w, y),
        (x + w + dx, y + dy),
        (x + w + dx, y + h + dy),
        (x + w, y + h),
    ]
    ax.add_patch(
        patches.Polygon(
            side_verts,
            closed=True,
            facecolor=s_col,
            edgecolor=e_col,
            linewidth=1.8,
            zorder=z,
        )
    )


# -------------------------------------------------------------
# 2. Main Framework Header (3D Floating Plinth)
# -------------------------------------------------------------
header_w = 18.0
header_h = 2.0
hx = 13.0 - header_w / 2
hy = 18.2

draw_3d_card(
    hx, hy, header_w, header_h,
    dx=0.55, dy=0.42,
    f_col="#0B2545", s_col="#07192E", t_col="#134074", e_col="#93C5FD",
    z=5
)

ax.text(
    13.0,
    hy + header_h / 2,
    "Circular Cubic Pythagorean\nFuzzy Neural Network",
    color="#FFFFFF",
    ha="center",
    va="center",
    fontsize=29,
    fontweight="bold",
    linespacing=1.25,
    path_effects=[pe.withStroke(linewidth=3.0, foreground="#000000")],
    zorder=10,
)

# -------------------------------------------------------------
# 3. Stage Column Data & Color Tokens
# -------------------------------------------------------------
columns = [
    {
        "id": "input",
        "title": "INPUT LAYER",
        "x": 4.5,
        "f_col": "#F0FDF4",
        "s_col": "#BBF7D0",
        "t_col": "#DCFCE7",
        "e_col": "#16A34A",
        "badge_f": "#166534",
        "badge_s": "#14532D",
        "badge_t": "#15803D",
        "step1": "Collect the expert\nassessments in the\nform of CCuPFNs",
        "step2": "Combine the individual\ndecision matrices to\nformulate the collective\ndecision matrix",
    },
    {
        "id": "hidden",
        "title": "HIDDEN LAYER",
        "x": 13.0,
        "f_col": "#FAF5FF",
        "s_col": "#DDD6FE",
        "t_col": "#EDE9FE",
        "e_col": "#7C3AED",
        "badge_f": "#4C1D95",
        "badge_s": "#3B0764",
        "badge_t": "#6D28D9",
        "step1": "Calculate the hidden\nlayer criterion weights",
        "step2": "Aggregate the collective\ndecision matrix by applying\nthe proposed aggregation\noperators",
    },
    {
        "id": "output",
        "title": "OUTPUT LAYER",
        "x": 21.5,
        "f_col": "#F0F9FF",
        "s_col": "#BAE6FD",
        "t_col": "#E0F2FE",
        "e_col": "#0284C7",
        "badge_f": "#075985",
        "badge_s": "#0C4A6E",
        "badge_t": "#0369A1",
        "step1": "Criterion-wise\nDistance Measures",
        "step2": "Computing score values\nfor each known class",
    },
]

# -------------------------------------------------------------
# 4. Pipeline Connectors (Header to 3 Columns)
# -------------------------------------------------------------
trunk_y = 17.0
ax.plot([13.0, 13.0], [hy, trunk_y], color="#0B2545", linewidth=3.0, zorder=2)
ax.plot([4.5, 21.5], [trunk_y, trunk_y], color="#0B2545", linewidth=3.0, zorder=2)

for col in columns:
    xc = col["x"]
    ax.annotate(
        "",
        xy=(xc, 16.0),
        xytext=(xc, trunk_y),
        arrowprops=dict(
            arrowstyle="-|>",
            color="#0B2545",
            lw=3.0,
            mutation_scale=20,
        ),
        zorder=3,
    )

# -------------------------------------------------------------
# 5. Render 3D Column Headers & Step Boxes (Large Text)
# -------------------------------------------------------------
box_w = 6.8
box_h = 4.2
y_step1 = 12.0
y_step2 = 6.0

for col in columns:
    xc = col["x"]

    # 3D Layer Header Box
    hdr_w = 6.2
    hdr_h = 1.1
    draw_3d_card(
        xc - hdr_w / 2, 14.8, hdr_w, hdr_h,
        dx=0.45, dy=0.35,
        f_col=col["badge_f"], s_col=col["badge_s"], t_col=col["badge_t"], e_col="#FFFFFF",
        z=6
    )

    ax.text(
        xc,
        14.8 + hdr_h / 2,
        col["title"],
        color="#FFFFFF",
        ha="center",
        va="center",
        fontsize=25,
        fontweight="bold",
        zorder=10,
    )

    # Arrow: Layer Header -> Step 1
    ax.annotate(
        "",
        xy=(xc, y_step1 + box_h / 2 + 0.35),
        xytext=(xc, 14.8),
        arrowprops=dict(
            arrowstyle="-|>",
            color=col["badge_f"],
            lw=2.8,
            mutation_scale=18,
        ),
        zorder=3,
    )

    # ------------------ STEP 1 (3D BOX) ------------------
    draw_3d_card(
        xc - box_w / 2, y_step1 - box_h / 2, box_w, box_h,
        dx=0.45, dy=0.35,
        f_col=col["f_col"], s_col=col["s_col"], t_col=col["t_col"], e_col=col["e_col"],
        z=4
    )

    # Step 1 Top 3D Badge
    pill_w = 2.8
    pill_h = 0.75
    draw_3d_card(
        xc - pill_w / 2, y_step1 + box_h / 2 - pill_h / 2, pill_w, pill_h,
        dx=0.30, dy=0.22,
        f_col=col["badge_f"], s_col=col["badge_s"], t_col=col["badge_t"], e_col="#FFFFFF",
        z=7
    )

    ax.text(
        xc,
        y_step1 + box_h / 2,
        "Step 1:",
        color="#FFFFFF",
        ha="center",
        va="center",
        fontsize=25,
        fontweight="bold",
        zorder=10,
    )

    # Step 1 Large Bold Text
    ax.text(
        xc,
        y_step1 - 0.30,
        col["step1"],
        color="#0F172A",
        ha="center",
        va="center",
        fontsize=25,
        fontweight="bold",
        linespacing=1.35,
        zorder=8,
    )

    # Arrow: Step 1 -> Step 2
    ax.annotate(
        "",
        xy=(xc, y_step2 + box_h / 2 + 0.35),
        xytext=(xc, y_step1 - box_h / 2),
        arrowprops=dict(
            arrowstyle="-|>",
            color=col["badge_f"],
            lw=2.8,
            mutation_scale=18,
        ),
        zorder=3,
    )

    # ------------------ STEP 2 (3D BOX) ------------------
    draw_3d_card(
        xc - box_w / 2, y_step2 - box_h / 2, box_w, box_h,
        dx=0.45, dy=0.35,
        f_col=col["f_col"], s_col=col["s_col"], t_col=col["t_col"], e_col=col["e_col"],
        z=4
    )

    # Step 2 Top 3D Badge
    draw_3d_card(
        xc - pill_w / 2, y_step2 + box_h / 2 - pill_h / 2, pill_w, pill_h,
        dx=0.30, dy=0.22,
        f_col=col["badge_f"], s_col=col["badge_s"], t_col=col["badge_t"], e_col="#FFFFFF",
        z=7
    )

    ax.text(
        xc,
        y_step2 + box_h / 2,
        "Step 2:",
        color="#FFFFFF",
        ha="center",
        va="center",
        fontsize=25,
        fontweight="bold",
        zorder=10,
    )

    # Step 2 Large Bold Text
    ax.text(
        xc,
        y_step2 - 0.30,
        col["step2"],
        color="#0F172A",
        ha="center",
        va="center",
        fontsize=25,
        fontweight="bold",
        linespacing=1.35,
        zorder=8,
    )

# -------------------------------------------------------------
# 6. Final Result (3D Convergence Plinth)
# -------------------------------------------------------------
res_w = 16.5
res_h = 2.4
rx = 13.0 - res_w / 2
ry = 0.8

draw_3d_card(
    rx, ry, res_w, res_h,
    dx=0.55, dy=0.42,
    f_col="#FFFBEB", s_col="#FDE68A", t_col="#FEF3C7", e_col="#F59E0B",
    z=5
)

# Final Result Top Badge (3D)
tag_w = 4.8
tag_h = 0.75
draw_3d_card(
    13.0 - tag_w / 2, ry + res_h - tag_h / 2, tag_w, tag_h,
    dx=0.30, dy=0.22,
    f_col="#D97706", s_col="#92400E", t_col="#B45309", e_col="#FFFFFF",
    z=7
)

ax.text(
    13.0,
    ry + res_h,
    "FINAL RESULT",
    color="#FFFFFF",
    ha="center",
    va="center",
    fontsize=25,
    fontweight="bold",
    zorder=10,
)

ax.text(
    13.0,
    ry + 0.85,
    "Ranked alternatives based on the score values\nobtained from the proposed methodology.",
    color="#0F172A",
    ha="center",
    va="center",
    fontsize=25,
    fontweight="bold",
    linespacing=1.35,
    zorder=8,
)

# -------------------------------------------------------------
# 7. Convergence Routing Lines to Final Result
# -------------------------------------------------------------
# Left Pipeline (Input -> Final Result)
path_left = patches.Path(
    [
        (4.5, y_step2 - box_h / 2),
        (4.5, ry + res_h / 2),
        (rx, ry + res_h / 2),
    ],
    [patches.Path.MOVETO, patches.Path.LINETO, patches.Path.LINETO],
)
ax.add_patch(
    patches.PathPatch(
        path_left,
        facecolor="none",
        edgecolor=columns[0]["badge_f"],
        linewidth=2.8,
        zorder=3,
    )
)
ax.annotate(
    "",
    xy=(rx, ry + res_h / 2),
    xytext=(rx - 0.8, ry + res_h / 2),
    arrowprops=dict(
        arrowstyle="-|>",
        color=columns[0]["badge_f"],
        lw=2.8,
        mutation_scale=20,
    ),
    zorder=4,
)

# Center Pipeline (Hidden -> Final Result)
ax.annotate(
    "",
    xy=(13.0, ry + res_h + 0.42),
    xytext=(13.0, y_step2 - box_h / 2),
    arrowprops=dict(
        arrowstyle="-|>",
        color=columns[1]["badge_f"],
        lw=2.8,
        mutation_scale=20,
    ),
    zorder=4,
)

# Right Pipeline (Output -> Final Result)
path_right = patches.Path(
    [
        (21.5, y_step2 - box_h / 2),
        (21.5, ry + res_h / 2),
        (rx + res_w + 0.55, ry + res_h / 2),
    ],
    [patches.Path.MOVETO, patches.Path.LINETO, patches.Path.LINETO],
)
ax.add_patch(
    patches.PathPatch(
        path_right,
        facecolor="none",
        edgecolor=columns[2]["badge_f"],
        linewidth=2.8,
        zorder=3,
    )
)
ax.annotate(
    "",
    xy=(rx + res_w + 0.55, ry + res_h / 2),
    xytext=(rx + res_w + 1.35, ry + res_h / 2),
    arrowprops=dict(
        arrowstyle="-|>",
        color=columns[2]["badge_f"],
        lw=2.8,
        mutation_scale=20,
    ),
    zorder=4,
)

# -------------------------------------------------------------
# 8. Viewport & Export Settings
# -------------------------------------------------------------
ax.set_xlim(0.0, 26.0)
ax.set_ylim(-0.4, 21.2)
ax.axis("off")

plt.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)

# Output Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
png_path = os.path.join(script_dir, "Circular_Cubic_Pythagorean_FNN_3D_LargeText.png")
pdf_path = os.path.join(script_dir, "Circular_Cubic_Pythagorean_FNN_3D_LargeText.pdf")

plt.savefig(
    png_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor()
)
plt.savefig(
    pdf_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor()
)

print(f"Files saved successfully:\n- {png_path}\n- {pdf_path}")
plt.show()