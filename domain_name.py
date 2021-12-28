"""
domain name: has one or multiple prefixes AND suffixes
prefixes examples. :    http://
                        https://
                        http://www.
                        https://www.
                        http://<value>.
                        https://<value>.
                        www.
                        <value>.

suffixes:               .<domain_extension> (.com etc) has a lenght of 3 (4 with the dot)
                        .<domain_extension1>.<domain_extension2>
                        /<value>.<domain_extension>
                        /<value>/<value2>...+/<value>.<domain_extension>

domain name:
                        has no dots '.'
                        has no slashes '/'
                        words can only be connected by hyphen '-'
                        hyphen can not be start or end of domain name

idea: 
                        first get rid of http:// and https://
                        then get rif of all domain suffixes (www. or <value>.) by splitting on dot and take second element
"""
# first working solution
def domain_name(url):
    # get rid of http:// and https://
    no_https = url.split('//')
    if len(no_https) == 2:
        no_https = no_https[1]
    else:
        no_https = no_https[0]
    # remove domain prefix and its dot
    no_suffix = no_https.split('www.')
    if len(no_suffix) == 2:
        no_suffix = no_suffix[1]
    else:
        no_suffix = no_suffix[0]
    # now if string is split on dot , first element is domain name
    res = no_suffix.split('.')[0]        
    return res

# shorter solution (could just use -1 instead of if .. else ..)
def domain_name(url):
    no_https = url.split('//')
    # no_https = no_https[1] if len(no_https) == 2 else no_https[0]
    no_https = no_https[-1]
    no_suffix = no_https.split('www.')
    # no_suffix = no_suffix[1] if len(no_suffix) == 2 else no_suffix[0]
    no_suffix = no_suffix[-1]
    return no_suffix.split('.')[0]     


# codewars solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]



print(domain_name("http://github.com/carbonfive/raygun")) # == "github"
print(domain_name("http://www.zombie-bites.com")) # == "zombie-bites"
print(domain_name("https://www.cnet.com")) # == "cnet"
print(domain_name("https://youtube.com")) # == "youtube"
print(domain_name("http://google.co.jp")) # == "google"
print(domain_name("www.xakep.ru")) # == "xakep"



