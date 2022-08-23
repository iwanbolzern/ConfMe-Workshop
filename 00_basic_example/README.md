# Very Basic Usage of ConfME
To get familiar with ConfMe, the first thing we will do is run through a very simple example with no real context.
For that, we will go through the example from the official ConfME readme [README](https://github.com/iwanbolzern/ConfMe).

## Why are we here today?
1. Access to configuration values must be safe at runtime. **No ```myconfig['value1']['subvalue']``` anymore!**
2. The configuration must be checked for consistency at startup e.g. type check, range check, ...
3. Secrets shall be injectable from environment variables

## 1. Install ConfME
For chapter 1 - 5 of this README please use the source code located in ```src/```.
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
python first_steps.py ++database.host "Awesome ConfME Host"
```
## 6. Advanced usage (register_folder(..))
An always requested feature was to switch from development configuration to a production configuration. This concept is 
supported by ConfME as follows (please see the ```src_advanced``` directory):
1. As before, we have now an ```AdvancedConfig``` class, which inherit from ```BaseConfig```.
2. Now instead of loading the config file directly, we register a directory containing one or multiple config files:
```
AdvancedConfig.register_folder(config_folder)
```
3. When you now call ```AdvancedConfig.get()``` you get an instance based on the environment you are in. This is done 
by parsing the following environment variables and taking the configuration with the same name: ENV, ENVIRONMENT, 
ENVIRON, env, environment, environ
4. Let's try it out. If we run ```export/set "ENV=dev" && python advanced_usage.py``` we expect to get the development 
configuration file. Ohh cool... And if we run ```export/set "ENV=prod" && python advanced_usage.py``` it changes to the 
prod config.
