import re, json, urllib.request, os, sys

# 一次性数据生成脚本：输入为 ARK-Supreme 资料页的本地 HTML 缓存，输出为英文版攻略 MD。
# 路径已参数化，不含任何本机绝对路径。用法: python extract_supreme.py [输入HTML] [输出MD]
BASE = os.path.dirname(os.path.abspath(__file__))
HTML = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "as.html")
OUT  = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE, "ARK-Supreme-完整攻略与生成代码.md")

html = open(HTML, encoding="utf-8").read()

def grab(start_marker, end_marker):
    i = html.index(start_marker) + len(start_marker)
    j = html.index(end_marker, i)
    s = html[i:j].strip()
    return s.rstrip(";").strip()

raw_cre = grab("const CREATURE_DATA=", "\nconst TIER_MAP=")
raw_itm = grab("const ITEM_DATA = ", "\nconst ITEM_SUBCATEGORY_ORDER")
raw_order = grab("const ITEM_SUBCATEGORY_ORDER = ", "\nconst NAME_MAP")

CRE = json.loads(raw_cre)
ITM = json.loads(raw_itm)
ORDER = json.loads(raw_order)

# ---- load the narrative guide markdown (fetched locally) ----
GUIDE = os.path.join(BASE, "ark-supreme-guide.md")
guide_md = ""
try:
    guide_md = open(GUIDE, encoding="utf-8").read()
except Exception as e:
    guide_md = f"> ⚠️ 攻略正文读取失败（{e}），可手动访问 https://rokiarknet.github.io/ark-supreme.html 查看。\n"

# ---- group creatures by tier prefix ----
cre_by_tier = {}
for name, d in CRE.items():
    tier = name.split(" ", 1)[0]
    cre_by_tier.setdefault(tier, []).append((name, d))
for t in cre_by_tier:
    cre_by_tier[t].sort(key=lambda x: x[0])

# ---- group items by subcategory (respect declared order) ----
itm_by_sub = {}
for name, d in ITM.items():
    sub = d.get("subcategory") or d.get("category") or "未分类"
    itm_by_sub.setdefault(sub, []).append((name, d))
ordered_subs = [s for s in ORDER if s in itm_by_sub]
for s in itm_by_sub:
    if s not in ordered_subs:
        ordered_subs.append(s)

L = []
L.append("# ARK Supreme（方舟生存飞升）完整攻略 + 全量生成代码\n")
L.append("> 资料来源：社区站 https://rokiarknet.github.io/ark-supreme.html （第三方粉丝站，非官方；官方以 CurseForge + Discord 为准）\n")
L.append("> 数据基于模组实际资产提取；数值按 **150 级无增益、无服务器倍率** 标注。模组持续更新，最新机制请以官方 Discord 为准。\n")
L.append(f"> 本文件含 **{len(CRE)}** 条生物生成代码、**{len(ITM)}** 条物品生成代码。\n")

# ===== Part 1: narrative guide =====
L.append("\n---\n")
L.append("# 第一部分：详细图文攻略（正文）\n")
L.append(guide_md)

# ===== Part 2: creature codes =====
L.append("\n\n---\n")
L.append("# 第二部分：生物生成代码（全量）\n")
L.append("使用说明：\n")
L.append("- `召唤(野生)` = `cheat summon <类名>`：在身边生成一只野生。\n")
L.append("- `召唤(驯服)` = `admincheat GMSummon \"<类名>\" 150`：直接生成一只 150 级已驯服。\n")
L.append("- `SpawnDino` = `cheat spawndino \"<蓝图路径>\" X Y Z 等级`：在指定坐标生成（示例坐标 500 0 0）。\n")
L.append("- `Game.ini 屏蔽`：写入 Game.ini 可让该生物不再自然刷新。\n\n")

for tier in sorted(cre_by_tier.keys()):
    L.append(f"\n## {tier} 阶（{len(cre_by_tier[tier])} 种）\n")
    L.append("| 生物 | 蓝图类名 | 召唤(野生) | 召唤(驯服) | SpawnDino | Game.ini 屏蔽 |\n")
    L.append("|---|---|---|---|---|---|\n")
    for name, d in cre_by_tier[tier]:
        bp = d.get("blueprint","")
        sw = d.get("summonWild","")
        st = d.get("summonTamed","")
        sd = d.get("spawnDino","")
        dis = d.get("disable","")
        # escape pipe chars
        def esc(s): return (s or "").replace("|","\\|")
        L.append(f"| {esc(name)} | `{esc(bp)}` | `{esc(sw)}` | `{esc(st)}` | `{esc(sd)}` | `{esc(dis)}` |\n")

# ===== Part 3: item codes =====
L.append("\n\n---\n")
L.append("# 第三部分：物品生成代码（全量）\n")
L.append("使用说明：\n")
L.append("- `生成(gfi)` = `cheat gfi <物品ID> 1 0 0`：直接获得 1 个物品。\n")
L.append("- `类名`：可用于蓝图/高级指令。\n")
L.append("- `蓝图路径`：完整资产路径。\n")
L.append("- `Game.ini 屏蔽`：用 `OverrideNamedEngramEntries` 可隐藏/移除该印痕。\n\n")

for sub in ordered_subs:
    items = itm_by_sub[sub]
    L.append(f"\n## {sub}（{len(items)} 项）\n")
    L.append("| 物品 | 生成(gfi) | 类名 | 蓝图路径 | Game.ini 屏蔽 |\n")
    L.append("|---|---|---|---|---|\n")
    for name, d in sorted(items, key=lambda x: x[0]):
        eng = d.get("engramName") or name
        cl = d.get("class","")
        sp = d.get("spawn","")
        bp = d.get("blueprintPath","")
        dis = d.get("disable","")
        def esc(s): return (s or "").replace("|","\\|")
        L.append(f"| {esc(eng)} | `{esc(sp)}` | `{esc(cl)}` | `{esc(bp)}` | `{esc(dis)}` |\n")

out = "".join(L)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(out)
print("WROTE", OUT, "bytes=", len(out.encode("utf-8")))
print("creatures=", len(CRE), "items=", len(ITM))
print("tiers=", sorted(cre_by_tier.keys()))
print("subs=", len(ordered_subs))
