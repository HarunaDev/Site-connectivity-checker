# import urllib
import urllib.request as urllib

# write function that takes url & returns a response
def main(url):
    # use urllib.request to get the data from the url
    print("checking connectivity...")

    res = urllib.urlopen(url)
    
    
    if res.getcode() == 200:
        print(f'''connected to {url} successfuly.
        the response code is {res.getcode()}''')
    else:
        print(f'''something went wrong
        the response code is {res.getcode()}''')

print("This is a site conectivity checker program")

input_url = input("Input the link to the site: ")

main(input_url)