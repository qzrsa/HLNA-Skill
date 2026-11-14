import json, os, sys

# 一次性数据生成脚本：输入为资料页本地 HTML 缓存，输出为鞍具代码 MD。
# 路径已参数化，不含任何本机绝对路径。用法: python make_saddles.py [输入HTML] [输出MD]
BASE = os.path.dirname(os.path.abspath(__file__))
HTML = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "as2.html")

html = open(HTML, encoding="utf-8").read()

def grab(s, e):
    i = html.index(s) + len(s)
    j = html.index(e, i)
    return html[i:j].strip().rstrip(";").strip()

ITM = json.loads(grab("const ITEM_DATA = ", "\nconst ITEM_SUBCATEGORY_ORDER"))

CN_TIER = {
    "Elite":"精英","Savage":"野蛮","Toxic":"剧毒","Berserk":"狂暴","Necrotic":"坏死",
    "Grenadier":"榴弹","Prime":"至尊","Nuclear":"核","Vampiric":"吸血","Wardens":"守望者",
    "Warden":"守望者","Hellfire":"地狱火","DarkGod":"暗神","Darkgod":"暗神","Corrupted":"腐化暗神",
    "Spectral":"光谱","Primordial":"原初",
}

sad = {}
for name, d in ITM.items():
    eng = d.get("engramName") or name
    if "saddle" in eng.lower():
        tier = eng.split(" ")[0]
        sad.setdefault(tier, []).append((eng, d))

def esc(s): return (s or "").replace("|", "\\|")

L = []
L.append("# ARK Supreme 鞍具(Saddle)生成代码 全量（432 个）\n")
L.append("> 资料来源：社区站 rokiarknet.github.io（第三方粉丝站，非官方）。数值基于 150 级无增益。\n")
L.append("> 用法：`cheat gfi <ID> 1 0 0` 直接获得对应鞍具；`Game.ini 屏蔽` 用 `OverrideNamedEngramEntries` 可隐藏印痕。\n")
L.append("> 鞍具名保留英文原名（印痕/蓝图路径需原样复制）。\n\n")

total = 0
for tier in sorted(sad.keys()):
    items = sorted(sad[tier], key=lambda x: x[0])
    cn = CN_TIER.get(tier, tier)
    L.append(f"## {tier} 阶 / {cn}（{len(items)} 个）\n\n")
    L.append("| 鞍具(英文名) | 生成(gfi) | 蓝图路径 | Game.ini 屏蔽 |\n")
    L.append("|---|---|---|---|\n")
    for eng, d in items:
        L.append(f"| {esc(eng)} | `{esc(d.get('spawn',''))}` | `{esc(d.get('blueprintPath',''))}` | `{esc(d.get('disable',''))}` |\n")
    L.append("\n")
    total += len(items)

out = "".join(L)
path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE, "ARK-Supreme-鞍具代码.md")
open(path, "w", encoding="utf-8").write(out)
print("WROTE", path, "bytes=", len(out.encode("utf-8")), "total_saddles=", total)
print("tiers:", {t: len(sad[t]) for t in sorted(sad)})
