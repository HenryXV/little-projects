import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-09-2020.csv')
cases_list = list()
cases = dict()
for line in fhand:
    active = line.decode().split(",")
    cases_list.append(active[7])

cases_list.pop(0)

for case in cases_list:
    cases[case] = cases.get(case, 0) + 1

total = 0
for k, v in cases.items():
    if k != '':
        try:
            total = total + (int(k) * v)
        except:
            k = 0
print(total)
