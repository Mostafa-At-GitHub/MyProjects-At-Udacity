SELECT 	Month, c.Description as Carrier, ArrDelay,
		Cancelled,CancellationCode,Diverted,
		CarrierDelay,WeatherDelay,NASDelay,SecurityDelay
FROM '2008' as flights
LEFT JOIN carriers as c 
ON flights.UniqueCarrier = c.Code;