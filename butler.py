import time, os, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- ⚡️ 最终起航配置 ⚡️ ---
TOKEN = os.getenv("MY_GITHUB_TOKEN")  # 你的黄金钥匙
USER = "BTXeplore"
REPO = "btx-2026-revival"

# 【防斜杠补丁】：我们手动构建一个绝对干净的推送命令
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
                # 2. 联觉记录
                msg = f"联觉同步：'{filename}' 产生共鸣。向着光的源头起航。"
                subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)

                # 3. 【核心爆破】：我们直接在命令里禁用 credential.helper
                print(f"正在穿刺 'Not Found' 迷雾...")
                cmd = ["git", "-c", "credential.helper=", "push", MAGIC_URL, "main", "--force"]
                subprocess.run(cmd, check=True)
                print(f"✅ 成功！！琥珀色的绿格子已在云端亮起！")
            except Exception as e:
                print(f"❌ 干扰预警：{e}")


if __name__ == "__main__":
    event_handler = ButlerHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    print("=" * 50 + "\n🕵️ 联觉管家 2.1 (纯净起航版) 已上线\n" + "=" * 50)
    observer.start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()