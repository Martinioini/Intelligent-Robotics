#!/usr/bin/env python3
"""Build the single study PDF; keep compiler cache and temporary files on this disk."""
from pathlib import Path
import argparse
import os
import platform
import shutil
import subprocess
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.17.0"
URL = f"https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%40{VERSION}/tectonic-{VERSION}-x86_64-unknown-linux-musl.tar.gz"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install-compiler", action="store_true", help="download pinned official Tectonic into .tools (Linux x86_64)")
    args = parser.parse_args()
    local = ROOT / ".tools" / "tectonic"
    if args.install_compiler and not local.exists():
        if platform.system() != "Linux" or platform.machine() != "x86_64":
            parser.error("Automatic installation supports Linux x86_64 only; install Tectonic separately.")
        local.parent.mkdir(exist_ok=True)
        archive = local.parent / "tectonic.tar.gz"
        urllib.request.urlretrieve(URL, archive)
        with tarfile.open(archive) as bundle:
            member = next(m for m in bundle.getmembers() if Path(m.name).name == "tectonic" and m.isfile())
            with bundle.extractfile(member) as source, local.open("wb") as target:
                shutil.copyfileobj(source, target)
        local.chmod(0o755)
        archive.unlink()
    compiler = str(local) if local.exists() else shutil.which("tectonic")
    if not compiler:
        parser.error("Tectonic not found. Run: python3 scripts/build.py --install-compiler")
    cache, temporary = ROOT / ".cache", ROOT / ".tmp"
    out = ROOT / "output" / "pdf"
    for directory in (cache, temporary, out):
        directory.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.update(XDG_CACHE_HOME=str(cache), TECTONIC_CACHE_DIR=str(cache / "tectonic"), TMPDIR=str(temporary))
    subprocess.run([compiler, "--keep-logs", "--outdir", str(out), "main.tex"], cwd=ROOT / "latex", env=env, check=True)
    (out / "main.pdf").replace(out / "intelligent-robotics-notes.pdf")
    print(f"PDF: {out / 'intelligent-robotics-notes.pdf'}")

if __name__ == "__main__":
    main()
