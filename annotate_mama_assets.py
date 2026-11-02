import os
from PIL import Image, ImageDraw

assets_dir = "/home/hermesagent/obsidian-vault/projects/report_assets_mama"

# 1. Desktop Hero: Highlight Header & Stats
im_hero = Image.open(f"{assets_dir}/ss_desktop_hero.png").convert("RGB")
draw_h = ImageDraw.Draw(im_hero)
w_h, h_h = im_hero.size
# Top Bar & Header (Mama WA + Logo)
draw_h.rectangle([10, 0, w_h - 10, int(h_h * 0.16)], outline=(220, 38, 38), width=6)
# Stats Grid (50+ Artis, 300+ Event, 1 Pintu)
draw_h.rectangle([int(w_h * 0.12), int(h_h * 0.68), int(w_h * 0.88), int(h_h * 0.96)], outline=(220, 38, 38), width=6)
im_hero.save(f"{assets_dir}/annotated_hero.jpg", quality=95)

# 2. Desktop Roster: Highlight Filter Kategori & Roster Artis
im_roster = Image.open(f"{assets_dir}/ss_desktop_roster.png").convert("RGB")
draw_r = ImageDraw.Draw(im_roster)
w_r, h_r = im_roster.size
# Category Pills & Artist Grid
draw_r.rectangle([int(w_r * 0.05), int(h_r * 0.45), int(w_r * 0.95), int(h_r * 0.98)], outline=(220, 38, 38), width=6)
im_roster.save(f"{assets_dir}/annotated_roster.jpg", quality=95)

# 3. Mobile View: Highlight Mobile Responsive & Action
im_mob = Image.open(f"{assets_dir}/ss_mobile_hero.png").convert("RGB")
draw_m = ImageDraw.Draw(im_mob)
w_m, h_m = im_mob.size
# Mobile header & CTA
draw_m.rectangle([10, int(h_m * 0.02), w_m - 10, int(h_m * 0.52)], outline=(220, 38, 38), width=6)
im_mob.save(f"{assets_dir}/annotated_mobile.jpg", quality=95)

# 4. Form Booking WhatsApp Mama
im_form = Image.open(f"{assets_dir}/ss_mobile_full.png").convert("RGB")
draw_f = ImageDraw.Draw(im_form)
w_f, h_f = im_form.size
# Booking form & Send to Mama WA button
draw_f.rectangle([int(w_f * 0.04), int(h_f * 0.60), int(w_f * 0.96), int(h_f * 0.98)], outline=(220, 38, 38), width=6)
im_form.save(f"{assets_dir}/annotated_form.jpg", quality=95)

print("All mama report assets annotated with red boxes successfully!")
