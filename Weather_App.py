import tkinter as tk
import requests

HEIGHT = 600
WIDTH = 700

def format_response(weather):
    print(weather)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature: (F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving the information, likely due to invalid input.'

    return final_str

def get_weather(city):
    weather_key = '317dacab64927d87024c50bc24988a3f'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)  # size of the screen
canvas.pack()

background_image = tk.PhotoImage(file='weather.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)  # inner screen
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Berlin Sans FB', 25))  # for user to type stuff in
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get Weather', font=('Berlin Sans FB', 20),
                   command=lambda: get_weather(entry.get()))  # command -> trigger the function
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Berlin Sans FB', 25), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

# root.mainloop()