SELECT a.region
	   ,week_date_trip
  	   ,avg(a.qtd_region) as average
FROM
  (SELECT WEEK(date_trip) as week_date_trip, region, COUNT(region) as qtd_region 
   FROM Trip
   GROUP BY WEEK(date_trip), region
   ORDER BY 1
  ) a
group by a.region, week_date_trip
order by 2, 1