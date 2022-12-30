#!/usr/bin/env python3
from collections import deque
import os
import sys
import yadisk


def get_all_dirs(y, start_path):
    q = deque([(start_path, start_path)])
    result = deque([])
    while q:
        name, path = q.pop()
        result.append((name, path))
        resources = y.listdir(path)
        for res in resources:
            if y.is_dir(res.path):
                q.append((res.name, res.path))
                continue
    return result


def get_ya_client():
    y = yadisk.YaDisk(
        os.environ["YA_APP_CLIENT_ID"], 
        os.environ["YA_APP_CLIENT_SECRET"],
        os.environ.get("YA_APP_TOKEN"))
    if not y.check_token():
        url = y.get_code_url()
            
        print(f"Go to the following url: {url}")
        code = input("Enter the confirmation code: ")
        
        try:
            response = y.get_token(code)
            print(f"Token: {response.access_token}")
        except yadisk.exceptions.BadRequestError:
            print("Bad code")
            sys.exit(1)
        
        y.token = response.access_token
        if y.check_token():
            print("Sucessfully received token!")
        else:
            print("Something went wrong. Not sure how though...")
            sys.exit(1)
    return y

    
def main():
    y = get_ya_client()
    dirs = get_all_dirs(y, "/")
    for name, path in dirs:
        print(f"{name}: {path}")

    # Create target dir structure
    # Download remote files to target dirs


if __name__ == '__main__':
    main()
