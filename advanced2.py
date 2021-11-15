def eval_temperature( temp ):
    if temp >= 50:
        print( temp, " => Very HOT!" )
    elif temp >= 30 and temp < 50:
        print( temp, " => HOT!" )
    elif temp >= 10 and temp < 30:
        print( temp, " => Warm!" )
    elif temp >= -10 and temp < 10:
        print( temp, " => Normal!" )
    elif temp >= -30 and temp < -10:
        print( temp, " => Cold!" )
    elif temp >= -50 and temp < -30:
        print( temp, " => Very Cold!" )
    else:
        print(temp, " => Freezing!!!")


# call - testing
eval_temperature( 60 )
eval_temperature( 40 )
eval_temperature( 20 )
eval_temperature( 0 )
eval_temperature( -20 )
eval_temperature( -40 )
eval_temperature( -60 )