import re

def replace_pingone_domain(text):
# Replace pingone.com with pingtwo.com (first occurrence only)
    return re.sub(r'pingone\.com', 'pingtwo.com', text, count=1)
text = "http://pingone.com/login?redirect=http://pingone.com/dashboard"
print(replace_pingone_domain(text))
