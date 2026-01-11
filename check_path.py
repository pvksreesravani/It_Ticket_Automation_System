import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
target = os.path.join(BASE_DIR, 'templates', 'base.html')

print(f"Project Root: {BASE_DIR}")
print(f"Looking for base.html at: {target}")
print(f"Does the file exist? {'✅ YES' if os.path.exists(target) else '❌ NO'}")

# List all files in the templates folder if it exists
if os.path.exists(os.path.join(BASE_DIR, 'templates')):
    print(f"Files found in templates folder: {os.listdir(os.path.join(BASE_DIR, 'templates'))}")
else:
    print("❌ The 'templates' folder was NOT found in the root directory.")