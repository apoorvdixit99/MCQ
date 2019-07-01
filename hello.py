import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcq.settings")
import django
django.setup()
from questions.models import Question
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def import_que( secc,i ):
	my_url = 'https://www.examveda.com/general-knowledge/practice-mcq-question-on-basic-general-knowledge/?section='+str(secc)+'&page='+str(i)
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, 'html.parser')

	containers = page_soup.findAll("article",{"class":"question single-question question-type-normal"})


	for i in range(len(containers)-1):
		name = containers[i].h2.select(".question-main")
		que = name[0].text
		options = containers[i].findAll("p")
		obj_a = options[0].select("label")
		opt_a = obj_a[1].text
		obj_b = options[1].select("label")
		opt_b = obj_b[1].text
		obj_c = options[2].select("label")
		opt_c = obj_c[1].text
		obj_d = options[3].select("label")
		opt_d = obj_d[1].text
		obj_ans = containers[i].strong.text
		ans = obj_ans[8]
		Question.objects.create(problem=que, option_a=opt_a, option_b=opt_b, option_c=opt_c, option_d=opt_d,
								correct_option=ans)

for sec in range(1,12):
	for id in range(1,15):
		import_que(sec,id)





