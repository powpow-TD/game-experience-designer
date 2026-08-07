import re, sys
from pathlib import Path
RULES={"F01":"体验 情绪 感受 期待", "F03":"难度 卡关 挑战", "F04":"叙事 剧情 角色 任务", "F05":"选择 决策 策略", "F06":"平衡 胜率 数值", "F08":"奖励 动机 留存", "F09":"界面 提示 可读 反馈", "F11":"原型 试玩 迭代 假设", "F13":"依赖 架构 返工", "F16":"风险 不可逆"}
t=Path(sys.argv[1]).read_text(encoding="utf-8").lower() if len(sys.argv)>1 else sys.stdin.read().lower()
for s,c in sorted(((sum(t.count(w) for w in ws.split()),c) for c,ws in RULES.items()), reverse=True)[:5]: print(f"{c}\t{s}")
