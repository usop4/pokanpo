import elegantt
import datetime

today = (
    datetime.date.today()
    + datetime.timedelta(hours=15)
    ).strftime('%Y-%m-%d')

g = elegantt.EleGantt(today=today, firstday=today)
g.set_font(
    regular="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    bold="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
g.set_max_day(21)
g.day_num = 21
with open("index.md") as file:
    content = file.read()
    events = g.parse_markdown(content)
    g.resize(size=(
        g.calc_width(21),
        g.calc_height(len(events))
    ), today=today, firstday=today)
    g.draw_calendar()
    for event in events:
        print(event)
        g.draw_campain(
            event["start"].strftime('%Y-%m-%d'),
            event["end"].strftime('%Y-%m-%d'),
            event["title"]
        )
g.save("ganttchart.png")
