
import json

post_json={}
blogpost = open("blogpost.txt","r")
count = 0

#While loop to fetch meta data
while count < 2:
    post = blogpost.readline()
    if(post.strip() == '---'):
        count += 1
        continue
    start = 0
    end = post.find(":")
    key = post[start:end].strip()
    key = key.strip("\"")
    value = post[end+1 :].strip()
    value = value.strip("\"")
    if("," in value):
        val = value.split(",")
        value= []
        for ele in val:
            value.append(ele.strip())
    post_json[key] = value
#End of meta data fetching

#Fetch Short Content from blog
post = blogpost.read()
start = post[3:].find('---') + 2
end = post[start:].find('READMORE')
post_json['short-content'] = post[start:end].strip()

#Fetch Main Content from blog
start = end + 8 
post_json['content'] = post[start:].strip()

#Dump to json
json_file = json.dumps(post_json)
print(json_file)
