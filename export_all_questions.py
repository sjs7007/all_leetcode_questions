import requests
from bs4 import BeautifulSoup


def update_question_links(question_links):
  with open('question_links.txt') as f:
    links =  f.read()


  links = links.split('\n')

  for each in links:
    if '/problems/' in each:
      question_links.append(each)


def get_question(question_link):
  
  resp = requests.get(question_link)
  soup = BeautifulSoup(resp.text, 'html.parser')

  return soup.find_all('meta')[0].find_all('meta')[1]['content']



def main():
  question_links = []
  update_question_links(question_links)
  for each_question_link in question_links:
    try:
      print '-----'
      print get_question(each_question_link)
      print '-----'
    except:
      continue


if __name__=='__main__':
  main()
  