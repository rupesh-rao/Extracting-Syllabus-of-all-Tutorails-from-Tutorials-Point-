from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

def page_soup(url):
    req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    furl = urlopen(req)
    html = furl.read()
    furl.close()
    soup = BeautifulSoup(html,'html.parser')
    return soup
    
url =  "https://www.tutorialspoint.com/tutorialslibrary.htm"
soup = page_soup(url)

containers = soup.findAll('div',{'class': 'featured-box'})

for container in containers[1:2]:
    headings = container.findAll('h4')
    ul = container.findAll('ul')
    no_of_headings = len(headings)
    
    for i in range(7,9):
        print(i)
        
        topics = ul[i].findAll('li')
        print(len(topics))
        
        for topic in topics:
            topic_name = topic.text
            f = open(topic_name.replace('/',' ')+'_'+headings[i].text.split()[0]+'.txt','w',encoding = 'utf-8')
            url = 'https://www.tutorialspoint.com/' + topic.a['href']
            soup = page_soup(url)
            con = soup.findAll('aside',{'class':'sidebar'})
            if (len(con)==0):
                continue
            uls = con[0].findAll('ul')
            for u in uls:
                lis = u.findAll('li')
                if (lis[0].text == 'Selected Reading'):
                    continue
                for li in lis[1:]:
                    f.write(li.text+'\n')
            f.close()
                    
                    
            

