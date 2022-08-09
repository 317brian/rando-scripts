import json
import os


input_file=open('pr1061.json', 'r')
output_file=open('comments.json', 'w')

json_decode=json.load(input_file)

result=[]

for item in json_decode:
  my_dict={}
  #my_dict['line']=item.get('diff_hunk')
  my_dict['owner']=item.get('user').get('login')
  my_dict['comment']=item.get('body')
  result.append(my_dict)

#Unformatted JSON output that gets run through jq
#output_file.write(json.dumps(result))
#print(json.dumps(result))
# For some reason jq does not like my_dict[line] being commented out
#os.system("jq . comments.json > pretty.json")


# Formatted JSON output
output_file.write(json.dumps((result), indent=2, sort_keys=True))
print (json.dumps((result), indent=2, sort_keys=True))




# Stuff to do later

# Add pulling the comments into this script
#import http.client

# The PAT from GitHub needs full repo rights

# Python code from Postman so that I can do it all in one file later
# Update the get request to be an fstring for owner, repo, and pr
#conn = http.client.HTTPSConnection("api.github.com")
#payload = ''
#headers = {
#  'Accept': 'application/vnd.github.v3+json',
#  'Authorization': 'Bearer BEARER_TOKEN_SET_ENV_VAR_FOR_THIS'
#}
#conn.request("GET", "/repos/owner/implydata/pulls/1058/comments", payload, headers)
#res = conn.getresponse()
#data = res.read()
#print(data.decode("utf-8"))