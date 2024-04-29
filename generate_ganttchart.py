import elegantt
import re

chartsize = (720,320)
bgcolor = (255,255,255)

gchart = elegantt.EleGantt( chartsize, bgcolor)
#gchart.set_font("ipaexg.ttf")

gchart.set_max_day(28)

gchart.draw_calendar()

with open("index.md") as file:
    for line in file:
        if line[0] == "|":
            line = line.split("|")
            print(line)
            if re.match(r'^\d{4}-\d{2}-\d{2}$',line[1]):
                gchart.draw_campain(line[1],line[2],line[3])

gchart.save("ganttchart.png")
