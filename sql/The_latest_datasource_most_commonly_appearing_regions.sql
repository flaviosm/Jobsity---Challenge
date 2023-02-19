select datasource
from Trip T
INNER JOIN  (
		select concat(region, max_date_trip) AS region_max_date_trip
		FROM
		(
			select region, max(date_trip) max_date_trip
			from Trip
			where region in
			        (
			        select region
			        from (
			                        SELECT
			                            region,
			                            count(1) qtd,
			                            RANK() OVER(                                        
			                                         ORDER BY
			                                             count(1) DESC
			                                        ) qtd_trip    
			                        FROM
			                            Trip
			                        group by region
			                        ) as t
			        where t.qtd_trip <= 2)
			group by region 
			)as t
		ORDER BY max_date_trip DESC LIMIT 1) AS TF
ON concat(T.region, T.date_trip) = TF.region_max_date_trip