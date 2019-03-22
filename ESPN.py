from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


url = input("Please enter the game log url from espn")
# url = "http://www.espn.com/mens-college-basketball/player/gamelog/_/id/4395628/zion-williamson"

urlReading = urlopen(url)

playerhtml = urlReading.read()

urlReading.close()

pageSoup = soup(playerhtml, "html.parser")
filename = input("please name the csv for this player")

# filename = "test"

playerCSV = open(filename, "w")

playerCSV.write("Date" + "," + "home/away" + "," + "Opponent" + "," + "minutesPlayed" + "," + "fieldGoals" + "," + "rebounds" + "," + "assists"+"," +
                "blocks" + "," + "steals" + ',' + "fouls" + "," + "turnovers" + ","+"points\n")


tables = pageSoup.findAll(
    "table", {"class": "Table2__table-scroller Table2__right-aligned Table2__table"})

table = tables[0]

try:

    stats = table.findAll("tr", {"class": "bwb-0 Table2__tr Table2__tr--sm Table2__even"})
    stats2 = table.findAll("tr", {"class": "filled bwb-0 Table2__tr Table2__tr--sm Table2__even"})
    stats3 = table.findAll("tr", {"class": "filled Table2__tr Table2__tr--sm Table2__even"})
    stats4 = table.findAll("tr", {"class": "Table2__tr Table2__tr--sm Table2__even"})

    for i in range(len(stats)):
        game = stats[i]

        info = game.findAll("td", {"class": "Table2__td"})

        date = info[0].text
        location = info[1].findAll("span", {"class": "pr2"})[0].text
        opponent = info[1].findAll("a", {"class": "v-mid"})[1].text
        minutesPlayed = info[3].text
        fieldGoals = info[4].text
        rebounds = info[9].text
        assists = info[10].text
        blocks = info[11].text
        steals = info[12].text
        fouls = info[13].text
        turnovers = info[14].text
        points = info[15].text
        playerCSV.write(date + ",")
        playerCSV.write(location + ",")
        playerCSV.write(opponent + ',')
        playerCSV.write(minutesPlayed + ",")
        playerCSV.write(fieldGoals + ",")
        playerCSV.write(rebounds + ",")
        playerCSV.write(assists + ",")
        playerCSV.write(blocks + ",")
        playerCSV.write(steals + ",")
        playerCSV.write(fouls + ",")
        playerCSV.write(turnovers + ",")
        playerCSV.write(points + "\n")

    for i in range(len(stats2)):
        game = stats2[i]

        info = game.findAll("td", {"class": "Table2__td"})

        date = info[0].text
        location = info[1].findAll("span", {"class": "pr2"})[0].text
        opponent = info[1].findAll("a", {"class": "v-mid"})[1].text
        minutesPlayed = info[3].text
        fieldGoals = info[4].text
        rebounds = info[9].text
        assists = info[10].text
        blocks = info[11].text
        steals = info[12].text
        fouls = info[13].text
        turnovers = info[14].text
        points = info[15].text
        playerCSV.write(date + ",")
        playerCSV.write(location + ",")
        playerCSV.write(opponent + ',')
        playerCSV.write(minutesPlayed + ",")
        playerCSV.write(fieldGoals + ",")
        playerCSV.write(rebounds + ",")
        playerCSV.write(assists + ",")
        playerCSV.write(blocks + ",")
        playerCSV.write(steals + ",")
        playerCSV.write(fouls + ",")
        playerCSV.write(turnovers + ",")
        playerCSV.write(points + "\n")

    for i in range(len(stats3)):
        game = stats3[i]

        info = game.findAll("td", {"class": "Table2__td"})

        date = info[0].text
        location = info[1].findAll("span", {"class": "pr2"})[0].text
        opponent = info[1].findAll("a", {"class": "v-mid"})[1].text
        minutesPlayed = info[3].text
        fieldGoals = info[4].text
        rebounds = info[9].text
        assists = info[10].text
        blocks = info[11].text
        steals = info[12].text
        fouls = info[13].text
        turnovers = info[14].text
        points = info[15].text
        playerCSV.write(date + ",")
        playerCSV.write(location + ",")
        playerCSV.write(opponent + ',')
        playerCSV.write(minutesPlayed + ",")
        playerCSV.write(fieldGoals + ",")
        playerCSV.write(rebounds + ",")
        playerCSV.write(assists + ",")
        playerCSV.write(blocks + ",")
        playerCSV.write(steals + ",")
        playerCSV.write(fouls + ",")
        playerCSV.write(turnovers + ",")
        playerCSV.write(points + "\n")

    for i in range(len(stats4)):
        game = stats3[i]

        info = game.findAll("td", {"class": "Table2__td"})

        date = info[0].text
        location = info[1].findAll("span", {"class": "pr2"})[0].text
        opponent = info[1].findAll("a", {"class": "v-mid"})[1].text
        minutesPlayed = info[3].text
        fieldGoals = info[4].text
        rebounds = info[9].text
        assists = info[10].text
        blocks = info[11].text
        steals = info[12].text
        fouls = info[13].text
        turnovers = info[14].text
        points = info[15].text
        playerCSV.write(date + ",")
        playerCSV.write(location + ",")
        playerCSV.write(opponent + ',')
        playerCSV.write(minutesPlayed + ",")
        playerCSV.write(fieldGoals + ",")
        playerCSV.write(rebounds + ",")
        playerCSV.write(assists + ",")
        playerCSV.write(blocks + ",")
        playerCSV.write(steals + ",")
        playerCSV.write(fouls + ",")
        playerCSV.write(turnovers + ",")
        playerCSV.write(points + "\n")
finally:
    print("Your file has been created")


playerCSV.close()
