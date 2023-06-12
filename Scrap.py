import requests
from bs4 import BeautifulSoup 
import csv

Date = input("Please Enter a Date DD/MM/YYYY: ").strip()
page = requests.get(f"https://www.yallakora.com/match-center/مركز-المباريات?date={Date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src,"lxml")
    Matches_Details = []
    Championships = soup.find_all("div",{'class':'matchCard'})
    
    def get_match_info(Championships):
        Championship_title = Championships.contents[1].find("h2").text.strip()
        all_matches = Championships.contents[3].find_all("li")
        numbers_of_match = len(all_matches)

        for i in range(numbers_of_match):
            team_a = all_matches[i].find("div",{"class" :"teamA"}).text.strip()
            team_b = all_matches[i].find("div",{"class" :"teamB"}).text.strip()

            get_score = all_matches[i].find("div",{"class" : "MResult"}).find_all("span",{"class" :"score"})
            score = f"{get_score[0].text.strip()} - {get_score[1].text.strip()}"

            get_match_Time = all_matches[i].find("div",{"class" :"MResult"}).find("span",{"class" :"time"}).text.strip()
            Matches_Details.append({"اسم البطولة" : Championship_title, "الفريق الأول" : team_a, "الفريق الثاني" : team_b,
                                     "ميعاد المباراة" : get_match_Time, "النتيجة" : score})
    
    for i in range(len(Championships)):
        get_match_info(Championships[i])

    keys = Matches_Details[0].keys()
    with open (r'D:\Python\Applications\0.Web Scrapping using Soup\Files\1.csv','w') as f:
        dict_writer = csv.DictWriter(f,keys)
        dict_writer.writeheader()
        dict_writer.writerows(Matches_Details) #write the Details
main(page)