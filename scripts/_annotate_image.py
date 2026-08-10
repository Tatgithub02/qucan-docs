"""Reusable helper for adding UI callouts (highlight boxes + arrows) to
screenshots used in the docs. Draws directly on a copy of the source image
using Pillow, so no external image editor is needed.

Usage pattern (see bottom of file for a worked example):

    from _annotate_image import annotate, Box, Arrow

    annotate(
        "docs/qanvas/images/tour-overview.png",
        "docs/qanvas/images/tour-overview-rename.png",
        boxes=[Box(64, 38, 154, 57)],
        arrows=[Arrow(start=(109, 150), end=(109, 60))],
    )
"""

from dataclasses import dataclass, field
from typing import Tuple
import math

from PIL import Image, ImageDraw

ACCENT = (255, 176, 32, 255)  # warm amber - stands out against the midnight-blue UI
ACCENT_SOFT = (255, 176, 32, 90)


@dataclass
class Box:
    x0: int
    y0: int
    x1: int
    y1: int
    color: Tuple[int, int, int, int] = ACCENT
    width: int = 3
    radius: int = 8
    pad: int = 4


@dataclass
class Arrow:
    start: Tuple[int, int]
    end: Tuple[int, int]
    color: Tuple[int, int, int, int] = ACCENT
    width: int = 4
    head_len: int = 14
    head_width: int = 10
    cursor_dot: bool = True


def _draw_box(draw: ImageDraw.ImageDraw, box: Box) -> None:
    x0, y0, x1, y1 = box.x0 - box.pad, box.y0 - box.pad, box.x1 + box.pad, box.y1 + box.pad
    # soft glow behind the outline so it reads clearly on busy/dark screenshots
    draw.rounded_rectangle(
        (x0 - 2, y0 - 2, x1 + 2, y1 + 2), radius=box.radius + 2, outline=ACCENT_SOFT, width=box.width + 4
    )
    draw.rounded_rectangle((x0, y0, x1, y1), radius=box.radius, outline=box.color, width=box.width)


def _draw_arrow(draw: ImageDraw.ImageDraw, arrow: Arrow) -> None:
    sx, sy = arrow.start
    ex, ey = arrow.end
    draw.line((sx, sy, ex, ey), fill=arrow.color, width=arrow.width)

    angle = math.atan2(ey - sy, ex - sx)
    left = (
        ex - arrow.head_len * math.cos(angle - math.pi / 7),
        ey - arrow.head_len * math.sin(angle - math.pi / 7),
    )
    right = (
        ex - arrow.head_len * math.cos(angle + math.pi / 7),
        ey - arrow.head_len * math.sin(angle + math.pi / 7),
    )
    draw.polygon([arrow.end, left, right], fill=arrow.color)

    if arrow.cursor_dot:
        r = arrow.head_width // 2 + 2
        draw.ellipse((sx - r, sy - r, sx + r, sy + r), fill=arrow.color)


def annotate(src_path: str, dst_path: str, boxes=(), arrows=()) -> None:
    base = Image.open(src_path).convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for box in boxes:
        _draw_box(draw, box)
    for arrow in arrows:
        _draw_arrow(draw, arrow)

    out = Image.alpha_composite(base, overlay).convert("RGB")
    out.save(dst_path)


if __name__ == "__main__":
    annotate(
        "docs/qanvas/images/tour-overview.png",
        "docs/qanvas/images/tour-overview-rename.png",
        boxes=[Box(64, 38, 154, 57)],
        arrows=[Arrow(start=(109, 160), end=(109, 63))],
    )
    print("wrote docs/qanvas/images/tour-overview-rename.png")
