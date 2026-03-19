# Create a function 'build_query_string' that takes **params
# Returns a URL query string: key1=value1&key2=value2
# Sort keys alphabetically
# Values should be URL-encoded (spaces become %20)

# Example:
# build_query_string(name="Alice Smith", age=25, city="New York")
# Returns: "age=25&city=New%20York&name=Alice%20Smith"

# Hint: Use urllib.parse.quote() for encoding

# Your code here:

from urllib.parse import quote_plus


def build_query_string(**params):
    query_string = ""
    for key, value in params.items():
        query_string += f"{key}={value}&"

    return quote_plus(query_string)


print(build_query_string(name="Alice Smith", age=25, city="New York"))
