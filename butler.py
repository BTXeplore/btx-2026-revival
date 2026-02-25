import time, os, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- ⚡️ 2.2 防护起航版 ⚡️ ---
TOKEN = os.getenv("MY_GITHUB_TOKEN")
USER = "BTXeplore"
REPO = "btx-2026-revival"

if not TOKEN:
    print("❌ [严重预警] 未检测到黄金钥匙 (MY_GITHUB_TOKEN)！请在系统环境变量中检查。")
    # 为了防止 None 导致报错，我们先占个位，但还是会失败，提醒你检查
    TOKEN = "MISSING_TOKEN"

MAGIC_URL = f"https://{USER}:{TOKEN}@github.com/{USER}/{REPO}.git"


class ButlerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if any(x in event.src_path for x in [".git", ".venv", "__pycache__", "butler.py", "~"]):
            return
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f"\n[脉冲捕捉] 波段 '{filename}' 震动中...")

            try:
                # 1. 强制加入
                subprocess.run(["git", "add", "."], check=True)
                # 2. 联觉记录 (增加 encoding 参数修复 GBK 报错)
                msg = f"联觉同步：'{filename}' 产生共鸣。"
                subprocess.run(["git", "commit", "-m", msg],
                               capture_output=True, text=True, encoding='utf-8', errors='ignore')

                # 3. 【核心爆破】：强制禁用代理，直接穿刺
                print(f"正在强力穿刺云端，跳过所有本地代理...")
                cmd = [
                    "git",
                    "-c", "http.proxy=",  # ⚡️ 强制取消 http 代理
                    "-c", "https.proxy=",  # ⚡️ 强制取消 https 代理
                    "-c", "credential.helper=",
                    "push", MAGIC_URL, "main", "--force"
                ]
                subprocess.run(cmd, check=True)
                print(f"✅ 成功！！琥珀色的绿格子已在云端亮起！")
            except Exception as e:
                print(f"❌ 干扰预警：{e}")


if __name__ == "__main__":
    # 打印一下，确认钥匙是否读到 (只显示前4位保护安全)
    status = "已就绪" if TOKEN != "MISSING_TOKEN" else "未加载"
    print(f"🔑 钥匙状态: {status} | 目标: {REPO}")

    event_handler = ButlerHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    print("=" * 50 + "\n🕵️ 联觉管家 2.2 (强制穿刺版) 已上线\n" + "=" * 50)
    observer.start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()