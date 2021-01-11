# Very Basic Usage of ConfME
To get familiar with ConfMe, the first thing we will do is run through a very simple example with no real context.
For that we will go through the example from the official ConfME readme [README](https://github.com/iwanbolzern/ConfMe).

## Why are we here today?
1. Access to configuration values must be safe at runtime. **No ```myconfig['value1']['subvalue']``` anymore!**
2. The configuration must be checked for consistency at startup e.g. type check, range check, ...
3. Secrets shall be injectable from environment variables

## 1. Install ConfME
```
pip install confme
```
or simply
```
pip install -r requirements.txt
```

## 2. Create your first config
Therefore, have a look at the two files ```first_steps.py``` and ```config.yaml```. It should mostly be self explainable. When you now execute ```first_steps.py``` with
```
python first_steps.py
```
you should see that the configuration is successfully parsed.

## 3. Adding an Enum
After we have our first configuration, we will extend it by adding a ```connection_type```, which is an enum value and only allows the value "tcp" or "udp". (btw this is not a real example, I would not know any database that uses an udp connection 😉). To do so, please uncomment the following lines in ```first_steps.py```:
```
# class DatabaseConnection(Enum):
#     TCP = 'tcp'
#     UDP = 'udp'
...

    # connection_type: DatabaseConnection
...

    # f'with connection type: {my_config.database.connection_type} '
```
Now try again to execute ```python first_steps.py```.  
...  
As I said, I would like to get notified right at the beginning that my configuration is missing a value... Lets uncomment the value in the ```config.yaml``` as well.

## 4. Adding a Secret
Even though, we now have a valid database configuration, we can not connect because we are missing a password. Therefore, uncomment the following lines in ```first_steps.py```:
```
   # password: str = Secret('HIGH_SECURE_PASSWORD')
```
What it happens in the back is that the environment variable ```HIGH_SECURE_PASSWORD``` gets mapped to this config value. Let's try it out: ```python first_steps.py``` As you see, also here it recognises that this value is missing. Seems as we should set it and try again:  
For windows:
```
set HIGH_SECURE_PASSWORD="uhhhVerySecret" && python first_steps.py
```
For linux:
```
export HIGH_SECURE_PASSWORD="uhhhVerySecret" && python first_steps.py
```
## 5. Using Command Line overwrites
Type in the command bellow and see what you get:
```
python first_steps.py -h
```
Yes, it is what you think 😊 We can change parameters by passing them as command line arguments. Let's try it out:
```
python first_steps.py --database.host "Awesome ConfME Host"
```
