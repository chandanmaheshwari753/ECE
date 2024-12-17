import pandas as pd
import pvlib
import time
# Define the location (latitude, longitude, and timezone)
latitude = 22.43462316321501 # Narendrapur
longitude = 88.39079745873036 # Narendrapur
#latitude = 28.4114356 # Faridabad
#longitude = 77.3400727 # Faridabad
tz = 'Asia/Kolkata'

# Create a time range for which you want to calculate the solar position
times = pd.date_range(start='2024-05-30 09:15:00', end='2024-05-30 17:15:00', freq='0.0166667h', tz=tz)

# Loop through each timestamp in the time range
for t in times:
    # Calculate solar position
    solar_position = pvlib.solarposition.get_solarposition(t, latitude, longitude)
    
    # Extract elevation and azimuth
    #elevation = solar_position['elevation'].iloc[0]
    azimuth = solar_position['azimuth'].iloc[0]

    # Adjust servo angles based on solar position
    # Elevation: add 90 degrees to ensure servo can rotate properly
    #servo_elevation = elevation + 90
    
    # Azimuth: adjust to servo constraints
    servo_azimuth = 180 - (azimuth - 90)+18
    
    # Print for debugging
    #print(f" {int(servo_elevation)},"," ")
    print(f"{int(servo_azimuth )},","")
    time.sleep(0.001)
