import elegantt
import re
import datetime

chartsize = (720,320)
bgcolor = (255,255,255)

today = datetime.date.today()+datetime.timedelta(hours=15) 

gchart = elegantt.EleGantt( chartsize, bgcolor,today=today.strftime('%Y-%m-%d'))
gchart.set_font(
    regular = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    bold = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

print(gchart.get_today())

gchart.set_max_day(21)

gchart.draw_calendar()

with open("index.md") as file:
    for line in file:
        if line[0] == "|":
            line = line.split("|")
            if re.match(r'^\d{4}-\d{2}-\d{2}$',line[1]):
                print(line)
                gchart.draw_campain(line[1],line[2],line[3])

gchart.save("ganttchart.png")
