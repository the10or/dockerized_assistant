import shutil
import sys
from pathlib import Path
from normalize import normalize
from scan import scan, categories


def main(path):
    scan(path)
    for category, files in categories.items():
        category_dir = path / category
        category_dir.mkdir(exist_ok=True)

        for file in files:
            new_path = normalize(file.name)
            file.replace(path / category / new_path)

    scan(path)

    arch_path = Path(path / 'archives')
    for arch in arch_path.iterdir():
        shutil.unpack_archive(arch, arch_path / arch.stem)
        arch.unlink()

        scan(arch_path)


if __name__ == '__main__':
    main(Path(sys.argv[1]))
