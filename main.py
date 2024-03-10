from weather_check import get_weather

restart_ui = """
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

    Loading… 🔜

    ⏳ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 100% ⏳

    Restarted🔄✅

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

exit_ui = """
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

    Shutting down... 🔜

    ⏳ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 100% ⏳

    Exit⛔⛔

    Thank you for using our app 🥰 🥰 🥰

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""



# this dictionary contained all the ANSI color code, which is easily use for printed ui with color design
# in order that add color to text, at the start we use color code and at the end of text we use off.
color = {
    'white':      '\033[1;37m',
    'yellow':     '\033[1;33m',
    'blue':       '\033[1;34m',
    'red':        '\033[1;31m',
    'magenta':    '\033[1;35m',
    'darkyellow': '\033[0;33m',
    'darkmagenta':'\033[0;35m',
    'darkblack':  '\033[0;30m',
    'darkorange': '\033[38;5;166m',
    'off':        '\033[0;0m'
}




# to make more unique UI design, this collection of icon will print base on weather icon code that got from API result
weather_icon = {
   
  # day icon

    '01d': f''' {color['darkorange']}
              ============              
            +===============            
           ==================           
          ====================          
          =====================         
          ====================+         
          ====================          
           ==================+          
            ================+           
             +=============             
                 +=====      {color['off']}    
''',

    '02d': f'''
                       {color['darkorange']}+======{color['off']}          
               {color['white']}....{color['off']}  {color['darkorange']}==========={color['off']}        
             {color['white']}........{color['off']}{color['darkorange']}============{color['off']}       
            {color['white']}.........{color['off']}{color['darkorange']}:=++========={color['off']}      
           {color['white']}...............{color['off']}{color['darkorange']}-======={color['off']}      
        {color['white']}...................{color['off']}{color['darkorange']}=+====={color['off']}      
       {color['white']}......................{color['off']}{color['darkorange']}:==+{color['off']}       
       {color['white']}.........................{color['off']}        
       {color['white']}.........................{color['off']}        
        {color['white']}.......................{color['off']}                                           
''',

    '03d': f''' {color['white']}
               .......                  
             ..........                 
             ...............            
          ..................            
        .......................         
        ........................        
        ........................        
         .......................        
           ................... {color['off']}                                          
''',

    '04d': f'''
                    {color['darkblack']}+++++{color['off']}               
               {color['white']}...{color['off']}{color['darkblack']}#++++++++{color['off']}             
            {color['white']}.......{color['off']}{color['darkblack']}-#++++++++++{color['off']}         
           {color['white']}..........{color['off']}{color['darkblack']}++++++++++{color['off']}         
           {color['white']}..............{color['off']}{color['darkblack']}-++++++++{color['off']}      
       {color['white']}...................{color['off']}{color['darkblack']}+++++++++{color['off']}     
      {color['white']}.......................{color['off']}{color['darkblack']}+++++{color['off']}      
      {color['white']}.........................{color['off']}{color['darkblack']}+{color['off']}        
      {color['white']}.........................{color['off']}         
       {color['white']}.......................{color['off']}   
''',

    '09d':f'''
                    {color['darkblack']}###{color['off']}                 
               {color['white']}...{color['off']}{color['darkblack']}+#######{color['off']}              
             {color['white']}......{color['off']}{color['darkblack']}:#########{color['off']}           
            {color['white']}........{color['off']}{color['darkblack']}:-:=#######{color['off']}         
          {color['white']}..............{color['off']}{color['darkblack']}-#######{color['off']}        
        {color['white']}..................{color['off']}{color['darkblack']}-*###{color['off']}         
        {color['white']}....................{color['off']}            
         {color['white']}......:............{color['off']}            
            {color['blue']}  ##     #                  
             ## ### ##                  
             ## ## ##                   
                   ##{color['off']} 
''',

    '10d':f'''
                       {color['darkorange']}----{color['off']}             
               {color['white']}.....{color['off']}{color['darkorange']}----------{color['off']}          
             {color['white']}........{color['off']}{color['darkorange']}----------{color['off']}         
             {color['white']}............{color['off']}{color['darkorange']}------{color['off']}         
          {color['white']}................{color['off']}{color['darkorange']}-----{color['off']}         
         {color['white']}...................{color['off']}{color['darkorange']}--{color['off']}          
         {color['white']}....................{color['off']}           
          {color['white']}...................{color['off']}           
            {color['blue']}   ++    +#                 
              ++ +++ ++                 
              +  ++ ++                  
                    +    {color['off']}                 
''',

    '11d': f'''
                   {color['darkblack']}######{color['off']}               
             {color['white']}.....{color['off']}{color['darkblack']}+##########{color['off']}           
            {color['white']}.......{color['off']}{color['darkblack']}:*##########{color['off']}         
           {color['white']}.........{color['off']}{color['darkblack']}:+--########{color['off']}        
         {color['white']}................{color['off']}{color['darkblack']}=########{color['off']}      
       {color['white']}..................{color['off']}{color['darkblack']}-+*######{color['off']}      
      {color['white']}......................{color['off']}{color['darkblack']}:*###{color['off']}       
      {color['white']}........{color['off']}{color['darkyellow']}-==:{color['off']}{color['white']}............{color['off']}          
        {color['white']}.....{color['off']}{color['darkyellow']}:=+:{color['off']}{color['white']}............{color['off']}           
            {color['darkyellow']}=+===={color['off']}                      
             {color['darkyellow']}==={color['off']}                        
            {color['darkyellow']}+={color['off']}                                       
''',

# r here is the Raw string, since our ascii art was built with backslash (\), using raw string is to avoid syntax warning since backslash normally use as escape character
# for example, \n \t
    '13d': rf'''{color['darkblack']}
                __    __
               /_/ /\ \_\
              __ \ \/ / __
              \_\_\/\/_/_/
            /\___\_\/_/___/\
            \/ __/_/\_\__ \/
              /_/ /\/\ \_\
               __/ /\ \__
               \_\ \/ /_/ {color['off']}
''',

    '50d': f'''{color['darkblack']}
               ++++++++                 
                +#####                  
          ++++++++++++++                
              +++++++++++++++++         
         +++++++++++++++++              
          +++++++++++++++               
            +++++++++++++++++           
              ++++++++++++  {color['off']}
''',

  # night icon
  
    '01n': f'''{color['darkblack']}
              ============              
            +===============            
           ==================           
          ====================          
          =====================         
          ====================+         
          ====================          
           ==================+          
            ================+           
             +=============             
                 +====={color['off']}  
''',

    '02n': f'''
                       {color['darkblack']}+======{color['off']}          
               {color['white']}....{color['off']}  {color['darkblack']}==========={color['off']}        
             {color['white']}........{color['off']}{color['darkblack']}============{color['off']}       
            {color['white']}.........{color['off']}{color['darkblack']}:=++========={color['off']}      
           {color['white']}...............{color['off']}{color['darkblack']}-======={color['off']}      
        {color['white']}...................{color['off']}{color['darkblack']}=+====={color['off']}      
       {color['white']}......................{color['off']}{color['darkblack']}:==+{color['off']}       
       {color['white']}.........................{color['off']}        
       {color['white']}.........................{color['off']}        
        {color['white']}.......................{color['off']}                                            
''',

    '03n': f'''{color['white']}
               .......                  
             ..........                 
             ...............            
          ..................            
        .......................         
        ........................        
        ........................        
         .......................        
           ...................    {color['off']}                                       
''',

    '04n': f'''
                    {color['darkblack']}+++++{color['off']}               
               {color['white']}...{color['off']}{color['darkblack']}#++++++++{color['off']}             
            {color['white']}.......{color['off']}{color['darkblack']}-#++++++++++{color['off']}         
           {color['white']}..........{color['off']}{color['darkblack']}++++++++++{color['off']}         
           {color['white']}..............{color['off']}{color['darkblack']}-++++++++{color['off']}      
       {color['white']}...................{color['off']}{color['darkblack']}+++++++++{color['off']}     
      {color['white']}.......................{color['off']}{color['darkblack']}+++++{color['off']}      
      {color['white']}.........................{color['off']}{color['darkblack']}+{color['off']}        
      {color['white']}.........................{color['off']}         
       {color['white']}.......................{color['off']}   
''',

    '09n':f'''
                    {color['darkblack']}###{color['off']}                 
               {color['white']}...{color['off']}{color['darkblack']}+#######{color['off']}              
             {color['white']}......{color['off']}{color['darkblack']}:#########{color['off']}           
            {color['white']}........{color['off']}{color['darkblack']}:-:=#######{color['off']}         
          {color['white']}..............{color['off']}{color['darkblack']}-#######{color['off']}        
        {color['white']}..................{color['off']}{color['darkblack']}-*###{color['off']}         
        {color['white']}....................{color['off']}            
         {color['white']}......:............{color['off']}            
              {color['blue']}##     #                  
             ## ### ##                  
             ## ## ##                   
                   ##{color['off']} 
''',

    '10n':f'''
                       {color['darkblack']}----{color['off']}             
               {color['white']}.....{color['off']}{color['darkblack']}----------{color['off']}          
             {color['white']}........{color['off']}{color['darkblack']}----------{color['off']}         
             {color['white']}............{color['off']}{color['darkblack']}------{color['off']}         
          {color['white']}................{color['off']}{color['darkblack']}-----{color['off']}         
         {color['white']}...................{color['off']}{color['darkblack']}--{color['off']}          
         {color['white']}....................{color['off']}           
          {color['white']}...................{color['off']}           
               {color['blue']}++    +#                 
              ++ +++ ++                 
              +  ++ ++                  
                    +{color['off']}                     
''',

    '11n': f'''
                   {color['darkblack']}######{color['off']}               
             {color['white']}.....{color['off']}{color['darkblack']}+##########{color['off']}           
            {color['white']}.......{color['off']}{color['darkblack']}:*##########{color['off']}         
           {color['white']}.........{color['off']}{color['darkblack']}:+--########{color['off']}        
         {color['white']}................{color['off']}{color['darkblack']}=########{color['off']}      
       {color['white']}..................{color['off']}{color['darkblack']}-+*######{color['off']}      
      {color['white']}......................{color['off']}{color['darkblack']}:*###{color['off']}       
      {color['white']}........{color['off']}{color['darkyellow']}-==:{color['off']}{color['white']}............{color['off']}          
        {color['white']}.....{color['off']}{color['darkyellow']}:=+:{color['off']}{color['white']}............{color['off']}           
            {color['darkyellow']}=+===={color['off']}                      
             {color['darkyellow']}==={color['off']}                        
            {color['darkyellow']}+={color['off']}                                       
''',

# r here is the Raw string, since our ascii art was built with backslash (\), using raw string is to avoid syntax warning since backslash normally use as escape character
# for example, \n \t
    '13n': rf'''{color['darkblack']}
                __    __
               /_/ /\ \_\
              __ \ \/ / __
              \_\_\/\/_/_/
            /\___\_\/_/___/\
            \/ __/_/\_\__ \/
              /_/ /\/\ \_\
               __/ /\ \__
               \_\ \/ /_/ {color['off']}
''',

    '50n': f'''{color['darkblack']}
               ++++++++                 
                +#####                  
          ++++++++++++++                
              +++++++++++++++++         
         +++++++++++++++++              
          +++++++++++++++               
            +++++++++++++++++           
              ++++++++++++  {color['off']}
''',
    
}


# UI 


print(f"""
                                                                     {color['darkorange']}-----------{color['off']}                                        
                                                                  {color['darkorange']}-----------------{color['off']}                                     
                                                               {color['darkorange']}-----------------------{color['off']}                                  
                                                 {color['white']}........    {color['off']}{color['darkorange']}---------------------------{color['off']}                                
                                             {color['white']}................{color['off']}{color['darkorange']}+---------------------------{color['off']}                               
                                           {color['white']}...................{color['off']}{color['darkorange']}----------------------------{color['off']}                              
                                          {color['white']}.....................{color['off']}{color['darkorange']}-+--------------------------{color['off']}                             
                                         {color['white']}.......................{color['off']}{color['darkorange']}-+--------------------------{color['off']}                            
                                        {color['white']}.........................{color['off']}{color['darkorange']}+--------------------------{color['off']}                            
                                        {color['white']}..................................{color['off']}{color['darkorange']}------------------{color['off']}                            
                                        {color['white']}....................................{color['off']}{color['darkorange']}----------------{color['off']}                            
                                   {color['white']}..........................................{color['off']}{color['darkorange']}+--------------{color['off']}                            
                                {color['white']}.............................................{color['off']}{color['darkorange']}---------------{color['off']}                            
                               {color['white']}..............................................{color['off']}{color['darkorange']}+-------------{color['off']}                             
                              {color['white']}....................................................{color['off']}{color['darkorange']}--------{color['off']}                              
                            {color['white']}........................................................{color['off']}{color['darkorange']}-----{color['off']}                               
                            {color['white']}..........................................................{color['off']}{color['darkorange']}-+{color['off']}                                
                            {color['white']}...........................................................{color['off']}                                 
                            {color['white']}...........................................................{color['off']}                                 
                             {color['white']}..........................................................{color['off']}                                 
                              {color['white']}.........................................................{color['off']}                                 
                               {color['white']}.......................................................{color['off']}                                  
                                 {color['white']}.............{color['blue']}-##+-{color['off']}{color['white']}.................................{color['off']}                                    
                                     {color['white']}........{color['blue']}-+##+-{color['off']}{color['white']}..............   .............{color['off']}                                       
                                              {color['blue']}#++#               ###                                                    
                                                      +++      ++++++                                                   
                                           ++++     ++++++     ++++++                                                   
                                           +++++    ++++++       ++                                                     
                                          +++++    ++++++                                                               
                                          +++++     ++++                                                                
                                           ++      ++       +++++                                                       
                                                 ++++++     +++++                                                       
                                                 +++++    ++++++                                                        
                                                           +++++{color['off']}


     {color['blue']} ░██╗░░░░░░░██╗███████╗░█████╗░████████╗██╗░░██╗███████╗██████╗░{color['off']}  {color['yellow']}░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░{color['off']}
     {color['blue']} ░██║░░██╗░░██║██╔════╝██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗{color['off']}  {color['yellow']}██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗{color['off']}
     {color['blue']} ░╚██╗████╗██╔╝█████╗░░███████║░░░██║░░░███████║█████╗░░██████╔╝{color['off']}  {color['yellow']}██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝{color['off']}
     {color['blue']} ░░████╔═████║░██╔══╝░░██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗{color['off']}  {color['yellow']}██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗{color['off']}
     {color['blue']} ░░╚██╔╝░╚██╔╝░███████╗██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║{color['off']}  {color['yellow']}╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║{color['off']}
     {color['blue']} ░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝{color['off']}  {color['yellow']}░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝{color['off']}
""")

# to avoide a code that is too long, then create varibles to store short off of color changing 
shorted_mag = color['magenta']
shorted_blue = color['blue']
off_col = color['off']

print(f"""
  {shorted_mag}╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮{off_col}
  {shorted_mag}│{off_col}                                                                                                                              {shorted_mag}│{off_col}    
  {shorted_mag}│{off_col}                                               💡 𝕀ℕ 𝕊 𝕋 ℝ 𝕌 ℂ 𝕋 𝕀𝕆 ℕ  💡                                              {shorted_mag}│{off_col}
  {shorted_mag}│{off_col}                                                                                                                              {shorted_mag}│{off_col}    
  {shorted_mag}│{off_col}                                                                                                                              {shorted_mag}│{off_col}
  {shorted_mag}│{off_col}                                    💡 Enter city name to check weather 🌦️  ☁️  🌤️  ❄️  🌧️                                      {shorted_mag}│{off_col}
  {shorted_mag}│{off_col}                                                                                                                              {shorted_mag}│{off_col}
  {shorted_mag}╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯{off_col}
""")




while True:
  city = input("\n  ⛅  Enter city name to check weather: ")

  result = get_weather(city)

  if result == 'city not found':
    print("City not found!")
    check_continue = input('\n🔄🔄🔄 Do you want to start again? 🔄🔄🔄 y/n: ').lower()
    if check_continue != 'n':
        print(restart_ui)
        True
    else:
        print(exit_ui)
        break
  
  else:
    # return result separately, so it's easy to use in printing UI
    city_name = result['name']
    weather_condition = result['weather']
    temperature = result['temp']
    icon_id = result['icon']

    # change the color of temperature result as the lever of temperature cold or hot

    if temperature <= 25:
      temperature = f"{color['blue']}{temperature}{color['off']}°C ❄️"
    else:
      temperature = f"{color['red']}{temperature}{color['off']}°C 🌡️"

      
    print(weather_icon[icon_id])
    print(f"\n   {shorted_blue}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{off_col}")
    print(f"   {shorted_blue}║                                                                                                                             ║{off_col}")
    print(f"                        {city_name} is {weather_condition} with the temperature of {temperature}")
    print(f"   {shorted_blue}║                                                                                                                             ║{off_col}")
    print(f"   {shorted_blue}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{off_col}")
    check_continue = input('\n🔄🔄🔄 Do you want to start again? 🔄🔄🔄 y/n: ').lower()
    if check_continue != 'n':
        print(restart_ui)
        True
    else:
        print(exit_ui)
        break