import re

# Google API Key Scanner Project by Harshit Singh
sample_code_to_scan = """
GOOGLE_MAPS_API_KEY = "AIzaSyA123456789_ExampleLeakKeyDoNotUse"
"""

google_key_pattern = r"AIzaSy[A-Za-z0-9_-]{33}"

def scan_for_google_vulnerability(source_code):
    print("--- Scanning Code for Google Security Flaws ---")
    found_keys = re.findall(google_key_pattern, source_code)
    
    if found_keys:
        print(f"🚨 ALERT: Security Vulnerability Found!")
        print(f"⚠️ Critical Leak: Detected a Google API Key exposed in code!")
        print(f"Location Key: {found_keys}")
        return True
    else:
        print("✅ Safe: No leaks detected.")
        return False

scan_for_google_vulnerability(sample_code_to_scan)
