import json, os, sys

# 一次性数据生成脚本：输入为资料页本地 HTML 缓存，输出为金属工具代码 MD。
# 路径已参数化，不含任何本机绝对路径。用法: python make_metal_tools.py [输入HTML] [输出MD]
BASE = os.path.dirname(os.path.abspath(__file__))
HTML = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "as2.html")

html = open(HTML, encoding="utf-8").read()

def grab(s, e):
    i = html.index(s) + len(s)
    j = html.index(e, i)
    return html[i:j].strip().rstrip(";").strip()

ITM = json.loads(grab("const ITEM_DATA = ", "\nconst ITEM_SUBCATEGORY_ORDER"))

def esc(s): return (s or "").replace("|", "\\|")

# Modded Metal Tools 全量 + Elite 石头工具（同属该类）
items = []
for name, d in ITM.items():
    sub = d.get("subcategory") or d.get("category") or ""
    if sub == "Modded Metal Tools" and d.get("spawn"):
        items.append((d.get("engramName") or name, d))

# 按工具类型 + 阶层排序
def sortkey(x):
    eng = x[0]
    for t in ["MetalPick","MetalHatchet","Pike","Sickle","ChainSaw","StonePick","StoneHatchet"]:
        if t.lower() in eng.lower():
            return (t, eng)
    return (eng, eng)

items.sort(key=sortkey)

L = []
L.append("# ARK Supreme 金属工具(Modded Metal Tools)生成代码 全量\n")
L.append("> 资料来源：社区站 rokiarknet.github.io（第三方粉丝站，非官方）。数值基于 150 级无增益。\n")
L.append("> 用法：`cheat gfi <ID> 1 0 0` 直接获得；`Game.ini 屏蔽` 用 `OverrideNamedEngramEntries` 可隐藏印痕。\n")
L.append("> 采集倍率随阶层提升：Savage 1.5x → Toxic 2x → Berserk 2.5x → Necrotic 3x → Prime 3.5x → Hellfire 4x。\n\n")

# 分组展示
groups = {}
for eng, d in items:
    key = "其他"
    low = eng.lower()
    if "chain" in low: key="电锯 ChainSaw"
    elif "stonepick" in low: key="精英石头镐 StonePick"
    elif "stonehatchet" in low: key="精英石头斧 StoneHatchet"
    elif "metalpick" in low: key="金属镐 MetalPick"
    elif "metalhatchet" in low: key="金属斧 MetalHatchet"
    elif "pike" in low: key="长矛 Pike"
    elif "sickle" in low: key="镰刀 Sickle"
    groups.setdefault(key, []).append((eng, d))

for g in ["金属镐 MetalPick","金属斧 MetalHatchet","长矛 Pike","镰刀 Sickle","电锯 ChainSaw","精英石头镐 StonePick","精英石头斧 StoneHatchet","其他"]:
    if g not in groups: continue
    L.append(f"## {g}（{len(groups[g])} 个）\n\n")
    L.append("| 物品(英文名) | 生成(gfi) | 蓝图路径 | Game.ini 屏蔽 |\n")
    L.append("|---|---|---|---|\n")
    for eng, d in sorted(groups[g], key=lambda x: x[0]):
        L.append(f"| {esc(eng)} | `{esc(d.get('spawn',''))}` | `{esc(d.get('blueprintPath',''))}` | `{esc(d.get('disable',''))}` |\n")
    L.append("\n")

out = "".join(L)
path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE, "ARK-Supreme-金属工具代码.md")
open(path, "w", encoding="utf-8").write(out)
print("WROTE", path, "bytes=", len(out.encode("utf-8")), "total=", len(items))
for g, v in groups.items():
    print(g, len(v))
