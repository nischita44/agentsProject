# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.            
# the format for that file is (without the comment)                                                                                                                                       
def load_env():
    os.environ['your_key'] = '-'
    # Verify it was set
    if 'your_key' in os.environ:
        print("✅ your_key loaded successfully")
    else:
        print("❌ Failed to setyour_key!")

def get():
    return os.getenv("your_key")