import shutil
import sys
from pathlib import Path


def sort_and_copy_files(src_dir: Path, dst_dir: Path):
    try:
        for item in src_dir.iterdir():
            if dst_dir in item.parents or item.resolve() == dst_dir.resolve():
                continue
            try:
                if item.is_dir():
                    sort_and_copy_files(item, dst_dir)
                elif item.is_file():
                    ext = item.suffix[1:] or "no_ext"
                    ext_dir = dst_dir / ext
                    ext_dir.mkdir(parents=True, exist_ok=True)

                    destination = ext_dir / item.name

                    if item.resolve() == destination.resolve():
                        continue

                    try:
                        shutil.copy2(item, destination)
                        print(f"✅ Скопійовано: {item} ➜ {destination}")
                    except PermissionError:
                        print(f"⛔ Немає дозволу на копіювання: {item}")
                    except Exception as e:
                        print(f"⛔ Помилка при копіюванні {item}: {e}")
            except Exception as e:
                print(f"⚠️ Помилка при обробці {item}: {e}")
    except Exception as e:
        print(f"❌ Критична помилка при відкритті {src_dir}: {e}")


def main():
    if len(sys.argv) < 2:
        print("❌ Помилка: не вказано шлях до вихідної директорії.")
        print("Приклад: task_1.py source_dir [dest_dir]")
        sys.exit(1)

    src_path = Path(sys.argv[1])
    dst_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not src_path.exists() or not src_path.is_dir():
        print("❌ Помилка: вихідна директорія не існує або не є текою.")
        sys.exit(1)

    dst_path.mkdir(parents=True, exist_ok=True)
    sort_and_copy_files(src_path, dst_path)
    print(f"\n📦 Усі файли скопійовано у «{dst_path.resolve()}»")


if __name__ == "__main__":
    main()
