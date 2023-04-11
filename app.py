# import libraries
import sys
import urllib.request

# Open file in write mode to redirect stderr

with open("error.log", 'w') as file:
    # save current stderr to variable
    stderr_saved = sys.stderr

    # redirect stderr to file
    sys.stderr = file

# write function that takes url & returns a response
def main(url):
    # use urllib.request to get the data from the url
    print("checking connectivity...")

    with open("error.log", 'w') as file:
        # save current stderr to variable
        stderr_saved = sys.stderr

        # redirect stderr to file
        sys.stderr = file
        try:
            res = urllib.request.urlopen(url)

            if res.getcode() == 200:
                print(f'''connected to {url} successfuly.
                the response code is {res.getcode()}''')
            else:
                print(f'''something went wrong
                the response code is {res.getcode()}''')
        except Exception as e:
            print("Couldn't establish connection.")
            print(f"[{e}]", file=sys.stderr)

        sys.stderr = stderr_saved

print("This is a site conectivity checker program")

input_url = input("Input the link to the site: ")

main(input_url)