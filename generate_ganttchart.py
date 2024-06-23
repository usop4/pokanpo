import elegantt
import datetime

today = (
    datetime.date.today()
    + datetime.timedelta(hours=15)
    ).strftime('%Y-%m-%d')

gchart = elegantt.EleGantt(today=today, firstday=today)
gchart.set_font(
    regular="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    bold="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
gchart.set_max_day(21)
with open("index.md") as file:
    content = file.read()
    events = gchart.parse_markdown(content)
    gchart.resize(size=(
        692,
        60 + len(events)*45 + 10
    ))
    gchart.set_max_day(45)
    gchart.draw_calendar()
    for event in events:
        print(event)
        gchart.draw_campain(
            event["start"].strftime('%Y-%m-%d'),
            event["end"].strftime('%Y-%m-%d'),
            event["title"]
        )
gchart.save("ganttchart.png")
