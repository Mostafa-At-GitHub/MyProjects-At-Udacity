SELECT 	FlightNum,tailnum,
		Month,DayofMonth,DayOfWeek, c.Description as Carrier, ArrDelay,
		Cancelled,CancellationCode,Diverted,
		CarrierDelay,WeatherDelay,NASDelay,SecurityDelay,
		Origin,Dest,Distance,TaxiIn,TaxiOut
FROM '2008' as flights
LEFT JOIN carriers as c 
ON flights.UniqueCarrier = c.Code;