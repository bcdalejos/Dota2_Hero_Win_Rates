import requests
import pandas as pd

url_heroStat = "https://api.opendota.com/api/heroStats"

rHeroStat = requests.get(url_heroStat)
dota2_heroStat_json = rHeroStat.json()

dota_hero_list = []
dota_overAll_winRate_list = []
dota_perRank_winRate_list = [[],[],[],[],[],[],[],[]]
dota2_heroStat_winRate_dict = {}
dota2_ranks = ['Herald','Guardian','Crusader','Archon','Legend','Ancient','Divine','Immortal']


for heroStat in dota2_heroStat_json:
    total_pick = 0
    total_win = 0
    #1-8, rank i.e, crusader,guardian,herald,etc.
    for i in range(1, 9):
        total_pick += heroStat["{}_pick".format(i)]
        total_win += heroStat["{}_win".format(i)]
        dota_perRank_winRate_list[i-1].append("%.2f" %(heroStat["{}_win".format(i)]*100/heroStat["{}_pick".format(i)])+" %")
    
    winRate = total_win*100/total_pick
    dota_hero_list.append(heroStat['localized_name'])
    dota_overAll_winRate_list.append("%.2f" %winRate+" %")

dota2_heroStat_winRate_dict['Heroes'] = dota_hero_list
dota2_heroStat_winRate_dict['Overall Win Rate'] = dota_overAll_winRate_list


for rank in dota2_ranks:
    dota2_heroStat_winRate_dict['{} Win Rate'.format(rank)] = dota_perRank_winRate_list[dota2_ranks.index(rank)]

dota2_heroStat_winRate_dp = pd.DataFrame(dota2_heroStat_winRate_dict).sort_values(by = 'Herald Win Rate', ascending=False)

print(dota2_heroStat_winRate_dp)
