import time, os, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- ⚡️ 2.3 路径绝对对齐版 ⚡️ ---
TOKEN = os.getenv("MY_GITHUB_TOKEN")
USER = "BTXeplore"
REPO = "btx-2026-revival"

# 获取脚本所在的【绝对路径】，确保传感器点位 100% 正确
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not TOKEN:
    TOKEN = "MISSING_TOKEN"

MAGIC_URL = f"https://{USER}:{TOKEN}@github.com/{USER}/{REPO}.git"


class ButlerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # ⚡️ 调试脉冲：只要有任何动静，先在终端打印，证明传感器活着
        # print(f"信号探测中: {event.src_path}")

        if any(x in event.src_path for x in [".git", ".venv", "__pycache__", "butler.py", "~", ".idea"]):
            return

        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f"\n[脉冲捕捉] 波段 '{filename}' 强烈震动中...")

            try:
                subprocess.run(["git", "add", "."], check=True, cwd=BASE_DIR)
                msg = f"联觉同步：'{filename}' 产生共鸣。"
                subprocess.run(["git", "commit", "-m", msg],
                               capture_output=True, text=True, encoding='utf-8', errors='ignore', cwd=BASE_DIR)

                print(f"正在强力穿刺云端...")
                cmd = [
                    "git", "-c", "http.proxy=", "-c", "https.proxy=", "-c", "credential.helper=",
                    "push", MAGIC_URL, "main", "--force"
                ]
                subprocess.run(cmd, check=True, cwd=BASE_DIR)
                print(f"✅ 成功！！琥珀色的绿格子已在云端亮起！")
            except Exception as e:
                print(f"❌ 干扰预警：{e}")


if __name__ == "__main__":
    status = "已就绪" if TOKEN != "MISSING_TOKEN" else "未加载"
    print(f"🔑 钥匙状态: {status}")
    print(f"👁️ 传感器监控目录: {BASE_DIR}")  # ⚡️ 关键：确认这里是不是你存放 youhua.py 的地方！

    event_handler = ButlerHandler()
    observer = Observer()
    # 增加 recursive=True，防止文件嵌套导致的扫描不到
    observer.schedule(event_handler, BASE_DIR, recursive=True)
    print("=" * 50 + "\n🕵️ 联觉管家 2.3 (路径对齐版) 已上线\n" + "=" * 50)
    observer.start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()