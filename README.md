# splash_python_learning

### Some quick notes of Lua


Splash used the lua script so some important points may needed.

* To execute a script we need to send the lua script in endpoint **execute** (or **run**) where **lua_source** will be our argument.

* we need to define the **main** function which our entry point. This one is called by Splash. The result of this main function will be return as HTTP response.

    - Main function will one first argument which will be an object which has all the features of controlling the browser tab naming it as splash can be meaningfull. Below is the example of main function in lua script.

        Example is defined in basics_main.lua where we have taken splash as argument and used two function **go** and **wait** which is the features that splash provides us.
* Splash works on async so it is fast.


### Using Splash and Python Requests
