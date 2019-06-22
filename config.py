
sensors = [
    {
      "id": "01131657bc73",
      "name": "front_window_outside"
    },
    {
      "id": "011830cd8dff",
      "name": "front_window_inside"
    },
    {
      "id": "0113170ac3ed",
      "name": "front_radiator"
    },
    {
      "id": "021830b173ff",
      "name": "back_window_inside"
    },
    {
      "id": "011316f4161f",
      "name": "back_radiator"
    },
    {
      "id": "011316e9c41b",
      "name": "back_window_outside"
    }
  ]

influx_ip = "192.168.66.56"
influx_database = "smarthome"
influx_port = "8086"
influx_retention_policy = "2w"

'''
possible retention intervals:

ns	nanoseconds (1 billionth of a second)
u or µ	microseconds (1 millionth of a second)
ms	milliseconds (1 thousandth of a second)
s	second
m	minute
h	hour
d	day
w	week
'''
