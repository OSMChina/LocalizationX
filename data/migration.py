import json

content_file=open("content.json","r",encoding="utf-8")
content_json=json.loads(content_file.read())
new_content={}
for catagory in content_json:
    new_catagory=[]
    for entry in content_json[catagory]:
        new_entry={}
        new_entry["meta"]={}
        new_entry["translation"]={}
        new_entry["id"]=entry["name"]
        new_entry["meta"]["website"]=entry["website_url"]
        new_entry["meta"]["repository"]=entry["code_repository"]
        new_entry["meta"]["osmwiki"]=entry["osmwiki_page"]
        new_entry["translation"]["platform"]=entry["translate_platform"]
        new_entry["translation"]["status"]=entry["translate_status"]
        new_entry["translation"]["link"]=entry["translate_link"]
        new_entry["translation"]["contributor"]=entry["contributor"]
        new_catagory.append(new_entry)
    new_content[catagory]=new_catagory
# from pprint import pprint
# pprint(new_content)
