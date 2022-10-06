import click
import requests

# Click is the library that I used to create the easy command line interface. 

@click.group()
def logruncli():
    pass

type_of_run = {
    "re":"Recovery",
    "lsd":"Long slow distance",
    "s":"Sprints",
    "r":"Race"
}
# set a command called 'add'. will then be prompted if you do not enter anything.
@click.command() 
# @click.argument("file", type=click.Path(exist=False), required=1)
@click.option("--miles","-m", prompt="How many miles did you run?", help="Miles for the run")
@click.option("--time","-t", prompt="How long did the run take?", help="Duration of run")
@click.option("--run","-r", prompt="What type of run was this?", help="The RPE for this run",default="lsd")

def add(miles,time,run):
    filename = "mini-capstone/minicap/log.txt"
    with open(filename, "a+") as f:
        f.write(f"{miles}: {time} [RPE: {type_of_run[run.lower()]}]\n")


@click.command()
def view():
    filename = "mini-capstone/minicap/log.txt"  
    with open(filename, "r") as f:
        task_list = f.read().splitlines() 
    for i, task in enumerate(task_list):
        print (i, task)


@click.command()
@click.argument("index", type=int, required=1)

def remove(index):
    filename = "mini-capstone/minicap/log.txt"
    with open(filename, "r") as f:
        run_list = f.read().splitlines()
        run_list.pop(index)
    with open(filename, "w") as f:
        f.write("\n".join(run_list))
        f.write("\n")

@click.command()
@click.argument("weather")

def weather(weather):
    
    api = '4e865cbc120af5106cdb531655675627'
    city = input("Enter city: ")
    weather_request = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api}"
    )
    if weather_request.json()['cod'] == '404':
        print("Not a valid city name")

    else:
        weather_data =  weather_request.json()['weather'][0]['description']
        temp_data = round(weather_request.json()['main']['temp'])
        # if temp_data > 85:
        #     click.secho(f'Heat Advisory, {temp_data} degrees outside')
        #     click.secho(f'With {weather_data}',fg='white')
        # elif temp_data < 85:

        click.secho('WEATHER REPORT', blink=True, bold=True,fg='blue', bg='white')
        click.secho(f'The weather in: {city}',fg='white')
        click.secho(f'It is {temp_data} degrees outside', fg='white')
        click.secho(f'With {weather_data}',fg='white')

        # print(f'''
        # Currently in {weather} it is {temp_data} and {weather_data}
        # ''')

logruncli.add_command(add)
logruncli.add_command(view)
logruncli.add_command(remove)
logruncli.add_command(weather)


if __name__ == '__main__':
    logruncli()