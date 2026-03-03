import os
import subprocess
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# --- ⚡️ 2.4 安全提交版 ⚡️ ---
# 默认推送到当前分支，不再强制 push，不把 token 明文拼进 URL。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCLUDED_HINTS = {".git", ".venv", "__pycache__", "butler.py", "~", ".idea"}


def run_git(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, check=check)


def current_branch() -> str:
    result = run_git(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return result.stdout.strip()


class ButlerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if any(hint in event.src_path for hint in EXCLUDED_HINTS):
            return

        if event.is_directory:
            return

        filename = os.path.basename(event.src_path)
        print(f"\n[脉冲捕捉] 文件 '{filename}' 发生改动")

        try:
            run_git(["git", "add", "."])
            msg = f"联觉同步：'{filename}' 产生共鸣。"
            commit_result = run_git(["git", "commit", "-m", msg], check=False)

            if commit_result.returncode != 0:
                if "nothing to commit" in commit_result.stdout + commit_result.stderr:
                    print("ℹ️ 没有可提交变更，跳过 push。")
                    return
                raise RuntimeError(commit_result.stderr.strip() or commit_result.stdout.strip())

            branch = current_branch()
            run_git(["git", "push", "origin", branch])
            print(f"✅ 提交并推送成功：origin/{branch}（真实提交会计入小绿格）")

        except Exception as exc:
            print(f"❌ 提交流程失败：{exc}")


if __name__ == "__main__":
    print(f"👁️ 监控目录: {BASE_DIR}")
    print("🛡️ 运行模式: 安全提交（不强推、不明文 token）")

    observer = Observer()
    observer.schedule(ButlerHandler(), BASE_DIR, recursive=True)
    print("=" * 50 + "\n🕵️ 联觉管家 2.4（安全提交版）已上线\n" + "=" * 50)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
