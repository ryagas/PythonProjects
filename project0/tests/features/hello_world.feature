Feature: The Cheerful Greeting CLI interface provides a greeting
    to a specific name.

Scenario: When requested, the application writes the greeting message.
  When we run command "python src/hello_world.py"
  Then output has "Hello, World!"
  
Scenario: When requested, the application writes the greeting message.
  When we run command "python src/hello_world.py --who John"
  Then output has "Hello, John!"
  
Scenario: When requested, the application writes the help message.
  When we run command "python src/hello_world.py --help"
  Then output has "usage: hello_world.py [-h] [--who WHO]"