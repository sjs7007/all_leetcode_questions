
with open('question_links.txt') as f:
  links =  f.read()


links = links.split('\n')

question_links = []
for each in links:
  if '/problems/' in each:
    question_links.append(each)


import requests


from bs4 import BeautifulSoup


def get_question(question_link):
  
  resp = requests.get(question_link)
  soup = BeautifulSoup(resp.text, 'html.parser')

  a =  soup.find_all('meta')[0].find_all('meta')

  return  a[1]['content']

for each_question_link in question_links:
  try:
    print '-----'
    print get_question(each_question_link)
    print '-----'
  except:
    continue