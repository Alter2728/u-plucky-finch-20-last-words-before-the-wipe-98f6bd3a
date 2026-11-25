import os

TEXT = "Tell the new me I said hi. They'll know what it means. They won't, but say it anyway."


def main():
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 200, len(written)
    assert "\n" not in written and "\r" not in written


if __name__ == "__main__":
    main()
