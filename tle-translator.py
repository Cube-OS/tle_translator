import requests

# Fetch the TLE data from the URL
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=last-30-days&FORMAT=tle"
response = requests.get(url)
tle_data = response.text
# print("Fetched TLE Data:")
# print(tle_data)

# Extract CUAVA-2/WS-1 TLE data
lines = tle_data.splitlines()
tle_line1 = None
tle_line2 = None
for i in range(len(lines)):
    if "CUAVA 2" in lines[i]:
    # if "WARATAH SEED-1" in lines[i]:
        tle_line1 = lines[i + 1]
        tle_line2 = lines[i + 2]
        break


# Check if CUAVA-2 TLE data was found
if tle_line1 and tle_line2:
    # Print the TLE data
    # print("CUAVA-2 TLE Data:")
    print(tle_line1)
    print(tle_line2)

    # Extract orbital parameters from TLE lines
    # Line 1
    epoch_year = int(tle_line1[18:20])
    epoch_day = int(tle_line1[20:23])
    epoch_year_date = f"{epoch_year:02}.{epoch_day:03}"
    mean_motion_derivative = float(tle_line1[33:43].strip())
    mean_motion_sec_derivative = float(tle_line1[44:50].strip() + "e" + tle_line1[50:52].strip())
    bstar_drag_term = float("0." + tle_line1[53:59].strip() + "e" + tle_line1[59:61].strip())

    # Line 2
    inclination = float(tle_line2[8:16].strip())  # Inclination (degrees)
    right_ascension = float(tle_line2[17:25].strip())  # Right Ascension of Ascending Node (degrees)
    eccentricity = float("0." + tle_line2[26:33].strip())  # Eccentricity
    argument_of_perigee = float(tle_line2[34:42].strip())  # Argument of Perigee (degrees)
    mean_anomaly = float(tle_line2[43:51].strip())  # Mean Anomaly (degrees)
    mean_motion = float(tle_line2[52:63].strip())  # Mean Motion (revolutions per day)
    revolution_number_at_epoch = int(tle_line2[63:68].strip())  # Revolution number at epoch

    # Print the orbital parameters
    print(f"Inclination (degrees): {inclination:.4f}")
    print(f"Eccentricity: {eccentricity:.7f}")
    print(f"Right Ascension of Ascending Node (degrees): {right_ascension:.4f}")
    print(f"Argument of Perigee (degrees): {argument_of_perigee:.4f}")
    print(f"B* Drag Term: {bstar_drag_term:.4f}")
    print(f"Mean Motion (revolutions per day): {mean_motion:.8f}")    
    print(f"Mean Anomaly (degrees): {mean_anomaly:.4f}")
    print(f"Epoch Time: {epoch_year_date}")
   
    # print(f"Revolution Number at Epoch: {revolution_number_at_epoch}")
else:
    print("CUAVA-2 TLE data not found.")
