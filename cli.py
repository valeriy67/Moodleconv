#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
from convert import Convert_1c, Convert_Text   # готові функції з вашого коду

def auto_out_path(input_path: str) -> str:
    """Формує шлях до вихідного CSV поряд із вхідним файлом."""
    base_dir, fname = os.path.split(input_path)
    name, _ext = os.path.splitext(fname)
    return os.path.join(base_dir, f"mdl_{name}.csv")

def main():
    parser = argparse.ArgumentParser(
        description="Конвертер файлів у формат імпорту Moodle"
    )
    parser.add_argument("-i", "--input", required=True, help="шлях до вхідного файлу")
    parser.add_argument("-m", "--mode", choices=["1c", "text"], default="1c",
                        help="тип вхідного файлу: '1c' або 'text'")
    parser.add_argument("-o", "--output", help="шлях до вихідного CSV")
    parser.add_argument("--rename-photos", action="store_true",
                        help="для режиму 1c: перейменувати фото")
    parser.add_argument("--max-width", type=int, default=800, help="макс. ширина фото")
    parser.add_argument("--max-height", type=int, default=600, help="макс. висота фото")

    args = parser.parse_args()
    in_path = args.input
    out_path = args.output or auto_out_path(in_path)

    if not os.path.exists(in_path):
        print(f"Помилка: файл '{in_path}' не знайдено", file=sys.stderr)
        sys.exit(2)

    try:
        if args.mode == "1c":
            Convert_1c(
                in_path,
                out_path,
                flag=args.rename_photos,
                max_img_size=(args.max_width, args.max_height)
            )
        else:
            Convert_Text(in_path, out_path)
        print(f"Готово. CSV збережено у: {out_path}")
    except Exception as e:
        print(f"Помилка конвертації: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
