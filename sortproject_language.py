import requests
import bs4 as bs
import json

year = input("Enter the year: \t")
limit = input("Enter the limit(type '-' if no limit): \t")
language = input("Enter the language: \t")

url = 'https://summerofcode.withgoogle.com/api/archive/programs/'+year+'/organizations/'
#https://summerofcode.withgoogle.com/programs/2022/organizations

res = requests.get(url)
res.raise_for_status()

wholedata = json.loads(res.text);

companies_list = []

if(limit=='-'):
    limit = 512
else:
    limit = int(limit)
a = 0 

for key in wholedata:
    if a==limit:
        break
    else:
        tech_stack_list = key['tech_tags']
        tech_stack_list_topics = key['topic_tags']
        company_name = key['name']

        for lang in tech_stack_list:
            if lang==language:
                companies_list.append(company_name)
                a += 1

        for tags in tech_stack_list:
            if tags==language:
                if company_name in companies_list:
                    continue
                companies_list.append(company_name)
                a += 1

print(companies_list)