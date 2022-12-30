#!/usr/bin/env python3
import os
import sys
import yadisk


def main():
    y = yadisk.YaDisk(os.environ["YA_APP_CLIENT_ID"], os.environ["YA_APP_CLIENT_SECRET"])
    url = y.get_code_url()
    
    print(f"Go to the following url: {url}")
    code = input("Enter the confirmation code: ")
    
    try:
        response = y.get_token(code)
    except yadisk.exceptions.BadRequestError:
        print("Bad code")
        sys.exit(1)
    
    y.token = response.access_token
    if y.check_token():
        print("Sucessfully received token!")
    else:
        print("Something went wrong. Not sure how though...")
        sys.exit(1)
    
    # Get general disk info
    print(y.get_disk_info())
    
    # Get directory contents
    print(list(y.listdir("/")))


if __name__ == '__main__':
    main()
