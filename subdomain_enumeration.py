import sys
import requests

sub_lists = open("https-github.com-MicrosoftDocs-pipelines-java/wordlist2.txt").read()

sub_domain=sub_lists.splitlines

for sub in sub_domain:
    subdomains = f"http://{sub}.{sys.argv[1]}"


    try:
        requests.get(subdomains)
    except requests.ConnectionError:
        pass
    else:
        print("valid domain ",subdomains)


